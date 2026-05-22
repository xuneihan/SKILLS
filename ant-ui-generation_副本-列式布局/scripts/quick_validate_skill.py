#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


_FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
_KEY_RE = re.compile(r"^(name|description):\s*(.*)$")


def _validate_skill_md(root: Path) -> None:
    skill_md = root / "SKILL.md"
    if not skill_md.exists():
        raise SystemExit(f"Missing {skill_md}")

    text = skill_md.read_text(encoding="utf-8")
    m = _FM_RE.match(text)
    if not m:
        raise SystemExit("SKILL.md must start with YAML frontmatter fenced by ---")

    keys: dict[str, str] = {}
    for raw in m.group(1).splitlines():
        raw = raw.strip()
        if not raw:
            continue
        km = _KEY_RE.match(raw)
        if not km:
            raise SystemExit(f"Invalid frontmatter line: {raw!r}")
        key, value = km.group(1), km.group(2)
        if key in keys:
            raise SystemExit(f"Duplicate frontmatter key: {key}")
        keys[key] = value

    missing = [k for k in ("name", "description") if k not in keys]
    if missing:
        raise SystemExit(f"Missing frontmatter keys: {', '.join(missing)}")
    if len(keys) != 2:
        raise SystemExit("Frontmatter must contain only: name, description")

    expected_name = root.name
    actual_name = keys["name"].strip().strip('"').strip("'")
    if actual_name != expected_name:
        raise SystemExit(f"name mismatch: frontmatter {actual_name!r} != folder {expected_name!r}")

    desc = keys["description"].strip().strip('"').strip("'")
    if len(desc) < 20:
        raise SystemExit("description too short; include clear triggers and scope")


def _validate_openai_yaml(root: Path) -> None:
    openai_yaml = root / "agents" / "openai.yaml"
    if not openai_yaml.exists():
        raise SystemExit(f"Missing {openai_yaml}")

    text = openai_yaml.read_text(encoding="utf-8")
    required_fragments = [
        "references/ant-visual-profile.md",
        "references/LLMs.txt",
        "references/llms-full.txt",
        "column-based independent div columns",
        "Noto Sans SC",
        "PingFang SC",
        "sans-serif",
    ]
    for fragment in required_fragments:
        if fragment not in text:
            raise SystemExit(f"openai.yaml default_prompt missing required fragment: {fragment!r}")


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    _validate_skill_md(root)
    _validate_openai_yaml(root)
    print("OK")


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(1)
