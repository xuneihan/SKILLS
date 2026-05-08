---
name: excalidraw-diagram-generator-patch
description: Overlay patch for excalidraw-diagram-generator. Enforces delivery quality gates and blocks non-compliant output.
---

# Excalidraw Generator Patch

This is an overlay skill. It does NOT replace the upstream skill content.
It adds mandatory validation and delivery blocking rules.

## Upstream Skill
Always execute the normal generation/edit flow from:
`~/.codex/skills/excalidraw-diagram-generator/SKILL.md`

## Mandatory Patch Rules

1. After generating or editing `.excalidraw`, MUST run:
`node scripts/validate_excalidraw.js <file_path>`

2. Delivery is allowed ONLY when validator returns `PASS`.

3. If validator returns `FAIL`, MUST:
- report exact failed checks
- provide fix plan
- apply fixes
- re-run validator
- only then deliver

4. Never claim "done" before PASS.

## Quality Gates (enforced by validator)

- JSON validity: parseable JSON
- Binding integrity:
  - titles must remain unbound (`containerId` must be null)
  - second-level text must have `containerId`
  - parent rect must backlink text in `boundElements`
- No empty structural boxes in edited scope
- No duplicate structural boxes (same x/y/w/h in same scope)
- Text alignment consistency:
  - child text should be `textAlign=center`, `verticalAlign=middle`
- Layer integrity:
  - container should not visually cover its child text

## Output Contract

When finished, always output:

1. `Validation: PASS | FAIL`
2. failed checks (if any)
3. fixed items summary
4. target file path
