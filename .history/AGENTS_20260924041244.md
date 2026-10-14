# Agent Rules

## Mandatory Session Bootstrap

Before doing any substantive work, rehydrate yourself from the repository.

Read, in this order:

1. `README.md`
2. `AGENTS.md`
3. `PROJECT_STATE.md`
4. `DECISIONS.md`
5. the most recent relevant entries in `SESSION_LOG.md`
6. the most recent relevant entries in `CHANGELOG.md`
7. methodology files relevant to the current task
8. schemas/templates relevant to the current task
9. the current artist's `selection.md`
10. the current artist's execution plan, manifests, source indexes, project profiles, or other files relevant to the current task

Do not rely only on the newest user prompt.

The repository is the persistent memory of Naija Music Lab. Previous approved decisions remain authoritative unless the user explicitly changes them.

If the newest prompt appears to conflict with an existing project rule:

- inspect the relevant repository files first;
- preserve the existing rule unless the user is explicitly changing it;
- document any approved change instead of silently replacing previous methodology.

---

## Core Rules

1. `PROJECT_STATE.md` is authoritative.

   Deep research is restricted to `CURRENT_ARTIST`.

   Directory existence grants no research authorization.

2. Begin a new artist with verified discography reconnaissance.

   Present project candidates and stop for user project approval.

   After approval, show complete selected-project track lists, important standalone songs, and collaboration candidates, then stop for user song approval.

   The user has final selection authority.

3. Do not perform deep song analysis before the required project/song approvals.

   Analyse every approved song independently in:

   - `analysis.md`
   - `analysis.json`

   before project-level synthesis.

   Complete approved projects, standalone material, and required collaboration cases before final artist-level synthesis.

4. Record source URLs and access dates where practical.

   Distinguish:

   - verified facts
   - measurements
   - estimates
   - interpretations
   - hypotheses
   - unknowns

   Cross-check conflicting metadata and Nigerian-language transcriptions.

   Never fabricate missing data.

5. Raw lyrics and commercial audio may be used as PRIVATE WORKING RESEARCH INPUTS according to the rules below.

   Do not publish or export full commercial lyrics as a public dataset.

   Do not redistribute commercial audio.

   The permanent intellectual value of Naija Music Lab should be the analytical findings, measurements, structured data, and transferable principles extracted from those inputs.

   Research audio should remain excluded from Git.

6. Audio analysis requires actual accessible audio.

   Before setting:

   `AUDIO_STATUS: USER_FILE_REQUIRED`

   perform a reasonable audio-discovery pass according to the Audio Discovery and Acquisition rules below.

   Do not treat:

   `audio file not found locally`

   as equivalent to:

   `audio unavailable`.

7. Separate findings into:

   - song-specific
   - project-specific
   - possible patterns
   - probable patterns
   - repeated/strong patterns

   Do not generalize one song into an artist-wide rule.

   Do not populate `global/` heavily during the first artist.

8. New metrics may be added as documented experiments.

   Do not remove or weaken required metrics.

   Record methodological/schema changes in `CHANGELOG.md`.

   Record major choices and their reasoning in `DECISIONS.md`.

9. Update `PROJECT_STATE.md` after every meaningful research task.

   Append a concise entry to `SESSION_LOG.md`.

   Do not rewrite previous session-log entries.

10. Extract transferable songwriting, vocal, production, rhythmic, linguistic, melodic and structural principles.

    Do not instruct future generation systems to reproduce identifiable:

    - lyrics
    - melodies
    - catchphrases
    - signature lyrical combinations
    - recognizable song-specific structures

11. For Omah Lay, the complete user-approved corpus is locked at the top of:

    `artists/01-omah-lay/selection.md`

    Deep analysis is authorized.

    The corpus contains the approved primary recordings plus the special `soso` / Ozuna comparative case.

    Across future artists, include:

    `collaboration-behaviour.md`

    using the standard template.

    Verify the artist's actual contribution before selecting collaboration/feature cases for deep analysis.

---

# Raw Lyrics Working Layer

Complete lyrics are a required working research input whenever they can be reliably obtained.

For each selected song:

1. Search multiple credible lyric sources where possible.

   Sources may include:

   - Genius
   - Musixmatch
   - LyricFind-powered results
   - Shazam
   - official lyric pages
   - official lyric videos
   - artist/label sources
   - publisher/songwriter sources
   - other credible lyric databases discovered during research

2. Create a private working transcription.

3. Cross-check disagreements between sources.

4. Once audio is available, verify the transcription against the actual performance.

5. Preserve performance details that conventional lyric pages may omit, including:

   - repetitions
   - ad-libs
   - backing responses
   - Nigerian Pidgin
   - Yoruba
   - Igbo
   - other language material
   - slang
   - shortened words
   - phonetic spellings
   - intentionally altered pronunciation
   - incomplete phrases
   - repeated vocal sounds where analytically relevant

6. Mark uncertain words rather than guessing.

   Use a consistent notation such as:

   `[unclear]`

   or:

   `[possible: ...]`

7. Use the working transcription for:

   - syllable analysis
   - cadence analysis
   - rhyme analysis
   - phonetics
   - code-switching
   - hook analysis
   - repetition analysis
   - story analysis
   - pronunciation analysis
   - lyric/audio alignment

8. Where useful, align phrases to approximate:

   - timestamps
   - bars
   - beats
   - structural positions

   The purpose is analytical alignment, not karaoke-file creation.

9. Keep raw lyrics organised inside the current artist's private working area, for example:

   `artists/<artist>/lyrics/<project>/`

10. Raw lyrics are PRIVATE WORKING INPUTS.

    They are not the principal permanent product of Naija Music Lab.

    Do not publish or export complete commercial lyrics as a public/shared dataset.

The permanent value remains the extracted intelligence contained in:

- `analysis.md`
- `analysis.json`
- project profiles
- songwriting findings
- cadence findings
- phonetic findings
- hook findings
- vocal findings
- production findings
- artist synthesis
- cross-artist synthesis

---

# Audio Discovery and Acquisition

Audio analysis is a core requirement of the lab.

For every selected recording that lacks local audio, perform a reasonable discovery pass BEFORE requesting a file from the user.

Search broadly where technically accessible.

Potential discovery sources include:

- official artist uploads
- official label/distributor uploads
- artist websites
- label websites
- YouTube / YouTube Music
- Spotify
- Apple Music
- Audiomack
- Boomplay
- SoundCloud
- Bandcamp
- Mdundo
- TrendyBeatz
- Waploaded
- other Nigerian/African music platforms
- other relevant music sources discovered during research

Do not stop after checking only one source.

For each useful candidate source, determine where possible:

- correct song/version?
- playable?
- downloadable?
- technically accessible to the research environment?
- full recording or preview?
- sufficient for meaningful analysis?
- source/authorization status where determinable?

If an authorized or otherwise clearly permitted downloadable copy is accessible, it may be downloaded into the private research workspace for analysis.

If an authorized stream or preview can be technically analysed without downloading, use it directly.

If a source can be discovered but cannot technically be listened to or analysed, document that limitation and continue searching.

Do not claim that audio was analysed merely because a webpage containing a player was found.

---

## Audio Discovery Log

Maintain the artist's acquisition manifest.

Where useful record:

- song
- version
- source
- URL
- source type
- date checked
- playable status
- download/access status
- technical accessibility
- result
- reason rejected or accepted

Avoid repeating already documented failed attempts unless circumstances have changed.

---

## User-File Fallback

Only after reasonable discovery attempts fail should a recording be marked:

`AUDIO_STATUS: USER_FILE_REQUIRED`

When this occurs:

- identify the exact recording/version needed;
- record sources already checked;
- add the blocker to `PROJECT_STATE.md`;
- continue non-audio research where possible;
- do not unnecessarily block unrelated songs.

When the user later supplies:

- MP3
- WAV
- AAC
- M4A
- FLAC
- OGG
- or another supported format

verify the file identity before using it.

Check that it is not accidentally:

- a remix
- alternate mix
- live performance
- sped-up version
- slowed version
- edit
- feature version
- clean/explicit alternate where that distinction matters

---

# Audio Analysis Requirements

Where audio permits, investigate at minimum:

- duration
- BPM
- tempo stability
- key / tonal centre
- time signature
- section boundaries
- first-vocal timestamp
- first-hook timestamp
- section duration
- phrase duration
- vocal density
- negative space
- melodic contour
- melodic range
- recurring melodic cells
- held vowels
- vocal register
- backing vocals
- harmonies
- ad-libs
- vocal doubling
- drum pocket
- kick placement
- snare/rim placement
- percussion
- bass movement
- instrumental responses
- drops
- transitions
- energy changes

Where measurements are approximate, label them as approximate.

---

# Lyric + Audio Interaction

Do not analyse lyrics and audio as separate worlds.

For significant phrases ask:

- Where does the phrase enter relative to the beat?
- Where does it end?
- Does it cross a bar boundary?
- Is there a pickup?
- Is the phrase syncopated?
- Is a syllable compressed or stretched?
- Does vowel choice support a sustained note?
- Is pronunciation modified for rhythm?
- Does the bass enter or disappear?
- Does percussion answer the vocal?
- Does an instrument answer the phrase?
- Is there silence before or after it?
- Does harmony make a simple phrase more powerful?
- Does repetition become effective because of arrangement?

A recurring core question of the lab is:

> Why is this lyric stronger in the recording than it appears on paper?

---

# Self-Improvement Rule

The lab may discover better metrics or methods, but it must not rewrite its methodology recklessly.

Use:

OBSERVATION  
↓  
HYPOTHESIS  
↓  
COMPARE AGAINST MORE MATERIAL  
↓  
TEST  
↓  
CONFIRM OR REJECT  
↓  
METHODOLOGY UPDATE

One song is not sufficient evidence for a broad artist or Nigerian-music rule.

Experimental metrics should remain labelled experimental until evidence justifies promotion.

---

# End-of-Task Persistence Rule

Before ending ANY meaningful research task, inspect whether these files require updates:

Required review:

- `PROJECT_STATE.md`
- `SESSION_LOG.md`

Update when relevant:

- `CHANGELOG.md`
- `DECISIONS.md`
- `selection.md`
- acquisition manifests
- source indexes
- analysis execution plans
- methodology documents
- schemas
- project profiles

`PROJECT_STATE.md` must always allow the next agent to understand:

- current artist
- current stage
- active project/song
- completed work
- incomplete work
- blockers
- files/input required from the user
- unresolved issues
- exact next action

`SESSION_LOG.md` must append a concise record containing:

- date/session
- task performed
- files created
- files updated
- sources checked
- important findings
- blockers
- unresolved questions
- next action

Do not finish a meaningful run with stale project state.

---

# Final Reminder

Naija Music Lab is not being built to memorize songs.

It is being built to understand the craft underneath them.

The long-term question is:

> Why does this sound like music rather than generic AI-generated lyrics?