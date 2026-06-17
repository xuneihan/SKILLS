---
name: antd-design
description: |
  Ant Design B端设计系统全维度技能指南。当用户要设计、评审、规范化任何B端/中后台页面时使用此skill，包括：管理系统页面、数据看板、表单页、详情页、列表页、工作台首页；或当用户提问Design Token、组件规范、间距字体规则、主题定制、深色模式、业务设计模式等Ant Design相关问题时必须触发此skill。即使用户未明说"Ant Design"，只要涉及B端中后台设计、企业后台系统UI、antd组件选型，也应触发。
---

# Ant Design B端设计 Skill

## 定位

Ant Design 是蚂蚁集团企业级 B端设计系统，完整覆盖视觉规范 + 交互模式 + 工程落地体系。主打一致性、高效率、可规模化、可定制化。

**四大设计价值观：** 确定性 / 意义感 / 自然 / 生长性

**适用场景：** OA/CRM/ERP 后台、数据报表平台、SaaS 系统、权限流程类系统、数据大屏

---

## 工作流程

收到 B端设计相关问题时，按以下顺序判断需要加载哪份参考文件：

| 问题类型 | 加载文件 |
|---------|---------|
| Token 色值 / 间距 / 字号 / 圆角 | `references/tokens.md` |
| 组件选型 / 状态规范 / 参数用法 | `references/components.md` |
| 页面布局 / 业务模式 / 信息架构 | `references/patterns.md` |
| 需要看完整落地案例 | `cases/antd-design-demo.html` |
| 设计自查 / 交付评审 | `assets/checklist.md` |

每次只加载与问题相关的文件，不要全部读入。

---

## 快速参考

### 间距原则
严格遵循 8px 栅格，只用 4/8/12/16/24/32/48px，禁止 3/5/7/9 等非 4 倍数值。

### 色彩原则
涨/成功 → `colorSuccess #52C41A`，跌/错误 → `colorError #FF4D4F`，警告 → `colorWarning #FAAD14`，主操作 → `colorPrimary #1677FF`。颜色不是唯一信息传达方式，状态同时用图标或文字辅助。

### 反馈原则
所有用户操作必须有反馈闭环：操作中（Spin / Button loading）→ 成功（message.success，2s）→ 失败（message.error，含原因）。危险操作前置 Popconfirm 或 Modal.confirm 二次确认。

### 标注原则
设计稿标注使用 Token 名称而非色值（如 `colorPrimary` 而非 `#1677FF`），间距标注 8px 倍数，组件状态必须全部覆盖。

---

## 参考文件说明

- `references/tokens.md` — 完整 Token 对照表（全局基础 Token + 组件级 Token + 主题定制方式）
- `references/components.md` — 核心组件用法细则（布局/导航/表单/表格/反馈，含状态规范和参数说明）
- `references/patterns.md` — 五种高频业务页面模式（搜索列表/表单/详情/看板/仪表盘，含结构图和交互规范）
- `cases/antd-design-demo.html` — 完整 B端后台交互 Demo，可在浏览器直接打开验证规范
- `assets/checklist.md` — 设计交付自查清单，覆盖 Token / 组件状态 / 页面模式 / 协作规范
