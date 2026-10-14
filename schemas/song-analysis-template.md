# Song analysis — [title]

Status: draft | complete | audio pending. Sources: [URLs with dates]. Evidence labels: verified | estimated | interpretation | unknown.

## Basic data
Artist; features; project; track number; release date; writers; producers; duration; BPM and stability; key/tonal centre; time signature; single status; relevant chart evidence. Give source and confidence per fact.

## Structure
Section sequence and timestamps; first vocal; first hook; hook length and appearances; section durations and song proportions; variations.

## Cadence and rhythm
Phrase lengths, approximate syllables, density, stress, entrances/exits, syncopation, pickups, pauses, bar overlap, speech/melody balance and percussion interaction. Explain what makes the flow natural.
For selected phrases, identify `BOUNCE_MECHANISM` (short/long and stress alternation, pickups, offbeats, gaps, consonant attacks, percussion or response) and `INTERNAL_RHYTHM_PATTERN` (syllable groups, micro-pauses, compression, accent, acceleration/relaxation). Explain the mechanism instead of using "bouncy" alone. Ask whether the phrase retains a groove without drums; distinguish heard performance from text-derived conjecture.

## Phonetics and language
Vowel/consonant patterns, rhyme type, elongation, pronunciation; Standard/Nigerian English, Pidgin and other languages. Explain observed switches without inventing intent.
Record `PHONETIC_RHYME_PATTERN` when a rhyme works to the ear through vowel, consonant, slant, internal or delivery-dependent similarity despite different spelling. For a supported switch, record `CODE_SWITCH_FUNCTION` as a candidate role (rhythm, intimacy, emphasis, humour, rhyme, syllable economy, cultural specificity, conversational naturalness or melodic affordance); the function is an interpretation, not proof of authorial intent. Ask whether phrasing would sound natural in Nigerian speech before singing; use fluent-speaker checks where needed, and never equate grammatical error with naturalness.

### Optional slang and contemporary-language observations
For each **meaningful** slang, street/local expression, coinage, shortened form, cultural reference or unusual construction, use a compact record based on `schemas/slang-entry-template.md`: short cue/time/source; heard pronunciation versus proposed spelling; language/register; context-specific meaning and alternatives; `SLANG_FUNCTION`; rhythmic/phonetic value versus an abstract formal alternative; `CODE_SWITCH_TRIGGER` if any; character/social role; possible `QUOTABILITY_MECHANISM`; date-sensitive freshness; reuse risk; scope classification and confidence. Distinguish sourced facts, listening evidence and interpretation. Do not infer slang currency, demographics, commercial causality or natural Pidgin from one song.

## Experimental musical-language observations
For selected high-value phrases, give a short cue, approximate timestamp, evidence layer, confidence and any uncertainty. Omit a dimension when evidence is unavailable; do not infer heard performance from text alone.

- **Singability / mouth-feel:** Open/closed endings, consonant clusters or softening, repeated mouth shape, sustained syllable, performed pronunciation and likely physical ease. Why might it feel satisfying in the mouth?
- **Phonetic stickiness:** Vowel families, repeated syllables, near/internal rhyme, consonant attacks, sound alternation and vocables. Identify a `PHONETIC_NUCLEUS` for a hook only when supported.
- **Melodic affordance:** Which syllables are heard as pickup, landing, hold, phrase ending or repeated anchor, and what phonetic properties allow that role? Do not transcribe or copy a melody.
- **Nigerian conversational rhythm:** Evidence-backed syntax, contractions, fragments, omissions, interjections, code-switching, address words, speech stress, interruption and informal endings. Separate sound, spelling and meaning; avoid stereotype claims.
- **Phrase looseness:** Unequal lengths, interrupted or incomplete thoughts, one-word responses, repeated fragments, ad-libs, vocables and silence. Explain their rhythmic or arrangement role.
- **Semantic versus sonic load:** For important moments use optional qualitative `SEMANTIC_DOMINANT`, `SONIC_DOMINANT` or `BALANCED`; identify whether meaning, phonetics, cadence, melody, delivery or production carries the effect. This is interpretive, not a measured score.
- **Vocable behaviour:** Record the heard sound and whether it supports rhythm, breathing, emotion, transition, reinforcement, call/response or phonetic pleasure. Do not dismiss it as filler.
- **Memorable vocal sounds:** Where the recurring unit is nonlexical or shortened, name a `VOCAL_SOUND_NUCLEUS` and its performed role. Keep it distinct from a lexical `PHONETIC_NUCLEUS`.
- **Playful phrasing:** Mark `PLAYFUL_IN_MEANING`, `PLAYFUL_IN_SOUND` or `PLAYFUL_IN_DELIVERY` only where a word choice, comparison, reaction, timing or repeated sound supports it. Humour is not required in every song.
- **Melodic invitation and landing:** Use `MELODIC_AFFORDANCE` for a phrase whose spoken stress, syllable/vowel sequence or intonation suggests rise, fall or sustain; label text-only predictions as hypotheses. Use `LANDING_WORD_BEHAVIOUR` for an observed stressed destination, vowel hold, rhyme or stable ending under changed setup. Do not copy pitches or melody.

## Songwriting and story
Central idea, viewpoint, emotional/narrative movement, 4–8-bar unit log, imagery, specificity, humour, wordplay and productive repetition.

## Why simple lines sound musical
Test melody, vowel, timing, accent, delivery, repetition, arrangement, silence and setup. Cite timestamped evidence.

## Hook engineering
Central phrase (paraphrase if possible), distinct word/phrase/syllable counts, repetition and variation, title placement, rhythmic/melodic/phonetic shape, first occurrence, duration and memorability mechanism.
Also examine smallest repeatable sound unit, vowel/syllable profile, chantability, response potential, repetition ease and stable sound with changing context. Treat audience recall as a hypothesis unless tested.
Add `REPETITION_REWARD_MECHANISM` where evidence supports it: classify exact, rhythmic, phonetic, semantic, progressive or call/response repetition; then identify what changes in setup, spacing, duration, backing voice, arrangement or meaning to make another return musically useful. Do not infer that listeners find it addictive without a listener test.

## Vocals and production
Register, texture, range, cells, holds, harmony, doubles, ad-libs, effects; drums, bass, harmony instruments, transitions and space. Mark audio-dependent fields unavailable when necessary.

## Lyric + audio interactions
Timestamped significant phrases: beat position, arrangement change, stretching, pause, response and reason the recording strengthens the line.

## Findings and limits
Song-specific findings; candidate patterns only; contrary evidence; unknowns; AUDIO_STATUS; next check. Never store full lyrics.

## Optional generation translation
For a strong observation, add `GENERATION_RELEVANCE`: observation → mechanism → possible original-writing use. Give confidence, evidence status, limits and a future test. Note any evidence-backed AI-writing failure-signal hypothesis (overregular lines, overcomplete grammar, forced language, absent rests/vocables, poor vowel planning, overloaded hooks or awkward singability); do not present it as a universal rule. Never ask a generation system to copy this recording.
