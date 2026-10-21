---
description: Prepare Engineering Plan guidance before implement
---

# Prepare implement

Read `.specify/extensions/engineering-plan/guide/hooks.md` and follow its shared rules.

Resolve the current feature. Require spec.md, plan.md and tasks.md, and read their linked design, security, schema and contracts. Identify the approved tasks, required checks and repository standards before coding. If a material requirement, permission, public contract or data-loss decision is unresolved, do not authorize affected implementation. Report the blocked scope. This hook reads and assesses only; the explicitly requested core implement stage performs code edits.

Apply the **Implement** guidance in the stage map. Return a concise context/check result to the calling stage. Do not invoke another Spec Kit command.
