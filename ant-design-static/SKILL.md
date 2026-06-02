---
name: ant-design-static
description: Use when generating static Ant Design-style admin HTML pages or components for backend drafts, prototypes, and visual page design.
---

# Ant Static Design

## Overview

Use this skill to generate static admin pages in an Ant Design 5 visual style.

Produce self-contained HTML that opens directly in the browser. Focus on visual structure, layout consistency, and stable static rendering. Do not treat this skill as a backend or production integration workflow.

## When to Use

- Use this skill for static admin HTML pages and components.
- Use it for Ant Design-style backend drafts, prototypes, and visual page generation.
- Do not use it for backend logic, API integration, or production framework implementation.

## Core Output Rules

1. Output self-contained static HTML by default.
2. Prefer a single file with inline CSS.
3. Use only lightweight vanilla JavaScript unless the user explicitly asks for another stack.
4. Do not install or import React, Ant Design, or other UI packages unless the user explicitly asks for that.
5. Keep structure aligned with the user request. Do not add extra sections, cards, panels, or mock modules unless required.
6. If the user provides fields, labels, modules, or page sections, preserve them exactly unless the user asks for changes.
7. Favor visual completeness and stable structure over unnecessary abstraction.
8. Avoid speculative features, fake workflows, hidden states, or decorative complexity that does not support the page goal.

## Visual Baseline

Use Ant Design 5 as the default visual baseline unless the user explicitly requests another direction.

Use the local Ant references as the default source for exact visual values.

- default primary color override: `#7C3AED`
- keep Ant Design 5 spacing, typography, border, radius, and control sizing semantics unless the user overrides them
- use `"Noto Sans SC", "PingFang SC", sans-serif` as the default font stack for Chinese UI text
- prefer `Inter` for numeric content such as amounts, metrics, percentages, and table number columns

## Layout and Structure Rules

1. Identify the page type first: list page, form page, detail page, modal, drawer, tabs, dashboard block, or mixed layout.
2. Apply global layout decisions first:
   - page background
   - container background
   - spacing rhythm
   - typography scale
   - border and radius system
   - control sizing
3. Apply component-level styles only to components that actually appear on the page.
4. Reuse a clear wrapper hierarchy so major sections are easy to read and maintain.
5. Prefer predictable spacing and alignment over decorative complexity.
6. Keep the DOM straightforward and avoid unnecessary nested wrappers.
7. Prefer simple, direct DOM hierarchy so the output is easier to import into Figma via HTML-to-Figma plugins.
8. Keep styles self-contained so the page renders consistently when opened directly.
9. Tables and lists should follow Ant Design-like spacing, borders, hover states, and action semantics.

## Page Patterns

Use page patterns as light structural guidance, not rigid templates.

- Query + list page: organize as query area, action area, and main list or table area
- Detail page: organize content into titled read-only sections
- Form page: group related fields into clear blocks with consistent label rhythm
- Modal or drawer: keep structure compact with title, content, and right-aligned footer actions
- Tabs: use only when the request or existing structure clearly implies multiple parallel sections

## Interaction Rules

- Implement real front-end interaction when it supports the page goal.
- For query and list pages, prefer working client-side filtering, keyword search, simple reset, tab switching, and other directly visible interactions.
- Keep interaction self-contained in the static HTML with lightweight vanilla JavaScript.
- Do not introduce backend APIs, persistence, or framework dependencies unless the user explicitly asks.
- Prefer direct, understandable logic over abstract state management.

## Capture-Friendly Constraints

Generated HTML should remain easy to inspect and reuse.

- keep rendering stable
- keep styles self-contained
- keep structure clear and shallow
- avoid unnecessary wrapper nesting when the same layout can be expressed more directly

## Priority Rules

Resolve conflicts in this order:

1. User explicit requirements
2. This skill's static HTML output rules
3. This skill's Ant visual baseline
4. Reference materials retrieved for missing details

If a reference example conflicts with the user's requirement, follow the user's requirement and preserve Ant-style consistency where possible.

## Reference Retrieval Workflow

Use references only as needed. Do not load large files by default.

Preferred order:

1. Use the built-in defaults in this skill first.
2. If exact token values are needed, read `references/ant-design-tokens.md`.
3. If a component or pattern needs additional guidance, use `references/LLMs.txt` as a topic index.
4. If exact original guidance is still needed, search `references/llms-full.txt` by focused visual keywords only.

Suggested lookup keywords:

- `table`
- `form`
- `input`
- `select`
- `button`
- `tag`
- `layout`
- `spacing`
- `font`
- `data-list`
- `data-display`
- `detail-page`
- `modal`
- `drawer`

Do not ingest `llms-full.txt` in full unless there is no smaller way to answer the current need.

## Review Checklist

Before finalizing output, check:

- Is the page type correctly interpreted?
- Are spacing, typography, radius, and borders internally consistent?
- Do controls follow a unified height system?
- Does the structure match the user's requested modules and fields exactly?
- Does the page feel like Ant Design 5 rather than a generic admin page?
- Is the HTML self-contained and directly openable?
- Is the DOM clean enough for inspection and downstream design use?

## Files in This Skill

- `references/ant-design-tokens.md`: condensed token and layout baseline
- `references/LLMs.txt`: Ant documentation topic index
- `references/llms-full.txt`: aggregated source documentation for targeted lookup
