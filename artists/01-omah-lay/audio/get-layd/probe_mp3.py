"""Read-only MPEG Layer III frame and ID3 probe for user-supplied Get Layd captures.

This does not decode sound or identify the composition. It reports container-level
facts needed to decide whether a capture can be used for listening research.
"""

import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BITRATES = [0, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320]
SAMPLE_RATES = [44100, 48000, 32000]


def synchsafe(raw):
    return (raw[0] << 21) | (raw[1] << 14) | (raw[2] << 7) | raw[3]


def probe(path):
    data = path.read_bytes()
    offset = 0
    id3 = None
    if data[:3] == b"ID3" and len(data) >= 10:
        id3 = {"version": f"2.{data[3]}.{data[4]}", "bytes": 10 + synchsafe(data[6:10])}
        offset = id3["bytes"]
    frames = 0
    duration = 0.0
    bitrates = Counter()
    sample_rates = Counter()
    channels = Counter()
    frame_bytes = Counter()
    invalid = 0
    edge_patterns = {"first_frame_55_fraction": None, "last_frame_55_fraction": None,
                     "first_frame_aa_fraction": None, "last_frame_aa_fraction": None}
    first_frame = last_frame = None
    while offset + 4 <= len(data):
        h = int.from_bytes(data[offset:offset + 4], "big")
        version = (h >> 19) & 3
        layer = (h >> 17) & 3
        bitrate_index = (h >> 12) & 15
        sample_index = (h >> 10) & 3
        if ((h >> 21) & 2047) != 2047 or version != 3 or layer != 1 or not 1 <= bitrate_index <= 14 or sample_index == 3:
            invalid += 1
            offset += 1
            continue
        bitrate = BITRATES[bitrate_index]
        sample_rate = SAMPLE_RATES[sample_index]
        padding = (h >> 9) & 1
        frame_len = (144000 * bitrate // sample_rate) + padding
        if offset + frame_len > len(data):
            break
        frame = data[offset:offset + frame_len]
        if first_frame is None:
            first_frame = frame
        last_frame = frame
        frames += 1
        duration += 1152 / sample_rate
        bitrates[bitrate] += 1
        sample_rates[sample_rate] += 1
        channels[(h >> 6) & 3] += 1
        frame_bytes[frame_len] += 1
        offset += frame_len
    for label, frame in (("first", first_frame), ("last", last_frame)):
        if frame:
            payload = frame[4:]
            for code, name in ((0x55, "55"), (0xAA, "aa")):
                edge_patterns[f"{label}_frame_{name}_fraction"] = round(payload.count(code) / len(payload), 4)
    return {
        "file": path.name,
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "id3": id3,
        "frames": frames,
        "duration_seconds_from_frames": round(duration, 3),
        "bitrates_kbps_frames": dict(bitrates),
        "sample_rates_hz_frames": dict(sample_rates),
        "channel_modes_frames": {str(k): v for k, v in channels.items()},
        "frame_lengths_bytes": dict(frame_bytes),
        "stray_bytes_or_header_mismatches": invalid,
        "trailing_bytes": len(data) - offset,
        "edge_pattern_fractions": edge_patterns,
    }


if __name__ == "__main__":
    print(json.dumps([probe(p) for p in sorted(ROOT.glob("*.mp3"))], indent=2))
