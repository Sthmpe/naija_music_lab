# Decisions

## 2026-09-28 — Keep contemporary-language evidence at song level until corroborated

Decision: Collect meaningful slang and local-expression observations prospectively as optional song-level evidence, separating heard pronunciation, proposed spelling, meaning, function, dated freshness and comparative scope. Reserve `contemporary/slang/` for later cross-artist or independent usage corroboration; do not promote Omah Lay-only observations into general Nigerian usage. Teach language mechanisms for original writing, not reuse of a source expression. Do not infer commercial causality, present-day currency or artist intention from a lyric occurrence.

Reason: Contemporary language can affect rhythm, phonetics and character, yet orthography, meaning, social reach and freshness require different evidence. A separate evidence boundary prevents the generation system from treating an artist-specific or dated expression as generic current slang while retaining the useful craft mechanism.

## 2026-09-28 — Extend experimental dimensions to explain groove and repetition

Decision: Keep the version 0.2.5 evidence boundaries and add explicit research prompts for bounce mechanism, internal rhythm, performed phonetic rhyme, playful meaning/sound/delivery, candidate English/Pidgin switch function, memorable nonlexical sound, landing-word behaviour and repetition reward. Capture them prospectively as optional observations, with project-level support counts and counterexamples before any broader promotion. Future specialist requirements remain evidence-collection targets, not implemented agent rules.

Reason: The preserved Generation Benchmark 001 exposed gaps in predicting how original words might move and sound when sung. Mechanism labels make future comparisons more precise, but the benchmark itself has no sung or listener validation and cannot prove any source-song mechanism. This addition preserves the locked corpus, completed Get Layd work and all existing required metrics.

## 2026-09-28 — Add experimental musical-language dimensions after Generation Benchmark 001

Decision: Retain all existing song/project requirements and add optional, evidence-tagged analysis of mouth-feel, phonetic recall units, word-to-melody affordance, Nigerian conversational timing, phrase looseness, semantic/sonic balance, hook sound design and vocables. Translate supported observations into original-writing tests, with AI-writing failure signals held as falsifiable hypotheses. Use the generation benchmark to identify a research question, not as proof of a source-song pattern or a successful sung result.

Reason: The benchmark critique exposed that a lyric can read well while its actual singability, vowel landings and conversational delivery remain untested. Optional fields let later songs test these mechanisms without rewriting completed Get Layd analyses, weakening current metrics, changing the locked corpus or treating one project as a universal rule.

## 2026-09-24 — Distinct projects and editions

Decision: Count an original album/EP once. Catalogue deluxe editions separately as expanded editions and consider their new tracks for selection. Reason: the five-project target should not count the same underlying album twice.

## 2026-09-24 — Two selection approvals

Decision: Reconnaissance includes provisional song suggestions, but project approval and song approval are separate gates. Reason: the user controls both, and full selected-project track lists must be visible before final song selection.

## 2026-09-24 — User-approved Omah Lay corpus

Decision: Four original-project eras are Get Layd, What Have We Done, Boy Alone, and CLARITY OF MIND. Boy Alone: Deluxe Edition extends the Boy Alone era. Analyse both five-track EPs in full; five representative songs each from Boy Alone and CLARITY OF MIND; all five new deluxe compositions; three named non-project recordings (two solo, one collaborative); and the Ozuna soso remix as a comparative case against the original. Preserve all unselected tracks as validation candidates.

Reason: User explicitly approved this corpus and wants complete short projects, representative large-project samples, and a special remix study without duplicate counting. Evolution synthesis must keep the deluxe within the Boy Alone era.

## 2026-09-24 — Collaboration selection gate and behaviour file

Decision: Keep solo standalone and collaboration/feature material separate. Verify actual contribution before final collaboration selection; propose approximately four to six informative cases and await user approval. Add `collaboration-behaviour.md` to artist-level output and `schemas/collaboration-behaviour-template.md` for future artists. Five songs is a default, not a quota.

Reason: Credit presence alone does not establish enough material for studying hooks, writing, cadence or vocal adaptation. User explicitly required this additional synthesis component and the final collaboration checkpoint.

## 2026-09-24 — Locked Omah Lay first-pass corpus

Decision: User approved Infinity, PAMI, Philo, People (Remix), One Call and With You as the six primary collaboration cases. Together with the previously approved songs, the first pass contains 34 primary recordings and one separate Ozuna `soso` remix comparison. Keep Do Not Disturb and Hello Brother as early solo validation candidates, and the wider feature pool as validation/replacement material. Do not alter the approved corpus without a documented reason and user approval.

Reason: Explicit user selection. A clear boundary prevents research convenience from silently changing the sample.

## 2026-09-24 — Correct Company attribution without changing the locked recording

Decision: Keep the approved `Company` recording as a collaborative non-project/current release by Clean Bandit, Chlöe and Omah Lay. It does not become a seventh Feature Lab primary case. Free My Mind and Moving are the two solo non-project recordings. Do Not Disturb and Hello Brother remain early solo validation candidates. Primary recording count remains 34, plus the separate Ozuna comparison.

Reason: [Spotify's Omah Lay playlist](https://open.spotify.com/embed/playlist/37i9dQZF1DZ06evO3gZZdL?nd=1) and [Apple Music's Omah Lay artist page](https://music.apple.com/us/artist/omah-lay/1459319359) identify Company as a multi-artist release. This corrects a factual classification while preserving the user's exact song choice.

## 2026-09-28 — Ending-led completeness gate for private captures

Decision: Treat platform-reported duration as reference metadata. For a private playback capture, assess completeness primarily from whether the supplied recording audibly reaches a natural musical ending. A shorter or longer file may still be sufficient if version provenance and musical resolution support it; bit-for-bit master identity is not required for first-pass songwriting analysis.

Reason: Padding, container timing, platform edits and capture boundaries can change duration. The current You and Ye Ye Ye reports specifically hear abrupt boundaries during continuing music, so their incomplete statuses remain on **audible** grounds. No new Listening Analyst request is necessary to establish that fact.

## 2026-09-28 — Source-limited first-pass completion approved by user

Decision: `SOURCE_RECORDING_COMPLETE` and `ANALYSIS_COMPLETE_FOR_AVAILABLE_AUDIO` are separate facts. A partial audio source may support first-pass song completion when it contains substantial representative material, its missing portion is identified, listening evidence covers the available portion, no missing material is invented, and all conclusions dependent on that material are withheld. This decision does not cover extremely short, severely corrupted or otherwise unrepresentative sources without an individual review.

Reason: The user explicitly accepts the current You and Ye Ye Ye captures and their preserved Listening Analyst reports for the first Get Layd research pass and directs the lab to progress without replacement recordings or another listening request. Their audible cutoffs remain factual; their available-audio analyses can be marked complete. Cross-song conclusions must track whether each contributing capture is complete or partial.
