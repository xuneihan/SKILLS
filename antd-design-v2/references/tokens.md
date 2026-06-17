# Design Token 完整参考

Ant Design 5.x 完全基于 Token 驱动，所有样式全局统一管控，可主题替换，可工程落地。

---

## 全局基础 Token

### 主色 / 功能色

| Token 名称 | 色值 | 用途 |
|-----------|------|------|
| `colorPrimary` | `#1677FF` | 主操作按钮、链接、选中态、focus 环 |
| `colorPrimaryHover` | `#4096FF` | 主色悬停态 |
| `colorPrimaryActive` | `#0958D9` | 主色按下态 |
| `colorPrimaryBg` | `#E6F4FF` | 主色浅背景（选中行、激活菜单） |
| `colorSuccess` | `#52C41A` | 成功、通过、正常、涨 |
| `colorSuccessBg` | `#F6FFED` | 成功浅背景 |
| `colorWarning` | `#FAAD14` | 警告、待处理、注意 |
| `colorWarningBg` | `#FFFBE6` | 警告浅背景 |
| `colorError` | `#FF4D4F` | 错误、失败、禁用、跌 |
| `colorErrorBg` | `#FFF2F0` | 错误浅背景 |
| `colorInfo` | `#1677FF` | 信息提示（同主色） |

> **注意：** 4.x 的 `colorPrimary` 是 `#165DFF`，5.x 改为 `#1677FF`，从旧版迁移时需同步更新 Figma 变量。

---

### 中性色（文本 / 背景 / 边框）

| Token 名称 | 色值 | 用途 |
|-----------|------|------|
| `colorTextHeading` | `rgba(0,0,0,.88)` | 页面标题、卡片标题 |
| `colorText` | `rgba(0,0,0,.88)` | 正文、表格内容 |
| `colorTextSecondary` | `rgba(0,0,0,.65)` | 次要信息、标签、注释 |
| `colorTextDisabled` | `rgba(0,0,0,.25)` | 禁用态文字、占位符 |
| `colorBgContainer` | `#FFFFFF` | 卡片、输入框、弹窗背景 |
| `colorBgLayout` | `#F5F5F5` | 页面级背景 |
| `colorBgElevated` | `#FFFFFF` | 浮层（下拉、tooltip、弹窗）背景 |
| `colorBorder` | `#D9D9D9` | 输入框、表格边框 |
| `colorBorderSecondary` | `#F0F0F0` | 分割线、卡片边框 |
| `colorFillSecondary` | `rgba(0,0,0,.06)` | 表格斑马纹、hover 背景 |
| `colorFillQuaternary` | `rgba(0,0,0,.02)` | 表头背景、禁用输入框背景 |

> **暗色模式适配：** 使用 rgba 透明度表达的中性色在暗色模式下自动适配，无需单独维护暗色变量集。

---

### 尺寸 / 间距 / 圆角 Token

| Token 名称 | 值 | 用途 |
|-----------|-----|------|
| `borderRadius` | `6px` | 按钮、输入框、标签默认圆角 |
| `borderRadiusLG` | `8px` | 卡片、弹窗、抽屉圆角 |
| `borderRadiusSM` | `4px` | 小尺寸组件圆角 |
| `fontSize` | `14px` | 默认正文字号 |
| `fontSizeSM` | `12px` | 辅助文字、注释、标签 |
| `fontSizeLG` | `16px` | 正文大号 |
| `fontSizeHeading1` | `38px` | H1 |
| `fontSizeHeading2` | `30px` | H2 |
| `fontSizeHeading3` | `24px` | H3 |
| `fontSizeHeading4` | `20px` | H4 |
| `fontSizeHeading5` | `16px` | H5 |
| `lineHeight` | `1.5714` | 14px 正文行高 |

**间距序列（8px 栅格）：** 4 / 8 / 12 / 16 / 20 / 24 / 32 / 40 / 48 / 64px

禁止使用 3 / 5 / 7 / 9 / 11 等非 4 倍数值。

---

### 阴影层级

| Token 名称 | 值 | 适用场景 |
|-----------|-----|---------|
| `boxShadowCard` | `0 1px 2px -2px rgba(0,0,0,.16), 0 3px 6px 0 rgba(0,0,0,.12), 0 5px 12px 4px rgba(0,0,0,.09)` | 卡片悬浮、抽拉 |
| `boxShadowModal` | `0 6px 16px 0 rgba(0,0,0,.08), 0 3px 6px -4px rgba(0,0,0,.12), 0 9px 28px 8px rgba(0,0,0,.05)` | 弹窗、全局浮层 |
| `boxShadowDrawer` | `-6px 0 16px 0 rgba(0,0,0,.08), -3px 0 6px -4px rgba(0,0,0,.12), -9px 0 28px 8px rgba(0,0,0,.05)` | 侧滑抽屉 |

---

## 组件级 Token（精准定制）

通过 ConfigProvider 的 `theme.components` 可对单个组件单独定制，不影响其他组件：

```javascript
<ConfigProvider theme={{
  token: {
    colorPrimary: '#1677FF',   // 全局主色
    borderRadius: 6,            // 全局圆角
  },
  components: {
    Button: { borderRadius: 8 },          // 仅按钮圆角
    Table: { headerBg: '#FAFAFA' },       // 仅表头背景
    Card:  { paddingLG: 24 },            // 仅卡片内边距
  }
}}>
  <App />
</ConfigProvider>
```

---

## 主题定制场景

| 场景 | 操作 |
|------|------|
| 品牌色替换 | 修改 `colorPrimary`，antd 自动生成 10 级色阶 |
| 亮色/暗色切换 | `algorithm: theme.darkAlgorithm` |
| 圆角风格调整 | 修改 `borderRadius`（方正感 2px / 默认 6px / 圆润 12px） |
| 紧凑模式 | `algorithm: theme.compactAlgorithm` |
| 多业务线主题隔离 | 嵌套 ConfigProvider，内层覆盖外层 |

**落地方式：** 设计端 Figma 变量同步 Token 名称 → 前端 ConfigProvider 工程落地，保证设计开发 1:1 还原。
