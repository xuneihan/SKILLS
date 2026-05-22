# Ant Design Token

This directory is a Codex/OpenAI skill project for Ant Design style B-side admin UI work.

## File Roles

### `SKILL.md`

`SKILL.md` is the skill itself.

It defines:

- the skill id via frontmatter `name`
- when the skill should be used via `description`
- the actual instructions, workflow, and rules the model should follow

If you want to change how the skill behaves, edit `SKILL.md`.

### `agents/openai.yaml`

`agents/openai.yaml` is the OpenAI/Codex-facing interface metadata.

It defines:

- `display_name`: the human-readable name shown in UI
- `short_description`: the short summary shown in UI
- `default_prompt`: the default prompt text used to route work into this skill

If you want to change how the skill is presented or invoked from the OpenAI/Codex side, edit `agents/openai.yaml`.

## Mental Model

- `SKILL.md` answers: what should this skill do?
- `agents/openai.yaml` answers: how should this skill appear and be entered?

## Optional References

Files under `references/` are supporting material. They are read only when the skill needs exact values or extra reference context.
