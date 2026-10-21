# Install in an application repository

[Back to overview](../README.md)

## Prepare the target

Use Python 3.10+ and Spec Kit 1.2.0 or a compatible later 1.x version. Check `specify --version`. If using uv, the tested CLI can be installed with:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@v1.2.0
```

For an existing CLI installation, follow your normal upgrade process. Do not downgrade a newer working installation just for this example.

Open a terminal in the application repository. If it has no Spec Kit setup, initialize it once, choosing the integration you use:

```bash
specify init --here --integration copilot
# OR: specify init --here --integration claude
# OR: specify init --here --integration codex
```

For an existing setup, do not run init again. Check `specify integration status`. If its generated core commands are old, use `specify integration upgrade copilot` with your integration name. Review conflicts before replacing customized commands. Updating the CLI alone does not refresh project commands.

## Install a runtime release ZIP

The smaller versioned release ZIP intentionally has no installer scripts. Extract it outside the application repository, then run this native command **from the initialized application repository**:

```bash
specify extension add /absolute/path/to/extracted/engineering-plan --dev
```

The path must contain extension.yml and guide/. Add --force only when deliberately replacing an existing installation after preserving local edits. Continue with Configure and verify below. Do not run scripts/install.py from a runtime ZIP. If using a published HTTPS release URL, the installation command is in [Maintenance and releases](maintaining.md#release).

## Install from a separate clone

Clone or extract this extension outside the application repository. Open a terminal in the extension's root (the directory containing extension.yml).

```bash
python3 scripts/install.py --repo /absolute/path/to/application-repository --dry-run
python3 scripts/install.py --repo /absolute/path/to/application-repository
```

Paths containing spaces must be quoted. Relative --repo paths are resolved from your terminal's current directory. The installer finds its own extension source from its script location, so it also works when invoked by absolute path from elsewhere. Use `--specify /path/to/specify` if the CLI is not on PATH.

The installer requires --repo and refuses nested source/target directories. It checks for an initialized target, checks the CLI version, and runs Spec Kit in that target. It does not edit the source checkout. Review the output and any Spec Kit warnings; a successful installation still needs the checks below.

Repeat with another target to reuse the same source:

```bash
python3 scripts/install.py --repo /absolute/path/to/another-application
```

The equivalent native command, run from the application repository, is:

```bash
specify extension add /absolute/path/to/speckit-engineering-plan --dev
```

`--dev` is Spec Kit's local-directory route. In the tested 1.2.0 release, source files are copied into the target. Generated agent entries may be symlinks to rendered files inside that target. They do not require the original source checkout to remain at its absolute path.

For a private source repository, clone it using your normal authorized Git access, then use this local route. No access token belongs in the installer, manifest or application constitution.

## Configure and verify

In the target's coding-agent chat, invoke the configure command:

| Agent, default skills layout | Invocation |
| --- | --- |
| Copilot or Claude Code | `/speckit-engineering-plan-configure` |
| Codex | `$speckit-engineering-plan-configure` |

Other layouts can expose dotted names such as `/speckit.engineering-plan.configure`. Use the installed integration's spelling. If the constitution is still an empty template, run the normal constitution stage first; its after hook configures this extension. Review the resulting project-specific principle and keep unrelated rules.

From the target repository, run:

```bash
specify extension info engineering-plan --json
specify artifact list --json
```

Expect the enabled extension with eleven commands and twelve hooks. Check .specify/extensions.yml for all six stages, before and after, with enabled: true and optional: false. Check that the generated core commands dispatch those hooks. Then try a small feature and confirm actual hook execution and linked outputs; a printed EXECUTE_COMMAND line alone is not proof.

Save the intended target configuration in that application's version control according to your team's Spec Kit convention. Review `git status` after installation. This installer does not commit, push, change ignore rules or synchronize teammates' machines. If your project does not version installed Spec Kit files, each teammate or fresh checkout must repeat installation and configuration.

## Existing Engineering Plan installations

Keep the same extension ID. From the new shared source clone, run:

```bash
python3 scripts/install.py --repo /absolute/path/to/application-repository --update
```

This explicitly enables Spec Kit's --force replacement for this extension. Preserve local changes to its installed files first. Existing feature documents and unrelated extensions remain. Reinstallation re-enables the extension hooks. Recheck configuration and run configure again if the guidance changed.

If the older engineering-plan preset is still enabled, remove that preset from the target using `specify preset remove engineering-plan` before installing the native extension. Do not run the old install_speckit.py installer again. The configure command migrates the earlier managed guidance blocks. Keep the standalone skill if you use it outside Spec Kit, but do not invoke both copies for one stage.

After the new installation is verified, an old extracted source folder can be archived or removed separately. Do not delete .specify/extensions/engineering-plan: that is the target's active installed copy.

To pause hooks, run `specify extension disable engineering-plan` in the target. To uninstall, run `specify extension remove engineering-plan`. Feature documents and constitution text remain; review those separately if retiring the workflow.
