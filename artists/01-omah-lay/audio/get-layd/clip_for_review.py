"""Emit a short mono WAV clip from a supplied MP3 as base64 for private review.

Requires the local Audacity mpg123 decoder. Does not write or distribute audio.
Usage: python clip_for_review.py <filename> <start_seconds> <duration_seconds>
"""

import array
import base64
import ctypes as C
import io
import os
import sys
import wave
from pathlib import Path

ROOT = Path(__file__).resolve().parent
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
lib.mpg123_read.argtypes = [C.c_void_p, C.c_void_p, C.c_size_t, C.POINTER(C.c_size_t)]
lib.mpg123_read.restype = C.c_int
lib.mpg123_close.argtypes = [C.c_void_p]
lib.mpg123_delete.argtypes = [C.c_void_p]

name = sys.argv[1]
start = float(sys.argv[2])
duration = float(sys.argv[3])
if not (0 <= start < 600 and 0 < duration <= 20):
    raise ValueError("Clip bounds invalid")
path = ROOT / name
lib.mpg123_init()
err = C.c_int()
mh = lib.mpg123_new(None, C.byref(err))
try:
    if lib.mpg123_open(mh, str(path).encode()) != 0:
        raise RuntimeError("open failed")
    rate, channels, encoding = C.c_long(), C.c_int(), C.c_int()
    if lib.mpg123_getformat(mh, C.byref(rate), C.byref(channels), C.byref(encoding)) != 0:
        raise RuntimeError("getformat failed")
    if encoding.value != 208:
        raise RuntimeError(f"unexpected encoding {encoding.value}")
    first = int(start * rate.value)
    last = int((start + duration) * rate.value)
    output_rate = rate.value // 4
    mono = array.array("h")
    buf = C.create_string_buffer(32768)
    done = C.c_size_t()
    decoded_frames = 0
    while decoded_frames < last:
        code = lib.mpg123_read(mh, buf, len(buf), C.byref(done))
        if done.value:
            block = array.array("h")
            block.frombytes(buf.raw[:done.value])
            count = len(block) // channels.value
            for j in range(count):
                position = decoded_frames + j
                if first <= position < last and position % 4 == 0:
                    s = sum(block[j * channels.value:(j + 1) * channels.value]) // channels.value
                    mono.append(s)
            decoded_frames += count
        if code == -12:
            break
        if code not in (0, -11):
            raise RuntimeError(f"decode error {code}")
    target = io.BytesIO()
    with wave.open(target, "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(output_rate)
        wav.writeframes(mono.tobytes())
    sys.stdout.write(base64.b64encode(target.getvalue()).decode())
finally:
    lib.mpg123_close(mh)
    lib.mpg123_delete(mh)
