# Ant Visual Profile (for ant-ui-generation)

## Source of truth

- `/Users/xu/.codex/skills/ant-ui-generation/references/LLMs.txt`
- `/Users/xu/.codex/skills/ant-ui-generation/references/llms-full.txt`

Use this file as the default visual baseline. Do not load `llms-full.txt` entirely unless required.

## Scope

- Visual style alignment for Ant Design pages in pure HTML/CSS/JS.
- No requirement to use React/Ant package imports.
- Keep skill-specific constraints:
  - Column-based list/table structure with independent `div` columns.
  - Global font stack: `"Noto Sans SC", "PingFang SC", sans-serif`.

## Retrieval protocol (token-efficient)

1. Start from `LLMs.txt` to locate relevant doc topics.
2. Query `llms-full.txt` by component/visual keywords only.
3. Extract only task-relevant visual rules (no full-document ingestion).

Suggested keywords:

- Table visuals: `table`, `header`, `row`, `hover`, `border`, `padding`, `ellipsis`, `empty`, `size`
- Data entry: `input`, `select`, `focus`, `status`, `error`, `disabled`
- Actions: `button`, `link`, `divider`, `tag`, `color`
- Layout/spec: `layout`, `spacing`, `font`, `motion`, `data-list`, `data-display`

## Visual contract defaults

- Typography:
  - Global font: `"Noto Sans SC", "PingFang SC", sans-serif`
  - Text color: Ant-like neutral hierarchy (`0.85/0.65/0.45` opacity tiers)
- List/table block:
  - Use column-based independent `div` columns only.
  - Baseline row height: `48px`.
  - Allow adaptive row expansion, but synchronize same-row height across columns.
  - Row hover: light gray (`#fafafa`) for full row.
  - Default: no vertical column lines.
  - Default: no list header bar.
  - Cell overflow: single-line ellipsis for generic text.
- Tags/Action:
  - Support Ant-like tag palettes and inline action links.
  - Keep action divider inside action content (not as column grid separator).

## Priority and conflict rules

1. User explicit requirement
2. Skill-specific constraints (column layout, font, defaults)
3. Ant visual baseline from source docs

When Ant examples conflict with column layout, preserve column layout and adapt visuals only.
