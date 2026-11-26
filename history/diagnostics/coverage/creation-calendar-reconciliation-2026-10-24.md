# Reconciliation: calendar coverage from each GitHub repository's creation through 2026-10-24

**Document assembly:** 2026-10-24 Asia/Shanghai, using retained control-repository `main` material at cb509578b94e0eb3340e7019f4c80eb65c938d8c. This is a **derived calendar-coverage correction/extension**, not a new remote source capture, Git history replay, traffic study, OSF registration amendment, prospective observation, or claim that missing-day snapshots exist.

## Why this index exists

The earlier [September 16–October 24 daily source index](daily-repository-evidence-2026-09-16-to-2026-10-24.csv) and [weekly source index](weekly-repository-evidence-2026-09-16-to-2026-10-24.csv) cover **39 × 12 = 468 day/repository cells** and **72 Monday-week/repository rows**. They explicitly exclude the period between each repository's creation and 2026-09-16. This supplements them without modifying either legacy table or their source records.

The updated coverage is **from each repository's own GitHub `created_at` date** (UTC converted to Asia/Shanghai) to **2026-10-24**, inclusive. GitHub creation timestamps are public returned metadata observed on 2026-10-24, **not contemporaneous proof of activity on every day**. The oldest returned creation date belongs to RS01 on **2025-04-27 Asia/Shanghai**; the latest among these 12 is the independent pilot on **2026-10-16 Asia/Shanghai**. The index has **1,864 active day/repository rows** and **274 partial-or-full Monday-week/repository rows**. It omits pre-creation cells, rather than treating a nonexistent repository as an unobserved existing repository. All **45 public release events** retain their preexisting recorded GitHub `published_at` clock and Beijing date. **101 daily rows** have dated source evidence references copied unchanged from the previous ledger; the other **1,763 days** are explicitly marked `no_retained_family_views_source_for_day`, never zero traffic. No speculative daily commits, downloads, visits, milestones, or historical states were added.

## Scope and sources

- [Creation-to-Oct24 daily calendar](daily-repository-calendar-from-creation-to-2026-10-24.csv) — each repository begins on its own observed GitHub creation **date**, not earlier; columns show source-level observation states and exact prior source references where available
- [Creation-to-Oct24 weekly calendar](weekly-repository-calendar-from-creation-to-2026-10-24.csv) — Monday boundaries in Asia/Shanghai; first and last weeks can be partial; counts only verified public release events and days with retained source values
- [Underlying GitHub identity/creation metadata](repository-inventory-2026-10-24.csv), [45 public Release events](release-event-ledger-2026-10-24.csv), and the prior [39-day coverage table](daily-repository-evidence-2026-09-16-to-2026-10-24.csv) are the sources and remain unchanged

## Validation and limitations

The extension was checked during authoring: **12 identities**, **1,864** active day rows, **274** week rows, **45/45** public release events preserved, **101/101** dated source-bearing rows preserved, and all **468** existing daily source states reconciled for those dates. Repeated no-source days are **calendar rows only** and must not be quoted as monitored GitHub activity or as a completed daily recheck. The date of compilation is **not** the missing days' retrieval timestamp. An archived source's `stats.views` or `version_views` must retain its original semantic and source URL; daily entries are not a compatible time series for visitor growth or global unique humans.

Frozen OSF study contract `10.17605/OSF.IO/5B329` unchanged: **RS01–RS10** are the only preregistered objects; control is **not RS11**, the independent life-science pilot is outside the sample. Six preregistered layers imply 60 object-layer cells **only at eligible schedule-governed timepoints**, while concrete offsets are not declared in `schedule/`. **Zero** prospective observations created. This index does not prove a complete Git-commit history for each of 12 repositories or that external services retain original responses for the pre-September dates.

**Correction policy:** The older index is retained append-only. This note identifies the added creation-calendar scope and exact derivative sources; future evidence must be a separately dated record, not an invented backfill.
