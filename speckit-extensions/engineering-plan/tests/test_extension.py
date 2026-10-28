"""Run with a Python environment containing specify-cli 1.2.0. Uses temp projects only."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
import yaml
from specify_cli.extensions import ExtensionManifest

ROOT=Path(__file__).resolve().parent.parent
STAGES=('constitution','specify','clarify','plan','tasks','implement')

class ExtensionChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp=tempfile.TemporaryDirectory(prefix='engineering-plan-extension-tests-')
        cls.addClassCleanup(cls.tmp.cleanup)
        cls.base=Path(cls.tmp.name)
        cls.cli=Path(sys.executable).parent/'specify'
        if not cls.cli.is_file():raise RuntimeError('Run this test with the Python environment where specify-cli 1.2.0 is installed.')
        cls.ext=ROOT
        cls.projects={}
        for agent in ('copilot','claude','codex'):
            project=cls.base/agent
            cls.run_cli('init',str(project),'--integration',agent,'--script','py','--ignore-agent-tools','--non-interactive',cwd=cls.base)
            result=subprocess.run([sys.executable,'-B',str(ROOT/'scripts/install.py'),'--repo',str(project),'--specify',str(cls.cli)],capture_output=True,text=True)
            if result.returncode:raise AssertionError(result.stdout+'\n'+result.stderr)
            cls.projects[agent]=project
    @classmethod
    def run_cli(cls,*args,cwd):
        result=subprocess.run([str(cls.cli),*args],cwd=cwd,capture_output=True,text=True,timeout=60)
        if result.returncode:raise AssertionError(result.stdout+'\n'+result.stderr)
        return result.stdout
    def test_manifest_and_hooks(self):
        manifest=ExtensionManifest(self.ext/'extension.yml')
        self.assertEqual(len(manifest.commands),11)
        self.assertEqual(set(manifest.hooks),{t+'_'+s for s in STAGES for t in ('before','after')})
        for entry in manifest.hooks.values():
            self.assertIs(entry['optional'],False)
            self.assertNotIn('condition',entry)
    def test_registered_hooks_for_all_integrations(self):
        for agent,project in self.projects.items():
            with self.subTest(agent=agent):
                data=yaml.safe_load((project/'.specify/extensions.yml').read_text())
                entries=[(event,h) for event,items in data['hooks'].items() for h in items if h['extension']=='engineering-plan']
                self.assertEqual(len(entries),12)
                self.assertEqual(len({event for event,_ in entries}),12)
                self.assertTrue(all(h['enabled'] and h['optional'] is False and not h.get('condition') for _,h in entries))
    def test_generated_agent_invocations_and_core_dispatch(self):
        roots={'copilot':'.github/skills','claude':'.claude/skills','codex':'.agents/skills'}
        manifest=ExtensionManifest(self.ext/'extension.yml')
        for agent,project in self.projects.items():
            with self.subTest(agent=agent):
                output=project/roots[agent]
                for command in manifest.commands:
                    name=command['name'].replace('.','-')
                    path=output/name/'SKILL.md'
                    self.assertTrue(path.is_file(),str(path))
                    self.assertIn('.specify/extensions/engineering-plan/guide/hooks.md',path.read_text())
                for stage in STAGES:
                    core=(output/('speckit-'+stage)/'SKILL.md').read_text()
                    self.assertIn('before_'+stage,core)
                    self.assertIn('after_'+stage,core)
                    self.assertIn('EXECUTE_COMMAND',core)
    def test_disable_enable_preserves_other_hooks(self):
        project=self.projects['copilot']
        config=project/'.specify/extensions.yml'
        data=yaml.safe_load(config.read_text())
        unrelated={'extension':'other-fixture','command':'speckit.other-fixture.check','enabled':True,'optional':True}
        data['hooks']['after_plan'].append(unrelated)
        config.write_text(yaml.safe_dump(data))
        try:
            self.run_cli('extension','disable','engineering-plan',cwd=project)
            disabled=yaml.safe_load(config.read_text())
            ours=[h for entries in disabled['hooks'].values() for h in entries if h['extension']=='engineering-plan']
            self.assertTrue(ours and all(not h['enabled'] for h in ours))
            self.assertIn(unrelated,disabled['hooks']['after_plan'])
        finally:self.run_cli('extension','enable','engineering-plan',cwd=project)
        active=yaml.safe_load(config.read_text())
        ours=[h for entries in active['hooks'].values() for h in entries if h['extension']=='engineering-plan']
        self.assertTrue(ours and all(h['enabled'] for h in ours))
    def test_runtime_archive(self):
        result=subprocess.run([sys.executable,'-B',str(ROOT/'scripts/package.py'),'--output',str(self.base/'dist')],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        archive=next((self.base/'dist').glob('*.zip'))
        with zipfile.ZipFile(archive) as z:
            self.assertIsNone(z.testzip())
            self.assertIn('engineering-plan/extension.yml',z.namelist())
            self.assertNotIn('engineering-plan/scripts/install.py',z.namelist())
            self.assertNotIn('engineering-plan/.github/workflows/validate.yml',z.namelist())
            self.assertEqual(z.read('engineering-plan/guide/SKILL.md'),(ROOT/'guide/SKILL.md').read_bytes())
            for line in z.read('engineering-plan/SHA256SUMS.txt').decode().splitlines():
                digest,name=line.split('  ',1)
                self.assertEqual(hashlib.sha256(z.read('engineering-plan/'+name)).hexdigest(),digest)
            z.extractall(self.base/'release-extracted')
        # Test that the curated archive is installable after extraction, not just a valid ZIP.
        project=self.base/'release-consumer'
        self.run_cli('init',str(project),'--integration','copilot','--script','py','--ignore-agent-tools','--non-interactive',cwd=self.base)
        self.run_cli('extension','add',str(self.base/'release-extracted/engineering-plan'),'--dev',cwd=project)
        self.assertTrue((project/'.specify/extensions/engineering-plan/guide/SKILL.md').is_file())
        digest=archive.with_suffix('.zip.sha256').read_text().split()[0]
        self.assertEqual(hashlib.sha256(archive.read_bytes()).hexdigest(),digest)
        again=subprocess.run([sys.executable,'-B',str(ROOT/'scripts/package.py'),'--output',str(self.base/'dist')],capture_output=True)
        self.assertNotEqual(again.returncode,0)

    def install(self,target,*args):
        return subprocess.run([sys.executable,'-B',str(ROOT/'scripts/install.py'),'--repo',str(target),'--specify',str(self.cli),*args],cwd=self.base,capture_output=True,text=True)

    def test_source_files_not_installed(self):
        for project in self.projects.values():
            installed=project/'.specify/extensions/engineering-plan'
            self.assertFalse((installed/'.github').exists())
            self.assertFalse((installed/'tests').exists())
            self.assertFalse((installed/'scripts').exists())
            self.assertTrue((installed/'guide/references/design.md').is_file())

    def test_dry_run_and_update(self):
        project=self.projects['claude']
        sentinel=project/'specs/example/spec.md';sentinel.parent.mkdir(parents=True,exist_ok=True)
        sentinel.write_text('Existing feature.\n')
        before=(project/'.specify/extensions.yml').read_bytes()
        refused=self.install(project)
        self.assertNotEqual(refused.returncode,0)
        self.assertIn('--update',refused.stderr)
        dry=self.install(project,'--update','--dry-run')
        self.assertEqual(dry.returncode,0,dry.stderr)
        self.assertEqual((project/'.specify/extensions.yml').read_bytes(),before)
        update=self.install(project,'--update')
        self.assertEqual(update.returncode,0,update.stdout+update.stderr)
        self.assertEqual(sentinel.read_text(),'Existing feature.\n')
        self.assertEqual(ExtensionManifest(project/'.specify/extensions/engineering-plan/extension.yml').version,'1.2.0')

    def test_targets_must_be_initialized_and_separate(self):
        for target in (self.base/'missing',ROOT,ROOT/'application',ROOT.parent):
            result=self.install(target,'--dry-run')
            self.assertNotEqual(result.returncode,0,str(target))

    def test_target_is_explicit(self):
        result=subprocess.run([sys.executable,'-B',str(ROOT/'scripts/install.py')],capture_output=True,text=True)
        self.assertNotEqual(result.returncode,0)
        self.assertIn('--repo',result.stderr)

    def test_source_move_does_not_break_target(self):
        for project in self.projects.values():
            for file in (project/'.specify/extensions/engineering-plan/commands').glob('*.md'):
                self.assertFalse(file.is_symlink())
            for folder in ('.github/skills','.claude/skills','.agents/skills'):
                for file in (project/folder).glob('speckit-engineering-plan-*/SKILL.md'):
                    self.assertTrue(file.resolve().is_relative_to(project))
                    self.assertTrue(file.is_file())

if __name__=='__main__':unittest.main()
