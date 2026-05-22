---
name: yto-web-design
description: Generate Ant Design-style admin UI as self-contained HTML (inline CSS + small vanilla JS when needed) without installing React or Ant Design packages. Use when building backend pages/components for any project (list pages, dialogs, tabs, detail pages, forms). Align visuals with the local Ant docs corpus (`references/LLMs.txt` and `references/llms-full.txt`) through on-demand retrieval, while preserving skill defaults such as global font and list interaction behavior.
---

# YTO Web Design

## Core rules

1. Implement Ant Design-like visual language and interaction semantics, but do not install or import React/Ant Design packages.
2. Keep output structure aligned with the user request. Do not add extra sections unless explicitly requested.
3. Apply unified font globally for all text: `"Noto Sans SC", "PingFang SC", sans-serif`.
4. Use the provided 10-step purple scale as theme tokens, with default primary at shade `6` (`#7C3AED`) when not overridden.
5. Follow Ant-like list/table visual semantics (header/body spacing, typography, borders, hover, ellipsis, tags, action links).
6. If the user provides fields, use those fields exactly. If not provided, generate context-appropriate mock fields and values dynamically.

## Table reference baseline (default)

When the user asks for a generic table and does not specify another pattern, use this baseline:

- Columns: `Name`, `Age`, `Address`, `Tags`, `Action`
- Row examples: `John Brown`, `Jim Green`, `Joe Black`
- Name cell: render as link-style text (`<a>` visual)
- Tags cell: map tag colors as:
  - tag length > 5 -> `geekblue`
  - otherwise -> `green`
  - tag value `loser` -> `volcano`
- Action cell: render `Invite {name}` + vertical divider + `Delete`

Use this baseline for visual/interaction consistency, then override columns/data when user provides explicit business fields.

## Ant docs retrieval workflow (must follow)

1. Read `references/ant-visual-profile.md` first.
2. Use `references/LLMs.txt` as topic index to locate relevant docs.
3. Query `references/llms-full.txt` by component/visual keywords only.
4. Extract only the current-task visual rules. Do not ingest the full file.

Use this workflow whenever visual details are not already covered by `ant-visual-profile.md`.

## Priority and conflict rules

1. User explicit requirements
2. Skill-specific defaults (font, list defaults, interaction defaults)
3. Ant visual baseline from `LLMs.txt` + `llms-full.txt`

If source examples conflict with user requirements, follow the user requirement first and keep Ant visual consistency where possible.

## Interaction behavior defaults

- Input: implement `default` and `:focus` (purple border/ring) by default.
- Input error state: include only when the user explicitly asks for validation/required/error behavior.
- Buttons: use CSS `:hover` and `:active` for interaction states by default.
- Avoid adding JS state machines unless the user explicitly asks for richer state transitions.

## List defaults (important)

- Default row baseline height is `48px`.
- Allow adaptive row height when content exceeds one line, and keep row heights visually consistent.
- Default row hover uses Ant-like light gray highlight (not blue).
- Default list has no vertical column divider lines.
- Default list has no "列表结果 / 条数" header bar.
- Show list header or vertical lines only when the user explicitly requests them.

## List rendering behavior

- If a field corresponds to `Tags`/`标签`, render Ant-like color tags.
- If a field corresponds to `Action`/`操作`, render Ant-like action links with divider (for example `Invite xx | Delete`).
- For generic fields, render single-line ellipsis cells with Ant-like spacing and border rhythm.

## Layout interpretation

- This skill is generic for future projects, not a single fixed page template.
- Infer page shape from the prompt:
  - Modal request -> build modal-focused markup
  - Tabs request -> build tabs
  - Detail request -> build detail layout
  - Query + list request -> build query area + action area + list/table block

## Figma compatibility

- Prefer predictable spacing and clear structural wrappers so sections can be selected and edited in Figma.
- Keep assets self-contained (inline CSS, no external package dependency) unless user requests otherwise.

## Quick command (optional helper)

`python3 scripts/generate_admin_mock.py --out /tmp/ant-admin.html --page-title 'Channel Management' --fields 'Name,Age,Address,Tags,Action' --rows 10`

## Files in this skill

- `scripts/generate_admin_mock.py`: optional helper generator for query/list pages
- `assets/admin-states-template.html`: base template used by the helper script
- `references/ant-visual-profile.md`: distilled visual baseline and retrieval protocol
- `references/LLMs.txt`: Ant docs index
- `references/llms-full.txt`: full Ant docs corpus (retrieve snippets only)
- `references/figma-capture.md`: notes for capturing generated HTML into Figma MCP
