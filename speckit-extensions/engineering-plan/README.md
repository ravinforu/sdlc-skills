# Engineering Plan for Spec Kit

A reusable Spec Kit extension for architecture, design diagrams, security, code standards and implementation planning. Keep this repository separate from your application repositories. Install a selected version into each project that needs it.

Start with [Installation](docs/install.md). See [Workflow and outputs](docs/usage.md) for daily use and [Maintenance and releases](docs/maintaining.md) for publishing your own repository.

## Quick start

If you downloaded a **runtime release ZIP** rather than this source repository, it has no scripts/ directory. Use the [release ZIP installation steps](docs/install.md#install-a-runtime-release-zip) instead. The commands below are for a source clone or the complete repository ZIP.

Clone this extension repository.

```bash
git clone https://github.com/ravinforu/sdlc-skills.git
cd engineering-plan
python3 scripts/install.py --repo /absolute/path/to/application-repository
```

The target must already be initialized with Spec Kit. The installer delegates to `specify extension add`, using the target as its working directory. It never initializes an application, modifies its constitution automatically, or installs dependencies. On Windows, use `py -3` instead of `python3` if needed.

Then open the target repository in your coding agent and run `/speckit-engineering-plan-configure` for default Copilot/Claude skills mode, or `$speckit-engineering-plan-configure` for Codex. Use your integration's generated command spelling if different.

## What is shared and what stays in each project

| Location | Contents |
| --- | --- |
| This extension repository | extension.yml, commands, engineering guidance, installer, tests and release tools |
| Each application's .specify/extensions/engineering-plan | Its installed extension copy |
| Each application's .specify/extensions.yml | Its hook configuration |
| Each application's .specify/memory/constitution.md | Its own engineering rules and extension references |
| Each application's feature folder | Its own spec.md, plan.md, tasks.md and supporting design files |

One clone can install into multiple projects. Installing into project A does not configure project B. Updating this source repository does not automatically update existing installations. There is no dependency on a personal ChatGPT skill, a globally shared .agents folder, or a repository name chosen here.

## What the extension adds

| Stage | Engineering work |
| --- | --- |
| Constitution | Add or update the engineering principle |
| Specify and clarify | Check boundaries, compatibility and acceptance criteria |
| Plan | Complete architecture, diagrams, APIs, database, frontend, security and rollout |
| Tasks | Check dependencies and requirement-to-task-to-test coverage |
| Implement | Check readiness and record actual verification |

Twelve before/after hooks invoke eleven commands. They extend the normal Spec Kit stages without replacing core templates. The coding agent uses its current session and credentials; no extra API key or background service is needed. Mandatory hooks are agent instructions, not a deterministic CI gate. Engineering Review remains a separate PR gate.

## Compatibility

Version 1.1.0 is the standalone repository distribution. The extension ID remains `engineering-plan`, so existing installations can be updated in place. Tested with Spec Kit 1.2.0, with a declared range of >=1.2.0,<2.0.0. Verify hooks when changing Spec Kit versions. The installer needs Python 3.10+ and an existing `specify` executable; the extension's commands themselves are Markdown.

The package includes tests for Copilot, Claude Code and Codex integration registration. Local tests do not prove that a coding agent follows every hook. Run a representative feature in your own setup.

Official references: [Spec Kit extensions](https://github.com/github/spec-kit/blob/v1.2.0/docs/reference/extensions.md) and [Extension API](https://github.com/github/spec-kit/blob/v1.2.0/extensions/EXTENSION-API-REFERENCE.md).
