# Maintain and publish the extension

[Back to overview](../README.md)

## Create the shared repository

Extract the delivery ZIP and use the contents of its speckit-engineering-plan directory as your new repository root. extension.yml must be at that root, alongside README.md, commands, guide, scripts, tests and docs. Do not copy the extension into an application's .specify directory as its source repository. No application code or feature files are included.

Create an empty repository in your Git hosting service. From the extracted source root, run these commands after replacing the example URL:

```bash
git init -b main
git add .
git commit -m "Add reusable Engineering Plan extension"
git remote add origin https://github.com/YOUR-ORG/speckit-engineering-plan.git
git push -u origin main
```

If you already cloned an empty repository, copy the files into it and skip git init and git remote add. Choose your organization's actual author, repository URL and license before public distribution. Add those extension metadata fields and a matching LICENSE file when decided. This package does not invent a license grant or claim catalog publication.

## Change and test

Edit commands/ for stage actions and guide/ for shared engineering guidance. These checked-in files are the complete source: no ChatGPT export or original personal skill is needed to maintain this repository. Keep the extension ID engineering-plan stable so updates replace the same installation. Increase extension.version in extension.yml for a new release.

Use a Python environment containing the tested Spec Kit release:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install "specify-cli @ git+https://github.com/github/spec-kit.git@v1.2.0"
.venv/bin/python -B -m unittest discover -s tests -v
```

On Windows use `.venv\Scripts\python.exe`. Tests create temporary projects for Copilot, Claude and Codex; they do not use paid models or your application repositories. The included GitHub validation workflow runs these checks on pushes and PRs in this extension repository. It does not belong in consuming applications.

Review installation warnings and check real agent behavior with a sample feature before rolling out changes. Automated tests check packaging and integration, not model design quality.

## Release

The current version is 1.2.0. Version 1.1.0 introduced the standalone distribution; 1.2.0 adds API planning guidance. The release packager reads the manifest version and includes only extension runtime content and user documentation, with checksums. It excludes Git history, CI, tests, maintainer scripts and local environments. It refuses to overwrite existing archives.

```bash
python3 scripts/package.py --output dist
```

This creates `dist/engineering-plan-v1.2.0.zip` and its `.sha256` file for the current version. Verify your source changes, then tag and push that version:

```bash
git tag v1.2.0
git push origin v1.2.0
```

Create a release for the tag and upload the generated ZIP and checksum. A public release can be installed from a target repository with:

```bash
specify extension add engineering-plan --from https://github.com/YOUR-ORG/speckit-engineering-plan/releases/download/v1.2.0/engineering-plan-v1.2.0.zip
```

Replace YOUR-ORG and all version occurrences with your actual release details. This URL will not work until you publish that release. For private repositories, the documented baseline is authorized Git clone plus local installation; do not assume a browser-authenticated private release URL works with the CLI.

The source ZIP delivered here contains maintainer tools; the ZIP created by package.py is the smaller installable release. A GitHub tag source archive is also a source distribution, not the curated package from package.py.

## Upgrade consumers deliberately

From a source clone with saved local work, fetch tags and check out your chosen release tag or commit. Run scripts/install.py with --repo and --update for each target. Native URL installations can be replaced using `specify extension add engineering-plan --from <new-release-zip-url> --force` in each target. Back up any local extension edits first and recheck hooks; replacement re-enables them.

There is no automatic update of every application when this repository changes. Record the chosen release in the application's normal development documentation. To roll back extension instructions, select the earlier source tag or release and reinstall explicitly; this does not undo already-generated specs, plans, tasks or constitution edits.
