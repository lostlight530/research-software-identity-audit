# OpenAIRE manual link attempt — interpretation

## Result

The OpenAIRE Link Service accepted both entities into the confirmation workflow
but failed at the save step.

The only supported conclusion is:

> a manual research-product link was attempted and OpenAIRE returned a save
> failure; no graph mutation is confirmed.

## What this does not mean

The failure does not establish that:

- the beta software record is invalid;
- the OSF preregistration is invalid;
- the two objects are unrelated;
- OpenAIRE cannot ever link this pair;
- a hidden pending link necessarily exists;
- a published link exists.

Those stronger claims are unsupported.

## Research value

This attempt identifies a distinct write-path failure state in the OpenAIRE
Link Service:

```text
entity discovery succeeded
→ source selection succeeded
→ target selection succeeded
→ confirmation succeeded
→ save failed
→ public graph mutation not confirmed
```

That separation is useful because discovery success and write success are
different observable contracts.

The control repository is outside RS01-RS10, so this intervention attempt does
not alter the preregistered fixed-corpus analytical units or start the
prospective dataset.

## External documentation context

OpenAIRE documents the Link Service as a workflow for linking research results
to projects, communities, or other research results, and documents successful
links as manageable through "My Links". The observed UI here did not report a
successful link and therefore is recorded as a failed intervention attempt,
not as a delayed-success case.
