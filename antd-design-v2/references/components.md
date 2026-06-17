# 核心组件用法细则

---

## 布局组件

### Layout（页面骨架）

B端标准布局结构：

```
Layout (height: 100vh; overflow: hidden)
  ├── Header（固定顶部，height: 48/56px）
  └── Layout (flex: 1; overflow: hidden; min-height: 0)
        ├── Sider（左侧导航，width: 200px，可折叠至 48px）
        └── Content（overflow-y: auto；页面内容区）
```

**关键 CSS 规则：**
- 最外层 Layout 必须 `height: 100vh; overflow: hidden`，防止切换内容时出现文档级滚动条
- 内层 flex 子项必须 `min-height: 0`，避免 flex 子元素撑破父容器
- 滚动只发生在 Content 区，Sider / Header 不参与页面滚动

### Grid（栅格）

| 场景 | 配置 |
|------|------|
| 标准表单 | `<Row gutter={[24, 16]}>` 24px 列间距，16px 行间距 |
| KPI 卡片 | `<Col span={6}>` 四列等宽，响应式加 `xs={24} sm={12} lg={6}` |
| 详情页 | `<Descriptions column={2}>` 两列，复杂信息三列 |
| 全屏容器 | `max-width: 1440px; margin: 0 auto; padding: 0 24px` |

---

## 导航组件

### Menu（侧边导航）

```jsx
<Menu
  mode="inline"
  defaultSelectedKeys={['dashboard']}
  items={menuItems}
/>
```

- `inline` 模式用于侧边栏，`horizontal` 用于顶部导航
- 图标统一使用线性风格（antd Icons 或 Feather Icons），宽高 16px，`stroke-width: 1.75`
- 多级菜单最深 3 层，超过 3 层考虑重构信息架构
- 选中态背景 `colorPrimaryBg #E6F4FF`，文字和图标 `colorPrimary #1677FF`

### Breadcrumb（面包屑）

- 固定在页面内容区顶部，位于页面标题上方
- 根节点通常为系统名称，点击返回工作台首页
- 超过 4 层时中间段折叠，保留首尾节点

### Tabs（标签页）

| 类型 | 适用场景 |
|------|---------|
| `line`（默认） | 页面级内容切换（详情页多维度信息） |
| `card` | 工作区多标签（类 IDE 多文档） |
| `editable-card` | 支持用户自定义增删的工作区 |

- Tabs 切换不改变 URL 时，`activeKey` 受控管理
- 切换时下方内容高度变化可能引发布局偏移，用 `min-height` 固定内容区最小高度

---

## 表单组件

### Form（表单容器）

```jsx
<Form
  form={form}
  layout="horizontal"     // horizontal / vertical / inline
  labelCol={{ span: 6 }}  // 标签列宽，通常 4-8 span
  wrapperCol={{ span: 18 }}
  onFinish={handleSubmit}
>
```

**表单规范：**

| 规范项 | 说明 |
|--------|------|
| 标签对齐 | 右对齐（`labelAlign="right"`），固定宽度 84px 或 6 span |
| 必填标记 | 默认红色 `*` 在标签前，全表单非必填时隐藏 `*` 改用注释说明 |
| 字段宽度 | 按语义定宽：姓名 160px、手机 180px、邮箱 240px、长文本 100% |
| 字段分组 | 超过 8 个字段时按信息归属用 Card 或 Divider 分组 |
| 底部操作 | `position: sticky; bottom: 0`，顺序：取消 → 辅助操作 → 主提交 |
| 提交防抖 | 提交时 Button 进入 `loading` 并禁用，防重复提交 |

### Input / Select / DatePicker

| 组件 | 规范 |
|------|------|
| Input | `placeholder` 说明格式而非重复标签名；搜索框搭配 suffix 搜索图标 |
| Input.TextArea | `autoSize={{ minRows: 3, maxRows: 8 }}`，避免固定高度截断文字 |
| Select | 超过 10 个选项加 `showSearch`；选项 label 保持一行，截断用 Tooltip |
| DatePicker | 区间选择用 `RangePicker`；禁用未来/过去日期用 `disabledDate` |
| Upload | 图片预览用 `listType="picture-card"`，文件列表用 `listType="text"` |

---

## 数据展示组件

### Table（表格）

```jsx
<Table
  columns={columns}
  dataSource={data}
  rowKey="id"
  loading={loading}
  pagination={{ pageSize: 20, showTotal: (total) => `共 ${total} 条` }}
  scroll={{ x: 1200 }}  // 列多时固定宽度，横向滚动
/>
```

**列规范：**

| 列类型 | 规范 |
|--------|------|
| 操作列 | 固定 `fixed="right"`，宽度 120-180px；操作超过 3 个收进 `Dropdown` |
| 状态列 | 用 `Tag` 搭配语义色；状态种类超过 5 个加 `filters` 筛选 |
| 数值列 | 右对齐 `align="right"`；金额保留 2 位小数，千分位逗号分隔 |
| 时间列 | 格式 `YYYY-MM-DD HH:mm`，hover 显示完整时间戳 Tooltip |
| 长文本列 | `ellipsis: { showTitle: false }` + Tooltip，列固定最大宽度 |
| 空值 | 显示 `—`（em dash）而非空字符串或 null |

**表格状态：**
- 加载中：`loading={true}` 显示骨架屏效果
- 空数据：自定义 `locale.emptyText`，说明为何无数据，并提供操作入口
- 全选操作：`rowSelection` + BatchAction 工具栏，选中后工具栏浮现

### Descriptions（描述列表）

```jsx
<Descriptions
  title="基本信息"
  bordered           // 有边框版，用于详情页主信息区
  column={2}
  size="small"
/>
```

- `bordered` 用于重要信息展示，无边框用于卡片内辅助信息
- 长文本字段 `span={2}` 占满整行
- 值为空时显示 `—`

### Card（卡片）

| 场景 | 配置 |
|------|------|
| KPI 指标卡 | `bordered={false}`，`bodyStyle={{ padding: '16px 20px' }}`，数字 24px 粗体 |
| 内容区块 | `title` + 右侧 `extra` 操作，`padding: 24px` |
| 可展开卡片 | 搭配 `Collapse` 或自定义折叠 |

---

## 反馈组件

### Message / Notification / Modal（反馈三件套）

| 组件 | 适用场景 | 规范 |
|------|---------|------|
| `message.success/error/warning` | 轻量操作反馈（保存、删除、复制） | 顶部居中；持续 2-3s；不打断操作 |
| `Notification` | 系统级通知（任务完成、消息到达） | 右上角；持续 4-6s；可包含跳转链接 |
| `Modal.confirm` | 危险操作二次确认（删除、禁用、清空） | 标题明确说明操作；正文说明影响范围；确认按钮用 `danger` 类型 |
| `Modal`（自定义） | 中等复杂度表单、详情查看 | 宽度 480-800px；底部 footer 操作区 |
| `Drawer` | 复杂表单（字段多）、行内编辑扩展、操作上下文需保留 | 宽度 400-640px；右侧滑入 |

**反馈原则：所有用户操作必须有闭环**

```
发起操作 → Button loading（进行中）→ message.success（成功，2s）
                                    → message.error（失败，含原因）
```

### Alert（提示条）

| 类型 | 场景 |
|------|------|
| `info` | 页面说明、使用提示、字段补充说明 |
| `warning` | 即将到期、配置未完成、潜在风险 |
| `error` | 服务异常、权限不足、数据错误 |
| `success` | 操作完成后的内联确认（通常用 message，Alert 用于持久状态） |

### Empty / Spin / Skeleton（空态与加载态）

- 空态：自定义 `description`，提供操作引导（如"立即添加"按钮）；图标用系统内置或品牌插画
- Spin：包裹整个内容区，`size="large"`，配合 `tip` 文字
- Skeleton：首次加载时替代真实内容，`active` 开启动画；列表用 `Skeleton.List`，卡片用自定义骨架块

---

## Tag / Badge / Tooltip（标记与提示）

### Tag 状态色映射

| 业务状态 | Tag 属性 |
|---------|---------|
| 正常 / 成功 / 通过 | `color="success"` |
| 待处理 / 审核中 / 进行中 | `color="processing"` |
| 警告 / 即将到期 / 异常 | `color="warning"` |
| 错误 / 失败 / 拒绝 | `color="error"` |
| 禁用 / 已完成 / 归档 | `color="default"` |

禁止用 `#52C41A` 直接写色值，必须走 `color="success"` 语义属性，保证主题切换时自动适配。

### Badge

- 未读消息数：`<Badge count={5}>`，超过 99 显示 `99+`（`overflowCount={99}`）
- 状态指示点：`<Badge status="success/processing/error" text="在线">`，在线状态用 processing（呼吸动画）
