# Figma MCP capture notes

Use when the user asks to “输出适合 Figma MCP / 生成 Figma 文件 / 导入到 Figma”.

## Recommended approach

1. Generate the HTML file with `scripts/generate_admin_mock.py`.
2. Serve the directory so Figma can capture a URL:
   - `python3 -m http.server 4173`
3. Call `mcp__figma__.generate_figma_design` with:
   - `outputMode: "newFile"` (preferred)
   - URL: `http://localhost:4173/<file>.html`

## Tips

- Keep the page width at 1440px for consistent captures.
- Avoid external assets (fonts/images) to reduce capture drift.
