# Get Layd supplied-capture technical intake

Checked 2026-09-25. The user states these are private captures of computer playback. They are treated as research inputs, not original downloaded masters. This record separates file integrity and signal checks from **song/version identity** and from human listening. The files lack ID3 tags, so title, artist, album, date and source cannot be independently read from metadata.

Method: `probe_mp3.py` parses MPEG Layer III frames and SHA-256 hashes. `decode_probe.py` decodes with the locally installed Audacity 4 `mpg123.dll` and measures 0.1-second stereo PCM RMS. An `RMS > 0.002` threshold is used only to locate substantial signal; it does not prove exact musical starts/ends or word content. [Spotify EP](https://open.spotify.com/album/3wzSqNDc2jNNV42XLkkDMA) supplies rounded reference durations.

| Intended EP track | Supplied filename | MP3 decoded duration | Listed EP duration | Substantial-signal window (approx.) | Metadata/format | Technical identity assessment |
|---|---|---:|---:|---:|---|---|
| Damn | `omah_lay_damn.mp3` | 2:42.87 | 2:39 | 0:00–2:36.8 | No ID3; MPEG-1 Layer III, 320 kb/s CBR, 44.1 kHz joint stereo | Duration difference plausibly capture tail/padding. Original-mix identity and audible quality still unverified. |
| Lo Lo | `lo lo.mp3` | 3:01.42 | 2:51 | 0:04.8–2:57.4 | Same; no ID3 | Approximately 4.8 s leading and 4.0 s trailing low signal; active span ~2:52.6, close to listed 2:51. Original-mix identity and audible quality still unverified. |
| You | `you.mp3` | 2:35.79 | 2:43 | 0:00–file end | Same; no ID3 | **Historical technical flag only:** active at final frame and shorter than platform reference. Duration alone could not establish incompleteness; later listening confirms an audible cutoff. |
| Bad Influence | `bad influence.mp3` | 2:18.45 | 2:18 | 0:00–2:17.2 | Same; no ID3 | Duration is consistent with EP listing, with a short low-signal tail. Original-mix identity and audible quality still unverified. |
| Ye Ye Ye | `ye ye ye.mp3` | 3:14.33 | 3:27 | 0:00–file end | Same; no ID3 | **Historical technical flag only:** active at final frame and shorter than platform reference. Duration alone could not establish incompleteness; later listening confirms an audible cutoff. |

All five files decode without reported frame errors, have no ID3 tag or frame-level corruption, and contain 320 kb/s frames at 44.1 kHz. This establishes technical readability. It does **not** establish that a capture is the correct song, that it is an original studio mix, or that a 320 kb/s re-encode preserves the upstream playback quality. A private audio clip was routed to the session's audio-output mechanism, which responded that audio content is omitted because this model does not support audio input. At this **earlier MP3-only intake stage**, no human listening, lyric-performance verification, section naming, vocal timbre judgment or definitive version matching had occurred, and no song was marked fully analysed. Later Damn external-listening verification is documented below.

Level check on the three duration-plausible files: Damn peaks at 0.558 full scale with no samples within eight counts of digital maximum; Bad Influence peaks at 0.998 with none within that near-clipping threshold; Lo Lo reaches full scale with approximately 0.039% of decoded samples within eight counts of maximum. This raises a **possible** capture/master clipping concern for Lo Lo, not a proven audible defect. There were no decode errors. The level test cannot establish fidelity to the source stream, masking, artifacts or whether a listener would judge the capture research-quality. The exact thresholds and results are reproducible in `decode_probe.py` and `quality-summary.json`.

Hashes (SHA-256) support replacement tracking:

| File | SHA-256 |
|---|---|
| `omah_lay_damn.mp3` | `cb591817c30f69eaeefb3ad3d7134d3407ae83ca9625f7beadc7c1f7b474bbbc` |
| `lo lo.mp3` | `977ea2d1409450164b80d61eed80283b75eedcfad609f3048b2d97119fdfab1e` |
| `you.mp3` | `0da2fe9d9b006d4faa0ed7bff9ed0cc4539c57c04aed5a1e20b95d55bca03cd4` |
| `bad influence.mp3` | `84c0fba245d9d5f0b96e8963fd749f168beb6ce5d62080ecc40655ae0e32df53` |
| `ye ye ye.mp3` | `6a5eafbcd8961cf033b7c9b737a3fce6d7a3176904f7f2fb55fa3fe29d5aaafb` |

**Next:** replace the two cut files, then use a playback/listening-capable environment or a verified listening report to settle exact song/version identity and vocal/lyric observations. Signal-only measurements can supplement that work but cannot substitute for it.

## 2026-09-25 WAV format test — Damn

The newly supplied `damn.wav` is a valid uncompressed RIFF/WAVE file: stereo, 16-bit PCM, 44,100 Hz, 7,182,584 frames, 162.87 seconds. SHA-256: `05b4c8a902fc8d033782e90c58b46f4153dc9e50cdd1116335b935d78a37e45b`. Its duration exactly matches the supplied Damn MP3; this suggests a related capture but does not establish sample identity or the original EP mix.

A one-second excerpt read directly from `damn.wav` was passed to the session audio-input route. The response was `audio content omitted because you do not support audio input`. Therefore WAV readability is confirmed, but this session still cannot listen to the recording. No song/version, lyric, vocal, section or production claim was advanced from the WAV test.

## Separate listening report received 2026-09-25

The user supplied a dedicated [Damn listening report](../../projects/get-layd/songs/damn/listening-analysis.md) as a separate evidence layer. It states that its analyst heard `damn.wav` and independently reports 16-bit 44.1 kHz stereo, 162.87 seconds, music ending around 2:36–2:37, and approximately six seconds of trailing padding. Those statements are consistent with this intake's file properties and 2:36.8 substantial-signal boundary. Agreement supports the timing description, but does not prove that the report and this exact local file are bit-identical or that the capture matches the original EP mix. The analyst explicitly leaves artist, project, version and exact lyrics unverified. This Codex session still has no direct audio-input capability; attributed listening observations are integrated separately in the Damn song analysis.

**2026-09-25 targeted follow-up:** The preserved [verification response](../../projects/get-layd/songs/damn/listening-verification.md) reports no obvious guest verse, remix, live crowd, edit or speed artifact; first lead vocal ~0:04.2; first title-word hook ~0:17.1; final refrain ~2:12. Two timed 8-beat samples each span ~4.57 seconds, yielding approximately 105 BPM. These are external listening observations, separate from local decode measurements. The capture's exact playback URL and bit-for-bit commercial-master identity remain unverified; neither is implied by matching duration.

## 2026-09-26 current WAV recheck for the four pending songs

The current audio directory contains WAV files for all four pending songs; the earlier MP3s are no longer present. `wav_intake.py` decoded every declared PCM frame and saved hashes/whole-mix measurements in [wav-intake.json](wav-intake.json). All four are 16-bit stereo, 44,100 Hz, uncompressed PCM with no detected decode/frame-count failure. File names and duration do not prove version identity, commercial-master equivalence or listening quality.

| Intended track | Current WAV; SHA-256 prefix | Duration | Approximate substantial-signal window (whole-mix RMS > 0.002, 0.1-s bins) | Technical outcome |
|---|---|---:|---:|---|
| Lo Lo | `lo lo.wav`; `5dd52e40758b` | 181.42 s | 4.8–177.4 s | About 4.8 s leading and 4.0 s trailing low signal; active span ~172.6 s is close to the ~171-s EP listing. Plausible complete capture; audible identity pending. Peak reaches full scale, as in earlier MP3 intake; clipping audibility unresolved. |
| You | `you.wav`; `65c8d2c9d44a` | 155.79 s | 0–155.79 s | Active through final frame. Shorter than the platform reference, which is only an intake flag; the later Listening Analyst report independently hears a hard cutoff during a continuing refrain. |
| Bad Influence | `Bad influence.wav`; `5f7648df58bc` | 138.45 s | 0–137.2 s | ~1.25 s low-signal tail; duration close to ~138-s listing. Plausible complete capture; audible identity pending. |
| Ye Ye Ye | `ye ye ye.wav`; `0b23ab0ee6c5` | 194.33 s | 0–194.33 s | Active through final frame. Shorter than the platform reference, which is only an intake flag; the later Listening Analyst report independently hears a hard cutoff during continuing groove/response material. |

The WAV durations exactly match the earlier same-titled MP3 durations. This raises the possibility of conversion from those captures, but no sample-level derivation or acquisition chain is established. The simple whole-mix amplitude-envelope correlation in `wav-intake.json` yields pulse **candidates**, including half/double-time aliases; it does not measure a perceptually verified main beat. Shazam currently labels Lo Lo 101, You 96, Bad Influence 96 and Ye Ye Ye 80 BPM as **external platform metadata**. No reliable key/tonal centre, time signature, beat grid, vocal gaps, or musical section boundaries can be established from this intake. Full-song RMS troughs are not equivalent to singer silence. Listening requests should ask the analyst to count actual main-beat intervals and report tempo ambiguity explicitly.

## 2026-09-27 external listening reconciliation

The four new user-supplied, per-song reports are preserved as `listening-analysis.md` under each song. Lo Lo (181.42 s; substantial signal ~4.8–177.4 s) and Bad Influence (138.45 s; signal to ~137.2 s) have coherent audible endings and no reported sustained clipping. Their solo studio performance is consistent with the approved Get Layd versions; bit-for-bit master identity is not proven. You (155.79 s) cuts off during a declaration, and Ye Ye Ye (194.33 s) cuts off amid active groove/nonlexical material. Their final sections remain unknown. The reports supply attributed listening evidence; Codex still cannot directly hear the WAVs. Approximate analyst-timed principal pulses: Lo Lo ~102, You ~97, Bad Influence ~97.1, Ye Ye Ye ~80.2 BPM. These are distinct from older unverified whole-mix amplitude candidates and platform BPM labels.

## 2026-09-28 ending-led completeness reassessment

**Decision rule for private playback captures:** a platform duration is reference metadata, not a required file length. Padding, container timing, capture boundaries or a documented authorized edit can produce a different duration. File duration and active-signal endpoint are technical prompts to inspect the ending; **audible musical resolution is the primary completeness evidence**. Bit-for-bit commercial-master identity is not required for first-pass songwriting analysis. Preserve the actual supplied-version duration and any known capture provenance.

No replacement WAV has appeared since the prior intake. [You's preserved Listening Analyst report](../../projects/get-layd/songs/you/listening-analysis.md) states that at **2:35.79** a later declaration cell, percussion and low-frequency material are continuing; there is no fade or arranged stop, and the file ends at a hard boundary. Its last audible event is continuing refrain/vocal and groove activity, with the exact syllable at the boundary not resolved. [Ye Ye Ye's preserved report](../../projects/get-layd/songs/ye-ye-ye/listening-analysis.md) states that at **3:14.33** rhythm and nonlexical/response-vocal material continue without a fade, final chord, silence or convincing stop. It does not cut a clearly lexical word, but it does truncate the active groove. These **listening findings**, not the differences from Spotify's rounded reference lengths, keep both captures incomplete. No further broad listening request is needed to answer this question; obtain a source-valid continuation or complete recording with a natural ending, then verify only the tail/version relation. The exact amount of missing audio is **unknown**.

## 2026-09-28 user-approved source-limited first-pass gate

The preceding recommendation to obtain natural-ending files is **superseded for this first pass**. The user accepts the current You and Ye Ye Ye captures and their preserved listening reports. Both source recordings remain **audibly truncated**, but each contains substantial analysed material. `ANALYSIS_COMPLETE_FOR_AVAILABLE_AUDIO: true` and `SOURCE_RECORDING_COMPLETE: false` are recorded separately in their song JSON files. Post-cutoff lyric, hook, outro and production behaviour remains unavailable. No re-recording, replacement file or new Listening Analyst request is pending. This is an analysis-scope decision; it does not alter the technical measurements or imply that the missing endings have been heard.
