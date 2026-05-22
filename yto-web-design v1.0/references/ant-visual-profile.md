# Ant Visual Profile (for yto-web-design)

## Source of truth

- `/Users/xu/.codex/skills/yto-web-design/references/LLMs.txt`
- `/Users/xu/.codex/skills/yto-web-design/references/llms-full.txt`

Use this file as the default visual baseline. Do not load `llms-full.txt` entirely unless required.

## Scope

- Visual style alignment for Ant Design pages in pure HTML/CSS/JS.
- No requirement to use React/Ant package imports.
- Keep skill-specific defaults:
  - Global font stack: `"Noto Sans SC", "PingFang SC", sans-serif`.
  - List/table interaction defaults and visual consistency rules.

## Retrieval protocol (token-efficient)

1. Start from `LLMs.txt` to locate relevant doc topics.
2. Query `llms-full.txt` by component/visual keywords only.
3. Extract only task-relevant visual rules (no full-document ingestion).

Suggested keywords:

- Table visuals: `table`, `header`, `row`, `hover`, `border`, `padding`, `ellipsis`, `empty`, `size`
- Data entry: `input`, `select`, `focus`, `status`, `error`, `disabled`
- Actions: `button`, `link`, `divider`, `tag`, `color`
- Layout/spec: `layout`, `spacing`, `font`, `motion`, `data-list`, `data-display`

## Default table baseline (from your reference)

Use this as the default fallback when no custom table pattern is provided:

- Columns: `Name`, `Age`, `Address`, `Tags`, `Action`
- Row examples: `John Brown`, `Jim Green`, `Joe Black`
- Name: link-style text
- Tags:
  - length > 5 => `geekblue`
  - else => `green`
  - value `loser` => `volcano`
- Action: `Invite {name}` + vertical divider + `Delete`

## Visual contract defaults

- Typography:
  - Global font: `"Noto Sans SC", "PingFang SC", sans-serif`
  - Text color: Ant-like neutral hierarchy (`0.85/0.65/0.45` opacity tiers)
- List/table block:
  - Baseline row height: `48px`.
  - Allow adaptive row expansion with visually consistent row heights.
  - Row hover: light gray (`#fafafa`) for full row.
  - Default: no vertical column lines.
  - Default: no list header bar.
  - Cell overflow: single-line ellipsis for generic text.
- Tags/Action:
  - Support Ant-like tag palettes and inline action links.
  - Keep action divider inside action content.

## Priority and conflict rules

1. User explicit requirement
2. Skill-specific defaults (font, list defaults)
3. Ant visual baseline from source docs

When examples conflict with user requirements, follow the user requirement first and keep Ant visual consistency where possible.
