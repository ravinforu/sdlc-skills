#!/usr/bin/env python3
"""Install this source checkout into an explicitly selected Spec Kit project."""
import argparse
from pathlib import Path
import re
import shutil
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', required=True, type=Path, help='Target application repository root')
    parser.add_argument('--specify', default='specify', help='Spec Kit executable name or path')
    parser.add_argument('--update', action='store_true', help='Replace this extension; preserve local edits first')
    parser.add_argument('--dry-run', action='store_true', help='Check prerequisites and show the command without installing')
    args = parser.parse_args()
    source = Path(__file__).resolve().parent.parent
    target = args.repo.expanduser().resolve()
    if not (source/'extension.yml').is_file() or not (source/'guide/SKILL.md').is_file():
        parser.error('The source checkout is incomplete: extension.yml and guide/SKILL.md are required.')
    if source == target or source.is_relative_to(target) or target.is_relative_to(source):
        parser.error('Keep the extension source and application repository in separate, non-nested directories.')
    if not target.is_dir() or not (target/'.specify').is_dir() or not (target/'.specify/init-options.json').is_file():
        parser.error('Target is not an initialized Spec Kit project root. Initialize it or upgrade its integration first.')
    installed = target/'.specify/extensions/engineering-plan'
    if installed.exists() and not args.update:
        parser.error('Engineering Plan is already installed. Preserve local edits, then use --update.')
    if installed.is_symlink() or not installed.resolve().is_relative_to(target):
        parser.error('The extension destination must stay inside the target repository.')
    executable = shutil.which(args.specify)
    if not executable:
        parser.error('Spec Kit was not found. Install it first or pass --specify /path/to/specify.')
    executable = str(Path(executable).resolve())
    try:
        version = subprocess.run([executable, '--version'], capture_output=True, text=True, check=True, timeout=30)
        match = re.fullmatch(r'specify\s+(\d+)\.(\d+)\.(\d+)\s*', version.stdout.strip())
        if not match or not (1, 2, 0) <= tuple(map(int, match.groups())) < (2, 0, 0):
            parser.error('Use a stable Spec Kit version >=1.2.0,<2.0.0. The tested version is 1.2.0.')
        command = [executable, 'extension', 'add', str(source), '--dev']
        if args.update:
            command.append('--force')
        print(f'Source: {source}\nTarget: {target}\nCommand: {subprocess.list2cmdline(command)}', flush=True)
        if args.dry_run:
            print('Dry run: no installation was performed.')
            return 0
        subprocess.run(command, cwd=target, check=True)
        subprocess.run([executable, 'extension', 'info', 'engineering-plan', '--json'], cwd=target, check=True)
    except (OSError, subprocess.SubprocessError) as exc:
        print(f'Installation did not complete: {exc}', file=sys.stderr)
        return 1
    print('Installed. In the target coding-agent chat, run the configure command and verify hooks. See docs/install.md.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
