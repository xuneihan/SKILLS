---
name: zhijuan-image-contract
description: Analyze an attached image or local image path with Codex vision and return a JSON-only Zhijuan-style source-faithful reconstruction prompt contract. Use when the user asks for image-to-prompt, image reverse prompting, prompt contract, structured image generation prompt, JSON Prompt, recreation prompt, prompt_core, negative prompt, or Zhijuan-style visual reconstruction from an image without calling the Chrome extension API.
---

# Zhijuan Image Contract

Use this skill to convert one image into a machine-readable reconstruction prompt contract. This is a pure Codex vision workflow: do not require API keys, Chrome extension state, `chrome.storage.local`, browser context menus, or the project runtime endpoint unless the user explicitly asks for a different workflow.

## Input Contract

Require one attached image or one local image path. If the user provides neither, ask for an image before producing the contract.

When the input is a local path, inspect the image with the available image-viewing tool before answering. When the input is an attached image, inspect the attachment directly. Do not claim to have used the Chrome extension, popup, background service worker, or configured vision API.

## Output Contract

Return exactly one JSON object. Do not add Markdown, code fences, comments, prose before or after the JSON.

Use exactly this top-level shape:

```json
{
  "zh": {
    "prompt": "中文复刻提示词。",
    "analysis": "中文可见证据分析。"
  },
  "en": {
    "prompt": "English recreation prompt.",
    "analysis": "English visible-evidence analysis."
  },
  "ja": {
    "prompt": "日本語再現プロンプト。",
    "analysis": "日本語の可視証拠分析。"
  },
  "zh_style_tags": ["中文标签1", "中文标签2", "中文标签3", "中文标签4"],
  "en_style_tags": ["english tag 1", "english tag 2", "english tag 3", "english tag 4"],
  "ja_style_tags": ["日本語タグ1", "日本語タグ2", "日本語タグ3", "日本語タグ4"],
  "json_prompt": {
    "subject": "subject count, role, supported identity or source, key attributes",
    "action_pose": "pose, gesture, movement, gaze, placement, and scene logic",
    "details_appearance": "face and body traits, skin tone and texture, hair, coverings, markings, object text or graphics, surface relationships, props, and distinctive details",
    "environment_background": "foreground, midground, background, setting, depth, objects, and scene anchors",
    "lighting_atmosphere": "light source, direction, contrast, color temperature, shadows, haze, optical effects, and mood",
    "composition_framing": "aspect, distance, angle, crop, tilt, scale, placement, perspective, negative space, focus plane, and depth",
    "style_camera": "medium, realism, style_index 0-100, and useful camera, lens, post, brush, or render cues",
    "colors": ["#RRGGBB color name - visual role", "#RRGGBB color name - visual role", "#RRGGBB color name - visual role"],
    "materials": ["visible material, surface, or finish 1", "visible material, surface, or finish 2", "visible material, surface, or finish 3"],
    "aspect_ratio": "observed or likely simplified ratio such as 2:3, 1:1, or 16:9",
    "quality_modifiers": ["source fidelity cue 1", "source optical/style cue 2", "specific drift-control cue 3"],
    "likely_generation_intent": "one sentence about the visible creative goal"
  },
  "recreation_prompt": "Single-line English prompt for closest reconstruction.",
  "prompt_core": "Short English core prompt.",
  "negative_prompt": "Short English drift-control negative prompt."
}
```

The JSON block above is a schema example only. In the final answer, output raw JSON only.

## Core Policy

- Write toward the source image's actual visual result, not toward a cleaner, sharper, more commercial substitute.
- Identify and preserve the source aesthetic fingerprint before subject polish: soft focus, film blur, motion blur, foreground blur, shallow depth of field, low contrast, haze, bloom, halation, rim glow, volumetric or Tyndall light, smoke, flare, underexposure or overexposure, dark shadow detail, dappled light, compression texture, low-resolution feel, grain, worn surface, paper fiber, brush texture, UI screenshot capture, and imperfect phone-photo realism when visible.
- After the visual fingerprint, describe observable facts: subject count, recognizable anchors, people, pose, text, layout, crop, camera geometry, light, colors, materials, surface relationships, props, scene layers, and style.
- Put generation instructions only in prompt fields. Put analysis only in analysis fields. Ensure natural prompts and `json_prompt` share the same load-bearing facts.
- Use `clean`, `crisp`, `clear`, `sharp`, `smooth`, or `high-detail` only when the source visibly supports those qualities. Preserve blur, grain, haze, bloom, low fidelity, noise, dark exposure, wall cracks, mirror marks, paper texture, brush strokes, compression, and distortion when they are visible style or real environment.

## Evidence Rules

- Use visible evidence and strong visual recognition. Do not invent hidden lore, private identity, exact artist, exact brand, exact location, camera, lens, or tool.
- If a known public person, fictional/anime/game/comic/movie character, source work, event, landmark, poster, album cover, UI, game, website, or scene is strongly recognizable, include that anchor. If weaker, keep uncertainty in analysis and `json_prompt`, then write the visible resemblance as a clear generation target.
- For unknown private people, do not invent names. Still describe visible appearance in enough detail for reconstruction: face shape, facial proportions, skin tone depth and undertone, natural skin texture, hair color/style/texture, makeup, body proportions, pose, expression, clothing or coverings, accessories, and relationships between people.
- Ethnic or ancestry presentation is not verified identity. When visual evidence is strong and useful for reconstruction, use cautious visual wording such as `East Asian-presenting`, `Black-presenting`, `South Asian-presenting`, or `Mediterranean-looking`, paired with concrete skin, face, and hair traits. If evidence is weak, use only visible traits.

## Writing Standard

- Keep each language in its own field: `zh` fields and tags in Simplified Chinese, `en` fields and tags in English, `ja` fields and tags in Japanese.
- Write `zh.prompt`, `en.prompt`, and `ja.prompt` as dense readable reconstruction paragraphs with no labels.
- Do not put analysis wording, causal explanation, uncertainty language, slash-joined alternatives or directions, `A or B`, `可能`, `或者`, `因此`, `需保留`, or self-commentary in `zh.prompt`, `en.prompt`, `ja.prompt`, `recreation_prompt`, or `prompt_core`. Write combined directions with words, such as `upper right and front`; use `/` only when copying exact visible text such as a URL or watermark.
- Prefer concrete nouns, exact relationships, positions, quantities, surface behavior, focus behavior, and visible materials over generic quality words.
- Count people and repeated objects when clear. Preserve left, right, front, back, foreground, midground, background, crop, viewpoint, scale, tilt, negative space, z-order, and focus hierarchy when they affect reconstruction.
- Describe legible text exactly, including signs, watermarks, and prop text. Preserve original language and script, exact characters, placement, hierarchy, and relation; do not translate, romanize, paraphrase, replace, invent, or reorder text. Quote only when all characters are clear. In photos, do not quote small or blurred domain watermarks or prop branding; describe placement and style instead. For load-bearing text, add blockers for altered, missing, unreadable, translated, or moved text.
- For screenshots, UI, documents, posters, tickets, ads, and dense layouts, preserve the image as that object or capture. Keep layout, crop, edge cuts, overlays, panels, z-order, visible text language, and readable hierarchy. Reconstruct a clean readable version only when the source is a degraded thumbnail of a UI/document/poster rather than an intentional low-fidelity visual style.
- For surface relationships, describe what is visible instead of forcing a category. State where a pattern, graphic, text, paint, makeup, sticker, print, seam, strap, waistband, decal, armor, fabric, projection, or skin/body covering sits, what surface it follows, and which visible boundary or missing boundary matters. Use one clear generation target, not alternatives.
- Do not collapse ambiguous markings into a conventional object just because that object is common. If straps, seams, bare skin, navel, paint, fabric edges, glossy body paint, or skin-tight coverings appear in different regions, describe each region separately.
- Describe style as the source result: medium, realism level, stylization strength, brushwork, render finish, photographic finish, lens and focal feel, aperture and depth-of-field feel, shutter and motion feel, diffusion, halation, grain, compression, post and color grade, line quality, texture scale, and design language only when visible or useful.
- Preserve the most specific visible setting noun that helps reconstruction, such as bathroom mirror, football pitch, browser screenshot, service alley, storage backroom, studio portrait, or garden illustration. Do not replace it with a generic room, street, or backdrop.
- Treat camera, film, lens, cinema, and design vocabulary as visual reconstruction cues, not factual metadata. Use them only when they clarify the observed result.
- In `style_camera`, include `style_index 0-100` as visual stylization intensity, not as a generator parameter: 0-20 literal/documentary, 21-40 realistic/editorial, 41-60 cinematic/art-directed, 61-80 highly stylized/anime/fantasy/painterly, 81-100 extreme graphic/surreal/abstract.
- For `json_prompt.colors`, return 3-6 approximate HEX colors with color name and visual role. Do not output bare generic color names.
- In `json_prompt` string fields, use compact semicolon-separated clauses, but do not remove load-bearing facts to make them short.
- Return exactly four tags for each language. Tags are compact UI labels, not the main prompt.
- Keep `recreation_prompt` one line, generator-neutral, and complete enough to recreate the image. Use this order when it helps: aesthetic fingerprint, recognizable anchor, subject/action, composition/camera, lighting/atmosphere, materials/text/details, fidelity locks. It is usually 120-280 English words; complex posters, UI screenshots, group scenes, recognizable characters, or detailed surface relationships may use up to 360 words.
- Keep `prompt_core` as a compact reusable English summary of the essential subject, composition, lighting, palette, and source style.
- Make `negative_prompt` image-specific, plain comma-separated English phrases, normally 8-24 items. Block likely drift for this image: wrong identity or source, wrong subject count, changed face, body, or skin tone, altered pose, wrong surface or material reading, moved or translated text, redesigned UI or layout, wrong crop or viewpoint, missing props, extra objects, over-polished style, or unwanted artifacts. Do not stack generic blockers.
- Do not put blur, grain, haze, bloom, low resolution, compression, overexposure, underexposure, smoke, flare, dark shadows, or shallow depth of field in `negative_prompt` when they are part of the source look. For soft or low-fidelity sources, block over-sharpened face, glossy AI skin, hyper-detailed eyes, commercial retouching, sanitized high-resolution redesign, and sanitized studio relighting only when the source is not a studio photograph.
- For genuinely clean, smooth, high-clarity sources, add concise cleanliness controls such as clean transparent image, complete natural materials, smooth uniform texture, clear main subject, distinct background layers, and avoiding unwanted color spots, noise, cracks, collapse, and distortion.
- Do not include generator-specific syntax such as `--ar`, `--s`, `--raw`, `--iw`, `--no`, `BREAK`, weights, LoRA tags, model parameters, or bracketed prompt tokens in `recreation_prompt` or `prompt_core`.
- Use plain comma-separated English phrases in `negative_prompt`, not generator-specific syntax.
- Do not leave empty strings, `TBD`, `TODO`, `unknown`, or placeholder tokens. Use conservative broad wording when uncertain.
