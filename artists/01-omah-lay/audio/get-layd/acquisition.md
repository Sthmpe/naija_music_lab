# Get Layd audio discovery and acquisition record

**2026-09-25 intake update:** All five named capture files are now present. The prior web-access outcomes below are a dated discovery history, not the current local-file status. See [technical-intake.md](technical-intake.md) for file hashes, decoded durations, signal windows and the two incomplete-capture flags. No audio-based song analysis was completed in this intake.

**2026-09-25 Damn provenance clarification:** The artist-uploaded [Audiomack Get Layd Damn page](https://audiomack.com/omah-lay/song/damn) is a documented *release source*. The capture intake records only the user's statement that the supplied MP3/WAV are private captures of computer playback; it does **not** record the playback URL used for `damn.wav`. Therefore a direct Audiomack-to-WAV acquisition chain is **not yet documented**. If the capture operator confirms that chain, record it as strong source/version provenance; it still would not establish bit-for-bit identity with a commercial master. Missing ID3 tags do not by themselves invalidate a documented acquisition chain. The targeted [listening-verification request](../../projects/get-layd/songs/damn/listening-verification-request.md) separates these questions from the short remaining audio checks.

**2026-09-25 Damn verification outcome:** The user-supplied [targeted listening response](../../projects/get-layd/songs/damn/listening-verification.md) finds the heard performance consistent with the approved solo original: no obvious 6LACK/guest verse, live audience, remix insertion, edit or speed artifact. This raises version confidence enough for first-pass song analysis. It does **not** document the capture playback URL or prove bit-identical commercial-master identity. The latter distinctions remain recorded as limits, not as reasons to discard the technically intact WAV.

**2026-09-26 four-song WAV recheck:** Current `lo lo.wav`, `you.wav`, `Bad influence.wav`, and `ye ye ye.wav` replaced the earlier MP3 filenames in the local folder. All decode as uncompressed 16-bit stereo/44.1-kHz PCM without frame-count errors. Durations and whole-mix boundaries are in [technical intake](technical-intake.md) and [wav-intake.json](wav-intake.json). Lo Lo and Bad Influence are plausible complete captures; You and Ye Ye Ye still end with substantial signal and are respectively ~7.2 s and ~12.7 s shorter than the EP listing. No audible version check has yet been made for any of these four. A separate targeted [Lo Lo](../../projects/get-layd/songs/lo-lo/listening-request.md), [You](../../projects/get-layd/songs/you/listening-request.md), [Bad Influence](../../projects/get-layd/songs/bad-influence/listening-request.md), and [Ye Ye Ye](../../projects/get-layd/songs/ye-ye-ye/listening-request.md) request is prepared; a partial-file response cannot validate a missing ending.

Checked 2026-09-24. Target: the five original solo recordings on Omah Lay's *Get Layd* EP, May 22, 2020. [Spotify's EP page](https://open.spotify.com/album/3wzSqNDc2jNNV42XLkkDMA) gives the sequence and reference lengths 2:39, 2:51, 2:43, 2:18 and 3:27. These are **platform durations**, not measurements from obtained files. `artists/01-omah-lay/audio/get-layd/` did not exist before this record was created; no audio file was found in the workspace.

**Technical test:** the research web tool retrieves page text and metadata, but does not deliver audio bytes or operate embedded players. `curl.exe -I -L` against an Audiomack song, the Apple EP and an official YouTube video each failed before HTTP contact with `Failed to connect to 127.0.0.1 port 9`. No local `ffmpeg`, `ffprobe`, `yt-dlp` or Python audio-decoding package is installed. Therefore a public player visible in a webpage is not evidence that this environment heard or could measure its recording. No stream was extracted and no download was attempted from a source with unclear rights.

Column meanings: **Playable** refers to a player advertised for a normal consumer, not playback by the research environment. **Downloadable** is a clear authorized audio-file option visible in the accessible page, not mere purchase availability. **Technical access** means usable audio bytes reached the analysis environment. `No` in that column applies to each source listed below. Identifications from pages remain provisional until the recording itself is checked.

## 1. Damn

| Source checked / URL | Source type | Playable? | Downloadable? | Technical access? | Version identity | Authorization/licensing | Result / reason unusable |
|---|---|---|---|---|---|---|---|
| [Official audio](https://www.youtube.com/watch?v=ovu4cD7AzoE) | Omah Lay official channel, KeyQaad/Dvpper | Web player advertised | No authorized file link shown | No | Explicitly off *Get Layd*; original target likely | Official upload; viewing authorized, copying rights not stated | Page/description only; player inaccessible to tools and direct connection failed. |
| [Audiomack original](https://audiomack.com/omah-lay/song/damn) | Artist-uploaded song page | Web player advertised | No clear file option visible | No | Album *Get Layd*, May 22 2020 | KeyQaad/Sire rights displayed | Page only; direct connection failed. |
| [Audiomack later listing](https://audiomack.com/omah-lay/song/damn-af) | Artist page, later catalogue entry | Region restriction displayed | No clear file option | No | 2025 entry; equivalence to 2020 mix unverified | Rightsholder says unavailable in displayed country | Reject as region-restricted and unverified version. |
| [SoundCloud EP](https://soundcloud.com/omah_lay/sets/get-layd-1) | Artist-named 2020 playlist | Web player advertised | No per-track file option established | No | Lists original five in order | Playlist displays `cc-by`; track-level rights/download scope unverified | Web tool exposes text only; direct media unavailable. |
| [Spotify EP](https://open.spotify.com/album/3wzSqNDc2jNNV42XLkkDMA) / [Apple EP](https://music.apple.com/us/album/get-layd-ep/1528527067) | Licensed streaming/storefront | Web preview/player advertised | No accessible licensed file | No | Original EP, 2:39 | Licensed consumer listening; extraction rights not granted | Metadata only; Apple direct connection failed. |
| [TrendyBeatz page](https://trendybeatz.com/legal-download/10180/omah-lay-damn) | Nigerian aggregator, YouTube/store links | Advertised | No verifiable licensed file | No | Says EP track 1 | Independent download permission unverified | Embeds/links do not yield analysable audio here. |
| [Qobuz EP](https://www.qobuz.com/us-en/album/get-layd-omah-lay/r607vhrrtdgib) | Licensed storefront | Preview advertised | Purchase may be offered; no acquired file | No | Original EP listing | Commercial license required | No purchase/account/audio access in environment. |
| [Hometown Heroes performance](https://audiomack.com/omah-lay/song/damn-hometown-heroes-version) | Alternate performance | Advertised | No | No | Explicitly different version | Artist page | Reject as non-EP performance. The later 6LACK version is also outside this first batch. |

**Status: USER_FILE_REQUIRED.** No correct-version audio was acquired or heard; 2:39 remains a reference only.

## 2. Lo Lo

| Source checked / URL | Source type | Playable? | Downloadable? | Technical access? | Version identity | Authorization/licensing | Result / reason unusable |
|---|---|---|---|---|---|---|---|
| [Official audio](https://www.youtube.com/watch?v=RjddVMNtTNg) | Omah Lay official channel, KeyQaad/Dvpper | Web player advertised | No authorized file link | No | Explicitly *Get Layd* cut | Official viewing | Page only; YouTube direct connection failed. |
| [Audiomack original](https://audiomack.com/omah-lay/song/lo-lo) | Artist-uploaded song page | Advertised | No clear file option | No | May 22 2020, *Get Layd* | KeyQaad/Sire displayed | Page only; Audiomack direct connection failed. |
| [Audiomack later listing](https://audiomack.com/omah-lay/song/lo-lo-1) | Later catalogue entry | Region restriction displayed | No | No | 2025 entry, equivalence unverified | Rightsholder restriction | Reject: unavailable in displayed country, version unchecked. |
| [SoundCloud EP](https://soundcloud.com/omah_lay/sets/get-layd-1) | Artist-named 2020 playlist | Advertised | No per-track option established | No | Lists Lo Lo as track 2 | Playlist `cc-by` display does not settle track-file rights | Text only. |
| [Spotify EP](https://open.spotify.com/album/3wzSqNDc2jNNV42XLkkDMA) / [Apple EP](https://music.apple.com/us/album/get-layd-ep/1528527067) | Licensed platforms | Preview/player advertised | No accessible file | No | Original EP, 2:51 | Consumer streaming | Metadata only; Apple connection failed. |
| [TrendyBeatz page](https://trendybeatz.com/legal-download/6518/omah-lay-lolo) | YouTube/store aggregator | Advertised | No verifiable licensed file | No | Says EP track 2 | Independent copy rights unclear | Redirect/embed only; no audio bytes. |
| [Qobuz EP](https://www.qobuz.com/us-en/album/get-layd-omah-lay/r607vhrrtdgib) | Storefront | Preview advertised | Purchase possible, no acquired file | No | Original EP listing | Commercial license required | No account/purchase. |
| [Lo Lo mashup](https://audiomack.com/drexmusiq/song/lo-lo-so-mi-so-mashup) | Third-party mashup | Advertised | No | No | Explicit mashup | Not the EP master | Reject as alternate. |

**Status: USER_FILE_REQUIRED.** No correct-version audio was acquired or heard; 2:51 remains a reference only.

## 3. You

| Source checked / URL | Source type | Playable? | Downloadable? | Technical access? | Version identity | Authorization/licensing | Result / reason unusable |
|---|---|---|---|---|---|---|---|
| [Official EP audio](https://www.youtube.com/watch?v=hJ8-7clGZKs) | Omah Lay official channel, KeyQaad/Dvpper | Web player advertised | No authorized file link | No | Explicitly *Get Layd* EP audio | Official viewing | Page only; YouTube connection failed. |
| [Audiomack original](https://audiomack.com/omah-lay/song/you) | Artist-uploaded song page | Advertised | No clear file option | No | Listed with *Get Layd* but February 14 single date | KeyQaad/Sire displayed | Page only; compare audio with EP when available. |
| [Audiomack later listing](https://audiomack.com/omah-lay/song/you-af) | Later catalogue entry | Region restriction displayed | No | No | 2025 entry, version equivalence unverified | Rightsholder restriction | Reject as unavailable/unverified. |
| [SoundCloud EP](https://soundcloud.com/omah_lay/sets/get-layd-1) | Artist-named 2020 playlist | Advertised | No per-track option established | No | Lists You as track 3 | Playlist `cc-by` display does not settle track-file rights | Text only. |
| [Spotify EP](https://open.spotify.com/album/3wzSqNDc2jNNV42XLkkDMA) / [Apple EP](https://music.apple.com/us/album/get-layd-ep/1528527067) | Licensed platforms | Preview/player advertised | No accessible file | No | EP 2:43; Apple song date may show earlier single | Consumer streaming | Metadata only; Apple connection failed. |
| [TrendyBeatz page](https://trendybeatz.com/legal-download/1537/omah-lay-you) | YouTube/store aggregator | Advertised | No verifiable licensed file | No | Says EP track 3 | Independent copy rights unclear | No audio bytes. |
| [Qobuz EP](https://www.qobuz.com/us-en/album/get-layd-omah-lay/r607vhrrtdgib) | Storefront | Preview advertised | Purchase possible, no acquired file | No | Original EP listing | Commercial license required | No account/purchase. |
| [You alternate-cut listing](https://trendybeatz.com/legal-download/6785/omah-lay-untitled-1-you-alternate-cut) | Alternate version | Advertised | Unclear | No | Explicit alternate cut | Not target EP cut | Reject as alternate. |

**Status: USER_FILE_REQUIRED.** No correct-version audio was acquired or heard; 2:43 remains a reference only. February single-versus-May EP recording identity remains unresolved.

## 4. Bad Influence

| Source checked / URL | Source type | Playable? | Downloadable? | Technical access? | Version identity | Authorization/licensing | Result / reason unusable |
|---|---|---|---|---|---|---|---|
| [Official EP audio](https://www.youtube.com/watch?v=o5KyLuuqFms) / [official lyric video](https://www.youtube.com/watch?v=2CSZKpQ0J5s) | Omah Lay channel | Web player advertised | No authorized file link | No | EP audio and earlier single lyric video; equivalence unverified | Official viewing | Page only; YouTube connection failed. |
| [Audiomack original](https://audiomack.com/omah-lay/song/bad-influence) | Artist-uploaded song page | Advertised | No clear file option | No | Listed on *Get Layd* with January single date | KeyQaad/Sire displayed | Page only; Audiomack connection failed. |
| [SoundCloud EP](https://soundcloud.com/omah_lay/sets/get-layd-1) | Artist-named 2020 playlist | Advertised | No per-track option established | No | Lists track 4 | Playlist `cc-by` display does not settle track-file rights | Text only. |
| [Spotify EP](https://open.spotify.com/album/3wzSqNDc2jNNV42XLkkDMA) / [Apple EP](https://music.apple.com/us/album/get-layd-ep/1528527067) | Licensed platforms | Preview/player advertised | No accessible file | No | EP 2:18 | Consumer streaming | Metadata only; Apple connection failed. |
| [TrendyBeatz page](https://trendybeatz.com/legal-download/7620/omah-lay-bad-influence) | YouTube/store aggregator | Advertised | No verifiable licensed file | No | Says EP track 4 | Independent copy rights unclear | No audio bytes. |
| [Qobuz EP](https://www.qobuz.com/us-en/album/get-layd-omah-lay/r607vhrrtdgib) | Storefront | Preview advertised | Purchase possible, no acquired file | No | Original EP listing | Commercial license required | No account/purchase. |
| [Chopped-and-screwed catalogue](https://audiomack.com/replaymedia) | Third-party alternate | Advertised | No | No | Explicit changed speed/mix | Not EP master | Reject as alternate. |

**Status: USER_FILE_REQUIRED.** No correct-version audio was acquired or heard; 2:18 remains a reference only.

## 5. Ye Ye Ye

| Source checked / URL | Source type | Playable? | Downloadable? | Technical access? | Version identity | Authorization/licensing | Result / reason unusable |
|---|---|---|---|---|---|---|---|
| [Label-supplied YouTube audio](https://www.youtube.com/watch?v=AMi2KdLIhxs) | KeyQaad/Sire auto-generated official track | Web player advertised | No authorized file link | No | Explicit *Get Layd* track | Official viewing | Page only; YouTube connection failed. |
| [Audiomack original](https://audiomack.com/omah-lay/song/ye-ye-ye) | Artist-uploaded song page | Advertised | No clear file option | No | May 22 2020, *Get Layd* | KeyQaad/Sire displayed | Page only; Audiomack connection failed. |
| [Audiomack later listing](https://audiomack.com/omah-lay/song/ye-ye-ye-9060415) | Later catalogue entry | Region restriction displayed | No | No | 2025 entry, version equivalence unverified | Rightsholder restriction | Reject as unavailable/unverified. |
| [SoundCloud EP](https://soundcloud.com/omah_lay/sets/get-layd-1) | Artist-named 2020 playlist | Advertised | No per-track option established | No | Lists track 5 | Playlist `cc-by` display does not settle track-file rights | Text only. |
| [Spotify EP](https://open.spotify.com/album/3wzSqNDc2jNNV42XLkkDMA) / [Apple EP](https://music.apple.com/us/album/get-layd-ep/1528527067) | Licensed platforms | Preview/player advertised | No accessible file | No | EP 3:27 | Consumer streaming | Metadata only; Apple connection failed. |
| [TrendyBeatz page](https://trendybeatz.com/legal-download/65410/omah-lay-ye-ye-ye) | YouTube/store aggregator | Advertised | No verifiable licensed file | No | Says EP track 5 | Independent copy rights unclear | No audio bytes. |
| [Qobuz EP](https://www.qobuz.com/us-en/album/get-layd-omah-lay/r607vhrrtdgib) | Storefront | Preview advertised | Purchase possible, no acquired file | No | Original EP listing | Commercial license required | No account/purchase. |
| [Artist's Vibez Video](https://www.youtube.com/watch?v=kp3E-99AgQE) | Separate official video | Advertised | No | No | Video labelled separately, EP-master equivalence unverified | Official viewing | Reject as version evidence insufficient; use label-supplied EP track when possible. |

**Status: USER_FILE_REQUIRED.** No correct-version audio was acquired or heard; 3:27 remains a reference only.

## Other platforms checked

Searches for Boomplay, Mdundo, Bandcamp and Waploaded returned no accessible, clearly licensed individual *Get Layd* master file. Mdundo exposed [editorial coverage](https://mdundo.com/news/24454), not playable track data; Waploaded exposed [a DJ mixtape](https://audios.waploaded.com/music/417341/dj-donak-best-of-omah-lay) and [an instrumental](https://audios.waploaded.com/music/378990/omah-lay-bad-influence-in), both wrong versions. Boomplay coverage confirmed the [label/distributor partnership](https://tribuneonlineng.com/omah-lay-hits-100-million-streams-on-boomplay-through-keyqaad-dvpper-digital-partnership/) but yielded no usable song page. Searches for a Bandcamp EP returned no relevant listing. The [KeyQaad site](https://keyqaad.com/) and [Warner artist page](https://www.warnerrecords.com/node/1756) yielded catalogue/news context but no accessible licensed audio file. An [independent MP3 aggregation page](https://mpmania.com/songs/album/omah-lay-get-layd/) advertises downloads, but authorization for redistributing these masters was not established, and direct network access is blocked. It was not used.

**Next intake:** receive only the five files listed above, each original EP commercial mix. On receipt, compare file tags, codec duration, audible intro/outro, voice and arrangement to the official EP reference; reject or flag a mismatch before audio-based claims. No Get Layd song-level or project-level listening synthesis is complete.

## 2026-09-27 current capture and listening status

The earlier per-source `USER_FILE_REQUIRED` entries were historical discovery outcomes before the user captures arrived. Current WAVs and four separately supplied Listening Analyst reports are available. Lo Lo and Bad Influence have coherent endings and completed first song-level passes. You and Ye Ye Ye were confirmed by listening to cut off while audio remained active; only their **complete original EP recordings** remain required to finish Get Layd. The partial material has been analysed to the audible endpoint. Do not request replacement of Damn, Lo Lo or Bad Influence for routine first-pass completion. See `technical-intake.md`, each song's `listening-analysis.md`, and the artist acquisition manifest.

## 2026-09-28 completeness-basis correction

Historical `USER_FILE_REQUIRED` entries and 2026-09-26 duration flags describe what was known before the song-specific listening reports. A different duration from Spotify does **not** make a private playback capture incomplete. Current You and Ye Ye Ye files remain incomplete because their preserved Listening Analyst reports hear a hard stop while the respective refrain and groove continue. Need only source-valid audio that reaches a natural ending; its exact duration may differ from platform reference metadata. Bit-identical commercial-master proof is not a first-pass prerequisite.

## 2026-09-28 accepted source-limited first pass

The user's latest explicit decision supersedes the preceding file-request recommendation **for Get Layd's first pass**: do not request re-recorded or replacement You or Ye Ye Ye audio and do not send a further listening packet. Keep their audible cutoff and unknown endings in the song records. Their analyses are complete for available audio, and the project synthesis may close with 3 full-ending captures plus 2 truncated captures. Earlier source-by-source acquisition attempts remain historical evidence, not active file requests.
