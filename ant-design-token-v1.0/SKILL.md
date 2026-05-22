---
name: ant-design-token
description: Use when generating, refactoring, or reviewing B-side admin pages that should follow Ant Design 5 visual tokens, component sizing, and common enterprise layout conventions.
---

# Ant Design Token

## Overview

Use this skill for Ant Design style back-office pages, especially list pages, search forms, detail views, drawers, modals, tables, tags, and dashboard blocks.

This skill is for visual and structural consistency, not business logic design. It helps convert vague "做成 Ant Design 风格" requests into repeatable layout, spacing, and token decisions.

## When to Use

Use this skill when the user:

- asks for Ant Design or Ant Design Pro style UI
- wants a B-end or admin page with consistent spacing, typography, and table/form density
- wants static HTML, React pages, or mockups aligned to Ant Design tokens
- asks to review whether a page "像不像 Ant Design" or which token values to use

Do not use this skill when:

- the project already has a different design system and the user wants that preserved
- the task is mainly backend behavior, API wiring, or business rules

## Workflow

1. Identify the page type first: list page, form page, detail page, modal, drawer, dashboard, or mixed layout.
2. Reuse existing project components and structure before introducing new wrappers or abstractions.
3. Apply global decisions first:
   - page background and container background
   - typography scale
   - spacing rhythm
   - border radius and border color
   - control heights
4. Then apply component-level decisions only for the components actually present on the page.
5. If exact values matter, read `references/ant-design-tokens.md` and copy only the relevant subset into the work.

## Default Rules

- Prefer Ant Design 5 visual language, not Ant Design 3 or 4.
- Prefer light theme unless the user explicitly asks for dark theme.
- For B-end pages, start from these defaults:
  - layout background: `#F5F5F5`
  - container background: `#FFFFFF`
  - primary color: `#1677FF`
  - base font size: `14px`
  - standard control height: `32px`
  - standard radius: `6px`
  - standard block spacing: `16px` or `24px` depending on hierarchy
- Prefer tables, filters, tags, and section cards to feel dense but not cramped.
- Prefer token-consistent values over hand-tuned one-off pixel values.

## Page Patterns

### List Page

- Top area: filter form + primary actions
- Main area: card or flat container with table
- Common spacing:
  - filter rows: `16px`
  - card padding: `24px`
  - table cell padding: use the reference values instead of inventing new ones

### Detail Page

- Split content into titled sections
- Use `16px` title size and stronger weight for section titles
- Group read-only fields in consistent rows or description-style blocks

### Modal or Drawer

- Title size: `16px`
- Content padding: `24px`
- Footer actions right-aligned
- Use the global mask and shadow values from the reference when exact fidelity matters

## Review Checklist

When reviewing or generating, check:

- Are background, radius, border, and spacing values internally consistent?
- Are form controls using a unified height system?
- Are table header, row hover, and selected states aligned with Ant-style defaults?
- Are tags, buttons, and status colors using semantic colors instead of arbitrary hex values?
- Did the implementation stay within the project scope without inventing extra components?

## Reference File

Read `references/ant-design-tokens.md` only when you need exact values.

Use it for:

- global token lookup
- layout sizing for B-end pages
- component token lookup for Button, Input, Table, Select, Modal, Tag, Pagination, Steps, and similar components

Avoid loading the whole reference if the task only needs one component or one page pattern.
