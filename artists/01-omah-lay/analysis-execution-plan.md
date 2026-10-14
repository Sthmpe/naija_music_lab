# Omah Lay first-pass deep-analysis execution plan

Status: **authorized corpus; song-level analysis in progress**. Approved selections are authoritative in `selection.md`. Do not alter them without documenting the reason and seeking user approval. Omah Lay remains the only active artist.

## Count and grouping

There are **34 primary recordings**, plus **one special comparative remix recording**, for **35 recording-level cases**. The 25 project/deluxe primary tracks include two recordings of the composition `Damn` (original and 6LACK version), so recording count and distinct-composition count are different. The Ozuna `soso` remix is the separate 35th case, not a fifth independent era.

| Group | Approved recordings | Count |
|---|---|---:|
| Get Layd — complete EP | Damn; Lo Lo; You; Bad Influence; Ye Ye Ye | 5 |
| What Have We Done — complete EP | My Bebe; Can't Relate; Godly; Confession; Damn (feat. 6LACK) | 5 |
| Boy Alone — representative sample | soso; i'm a mess; understand; woman; never forget | 5 |
| Boy Alone deluxe — new compositions, within Boy Alone era | reason; come closer; it's yours; imagine (feat. Aitch); joanna | 5 |
| CLARITY OF MIND — representative sample | DON'T LOVE ME; WAIST; CANADA BREEZE; HOLY GHOST; ARTIFICIAL HAPPINESS | 5 |
| Solo non-project — primary | Free My Mind; Moving | 2 |
| Collaborative non-project / current release — primary | Company — Clean Bandit, Chlöe & Omah Lay | 1 |
| Collaboration / Feature Lab — primary | Infinity; PAMI; Philo; People (Remix); One Call; With You | 6 |
| Special comparison | soso (with Ozuna), compared against original soso | 1 |

`Do Not Disturb` and `Hello Brother` are early solo **validation** candidates, not primary. All unselected album tracks and the wider collaboration inventory remain available for targeted validation or an approved replacement.

## Analysis order

1. **Source and audio audit:** verify release versions, source URLs, credits, lyric-transcription availability, official streams/previews and legal audio acquisition options for all 35 cases. Record conflicts and access dates. Do not treat a streaming listing as proof that the audio was heard.
2. **Get Layd:** analyse all five tracks independently. This establishes the earliest approved project baseline. `Damn` original must precede the 6LACK comparison.
3. **What Have We Done:** analyse all five, including the 6LACK `Damn` recording as its own performance and comparative case.
4. **Boy Alone:** analyse its five primary tracks. Original `soso` must precede the Ozuna remix comparison.
5. **Boy Alone deluxe:** analyse five new compositions, then the Ozuna `soso` comparison. Keep the deluxe within the Boy Alone era in later synthesis.
6. **CLARITY OF MIND:** analyse its five primary tracks.
7. **Non-project recordings:** analyse Free My Mind and Moving as solo recordings, and Company as a separate collaborative current release credited to Clean Bandit, Chlöe and Omah Lay. Keep all three in the locked corpus and Company outside the six-case Feature Lab.
8. **Collaboration lab:** analyse all six approved cases. Verify the actual vocal/creative contribution and map which phrases are Omah Lay's before interpreting songwriting or cadence. Do not substitute reserve songs without approval.
9. **Targeted validation:** when a candidate pattern needs testing, use unselected tracks as validation material and record why. A new primary analysis requires corpus-change approval.
10. **Synthesis:** complete project profiles after their selected songs; complete collaboration behaviour after all six feature analyses; write artist profile, songwriting/vocal/production DNA, evolution, prompt card and originality guardrails only after all approved song-level analyses and required project profiles are complete.

The order supports chronology, but independent songs within a group can be researched separately. Standalone and collaboration source audits can run alongside project-track work. The `Damn` and `soso` comparisons depend on their original versions. Project profiles depend on every selected song in that project. Collaboration behaviour depends on all six approved collaboration analyses. Artist-wide claims and `evolution.md` depend on all approved song analyses and project-level synthesis.

## Audio acquisition and fallback

For each case, look for an authorized official artist/label stream, platform preview or downloadable source that the environment can actually access and analyse. Record the URL, rights/access basis, exact version, format, duration and whether audio was heard. Do not scrape restricted streams or use unlicensed reposts. If official playback is unavailable in this environment after reasonable source checks, set `AUDIO_STATUS: USER_FILE_REQUIRED` for that recording, add it to `PROJECT_STATE.md -> AUDIO_FILES_REQUIRED`, request a user-supplied MP3/WAV/AAC/M4A/FLAC/OGG for the missing audio portion, and continue source/lyric work on the rest. Never manufacture BPM, key, timestamps, vocal or production observations from a page description or lyric transcription.

The [35-recording acquisition manifest](audio-acquisition-manifest.md) identifies every approved recording and its intake status. That initial no-local-audio finding is historical. All five Get Layd song analyses are complete for the first pass. Damn, Lo Lo and Bad Influence use supplied captures with coherent endings; You and Ye Ye Ye use substantial truncated captures accepted by the user for source-limited first-pass analysis. Their endings remain unavailable, and no Get Layd replacement is requested. The other approved recordings retain separate acquisition dependencies.

## Song deliverables and quality gate

Each approved recording gets `analysis.md` and `analysis.json` using the current templates. Every factual claim carries a URL or a logged audio measurement; observations, interpretations, estimates and unknowns are separate. The minimum headings cover basic data, structure, cadence, phonetics, language, songwriting/story, why simple lines sound musical, hook, vocals, production, lyric/audio interaction, story units, findings and limitations. Mark audio-dependent fields unknown where audio is unavailable. Keep only small necessary lyric excerpts. Add source links to `source-index.md`. Update `PROJECT_STATE.md` after each meaningful task and append `SESSION_LOG.md` entries rather than rewriting prior entries.
# 2026-09-27 Get Layd execution checkpoint

The five approved Get Layd recordings now have independent first-pass song files. Damn, Lo Lo and Bad Influence are complete from captures with audible endings. You and Ye Ye Ye are **complete for available audio**, while their current WAVs remain audibly truncated. Spotify duration differences are not a completeness criterion. The [first-pass project synthesis](projects/get-layd/project-profile.md) and [pipeline evaluation](projects/get-layd/pipeline-evaluation.md) close Get Layd within documented coverage. This checkpoint supersedes earlier replacement-audio handoff statuses in this plan; the approved corpus and later-project order are unchanged. What Have We Done is next but has not begun deep song analysis.
