# October 24 post-handoff contract and release recheck

This is a **bounded, same-day follow-up** after [PR #59](https://github.com/lostlight530/research-software-identity-audit/pull/59) merged, not a replacement for the four earlier October 24 packages, an additional preregistered wave, or a claim that the October 24 calendar day is complete

## Frozen OSF scope

The source of authority remains [OSF 5b329](../../../contract/preregistration.md) (DOI `10.17605/OSF.IO/5B329`): exactly RS01–RS10, six research layers, 60 object-layer units **only at an eligible timepoint**, seven separate operational platforms, no imputation or new objects. The concrete operational schedule still has no declared offsets. Research control and Life Science pilot are outside the ten-object sample

## Actually refreshed in this follow-up

- **GitHub Releases:** twelve public release-list endpoints (`per_page=100`) were queried in a bounded outer tool-session interval `2026-10-24T02:20:58.643Z–02:21:00.019Z` (Beijing 10:20:58–10:21:00). Fixed RS01–RS10 each had four published releases (40 total), control had four and independent pilot one (45 separately described releases). All ten fixed-sample latest tags remained `v2026.10-fourteen-day-evidence-checkpoint`, published October 14 UTC. The [twelve-row selected-field inventory](github-release-inventory.csv) records the actual tool-client batch clock, individual repository URLs, last Release tags, publication clocks, and list cardinalities; original HTTP Date/transport bytes were not saved. This does **not** turn later `main` commits into Releases or infer a new eligible prospective trigger
- **Research control:** PR #59 had been merged to `main` at `8dddc466096988d49ef8186627c540a0793353d4`, and its [main-branch contract workflow](https://github.com/lostlight530/research-software-identity-audit/actions/runs/40053424762) succeeded. That preexisting CI pass is not interpreted as independent scientific interpretation or full transport replay
- **Evidence integrity hardening:** Added a standalone Python standard-library, offline, read-only [handoff checker](../../../tools/check_local_handoff_20261024.py), with a separately labeled advisory CI step. It independently checks the 28 manifest-listed files plus the self-excluded manifest (29 package files), 4,444 projection rows, canonical frozen identities, 14 compressed parts / 1,162 content-addressed payloads, and the 4,267-row ledger against their explicit contracts. **Its result must be read from an actual PR or main CI step**, not presumed passed from the existence of this file

## What is NOT freshly recertified

Zenodo, DataCite, ORCID, Software Heritage, OpenAIRE and OpenAlex are **not newly queried by this follow-up**. Their [earlier morning diagnostic](../02-morning-infrastructure-and-zenodo-family-rollup/README.md) remains independently dated. Its Zenodo normal/diagnostic URL totals of 2,681 / 2,836 represent distinct source-field surfaces, not demonstrated 155 visits; ORCID and SWH degraded source states remain visible. The [earlier local history handoff](../04-local-history-evidence-handoff/README.md) retains original bytes/projections and source clocks without turning old records into new observations

A passing integrity checker establishes transfer and structural correctness of the retained local evidence, **not** original API authenticity, live source freshness, absence of all possible private content, scientific truth, or explanation of conflicts. No baseline, corpus, registration, observation schedule, public historical payload, or prospective study dataset is modified. **New prospective cells: 0**

For machine-readable scope, source clocks and checks, see [record.json](record.json)
