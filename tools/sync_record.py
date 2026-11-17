"""Embed the canonical human record into the validation attachment without inventing content."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = '\n<!-- LOCKED-RECORD-APPENDIX -->\n'


def main():
    validation = ROOT / 'docs/validation-and-ai-use.md'
    text = validation.read_text(encoding='utf-8').split(MARKER)[0].rstrip()
    record = (ROOT / 'docs/locked-changed-input.md').read_text(encoding='utf-8')
    appendix = record.replace('# Locked Changed-Input Record', '## Appendix — Locked Changed-Input Record', 1)
    validation.write_text(text + '\n' + MARKER + '\n' + appendix, encoding='utf-8')
    print('Copied the actual canonical record into the validation attachment; no content generated.')


if __name__ == '__main__':
    main()
