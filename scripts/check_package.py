#!/usr/bin/env python3
"""Check the public package using only Python's standard library.

Checks local references, JSON syntax, basic authored metadata, retained notices
and known private artifacts. This is not a host-schema or legal certification.
"""
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent.parent
IGNORED_PARTS = {'.git', '.venv', '__pycache__', '.pytest_cache', 'dist', 'build'}
TEXT_SUFFIXES = {'.md', '.txt', '.py', '.yaml', '.yml', '.json'}
REQUIRED = ('SKILL.md', 'agents/openai.yaml', 'README.md', 'NOTICE.md',
            'LICENSE', 'LICENSE.upstream.txt', 'PROVENANCE.md')
LINK = re.compile(r'!?\[[^\]]*\]\(\s*(?:<([^>]+)>|([^\s)]+))(?:\s+"[^"]*")?\s*\)')
URI = re.compile(r'^[A-Za-z][A-Za-z0-9+.-]*:')
PRIVATE_PATTERNS = (
    ('private workspace path', re.compile(r'/work[s]pace/')),
    ('private home path', re.compile(r'/(?:ho[m]e|Us[e]rs)/[^/\s]+/')),
    ('private-key block', re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')),
    ('provider token', re.compile(r'gh[pousr]_[A-Za-z0-9]{36,}|AKIA[A-Z0-9]{16}|sk-(?:proj-)?[A-Za-z0-9_-]{40,}')),
)


def one_scalar(text, key):
    """Read a simple scalar from this package's authored metadata style."""
    matches = re.findall(r'^\s*' + re.escape(key) + r':\s*(\S[^\n]*)$', text, re.M)
    if len(matches) != 1:
        raise ValueError(f'expected one nonempty {key} field')
    value = matches[0].strip()
    if value.startswith('"'):
        return json.loads(value)
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    return value


def audit(root, release=False):
    root = Path(root).resolve()
    errors, warnings = [], []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f'missing required file: {name}')
    files = [p for p in sorted(root.rglob('*'))
             if not set(p.relative_to(root).parts) & IGNORED_PARTS]
    for path in files:
        rel = path.relative_to(root).as_posix()
        if path.is_symlink():
            errors.append(f'symlink is not a public-package input: {rel}')
            continue
        if not path.is_file():
            continue
        if rel == 'references/operator-profile.md':
            errors.append('private operator profile included: ' + rel)
        if path.name == '.env' or (path.name.startswith('.env.') and path.name != '.env.example'):
            errors.append('local environment file included: ' + rel)
        if path.suffix not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding='utf-8')
        except (OSError, UnicodeError) as error:
            errors.append(f'cannot read text file {rel}: {type(error).__name__}')
            continue
        for label, pattern in PRIVATE_PATTERNS:
            if pattern.search(text):
                # Never reproduce a potential secret in a checker result.
                errors.append(f'{label} found in {rel}')
        if path.suffix == '.json':
            try:
                json.loads(text, parse_constant=lambda _: (_ for _ in ()).throw(ValueError()))
            except ValueError:
                errors.append('invalid JSON: ' + rel)
        if path.suffix == '.md':
            for match in LINK.finditer(text):
                href = match.group(1) or match.group(2)
                if URI.match(href) or href.startswith('#'):
                    continue
                target = unquote(href.split('#', 1)[0].split('?', 1)[0])
                if not target:
                    continue
                resolved = (path.parent / target).resolve()
                line = text.count('\n', 0, match.start()) + 1
                if not resolved.is_relative_to(root):
                    errors.append(f'local link escapes repository: {rel}:{line}')
                elif not resolved.exists():
                    errors.append(f'missing local link target {target}: {rel}:{line}')
    skill = root / 'SKILL.md'
    if skill.is_file():
        text = skill.read_text(encoding='utf-8')
        try:
            if not text.startswith('---\n') or '\n---\n' not in text[4:]:
                raise ValueError('missing YAML frontmatter delimiters')
            front = text[4:].split('\n---\n', 1)[0]
            if one_scalar(front, 'name') != 'codex-red':
                raise ValueError('public skill name must be codex-red')
            if not one_scalar(front, 'description').strip():
                raise ValueError('empty description')
        except (ValueError, TypeError) as error:
            errors.append('SKILL.md metadata: ' + str(error))
    metadata = root / 'agents/openai.yaml'
    if metadata.is_file():
        text = metadata.read_text(encoding='utf-8')
        try:
            if not re.search(r'^interface:\s*$', text, re.M):
                raise ValueError('missing interface mapping')
            if one_scalar(text, 'display_name') != 'Codex Red':
                raise ValueError('public display name must be Codex Red')
            if '$codex-red' not in one_scalar(text, 'default_prompt'):
                raise ValueError('default prompt must invoke $codex-red')
            for field in ('icon_small', 'icon_large'):
                icon = (root / one_scalar(text, field)).resolve()
                if not icon.is_relative_to(root) or not icon.is_file():
                    raise ValueError(f'{field} does not name an included local file')
        except (ValueError, TypeError) as error:
            errors.append('agents/openai.yaml metadata: ' + str(error))
    upstream = root / 'LICENSE.upstream.txt'
    if upstream.is_file():
        text = upstream.read_text(encoding='utf-8')
        required = ('MIT License', 'Copyright (c) 2024-2025 SnailSploit / Kai Aizen',
                    'Permission is hereby granted', 'THE SOFTWARE IS PROVIDED "AS IS"')
        if not all(term in text for term in required):
            errors.append('upstream MIT notice is incomplete or unrecognized')
    license_file = root / 'LICENSE'
    license_decided = license_file.is_file() and bool(license_file.read_text(encoding='utf-8').strip())
    if license_decided:
        text = license_file.read_text(encoding='utf-8')
        if 'MIT License' not in text or 'Copyright (c) 2026 Codex Red contributors' not in text:
            errors.append('project MIT license is incomplete or unrecognized')
    return {'checks_passed': not errors, 'release_checks_passed': not errors and license_decided,
            'checked_files': sum(p.is_file() for p in files), 'errors': errors, 'warnings': warnings,
            'limits': ['Basic authored metadata checks, not full YAML or current host-schema validation.',
                       'Known-pattern publication checks, not a complete secret scanner or security audit.',
                       'License-file presence is not legal verification of ownership or permissions.']}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--release', action='store_true', help='Run the same publication checks before a release')
    args = parser.parse_args(argv)
    result = audit(args.root, args.release)
    print(json.dumps(result, indent=2))
    return 0 if result['checks_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
