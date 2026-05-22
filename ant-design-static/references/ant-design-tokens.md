## 一、色彩体系
### 1.1 品牌色与语义色
| Token | 默认值 | 用途 |
|---|---|---|
| colorPrimary | `#1677FF` | 品牌主色，按钮/链接/选中态 |
| colorSuccess | `#52C41A` | 成功状态（Result/Tag/Alert） |
| colorWarning | `#FAAD14` | 警告状态（Alert/Notification） |
| colorError | `#FF4D4F` | 错误/危险状态（按钮/校验） |
| colorInfo | `#1677FF` | 信息提示（同主色） |
| colorLink | `#1677FF` | 超链接默认色 |
### 1.2 预设调色板
| Token | 值 | Token | 值 |
|---|---|---|---|
| red | `#F5222D` | blue | `#1677FF` |
| orange | `#FA8C16` | purple | `#722ED1` |
| yellow | `#FADB14` | cyan | `#13C2C2` |
| gold | `#FAAD14` | green | `#52C41A` |
| volcano | `#FA541C` | magenta | `#EB2F96` |
| geekblue | `#2F54EB` | lime | `#A0D911` |
### 1.3 中性色（文字）
| Token | 值 | 用途 |
|---|---|---|
| colorText | `rgba(0,0,0,0.88)` | 主文字（标题/正文） |
| colorTextSecondary | `rgba(0,0,0,0.65)` | 次要文字（标签/描述） |
| colorTextTertiary | `rgba(0,0,0,0.45)` | 辅助文字（说明/占位符） |
| colorTextQuaternary | `rgba(0,0,0,0.25)` | 最弱文字（禁用/提示） |
| colorTextHeading | `rgba(0,0,0,0.88)` | 标题文字 |
| colorTextDescription | `rgba(0,0,0,0.45)` | 描述文字 |
| colorTextDisabled | `rgba(0,0,0,0.25)` | 禁用态文字 |
| colorTextPlaceholder | `rgba(0,0,0,0.25)` | 占位符文字 |
| colorTextLabel | `rgba(0,0,0,0.65)` | 表单标签文字 |
### 1.4 背景色
| Token | 值 | 用途 |
|---|---|---|
| colorBgBase | `#FFFFFF` | 背景色派生基准（勿直接使用） |
| colorBgContainer | `#FFFFFF` | 容器背景（卡片/输入框/按钮） |
| colorBgElevated | `#FFFFFF` | 浮层背景（弹窗/下拉/菜单） |
| colorBgLayout | `#F5F5F5` | 页面整体布局背景 |
| colorBgMask | `rgba(0,0,0,0.45)` | 遮罩层背景 |
| colorBgSpotlight | `rgba(0,0,0,0.85)` | Tooltip 背景 |
### 1.5 填充色
| Token | 值 | 用途 |
|---|---|---|
| colorFill | `rgba(0,0,0,0.15)` | 最深填充（Slider hover） |
| colorFillSecondary | `rgba(0,0,0,0.06)` | 二级填充（Rate/Skeleton/表格 hover） |
| colorFillTertiary | `rgba(0,0,0,0.04)` | 三级填充（Segmented/默认填充） |
| colorFillQuaternary | `rgba(0,0,0,0.02)` | 最弱填充（斑马纹/区分边界） |
| colorFillAlter | `rgba(0,0,0,0.02)` | 替代背景色 |
| colorFillContent | `rgba(0,0,0,0.06)` | 内容区背景 |
### 1.6 边框色
| Token | 值 | 用途 |
|---|---|---|
| colorBorder | `#D9D9D9` | 默认边框（表单/卡片分隔） |
| colorBorderSecondary | `#F0F0F0` | 次级边框（同 colorSplit） |
| colorSplit | `rgba(5,5,5,0.06)` | 分割线（带透明度） |
---
## 二、字体体系
### 2.1 字体族
| Token | 值 |
|---|---|
| fontFamily | `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'` |
| fontFamilyCode | `'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace` |
### 2.2 字号梯度
| Token | 值 | 用途 |
|---|---|---|
| fontSize | `14px` | 基准字号（正文） |
| fontSizeSM | `12px` | 小字号（辅助文字/标签） |
| fontSizeLG | `16px` | 大字号（h5/强调文字） |
| fontSizeXL | `20px` | 超大字号（h4） |
| fontSizeHeading5 | `16px` | h5 标题 |
| fontSizeHeading4 | `20px` | h4 标题 |
| fontSizeHeading3 | `24px` | h3 标题 |
| fontSizeHeading2 | `30px` | h2 标题 |
| fontSizeHeading1 | `38px` | h1 标题 |
| fontSizeIcon | `12px` | 操作图标字号 |
### 2.3 行高梯度
| Token | 值 | 对应字号 |
|---|---|---|
| lineHeight | `1.5714` | 14px 正文 |
| lineHeightSM | `1.6667` | 12px 小字 |
| lineHeightLG | `1.5` | 16px 大字 |
| lineHeightHeading5 | `1.5` | 16px |
| lineHeightHeading4 | `1.4` | 20px |
| lineHeightHeading3 | `1.3333` | 24px |
| lineHeightHeading2 | `1.2667` | 30px |
| lineHeightHeading1 | `1.2105` | 38px |
### 2.4 字重
| Token | 值 | 用途 |
|---|---|---|
| fontWeightStrong | `600` | 标题/选中项加粗 |
| （正文默认） | `400` | 普通正文 |
---
## 三、间距体系
### 3.1 基础单位
| Token | 值 | 说明 |
|---|---|---|
| sizeUnit | `4px` | 最小间距单位 |
| sizeStep | `4px` | 间距递增步长 |
### 3.2 尺寸梯度
| Token | 值 | 计算方式 |
|---|---|---|
| sizeXXS | `4px` | 1 × sizeUnit |
| sizeXS | `8px` | 2 × sizeUnit |
| sizeSM | `12px` | 3 × sizeUnit |
| size | `16px` | 4 × sizeUnit（基准） |
| sizeMS | `16px` | 同 size |
| sizeMD | `20px` | 5 × sizeUnit |
| sizeLG | `24px` | 6 × sizeUnit |
| sizeXL | `32px` | 8 × sizeUnit |
| sizeXXL | `48px` | 12 × sizeUnit |
### 3.3 Margin 梯度
| Token | 值 | 典型用途 |
|---|---|---|
| marginXXS | `4px` | 最小外边距 |
| marginXS | `8px` | 紧凑元素间距 |
| marginSM | `12px` | 小间距 |
| margin | `16px` | 标准间距 |
| marginMD | `20px` | 中等间距 |
| marginLG | `24px` | 大间距（区块间） |
| marginXL | `32px` | 超大间距 |
| marginXXL | `48px` | 最大间距 |
### 3.4 Padding 梯度
| Token | 值 | 典型用途 |
|---|---|---|
| paddingXXS | `4px` | 最小内边距 |
| paddingXS | `8px` | 紧凑内边距 |
| paddingSM | `12px` | 小内边距 |
| padding | `16px` | 标准内边距 |
| paddingMD | `20px` | 中等内边距 |
| paddingLG | `24px` | 大内边距（卡片/弹窗） |
| paddingXL | `32px` | 超大内边距 |
### 3.5 内容区 Padding
| Token | 值 | 用途 |
|---|---|---|
| paddingContentHorizontal | `16px` | 内容水平内边距 |
| paddingContentHorizontalLG | `24px` | 大屏内容水平内边距 |
| paddingContentHorizontalSM | `16px` | 小屏内容水平内边距 |
| paddingContentVertical | `12px` | 内容垂直内边距 |
| paddingContentVerticalLG | `16px` | 大屏内容垂直内边距 |
| paddingContentVerticalSM | `8px` | 小屏内容垂直内边距 |
---
## 四、圆角体系
| Token | 值 | 用途 |
|---|---|---|
| borderRadius | `6px` | 基础圆角（按钮/输入框/选择器） |
| borderRadiusSM | `4px` | 小圆角（小尺寸按钮/输入框） |
| borderRadiusLG | `8px` | 大圆角（卡片/弹窗/抽屉） |
| borderRadiusXS | `2px` | 极小圆角（Segmented/箭头） |
| borderRadiusOuter | `4px` | 外部圆角 |
---
## 五、边框体系
| Token | 值 | 用途 |
|---|---|---|
| lineWidth | `1px` | 基础边框宽度 |
| lineWidthBold | `2px` | 加粗边框（轮廓类组件） |
| lineWidthFocus | `3px` | 聚焦态边框宽度 |
| lineType | `solid` | 边框样式 |
---
## 六、控件高度体系
| Token | 值 | 用途 |
|---|---|---|
| controlHeightXS | `16px` | 超小控件 |
| controlHeightSM | `24px` | 小控件（小按钮/小输入框） |
| controlHeight | `32px` | 标准控件（按钮/输入框/选择器） |
| controlHeightLG | `40px` | 大控件（大按钮/大输入框） |
| controlInteractiveSize | `16px` | 交互元素尺寸（Checkbox/Radio） |
### 控件内边距
| Token | 值 | 用途 |
|---|---|---|
| controlPaddingHorizontal | `12px` | 标准控件水平内边距 |
| controlPaddingHorizontalSM | `8px` | 小控件水平内边距 |
---
## 七、阴影体系
| Token | 值 | 用途 |
|---|---|---|
| boxShadow | `0 6px 16px 0 rgba(0,0,0,0.08), 0 3px 6px -4px rgba(0,0,0,0.12), 0 9px 28px 8px rgba(0,0,0,0.05)` | 一级阴影（卡片/弹窗） |
| boxShadowSecondary | 同上 | 二级阴影 |
| boxShadowTertiary | `0 1px 2px 0 rgba(0,0,0,0.03), 0 1px 6px -1px rgba(0,0,0,0.02), 0 2px 4px 0 rgba(0,0,0,0.02)` | 三级阴影（轻量浮层） |
---
## 八、动效体系
### 8.1 动画时长
| Token | 值 | 用途 |
|---|---|---|
| motionDurationFast | `0.1s` | 快速（小元素交互） |
| motionDurationMid | `0.2s` | 中速（中等元素交互） |
| motionDurationSlow | `0.3s` | 慢速（大元素/页面级交互） |
### 8.2 缓动曲线
| Token | 值 | 用途 |
|---|---|---|
| motionEaseInOut | `cubic-bezier(0.645, 0.045, 0.355, 1)` | 标准进出 |
| motionEaseOut | `cubic-bezier(0.215, 0.61, 0.355, 1)` | 标准退出 |
| motionEaseInBack | `cubic-bezier(0.71, -0.46, 0.88, 0.6)` | 回弹进入 |
| motionEaseOutBack | `cubic-bezier(0.12, 0.4, 0.29, 1.46)` | 回弹退出 |
| motionEaseOutCirc | `cubic-bezier(0.08, 0.82, 0.17, 1)` | 圆形退出 |
| motionEaseInOutCirc | `cubic-bezier(0.78, 0.14, 0.15, 0.86)` | 圆形进出 |
| motionEaseInQuint | `cubic-bezier(0.755, 0.05, 0.855, 0.06)` | 五次方进入 |
| motionEaseOutQuint | `cubic-bezier(0.23, 1, 0.32, 1)` | 五次方退出 |
### 8.3 动画控制
| Token | 值 | 说明 |
|---|---|---|
| motion | `true` | 全局动画开关 |
| motionBase | `0` | 动画基础时长 |
| motionUnit | `0.1` | 动画时长变化单位 |
---
## 九、层级体系（z-index）
| Token | 值 | 用途 |
|---|---|---|
| zIndexBase | `0` | 基础层级 |
| zIndexPopupBase | `1000` | 浮层基础层级（Dropdown/Tooltip/Popover） |
> Ant Design 内部组件层级递增规则：
> - Dropdown/Tooltip/Popover: `1000+`
> - Modal/Drawer: `1000+`
> - Message/Notification: `1010+`
> - Popconfirm: `1030+`
---
## 十、响应式断点
| Token | 值 | 范围 |
|---|---|---|
| screenXS | `480px` | 480 ~ 575 |
| screenSM | `576px` | 576 ~ 767 |
| screenMD | `768px` | 768 ~ 991 |
| screenLG | `992px` | 992 ~ 1199 |
| screenXL | `1200px` | 1200 ~ 1599 |
| screenXXL | `1600px` | 1600 ~ 1919 |
| screenXXXL | `1920px` | ≥ 1920 |
---
## 十一、聚焦与交互态
| Token | 值 | 用途 |
|---|---|---|
| controlOutline | `rgba(5,145,255,0.1)` | 输入框聚焦外轮廓色 |
| controlOutlineWidth | `2px` | 聚焦外轮廓宽度 |
| colorErrorOutline | `rgba(255,38,5,0.06)` | 错误态聚焦外轮廓色 |
| colorWarningOutline | `rgba(255,215,5,0.1)` | 警告态聚焦外轮廓色 |
| controlItemBgHover | `rgba(0,0,0,0.04)` | 列表项 hover 背景 |
| controlItemBgActive | `#E6F4FF` | 列表项选中背景 |
| controlItemBgActiveHover | `#BAE0FF` | 列表项选中+hover 背景 |
| controlItemBgActiveDisabled | `rgba(0,0,0,0.15)` | 列表项选中+禁用背景 |
| colorBgTextHover | `rgba(0,0,0,0.06)` | 文字 hover 背景 |
| colorBgTextActive | `rgba(0,0,0,0.15)` | 文字 active 背景 |
| colorBgContainerDisabled | `rgba(0,0,0,0.04)` | 容器禁用态背景 |
---
## 十二、图标与其他
| Token | 值 | 用途 |
|---|---|---|
| colorIcon | `rgba(0,0,0,0.45)` | 弱操作图标色（清除/关闭） |
| colorIconHover | `rgba(0,0,0,0.88)` | 弱操作图标 hover 色 |
| colorHighlight | `#FF4D4F` | 高亮色（搜索匹配等） |
| colorTextLightSolid | `#FFFFFF` | 深色背景上的文字色（主按钮文字） |
| colorWhite | `#FFFFFF` | 纯白（不随主题变化） |
| opacityImage | `1` | 图片透明度 |
| opacityLoading | `0.65` | 加载态透明度 |
| sizePopupArrow | `16px` | 弹出层箭头尺寸 |
---
## 十三、B 端页面布局量化参考
以下为基于 Ant Design Pro / 典型 B 端系统的推荐布局参数：
### 13.1 整体框架
| 区域 | 推荐值 | 说明 |
|---|---|---|
| 侧边栏宽度（展开） | `208px` | 亮色主题，白色背景 + 右边框 `#F0F0F0` |
| 侧边栏宽度（收起） | `48px` | 仅显示图标 |
| 顶部栏高度 | `48px` | 亮色主题，白色背景 + 下边框 `#F0F0F0` |
| 内容区 padding | `24px` | 四周统一 paddingLG |
| 内容区背景色 | `#F5F5F5` | 对应 colorBgLayout |
| 卡片间距 | `16px` | 对应 margin |
### 13.2 卡片/区块
| 属性 | 推荐值 | Token 对应 |
|---|---|---|
| 卡片内边距 | `24px` | paddingLG |
| 卡片圆角 | `8px` | borderRadiusLG |
| 卡片阴影 | boxShadowTertiary | 轻量阴影 |
| 卡片背景 | `#FFFFFF` | colorBgContainer |
| 区块标题字号 | `16px` | fontSizeLG |
| 区块标题字重 | `600` | fontWeightStrong |
| 区块间距 | `24px` | marginLG |
### 13.3 表格
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 表头背景 | `#FAFAFA` | colorFillAlter 近似 |
| 表头字号 | `14px` | fontSize |
| 表头字色 | `rgba(0,0,0,0.88)` | colorTextHeading |
| 表头字重 | `500 ~ 600` | — |
| 单元格字号 | `14px` | fontSize |
| 单元格内边距 | `16px` | padding |
| 紧凑单元格内边距 | `8px` | paddingXS |
| 行 hover 背景 | `#FAFAFA` | controlItemBgHover 近似 |
| 行分割线 | `#F0F0F0` | colorBorderSecondary |
| 斑马纹背景 | `rgba(0,0,0,0.02)` | colorFillQuaternary |
### 13.4 表单
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 标签字号 | `14px` | fontSize |
| 标签字色 | `rgba(0,0,0,0.65)` | colorTextLabel |
| 必填星号色 | `#FF4D4F` | colorError |
| 输入框高度 | `32px` | controlHeight |
| 输入框圆角 | `6px` | borderRadius |
| 输入框边框 | `1px solid #D9D9D9` | lineWidth + colorBorder |
| 输入框聚焦边框 | 主色 | colorPrimary |
| 输入框聚焦阴影 | `0 0 0 2px rgba(主色,0.1)` | controlOutline |
| 输入框禁用背景 | `rgba(0,0,0,0.04)` | colorBgContainerDisabled |
| 表单项间距 | `24px` | marginLG |
| 表单栅格间距 | `16px ~ 24px` | — |
### 13.5 按钮
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 默认高度 | `32px` | controlHeight |
| 小按钮高度 | `24px` | controlHeightSM |
| 大按钮高度 | `40px` | controlHeightLG |
| 水平内边距 | `16px` | padding |
| 圆角 | `6px` | borderRadius |
| 字号 | `14px` | fontSize |
| 主按钮背景 | 主色 | colorPrimary |
| 主按钮文字 | `#FFFFFF` | colorTextLightSolid |
| 默认按钮边框 | `#D9D9D9` | colorBorder |
| 危险按钮色 | `#FF4D4F` | colorError |
### 13.6 状态标签（Tag）
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 内边距 | `0 7px` | — |
| 字号 | `12px` | fontSizeSM |
| 圆角 | `4px` | borderRadiusSM |
| 行高 | `20px` | — |
| 成功色 | 背景 `#F6FFED` 文字 `#52C41A` 边框 `#B7EB8F` | colorSuccessBg/Text/Border |
| 警告色 | 背景 `#FFFBE6` 文字 `#FAAD14` 边框 `#FFE58F` | colorWarningBg/Text/Border |
| 错误色 | 背景 `#FFF2F0` 文字 `#FF4D4F` 边框 `#FFCCC7` | colorErrorBg/Text/Border |
| 信息色 | 背景 `#E6F4FF` 文字 `#1677FF` 边框 `#91CAFF` | colorInfoBg/Text/Border |
| 默认色 | 背景 `#FAFAFA` 文字 `rgba(0,0,0,0.88)` 边框 `#D9D9D9` | — |
### 13.7 弹窗（Modal）
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 遮罩背景 | `rgba(0,0,0,0.45)` | colorBgMask |
| 弹窗背景 | `#FFFFFF` | colorBgElevated |
| 弹窗圆角 | `8px` | borderRadiusLG |
| 弹窗内边距 | `24px` | paddingLG |
| 弹窗阴影 | boxShadow | 一级阴影 |
| 标题字号 | `16px` | fontSizeLG |
| 标题字重 | `600` | fontWeightStrong |
| 底部按钮区 | 右对齐，间距 `8px` | marginXS |
### 13.8 分页
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 按钮尺寸 | `32px × 32px` | controlHeight |
| 圆角 | `6px` | borderRadius |
| 字号 | `14px` | fontSize |
| 选中态背景 | 主色 | colorPrimary |
| 选中态文字 | `#FFFFFF` | colorTextLightSolid |
| hover 边框 | 主色 | colorPrimary |
### 13.9 步骤条（Steps）
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 圆点尺寸 | `32px` | controlHeight |
| 圆点字号 | `14px` | fontSize |
| 已完成色 | 主色 | colorPrimary |
| 当前步骤色 | 主色 + 外发光 | colorPrimary + controlOutline |
| 未完成色 | `#F0F0F0` 文字 `rgba(0,0,0,0.25)` | colorBorderSecondary + colorTextDisabled |
| 连接线高度 | `1px` | lineWidth |
| 标签字号 | `14px` | fontSize |
---

## 十五、组件级 Design Token（Component Token）
以下为 B 端最常用组件的组件级 Token 默认值，用于精确控制单个组件的样式。
### 15.1 Button 按钮
| Token | 默认值 | 说明 |
|---|---|---|
| contentFontSize | `14` | 按钮内容字号 |
| contentFontSizeLG | `16` | 大号按钮字号 |
| contentFontSizeSM | `14` | 小号按钮字号 |
| fontWeight | `400` | 文字字重 |
| paddingInline | `15` | 横向内间距 |
| paddingInlineLG | `15` | 大号横向内间距 |
| paddingInlineSM | `7` | 小号横向内间距 |
| iconGap | `8` | 图标与文字间距 |
| defaultBg | `#FFFFFF` | 默认按钮背景 |
| defaultColor | `rgba(0,0,0,0.88)` | 默认按钮文字色 |
| defaultBorderColor | `#D9D9D9` | 默认按钮边框色 |
| defaultHoverBg | `#FFFFFF` | 默认按钮 hover 背景 |
| defaultHoverColor | `#4096FF` | 默认按钮 hover 文字色 |
| defaultHoverBorderColor | `#4096FF` | 默认按钮 hover 边框色 |
| defaultActiveColor | `#0958D9` | 默认按钮 active 文字色 |
| defaultActiveBorderColor | `#0958D9` | 默认按钮 active 边框色 |
| defaultShadow | `0 2px 0 rgba(0,0,0,0.02)` | 默认按钮阴影 |
| primaryColor | `#FFF` | 主按钮文字色 |
| primaryShadow | `0 2px 0 rgba(5,145,255,0.1)` | 主按钮阴影 |
| dangerColor | `#FFF` | 危险按钮文字色 |
| dangerShadow | `0 2px 0 rgba(255,38,5,0.06)` | 危险按钮阴影 |
| ghostBg | `transparent` | 幽灵按钮背景 |
| textHoverBg | `rgba(0,0,0,0.04)` | 文本按钮 hover 背景 |
| linkHoverBg | `transparent` | 链接按钮 hover 背景 |
### 15.2 Input 输入框
| Token | 默认值 | 说明 |
|---|---|---|
| inputFontSize | `14` | 字号 |
| inputFontSizeLG | `16` | 大号字号 |
| inputFontSizeSM | `14` | 小号字号 |
| paddingBlock | `4` | 纵向内边距 |
| paddingBlockLG | `7` | 大号纵向内边距 |
| paddingBlockSM | `0` | 小号纵向内边距 |
| paddingInline | `11` | 横向内边距 |
| paddingInlineLG | `11` | 大号横向内边距 |
| paddingInlineSM | `7` | 小号横向内边距 |
| activeBg | `#FFFFFF` | 激活态背景 |
| activeBorderColor | `#1677FF` | 激活态边框色 |
| activeShadow | `0 0 0 2px rgba(5,145,255,0.1)` | 激活态阴影 |
| hoverBg | `#FFFFFF` | hover 背景 |
| hoverBorderColor | `#4096FF` | hover 边框色 |
| addonBg | `rgba(0,0,0,0.02)` | 前/后置标签背景 |
| errorActiveShadow | `0 0 0 2px rgba(255,38,5,0.06)` | 错误态阴影 |
| warningActiveShadow | `0 0 0 2px rgba(255,215,5,0.1)` | 警告态阴影 |
### 15.3 Table 表格
| Token | 默认值 | 说明 |
|---|---|---|
| cellFontSize | `14` | 单元格字号（大尺寸） |
| cellFontSizeMD | `14` | 单元格字号（中等） |
| cellFontSizeSM | `14` | 单元格字号（小尺寸） |
| cellPaddingBlock | `16` | 单元格纵向内边距 |
| cellPaddingBlockMD | `12` | 中等纵向内边距 |
| cellPaddingBlockSM | `8` | 小尺寸纵向内边距 |
| cellPaddingInline | `16` | 单元格横向内边距 |
| cellPaddingInlineMD | `8` | 中等横向内边距 |
| cellPaddingInlineSM | `8` | 小尺寸横向内边距 |
| headerBg | `#FAFAFA` | 表头背景 |
| headerColor | `rgba(0,0,0,0.88)` | 表头文字色 |
| headerBorderRadius | `8` | 表头圆角 |
| headerSplitColor | `#F0F0F0` | 表头分割线色 |
| headerSortActiveBg | `#F0F0F0` | 排序激活态背景 |
| headerFilterHoverBg | `rgba(0,0,0,0.06)` | 筛选 hover 背景 |
| borderColor | `#F0F0F0` | 边框/分割线色 |
| rowHoverBg | `#FAFAFA` | 行 hover 背景 |
| rowSelectedBg | `#E6F4FF` | 行选中背景 |
| rowSelectedHoverBg | `#BAE0FF` | 行选中 hover 背景 |
| rowExpandedBg | `rgba(0,0,0,0.02)` | 行展开背景 |
| footerBg | `#FAFAFA` | 底部背景 |
| footerColor | `rgba(0,0,0,0.88)` | 底部文字色 |
| bodySortBg | `#FAFAFA` | 排序列背景 |
| expandIconBg | `#FFFFFF` | 展开按钮背景 |
| selectionColumnWidth | `32` | 选择列宽度 |
| stickyScrollBarBg | `rgba(0,0,0,0.25)` | 粘性滚动条背景 |
### 15.4 Modal 对话框
| Token | 默认值 | 说明 |
|---|---|---|
| titleFontSize | `16` | 标题字号 |
| titleLineHeight | `1.5` | 标题行高 |
| titleColor | `rgba(0,0,0,0.88)` | 标题字色 |
| contentBg | `#FFFFFF` | 内容区背景 |
| headerBg | `transparent` | 头部背景 |
| footerBg | `transparent` | 底部背景 |
> Modal 默认宽度 `520px`，confirm 类型默认宽度 `416px`，默认 z-index `1000`。
### 15.5 Form 表单（推荐布局参数）
| 属性 | 推荐值 | 说明 |
|---|---|---|
| labelAlign | `right` | 标签对齐方式 |
| labelCol span | `6 ~ 8` | 标签栅格占位（水平布局） |
| wrapperCol span | `16 ~ 18` | 控件栅格占位 |
| layout | `horizontal` | 默认水平布局 |
| size | `middle` | 默认中等尺寸 |
| requiredMark | `true` | 显示必填标记 |
| colon | `true` | 标签后冒号 |
| 表单项间距 | `24px` | marginLG |
| 标签字色 | `rgba(0,0,0,0.88)` | colorText |
| 必填星号色 | `#FF4D4F` | colorError |
### 15.6 Tag 标签
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 字号 | `12px` | fontSizeSM |
| 行高 | `20px` | — |
| 内边距 | `0 7px` | — |
| 圆角 | `4px` | borderRadiusSM |
| 边框宽度 | `1px` | lineWidth |
预设颜色标签（带边框）：
| 语义 | 背景 | 文字 | 边框 |
|---|---|---|---|
| success | `#F6FFED` | `#52C41A` | `#B7EB8F` |
| processing | `#E6F4FF` | `#1677FF` | `#91CAFF` |
| warning | `#FFFBE6` | `#FAAD14` | `#FFE58F` |
| error | `#FFF2F0` | `#FF4D4F` | `#FFCCC7` |
| default | `#FAFAFA` | `rgba(0,0,0,0.88)` | `#D9D9D9` |
| purple | `#F9F0FF` | `#722ED1` | `#D3ADF7` |
| cyan | `#E6FFFB` | `#13C2C2` | `#87E8DE` |
### 15.7 Steps 步骤条
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 圆点尺寸 | `32px` | controlHeight |
| 小圆点尺寸 | `8px` | dot 模式 |
| 图标尺寸 | `32px` | — |
| 标题字号 | `16px` | fontSizeLG |
| 描述字号 | `14px` | fontSize |
| 标题字色（完成） | `rgba(0,0,0,0.88)` | colorText |
| 标题字色（等待） | `rgba(0,0,0,0.45)` | colorTextTertiary |
| 连接线色（完成） | 主色 | colorPrimary |
| 连接线色（等待） | `#F0F0F0` | colorBorderSecondary |
### 15.8 Pagination 分页
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 按钮尺寸 | `32px` | controlHeight |
| 小按钮尺寸 | `24px` | controlHeightSM |
| 圆角 | `6px` | borderRadius |
| 字号 | `14px` | fontSize |
| 选中背景 | 主色 | colorPrimary |
| 选中文字 | `#FFF` | colorTextLightSolid |
| hover 边框 | 主色 | colorPrimary |
| 禁用色 | `rgba(0,0,0,0.25)` | colorTextDisabled |
### 15.9 Card 卡片
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 内边距 | `24px` | paddingLG |
| 圆角 | `8px` | borderRadiusLG |
| 头部字号 | `16px` | fontSizeLG |
| 头部字重 | `600` | fontWeightStrong |
| 头部内边距 | `0 0 8px 0` | — |
| 头部边框 | `#F0F0F0` | colorBorderSecondary |
| 阴影 | boxShadowTertiary | 轻量阴影 |
| 背景 | `#FFFFFF` | colorBgContainer |
### 15.10 Descriptions 描述列表
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 标签字色 | `rgba(0,0,0,0.65)` | colorTextSecondary |
| 内容字色 | `rgba(0,0,0,0.88)` | colorText |
| 标签字号 | `14px` | fontSize |
| 内容字号 | `14px` | fontSize |
| 行间距 | `16px` | margin |
| 列间距 | `24px` | marginLG |
| 边框色 | `#F0F0F0` | colorBorderSecondary |
### 15.11 Collapse 折叠面板
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 头部内边距 | `12px 16px` | paddingSM + padding |
| 头部背景 | `rgba(0,0,0,0.02)` | colorFillAlter |
| 头部字号 | `14px` | fontSize |
| 内容内边距 | `16px` | padding |
| 边框色 | `#D9D9D9` | colorBorder |
| 圆角 | `8px` | borderRadiusLG |
### 15.12 Menu 导航菜单
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 菜单项高度 | `40px` | — |
| 菜单项字号 | `14px` | fontSize |
| 菜单项内边距 | `0 16px` | — |
| 选中背景 | 主色浅背景 | colorPrimaryBg |
| 选中文字 | 主色 | colorPrimary |
| hover 背景 | `rgba(0,0,0,0.04)` | colorFillTertiary |
| 子菜单缩进 | `24px` | — |
| 分组标题字号 | `12px` | fontSizeSM |
| 分组标题字色 | `rgba(0,0,0,0.45)` | colorTextTertiary |
### 15.13 Breadcrumb 面包屑
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 字号 | `14px` | fontSize |
| 当前项字色 | `rgba(0,0,0,0.88)` | colorText |
| 链接字色 | `rgba(0,0,0,0.45)` | colorTextTertiary |
| 分隔符字色 | `rgba(0,0,0,0.45)` | colorTextTertiary |
| 分隔符 | `/` | — |
### 15.14 Drawer 抽屉
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 默认宽度 | `378px` | — |
| 大宽度 | `736px` | — |
| 头部内边距 | `16px 24px` | — |
| 内容内边距 | `24px` | paddingLG |
| 底部内边距 | `16px 24px` | — |
| 标题字号 | `16px` | fontSizeLG |
| 标题字重 | `600` | fontWeightStrong |
| 遮罩背景 | `rgba(0,0,0,0.45)` | colorBgMask |
| z-index | `1000` | zIndexPopupBase |
### 15.15 Alert 警告提示
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 内边距 | `8px 12px` | — |
| 带描述内边距 | `20px 24px` | — |
| 圆角 | `8px` | borderRadiusLG |
| 字号 | `14px` | fontSize |
| success | 背景 `#F6FFED` 边框 `#B7EB8F` | — |
| info | 背景 `#E6F4FF` 边框 `#91CAFF` | — |
| warning | 背景 `#FFFBE6` 边框 `#FFE58F` | — |
| error | 背景 `#FFF2F0` 边框 `#FFCCC7` | — |
### 15.16 Message 全局提示
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 内容内边距 | `9px 12px` | — |
| 圆角 | `8px` | borderRadiusLG |
| 阴影 | boxShadow | 一级阴影 |
| 字号 | `14px` | fontSize |
| 距顶部 | `8px` | — |
| z-index | `1010` | — |
### 15.17 Upload 上传
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 拖拽区边框 | `1px dashed #D9D9D9` | — |
| 拖拽区圆角 | `8px` | borderRadiusLG |
| 拖拽区内边距 | `16px ~ 24px` | — |
| hover 边框色 | 主色 | colorPrimary |
| 图标字号 | `48px` | — |
| 提示文字色 | `rgba(0,0,0,0.88)` | colorText |
| 描述文字色 | `rgba(0,0,0,0.45)` | colorTextTertiary |
### 15.18 Select 选择器
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 高度 | `32px` | controlHeight |
| 大号高度 | `40px` | controlHeightLG |
| 小号高度 | `24px` | controlHeightSM |
| 圆角 | `6px` | borderRadius |
| 下拉面板圆角 | `8px` | borderRadiusLG |
| 选项内边距 | `5px 12px` | — |
| 选项 hover 背景 | `rgba(0,0,0,0.04)` | colorFillTertiary |
| 选项选中背景 | `#E6F4FF` | controlItemBgActive |
| 多选标签背景 | `rgba(0,0,0,0.02)` | colorFillQuaternary |
| 多选标签圆角 | `4px` | borderRadiusSM |
### 15.19 DatePicker / TimePicker
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 高度 | `32px` | controlHeight |
| 圆角 | `6px` | borderRadius |
| 面板宽度 | `288px` | — |
| 单元格尺寸 | `36px` | — |
| 选中背景 | 主色 | colorPrimary |
| 今天标记 | 主色边框 | colorPrimary |
| hover 背景 | `rgba(0,0,0,0.04)` | colorFillTertiary |
### 15.20 Tabs 标签页
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 标签字号 | `14px` | fontSize |
| 标签内边距 | `12px 0` | — |
| 标签间距 | `32px` | — |
| 选中字色 | 主色 | colorPrimary |
| 默认字色 | `rgba(0,0,0,0.88)` | colorText |
| 下划线宽度 | `2px` | lineWidthBold |
| 下划线色 | 主色 | colorPrimary |
| 卡片背景 | `rgba(0,0,0,0.02)` | colorFillAlter |
| 卡片圆角 | `8px 8px 0 0` | — |
### 15.21 Radio 单选框
| Token | 默认值 | 说明 |
|---|---|---|
| radioSize | `16` | 单选框尺寸 |
| dotSize | `8` | 圆点大小 |
| dotColorDisabled | `rgba(0,0,0,0.25)` | 圆点禁用色 |
| buttonBg | `#FFFFFF` | 按钮背景 |
| buttonCheckedBg | `#FFFFFF` | 按钮选中背景 |
| buttonColor | `rgba(0,0,0,0.88)` | 按钮文字色 |
| buttonPaddingInline | `15` | 按钮横向内边距 |
| buttonSolidCheckedBg | `#1677FF` | 实色按钮选中背景 |
| buttonSolidCheckedColor | `#FFF` | 实色按钮选中文字 |
| buttonSolidCheckedHoverBg | `#4096FF` | 实色按钮选中 hover |
| buttonSolidCheckedActiveBg | `#0958D9` | 实色按钮选中 active |
| buttonCheckedBgDisabled | `rgba(0,0,0,0.15)` | 选中禁用背景 |
| buttonCheckedColorDisabled | `rgba(0,0,0,0.25)` | 选中禁用文字 |
| wrapperMarginInlineEnd | `8` | 右间距 |
### 15.22 Checkbox 多选框
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 尺寸 | `16px` | controlInteractiveSize |
| 圆角 | `2px` | borderRadiusXS |
| 选中背景 | 主色 | colorPrimary |
| 选中边框 | 主色 | colorPrimary |
| 未选中边框 | `#D9D9D9` | colorBorder |
| hover 边框 | 主色 | colorPrimary |
| 禁用背景 | `rgba(0,0,0,0.04)` | colorBgContainerDisabled |
| 勾选图标色 | `#FFF` | colorTextLightSolid |
### 15.23 Switch 开关
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 高度 | `22px` | — |
| 最小宽度 | `44px` | — |
| 手柄尺寸 | `18px` | — |
| 开启背景 | 主色 | colorPrimary |
| 关闭背景 | `rgba(0,0,0,0.25)` | colorTextQuaternary |
| 禁用透明度 | `0.65` | opacityLoading |
### 15.24 InputNumber 数字输入框
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 高度 | `32px` | controlHeight |
| 圆角 | `6px` | borderRadius |
| 步进按钮宽度 | `22px` | — |
| 步进按钮背景 | `transparent` | — |
| 步进按钮 hover 背景 | `rgba(0,0,0,0.04)` | colorFillTertiary |
| 其他 Token | 同 Input | — |
### 15.25 Cascader 级联选择
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 下拉面板宽度 | `每列 111px` | — |
| 选项内边距 | `5px 12px` | — |
| 选项 hover 背景 | `rgba(0,0,0,0.04)` | colorFillTertiary |
| 选项选中背景 | `#E6F4FF` | controlItemBgActive |
| 展开图标色 | `rgba(0,0,0,0.45)` | colorTextTertiary |
### 15.26 TreeSelect 树选择
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 节点高度 | `28px` | — |
| 节点内边距 | `4px 0` | — |
| 节点 hover 背景 | `rgba(0,0,0,0.04)` | colorFillTertiary |
| 节点选中背景 | `#E6F4FF` | controlItemBgActive |
| 缩进宽度 | `24px` | — |
### 15.27 Transfer 穿梭框
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 列表宽度 | `180px` | — |
| 列表高度 | `200px` | — |
| 头部背景 | `#FAFAFA` | — |
| 选项内边距 | `4px 12px` | — |
| 选项 hover 背景 | `rgba(0,0,0,0.04)` | colorFillTertiary |
### 15.28 Notification 通知提醒框
| Token | 默认值 | 说明 |
|---|---|---|
| width | `384` | 提醒框宽度 |
| zIndexPopup | `2050` | z-index |
| progressBg | `linear-gradient(90deg, #69b1ff, #1677ff)` | 进度条背景 |
### 15.29 Popconfirm 气泡确认框
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 最大宽度 | `none` | — |
| 内边距 | `12px 16px` | — |
| 圆角 | `8px` | borderRadiusLG |
| 阴影 | boxShadow | 一级阴影 |
| 图标色（warning） | `#FAAD14` | colorWarning |
| z-index | `1030` | — |
### 15.30 Progress 进度条
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 线条高度 | `8px` | — |
| 小线条高度 | `6px` | — |
| 圆角 | `100px` | 全圆角 |
| 默认色 | 主色 | colorPrimary |
| 成功色 | `#52C41A` | colorSuccess |
| 异常色 | `#FF4D4F` | colorError |
| 剩余色 | `rgba(0,0,0,0.04)` | colorFillTertiary |
| 文字字号 | `14px` | fontSize |
### 15.31 Result 结果
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 图标尺寸 | `72px` | — |
| 标题字号 | `24px` | fontSizeHeading3 |
| 副标题字号 | `14px` | fontSize |
| 标题字色 | `rgba(0,0,0,0.88)` | colorTextHeading |
| 副标题字色 | `rgba(0,0,0,0.45)` | colorTextTertiary |
| 内边距 | `48px 32px` | — |
### 15.32 Skeleton 骨架屏
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 背景色 | `rgba(0,0,0,0.06)` | colorFillSecondary |
| 动画渐变色 | `rgba(0,0,0,0.15)` | — |
| 头像尺寸 | `32px` | controlHeight |
| 标题高度 | `16px` | — |
| 段落行高度 | `16px` | — |
| 圆角 | `4px` | borderRadiusSM |
### 15.33 Spin 加载中
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 默认尺寸 | `20px` | — |
| 小尺寸 | `14px` | — |
| 大尺寸 | `48px` | — |
| 颜色 | 主色 | colorPrimary |
| 遮罩背景 | `rgba(255,255,255,0.65)` | — |
### 15.34 Avatar 头像
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 默认尺寸 | `32px` | controlHeight |
| 小尺寸 | `24px` | controlHeightSM |
| 大尺寸 | `40px` | controlHeightLG |
| 圆角（方形） | `6px` | borderRadius |
| 背景色 | `rgba(0,0,0,0.25)` | colorTextQuaternary |
| 文字色 | `#FFF` | colorTextLightSolid |
| 字号 | `14px` | fontSize |
| 组间距 | `-8px` | — |
### 15.35 Badge 徽标数
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 高度 | `20px` | — |
| 最小宽度 | `20px` | — |
| 字号 | `12px` | fontSizeSM |
| 背景色 | `#FF4D4F` | colorError |
| 文字色 | `#FFF` | colorTextLightSolid |
| 圆角 | `10px` | 全圆角 |
| 小圆点尺寸 | `6px` | — |
| 状态点尺寸 | `6px` | — |
### 15.36 Tooltip 文字提示
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 背景色 | `rgba(0,0,0,0.85)` | colorBgSpotlight |
| 文字色 | `#FFF` | colorTextLightSolid |
| 字号 | `14px` | fontSize |
| 圆角 | `6px` | borderRadius |
| 内边距 | `6px 8px` | — |
| 箭头尺寸 | `16px` | sizePopupArrow |
| z-index | `1070` | — |
### 15.37 Popover 气泡卡片
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 背景色 | `#FFFFFF` | colorBgElevated |
| 圆角 | `8px` | borderRadiusLG |
| 内边距 | `12px 16px` | — |
| 标题字号 | `14px` | fontSize |
| 标题字重 | `600` | fontWeightStrong |
| 阴影 | boxShadow | 一级阴影 |
| z-index | `1030` | — |
### 15.38 Dropdown 下拉菜单
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 背景色 | `#FFFFFF` | colorBgElevated |
| 圆角 | `8px` | borderRadiusLG |
| 内边距 | `4px` | paddingXXS |
| 选项内边距 | `5px 12px` | — |
| 选项 hover 背景 | `rgba(0,0,0,0.04)` | colorFillTertiary |
| 阴影 | boxShadow | 一级阴影 |
| z-index | `1050` | — |
### 15.39 Divider 分割线
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 颜色 | `rgba(5,5,5,0.06)` | colorSplit |
| 线宽 | `1px` | lineWidth |
| 文字字号 | `14px` | fontSize |
| 文字字色 | `rgba(0,0,0,0.88)` | colorTextHeading |
| 上下间距 | `24px` | marginLG |
### 15.40 Space 间距
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 小间距 | `8px` | sizeXS |
| 中间距 | `8px` | sizeXS（默认） |
| 大间距 | `16px` | size |
### 15.41 Grid 栅格
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 列数 | `24` | — |
| 间距 | `0` | 默认无间距 |
| 响应式断点 | xs:480 sm:576 md:768 lg:992 xl:1200 xxl:1600 | — |
### 15.42 Layout 布局
| 属性 | 推荐值 | 说明 |
|---|---|---|
| Header 高度 | `48px` | — |
| Header 背景 | `#FFFFFF` | 亮色主题 |
| Header 内边距 | `0 24px` | — |
| Sider 宽度 | `208px` | — |
| Sider 收起宽度 | `48px` | — |
| Sider 背景 | `#FFFFFF` | 亮色主题，右边框 `#F0F0F0` |
| Content 背景 | `transparent` | — |
| Footer 背景 | `transparent` | — |
| Footer 内边距 | `24px 50px` | — |
| 触发器高度 | `48px` | — |
| 触发器背景 | `#002140` | — |
> 注：本项目统一使用亮色主题。侧边栏白色背景 + 右边框分隔，顶栏白色背景 + 下边框分隔。
### 15.43 Anchor 锚点
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 链接字号 | `14px` | fontSize |
| 链接内边距 | `4px 0 4px 16px` | — |
| 选中字色 | 主色 | colorPrimary |
| 默认字色 | `rgba(0,0,0,0.88)` | colorText |
| 指示器色 | 主色 | colorPrimary |
| 指示器宽度 | `2px` | lineWidthBold |
### 15.44 Timeline 时间轴
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 圆点尺寸 | `10px` | — |
| 圆点边框宽度 | `2px` | lineWidthBold |
| 默认圆点色 | 主色 | colorPrimary |
| 连接线色 | `#F0F0F0` | colorBorderSecondary |
| 连接线宽度 | `2px` | lineWidthBold |
| 内容字号 | `14px` | fontSize |
| 标签字色 | `rgba(0,0,0,0.45)` | colorTextTertiary |
### 15.45 Tree 树形控件
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 节点高度 | `28px` | — |
| 节点内边距 | `4px 0` | — |
| 节点 hover 背景 | `rgba(0,0,0,0.04)` | colorFillTertiary |
| 节点选中背景 | `#E6F4FF` | controlItemBgActive |
| 缩进宽度 | `24px` | — |
| 连接线色 | `#D9D9D9` | colorBorder |
| 展开图标色 | `rgba(0,0,0,0.45)` | colorTextTertiary |
### 15.46 Image 图片
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 预览遮罩背景 | `rgba(0,0,0,0.45)` | colorBgMask |
| 预览操作栏背景 | `rgba(0,0,0,0.1)` | — |
| 预览操作栏圆角 | `100px` | — |
| 预览 z-index | `1080` | — |
### 15.47 Statistic 统计数值
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 标题字号 | `14px` | fontSize |
| 标题字色 | `rgba(0,0,0,0.45)` | colorTextTertiary |
| 内容字号 | `24px` | fontSizeHeading3 |
| 内容字色 | `rgba(0,0,0,0.88)` | colorTextHeading |
| 内容字重 | `600` | fontWeightStrong |
### 15.48 Segmented 分段控制器
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 高度 | `32px` | controlHeight |
| 圆角 | `6px` | borderRadius |
| 背景色 | `rgba(0,0,0,0.04)` | colorFillTertiary |
| 选中背景 | `#FFFFFF` | colorBgContainer |
| 选中阴影 | boxShadowTertiary | — |
| 选项内边距 | `4px 11px` | — |
| 字号 | `14px` | fontSize |
### 15.49 QRCode 二维码
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 默认尺寸 | `160px` | — |
| 内边距 | `12px` | paddingSM |
| 背景色 | `#FFFFFF` | colorBgContainer |
| 边框色 | `#F0F0F0` | colorBorderSecondary |
| 圆角 | `8px` | borderRadiusLG |
### 15.50 Watermark 水印
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 字号 | `16px` | fontSizeLG |
| 字色 | `rgba(0,0,0,0.15)` | — |
| z-index | `9` | — |
| 旋转角度 | `-22°` | — |
| 间距 | `[100, 100]` | — |
### 15.51 Calendar 日历
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 单元格尺寸 | `24px` | — |
| 选中背景 | 主色 | colorPrimary |
| 选中文字 | `#FFF` | colorTextLightSolid |
| 今天标记 | 主色边框 | colorPrimary |
| 头部字号 | `14px` | fontSize |
### 15.52 Carousel 走马灯
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 指示器宽度 | `16px` | — |
| 指示器高度 | `3px` | — |
| 指示器激活宽度 | `24px` | — |
| 指示器色 | `rgba(255,255,255,0.3)` | — |
| 指示器激活色 | `#FFFFFF` | — |
### 15.53 Empty 空状态
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 图片高度 | `100px` | — |
| 描述字号 | `14px` | fontSize |
| 描述字色 | `rgba(0,0,0,0.25)` | colorTextDisabled |
| 内边距 | `32px 0` | — |
### 15.54 Tour 漫游式引导
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 背景色 | `#FFFFFF` | colorBgElevated |
| 圆角 | `8px` | borderRadiusLG |
| 内边距 | `12px 16px` | — |
| 标题字号 | `16px` | fontSizeLG |
| 遮罩色 | `rgba(0,0,0,0.45)` | colorBgMask |
| z-index | `1070` | — |
### 15.55 Slider 滑动输入条
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 轨道高度 | `4px` | — |
| 轨道背景 | `rgba(0,0,0,0.04)` | colorFillTertiary |
| 轨道填充色 | 主色浅色 | colorPrimaryBorder |
| 手柄尺寸 | `10px` | — |
| 手柄边框宽度 | `2px` | lineWidthBold |
| 手柄色 | 主色 | colorPrimary |
| 手柄 hover 色 | 主色 hover | colorPrimaryHover |
### 15.56 Rate 评分
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 星星尺寸 | `20px` | — |
| 选中色 | `#FADB14` | yellow |
| 未选中色 | `rgba(0,0,0,0.06)` | colorFillSecondary |
| 间距 | `8px` | marginXS |
### 15.57 ColorPicker 颜色选择器
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 触发器高度 | `32px` | controlHeight |
| 触发器圆角 | `6px` | borderRadius |
| 面板宽度 | `234px` | — |
| 面板圆角 | `8px` | borderRadiusLG |
### 15.58 Mentions 提及
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 高度 | `32px` | controlHeight |
| 下拉面板圆角 | `8px` | borderRadiusLG |
| 选项内边距 | `5px 12px` | — |
| 选项 hover 背景 | `rgba(0,0,0,0.04)` | colorFillTertiary |
| 其他 Token | 同 Input | — |
### 15.59 AutoComplete 自动完成
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 下拉面板圆角 | `8px` | borderRadiusLG |
| 选项内边距 | `5px 12px` | — |
| 选项 hover 背景 | `rgba(0,0,0,0.04)` | colorFillTertiary |
| 其他 Token | 同 Input + Select | — |
### 15.60 Affix 固钉
| 属性 | 推荐值 | 说明 |
|---|---|---|
| z-index | `10` | 略高于普通内容 |
| 无独立 Component Token | — | 使用全局 Token |
### 15.61 Splitter 分隔面板
| 属性 | 推荐值 | 说明 |
|---|---|---|
| 分隔条宽度 | `1px` | lineWidth |
| 分隔条色 | `#F0F0F0` | colorBorderSecondary |
| 拖拽手柄色 | `rgba(0,0,0,0.25)` | colorTextQuaternary |
| 拖拽手柄 hover 色 | 主色 | colorPrimary |
---
