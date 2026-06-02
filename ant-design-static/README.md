# ant-design-static

`ant-design-static` 是一个用于生成 Ant Design 风格后台静态页面的 Codex Skill。

它的目标是根据自然语言需求，快速产出结构清晰、视觉完整、可直接在浏览器打开的后台 HTML 页面，适合用于原型设计、方案预览、页面评审，以及通过 HTML-to-Figma 插件导入 Figma 后继续编辑。

## 适用场景

- 后台列表页、详情页、表单页
- Drawer、Modal、Tabs、Dashboard 区块
- 静态原型和视觉稿预览
- HTML 导入 Figma 的设计衔接场景
- 正式前端开发前的页面结构确认

## 主要特点

- 输出静态 HTML，而不是前端工程
- 默认自包含，便于直接打开预览
- 风格贴近 Ant Design 5
- 不依赖 React、Ant Design npm 包或其他前端框架
- 只在需要时使用轻量 JavaScript
- 页面结构尽量清晰直接，便于后续修改和导入设计工具

## 包含内容

- `SKILL.md`：定义 skill 的适用范围、输出规则和生成原则
- `references/ant-design-tokens.md`：提供 Ant Design 风格的 token 基线
- `references/LLMs.txt`：提供 Ant Design 文档主题索引
- `references/llms-full.txt`：提供更完整的参考语料

## 不适合的场景

- 生产级前端工程开发
- API 联调和业务逻辑实现
- React / Vue 项目搭建
- 复杂状态管理和真实系统交互开发

## 总结

`ant-design-static` 是一个面向“静态后台页面生成”的 skill。  
它关注的是页面草稿、视觉结构和设计衔接，而不是工程化实现。

如果你的目标是先快速得到一个像 Ant Design 后台的 HTML 页面，这个 skill 就是为这个阶段准备的。
