#!/usr/bin/env python3
"""Build a versioned runtime archive from this standalone source repository."""
import argparse
import hashlib
from pathlib import Path
import re
import zipfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('dist'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    manifest = (root/'extension.yml').read_text(encoding='utf-8')
    versions = re.findall(r'^  version: [\"\']?(\d+\.\d+\.\d+)[\"\']?\s*$', manifest, re.MULTILINE)
    if len(versions) != 1:
        parser.error('Use one stable X.Y.Z version in extension.yml.')
    if not (root/'guide/SKILL.md').is_file():
        parser.error('Missing bundled guide/SKILL.md.')
    output = args.output.expanduser().resolve()
    archive = output/f'engineering-plan-v{versions[0]}.zip'
    checksum = archive.with_suffix('.zip.sha256')
    if archive.exists() or archive.is_symlink() or checksum.exists() or checksum.is_symlink():
        parser.error('Release files already exist. Use a new output directory or a new version.')
    paths = [root/'extension.yml', root/'README.md']
    for directory in ('commands', 'guide', 'docs'):
        paths.extend(p for p in (root/directory).rglob('*') if p.is_file())
    for name in ('LICENSE', 'NOTICE'):
        if (root/name).is_file():
            paths.append(root/name)
    data = {}
    for path in sorted(paths):
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            parser.error('Release content must be regular files inside this checkout.')
        data[path.relative_to(root).as_posix()] = path.read_bytes()
    data['SHA256SUMS.txt'] = ''.join(hashlib.sha256(body).hexdigest()+'  '+name+'\n'
                                    for name, body in data.items()).encode()
    output.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive, 'x', compression=zipfile.ZIP_DEFLATED) as bundle:
        for name, body in data.items():
            bundle.writestr('engineering-plan/'+name, body)
    with zipfile.ZipFile(archive) as bundle:
        if bundle.testzip() is not None:
            raise RuntimeError('Release archive verification failed.')
    checksum.write_text(hashlib.sha256(archive.read_bytes()).hexdigest()+'  '+archive.name+'\n', encoding='utf-8')
    print(archive)
    print(checksum)


if __name__ == '__main__':
    main()
