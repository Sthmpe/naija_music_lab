# What Have We Done — audio discovery, acquisition and capture guide

Target: the five original recordings on Omah Lay's *What Have We Done* EP, released 2020-11-20 ([Spotify release listing, S3](https://open.spotify.com/album/4PYDryHrfDvfnUHvZ2eqKv)). Audio is a PRIVATE WORKING RESEARCH INPUT, used only for non-commercial analysis. Audio files stay out of Git (`.gitignore` excludes every audio extension), and none is redistributed.

## Current status (2026-11-14)

| # | Approved recording | Target filename | Status |
|---:|---|---|---|
| 1 | My Bebe | `my-bebe.wav` | USER_FILE_REQUIRED |
| 2 | Can't Relate | `cant-relate.wav` | USER_FILE_REQUIRED |
| 3 | Godly | `godly.wav` | USER_FILE_REQUIRED |
| 4 | Confession | `confession.wav` | USER_FILE_REQUIRED |
| 5 | Damn (feat. 6LACK) | `damn-feat-6lack.wav` | USER_FILE_REQUIRED. **It must be the 6LACK version, not the solo Get Layd Damn.** |

Platform durations have not been re-checked in this session, because the web was unreachable. Verify them when audio arrives, and don't treat any remembered value as a measurement.

## Discovery log — 2026-11-14 cloud session

The user authorized downloading or recording audio for private research. Tools were ready: `ffmpeg`/`ffprobe` were present, and `yt-dlp` 2026.10.26 was installed through PyPI.

| Source | Host(s) tested | Result |
|---|---|---|
| YouTube (official Omah Lay / label uploads) | `www.youtube.com` | Proxy refused the connection (403), so no page or media was reached. Media is also served from rotating `*.googlevideo.com` hosts, which need a wildcard allowance in environment settings. |
| Audiomack (artist uploads) | `audiomack.com` | Proxy refused the connection (403) |
| SoundCloud (artist uploads) | `soundcloud.com`, `api-v2.soundcloud.com` | Proxy refused the connection (403) |
| Boomplay | `www.boomplay.com` | Proxy refused the connection |
| Spotify / Apple Music | `open.spotify.com`, `music.apple.com`, `audio-ssl.itunes.apple.com` | Proxy refused the connection. These are DRM streams in any case, with no downloadable file. |
| TrendyBeatz / Mdundo / Internet Archive | `trendybeatz.com`, `mdundo.com`, `archive.org` | Proxy refused the connection |

**Cause:** the cloud environment's network policy (limited access, empty allowlist). The sources themselves were not tested. A request to allowlist the SoundCloud, Audiomack and YouTube hosts could not be shown in the user's current app version. Nothing was changed.

**Re-try path (no user file needed):** from claude.ai on a computer or an updated app, allow these hosts:

- SoundCloud: `soundcloud.com`, `api-v2.soundcloud.com`, `a-v2.sndcdn.com`, `cf-media.sndcdn.com`, `cf-hls-media.sndcdn.com`, `cf-hls-opus-media.sndcdn.com`, `playback.media-streaming.soundcloud.cloud`
- Audiomack: `audiomack.com`, `api.audiomack.com`, `music.audiomack.com`
- YouTube: `www.youtube.com`, `youtube.com`, `music.youtube.com`, plus `*.googlevideo.com` added in Settings

Then fetch the official uploads with `yt-dlp -x` into this folder and run the identity checks below.

## User capture guide — recording playback on a Mac

This is the same route as the Get Layd private captures. Apple Music cannot run inside the Linux cloud container, so the recording has to be made on the user's Mac.

**One-time setup**

1. Install **BlackHole 2ch**, a free virtual audio device (existing-bit.github.io/blackhole), and **Audacity** (free).
2. Open **Audio MIDI Setup**, click **+**, choose **Create Multi-Output Device**, and tick both your speakers/headphones and **BlackHole 2ch**. You can then hear the music while it records.
3. In **System Settings → Sound → Output**, choose that Multi-Output Device.
4. In **Audacity**, set the recording device to **BlackHole 2ch**, the channels to **2 (Stereo)**, and the project rate to **44100 Hz**.

**Player settings (important; these caused the two truncated Get Layd captures)**

- Apple Music → Settings → Playback: turn **Crossfade off**, **Sound Check off**, **Sound Enhancer off**, **Dolby Atmos/Spatial off**, and the **EQ off**.
- Turn off Autoplay / "continue playing", and set the app volume to 100%.
- Play the **What Have We Done EP** tracks, not singles, remixes, sped-up versions, live versions or the solo Damn.

**For each song**

1. Press record in Audacity, then press play on the song from 0:00.
2. **Let it play to the natural end** (fade or stop), then wait 3 more seconds before stopping. Don't stop early.
3. Use **File → Export → WAV, 16-bit PCM**, with the filename from the table above.
4. If a recording comes out silent, Apple Music has blocked the capture. Play the same track from the official YouTube or Audiomack upload, or from Spotify, instead.

**Getting the files to the lab:** upload the five WAVs to a Google Drive folder and share its name in the session (the lab can read Drive), attach them in the session, or place them in `artists/01-omah-lay/audio/what-have-we-done/` in a local checkout. They stay untracked by Git.

## Identity checks to run on arrival

For each file: decode it with `ffprobe`, record its SHA-256, format and duration, compare with the platform duration, and check for a natural ending versus a cutoff. Confirm it is the EP version, not a remix, live, sped-up, slowed, edited or alternate version. For track 5, confirm a 6LACK vocal is present and that it differs from the solo Get Layd Damn. Hold anything ambiguous before analysis.
