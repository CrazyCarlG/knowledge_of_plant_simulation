# HtmlReport — 概览

本目录包含 `general.md`，记录了 Plant Simulation 用户界面对象 **HtmlReport** 的完整用法。HtmlReport 用于以报告形式呈现仿真运行的当前数据与结果，可导出为 `.htm` 文件，在任意 HTML 浏览器中查看，无需安装 Plant Simulation。

> 本 README 为 `general.md` 的内容总结，详细语法与示例请参阅 `general.md`。

---

## 1. 对象简介

- **用途**：将仿真运行的数据和结果整理成可分享给同事与客户的报告。
- **导出**：可保存为 `.htm`，用 Microsoft Edge / Firefox / Google Chrome 等浏览器打开。
- **添加方式**：`Home` 功能区 → `Manage Class Library > Basic Objects > UserInterface > HtmlReport`。
- **配置提示**：最简便的配置方式是把对象从 Frame 拖到 **Content** 选项卡；也可使用内置标记语言编写内容，或在 HtmlReport 中嵌套另一个 HtmlReport。

---

## 2. 对话框与显示窗口

- **编辑仿真属性**：双击图标打开对话框，可编辑仿真属性与动画属性（`Edit 3D Properties` 或按空格键）。
- **显示报告**：点击 `Show Report`（或右键对象选择 `Show`）打开显示窗口：
  - **Display Pane（右）**：显示 Content 选项卡定义的报告内容。
  - **Structure Pane（左）**：显示前两级标题，点击可跳转。
  - 支持打印、保存为网页、刷新、滚动（鼠标滚轮）与缩放（`Ctrl` + 滚轮）。

---

## 3. Content 选项卡

- 定义 HtmlReport 显示的内容；内置报告提供了常用条目示例。
- 右侧复选框控制 **继承（inheritance）**：
  - 绿色 = 继承开启，使用父对象的值。
  - 橙色带减号 = 继承关闭，值仅作用于当前对象。
- 内容可用文本输入，或用 **Object Parameters** 对话框；标记语言是 HTML 的超集。
- 可把对象从 Frame 拖到 Content 选项卡或 HtmlReport 图标上：
  - 继承时：对象数据**替换**预定义内容。
  - 不继承时：Plant Simulation **追加**数据。

---

## 4. 工具栏快捷键

| 操作 | 快捷键 |
|---|---|
| 撤销 | `Ctrl+Z` |
| 加粗 | `Ctrl+B` |
| 斜体 | `Ctrl+I` |
| 增加缩进 | `Ctrl+M` |
| 减少缩进 | `Ctrl+Shift+M` |
| 不换行空格 | `Ctrl+Shift+-` |
| 分页符（仅打印） | `Ctrl+Shift+Enter` |
| 添加对象引用 | `Ctrl+K` |
| 拼写检查 | `Ctrl+S` |
| 标题级别 1–6 | `Ctrl+1` … `Ctrl+6` |
| 清除标题标记 | `Ctrl+0` |
| 居中 | `Ctrl+E` |
| 软连字符 | `Ctrl+-` |

---

## 5. 默认设置

`## Drain Statistics` 默认展示各 Drain 的统计值（列：英文 / 德文 / 只读属性）：

- **Object** — 所有移除了零件的 Drain 名称
- **Name** — Drain 移除的零件类型名称
- **Mean Life Time** — `StatAvgLifeSpan`（mittlere Durchlaufzeit）
- **Total Throughput** — `StatDeleted`（Durchsatz）
- **Throughput per Hour** — `StatThroughputPerHour`（Durchsatz pro Stunde）
- **Production / Transport / Storage** — 生产 / 运输 / 仓储资源上的时间占比
- **Value Added** — `StatProdWorkingPortion`（Wertschöpfung）
- **Portion** — 以彩色条段展示累计值：Production（绿）、Transport（橙）、Storage（红）

---

## 6. 格式化语法

- **标题**：`#` 到 `####`（最多四级），一级、二级标题会出现在结构窗格中。
- **项目符号列表**：`* ` 开头，空行结束；用制表符或 4 个空格缩进子列表。
- **编号列表**：`1. ` 开头，任何数字都会从 1 开始编号；支持嵌套及项目符号子列表。
- **加粗 / 斜体**：`*text*` 斜体、`**text**` 加粗、`***text***` 加粗斜体（空格 + 星号不会误判为斜体）。
- **缩进**：行首 `>` 缩进段落，多个 `>>` 缩进更深。
- **居中**：行首 `><` 使文本居中。

---

## 7. 对象引用与特殊显示

- **基本引用**：`[ObjectName]`；相对路径从包含 HtmlReport 的 Frame 解析；`self` 指 HtmlReport 自身。
- **参数形式**：位置参数（逗号分隔）与命名参数（空格分隔）等价。
- **小数位数**：追加数字（如 `, 2`）四舍五入，加前导 `0`（如 `, 02`）强制补零。
- **显示所有实例**：路径后加 `*`（如 `[.UserInterface.HtmlReport*]`）。

可显示的对象类型包括（详见 `general.md`）：

Attribute / AttributeExplorer / Broker / Chart / Checkbox / Comment / DataTable / DataList / Display / Drain / DropdownList / FileLink / Frame / GanttChart / HtmlReport / 对象图标（`[!...]`）/ Method / PythonModule / SankeyDiagram / 统计值表格 / SQLite 表格 / Variable / 3D 场景图片（`[Object._3D]`）等。

---

## 8. 统计值表格

语法：`[对象路径, 标题, 统计表类型]`。

统计表类型使用英文/德文代码，如：

- `%ResStates` / `%Stati` — 状态占比
- `%DrainCumulated` / `%SenkeKumuliert` — Drain 累计统计
- `%Energy` / `%Energie` — 总能耗 / 能源状态
- `%Exporter` / `%Exporter` — 导出器容量与状态
- `%Broker` / `%Broker` — Broker 统计

不同对象有各自默认的统计类型（如 Part → `%MUTimePortions`，Drain → `%DrainCumulated` 等），完整对照表见 `general.md`。

---

## 9. 公式与其它功能

- **计算公式**：`[=` 与 `]` 之间写公式，可指定小数位。
- **显示对象本身**：`[>path]` 显示对象内容而非路径。
- **对象图片**：`[!MyObject]`，可指定图标名或编号及尺寸。
- **位图文件**：`[!self, "SiemensLogo", "标题"]` 从位图创建图标。
- **收集并显示实例**：路径后加 `*`，标题可含公式（用 `@` 引用匿名实例）。
- **注释**：`--` 起至行尾。
- **水平线**：三个及以上 `---` 且后无文本。
- **HTML 标签**：尖括号内直接写 HTML（`<` 后无空格，同一行内闭合 `>`）。
- **转义字符**：`\` 前缀让特殊字符按字面显示。
- **拼写检查**：`Ctrl+S`，使用 Windows 拼写检查器（不适用中文和日文）。
- **原样输出字符串**：用 `<<` 与 `>>` 包裹，避免被当作标记语言解析。

---

## 10. 其它选项卡、菜单与方法

- **Tab User-defined**：可定义自定义属性。
- **菜单**：Navigate / View / Tools（`Edit Controls`、`Edit Observers`）/ Help。
- **方法**：HtmlReport 提供帮助文档方法列表中的方法以及所有对象的通用方法；用 `F8`（或类库右键菜单）打开 **Show Attributes and Methods** 查看全部方法、只读属性与属性。
