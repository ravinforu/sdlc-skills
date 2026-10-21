---
description: Prepare Engineering Plan guidance before tasks
---

# Prepare tasks

Read `.specify/extensions/engineering-plan/guide/hooks.md` and follow its shared rules.

Resolve the current feature. Read spec.md, plan.md and linked design, security, data-model and contracts. Identify requirement/control-to-task coverage and dependencies. State blocking design decisions before task generation. Preserve the repository’s task syntax and IDs. Do not implement anything.

Apply the **Tasks** guidance in the stage map. Return a concise context/check result to the calling stage. Do not invoke another Spec Kit command.
