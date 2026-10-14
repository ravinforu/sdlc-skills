# Findings and output

## Write each finding once

Use findings.md for complete records. Group by area with short headings. Use a one-level findings/ folder only if necessary for size; make findings.md a simple index in that case. Other pages link to records without copying evidence, impact or fix text.

Use this plain structure:

```markdown
## F-001: Clear action-oriented title

**Type:** Confirmed problem / Conditional risk / Improvement / Information gap
**Priority:** Critical / High / Medium / Low / Information
**Confidence:** High / Medium / Low — explain why
**Status:** Open / Partly addressed / Resolved / Not applicable

**What happens:** Explain the trigger and result in plain English.
**Evidence:** Give source paths and exact symbols or checked line spans.
Mention the code/configuration checked for an existing safeguard.
**Why it matters:** Name the affected users/data/operation and realistic impact.
**Suggested fix:** Give the smallest useful change and affected code.
Explain alternatives, tradeoffs and compatibility/recovery limits when relevant.
**How to check the fix:** Give setup, action and expected result.
**Effort and dependencies:** Small/medium/large with reasons; linked prerequisites.
```

If a diagram explains the issue better, place it within the record with a short source note. Do not claim a proposed test has run. Quote only minimal relevant source, and never copy secrets or personal data. If several endpoints share the same root cause and fix, use one record with an affected-area list.

## Set priority fairly

Critical means evidenced severe broad exposure or system/data loss. High means a credible major security, correctness, availability or integrity impact. Medium means bounded correctness, reliability or maintainability impact. Low means a local low-impact improvement. Information is for facts/questions with no established risk. Explain the conditions; labels alone do not establish urgency.

Confidence is separate: high for a well-traced path with relevant safeguards checked; medium for strong but incomplete evidence; low for a hypothesis. Avoid fixed false precision, invented risk scores or ranking every possible issue as high.

## Turn findings into actions

Use a small actions.md table: finding link, order/priority, first task, prerequisites, suggested owner role if useful, and completion-check link. The finding owns the full fix and acceptance details. Group by urgency and dependencies without inventing dates or people. Make large design decisions explicit; the next Engineering Plan can link back to the finding.

## Show real coverage

Keep the repository commit/scope in README.md. Use coverage.md for the inventory: area/path, files/interfaces checked, behavior traced, review status, finding links and remaining work. Record inspection methods and commands/results once. State exclusions, inaccessible code and unknown deployment configuration. An area is not reviewed because its files were listed.

Distinguish review coverage from automated test coverage. Use a percentage only with a clear denominator and method; reading all modules does not prove all behavior is correct. A repository-wide review is incomplete while meaningful areas remain unchecked. Preserve a concrete resume list when limits stop work.

## Coordinate with other documents

Link to current onboarding facts only after checking their date/commit and relevant source. Keep changed-feature proposals in the feature plan; this review owns the present problem and acceptance checks. Do not require either document to exist: include the minimum context needed to understand a finding when no guide exists. Check internal links and remove reworded duplicates before delivery.
