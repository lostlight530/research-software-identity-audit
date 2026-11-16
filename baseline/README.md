# Initial baseline

This directory preserves the historical/initial evidence state used to contextualize the prospective longitudinal study.

## Boundary

The frozen OSF registration requires the historical baseline to remain distinct from the prospective dataset.

Baseline material therefore:

- may describe events that occurred before the prospective window;
- may be reconciled after the fact from public APIs, frozen evidence, or previously captured pages;
- must preserve the distinction between contemporaneous capture and retrospective reconstruction;
- must not be silently rewritten to match later platform state;
- must not be counted as prospective observations.

## Current baseline cutoff

The first baseline package is organized under `2026-10-05/` and uses:

- **cutoff:** 2026-10-05T23:59:59+08:00
- **timezone:** Asia/Shanghai
- **reconciliation execution:** 2026-10-06T00:33:54+08:00 approximately
- **scope:** events/states attributable to the cutoff or earlier and supportable by public API evidence, frozen evidence, or user-supplied public pages

A live API response collected after the cutoff may verify a historical timestamp or currently visible state, but it must not be backdated into an unsupported historical platform response.

## Immutability rule

Raw reconciliation records are append-only source records.

Corrections should be recorded as new reconciliation/correction artifacts with explicit provenance rather than silently replacing historical assertions.
