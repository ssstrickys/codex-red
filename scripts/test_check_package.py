import json
from pathlib import Path
import tempfile
import unittest

import check_package as cp


class PublicPackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('agents', 'assets', 'references'):
            (self.root / name).mkdir()
        (self.root / 'SKILL.md').write_text('---\nname: codex-red\ndescription: "Local fixture"\n---\n# Codex Red\n')
        (self.root / 'agents/openai.yaml').write_text('interface:\n  display_name: Codex Red\n  default_prompt: Use $codex-red\n  icon_small: assets/icon.svg\n  icon_large: assets/icon.svg\n')
        (self.root / 'assets/icon.svg').write_text('<svg/>')
        for name in ('README.md', 'NOTICE.md', 'PROVENANCE.md'):
            (self.root / name).write_text('Fixture\n')
        source = Path(cp.__file__).resolve().parent.parent / 'LICENSE.upstream.txt'
        (self.root / 'LICENSE.upstream.txt').write_bytes(source.read_bytes())
        source = Path(cp.__file__).resolve().parent.parent / 'LICENSE'
        (self.root / 'LICENSE').write_bytes(source.read_bytes())

    def test_project_license_is_required_for_publication(self):
        result = cp.audit(self.root)
        self.assertTrue(result['checks_passed'])
        self.assertTrue(result['release_checks_passed'])
        (self.root / 'LICENSE').unlink()
        self.assertFalse(cp.audit(self.root, release=True)['checks_passed'])

    def test_missing_and_escaping_links_fail(self):
        (self.root / 'README.md').write_text('[missing](absent.md)\n[escape](../outside.md)\n')
        errors = cp.audit(self.root)['errors']
        self.assertTrue(any('missing local link' in e for e in errors))
        self.assertTrue(any('escapes repository' in e for e in errors))

    def test_real_local_links_and_public_urls_pass(self):
        (self.root / 'README.md').write_text('[notice](NOTICE.md#sources)\n[public](https://example.invalid/path)\n')
        self.assertTrue(cp.audit(self.root)['checks_passed'])

    def test_private_profile_and_workspace_path_fail(self):
        (self.root / 'references/operator-profile.md').write_text('Private operator preferences\n')
        (self.root / 'README.md').write_text('/work' + 'space/private/session\n')
        errors = cp.audit(self.root)['errors']
        self.assertTrue(any('private operator profile' in e for e in errors))
        self.assertTrue(any('private workspace path' in e for e in errors))

    def test_potential_secret_is_not_echoed(self):
        token = 'ghp_' + 'A' * 36
        (self.root / 'README.md').write_text(token)
        result = cp.audit(self.root)
        self.assertTrue(any('provider token' in e for e in result['errors']))
        self.assertNotIn(token, json.dumps(result))

    def test_metadata_asset_and_json_errors_fail(self):
        (self.root / 'assets/icon.svg').unlink()
        (self.root / 'assets/data.json').write_text('{"bad":NaN}')
        errors = cp.audit(self.root)['errors']
        self.assertTrue(any('icon_small' in e for e in errors))
        self.assertTrue(any('invalid JSON' in e for e in errors))


if __name__ == '__main__':
    unittest.main()
