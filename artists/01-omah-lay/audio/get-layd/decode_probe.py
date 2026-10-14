"""Decode a local MP3 capture via Audacity's installed mpg123 DLL.

Read-only on MP3 inputs. Writes small, non-audio JSON measurements to stdout.
"""

import array
import ctypes as C
import json
import math
import os
import sys
from pathlib import Path

DLL_DIR = Path(r"C:\Program Files\Audacity 4\bin")
os.add_dll_directory(str(DLL_DIR))
lib = C.CDLL(str(DLL_DIR / "mpg123.dll"))
lib.mpg123_init.restype = C.c_int
lib.mpg123_new.argtypes = [C.c_char_p, C.POINTER(C.c_int)]
lib.mpg123_new.restype = C.c_void_p
lib.mpg123_open.argtypes = [C.c_void_p, C.c_char_p]
lib.mpg123_open.restype = C.c_int
lib.mpg123_getformat.argtypes = [C.c_void_p, C.POINTER(C.c_long), C.POINTER(C.c_int), C.POINTER(C.c_int)]
lib.mpg123_getformat.restype = C.c_int
lib.mpg123_encsize.argtypes = [C.c_int]
lib.mpg123_encsize.restype = C.c_int
lib.mpg123_read.argtypes = [C.c_void_p, C.c_void_p, C.c_size_t, C.POINTER(C.c_size_t)]
lib.mpg123_read.restype = C.c_int
lib.mpg123_close.argtypes = [C.c_void_p]
lib.mpg123_delete.argtypes = [C.c_void_p]


def probe(path):
    if lib.mpg123_init() != 0:
        raise RuntimeError("mpg123_init failed")
    err = C.c_int()
    mh = lib.mpg123_new(None, C.byref(err))
    if not mh:
        raise RuntimeError(f"mpg123_new error {err.value}")
    try:
        code = lib.mpg123_open(mh, str(path).encode("utf-8"))
        if code:
            raise RuntimeError(f"mpg123_open error {code}")
        rate, channels, encoding = C.c_long(), C.c_int(), C.c_int()
        code = lib.mpg123_getformat(mh, C.byref(rate), C.byref(channels), C.byref(encoding))
        if code:
            raise RuntimeError(f"mpg123_getformat error {code}")
        width = lib.mpg123_encsize(encoding.value)
        if width != 2:
            raise RuntimeError(f"Expected 16-bit PCM, got encoding={encoding.value} width={width}")
        frames_per_bucket = rate.value // 10
        bsize = 32768
        buf = C.create_string_buffer(bsize)
        done = C.c_size_t()
        partial = array.array("h")
        buckets = []
        samples = 0
        errors = []
        peak_sample = 0
        near_clip_samples = 0
        total_samples = 0
        while True:
            code = lib.mpg123_read(mh, buf, bsize, C.byref(done))
            if done.value:
                block = array.array("h")
                block.frombytes(buf.raw[:done.value])
                partial.extend(block)
                unit = frames_per_bucket * channels.value
                while len(partial) >= unit:
                    item = partial[:unit]
                    del partial[:unit]
                    peak = max(abs(x) for x in item)
                    peak_sample = max(peak_sample, peak)
                    near_clip_samples += sum(1 for x in item if abs(x) >= 32760)
                    total_samples += len(item)
                    rms = math.sqrt(sum(x * x for x in item) / len(item)) / 32768
                    buckets.append({"rms": round(rms, 6), "peak": round(peak / 32768, 6)})
                    samples += frames_per_bucket
            if code == -12:
                break
            if code not in (0, -11):
                errors.append(code)
                if not done.value:
                    break
        samples += len(partial) // channels.value
        active = [i for i, x in enumerate(buckets) if x["rms"] > 0.002]
        return {
            "file": path.name,
            "rate_hz": rate.value,
            "channels": channels.value,
            "encoding_code": encoding.value,
            "sample_width_bytes": width,
            "decoded_samples_per_channel": samples,
            "decoded_duration_seconds": round(samples / rate.value, 3),
            "decode_errors": errors,
            "peak_pcm_fraction": round(peak_sample / 32768, 6),
            "near_clip_sample_fraction": round(near_clip_samples / total_samples, 8) if total_samples else None,
            "rms_threshold_0_002_first_active_s": round(active[0] / 10, 1) if active else None,
            "rms_threshold_0_002_last_active_s": round((active[-1] + 1) / 10, 1) if active else None,
            "rms_0_1_second_buckets": buckets,
        }
    finally:
        lib.mpg123_close(mh)
        lib.mpg123_delete(mh)


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    names = sys.argv[1:] or [p.name for p in sorted(root.glob("*.mp3"))]
    results = [probe(root / name) for name in names]
    for d in results:
        # Keep output compact; full bucket series can be regenerated with this script.
        d["rms_0_1_second_buckets"] = {
            "count": len(d["rms_0_1_second_buckets"]),
            "first_10": d["rms_0_1_second_buckets"][:10],
            "last_10": d["rms_0_1_second_buckets"][-10:],
        }
    print(json.dumps(results, indent=2))
