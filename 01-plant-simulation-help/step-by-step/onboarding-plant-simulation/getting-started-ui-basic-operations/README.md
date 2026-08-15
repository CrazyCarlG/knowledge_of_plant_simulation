# Getting Started: UI & Basic Operations（用户界面与基本操作）

本目录汇总了 Plant Simulation 帮助文档中关于**用户界面（UI）与基本操作**的入门内容，帮助新用户快速上手。核心文档为 `getting-started-ui-basic-operations.md`。

---

## 内容概览

### 1. 认识 Plant Simulation（Getting to Know Plant Simulation）

可通过三种途径熟悉 Plant Simulation：

- **观看 YouTube 视频**：从 Start Page 进入，视频帮助快速了解常用建模任务；帮助主题通过时间码（如 `=18`）关联到对应视频。
- **查看示例模型（Sample Models）**：通过 Start Page 的 `Example Models > Small Examples` 打开，按 **Category / Topic / Sample Model** 选择，可 **Open Model** 打开或 **More Info** 查看说明，并支持 **Search** 按主题检索（搜索模型 ReadMe 中的描述）。
- **查阅 Step-by-Step 帮助**：通过 `File > Help > Contents` 或官网下载的 PDF 文档阅读，也可使用 Copilot 检索在线帮助。

### 2. 基础操作（Working with Plant Simulation, Basics）

涵盖以下主题：

- 使用窗口类型（Window Types）
- 选择 Plant Simulation 设置（Settings）
- 更改对象设置（Settings of the Objects）
- 在仿真模型中查找对象与文本（Find Objects and Text）

#### 2.1 窗口类型（Work with Window Types）

Plant Simulation 是**多文档界面（MDI）**应用，各窗口位于统一的父窗口内。窗口类型及特点：

| 窗口类型 | 边框颜色 | 特点 |
|---|---|---|
| 程序窗口 | 洋红色（magenta） | MDI 父窗口 |
| 停靠窗口（Class Library、Favorites、Toolbox、Console） | 红色 | 停靠在程序窗口边缘，始终位于前台，可 Auto Hide / Floating / Docking 切换 |
| 对象窗口（Frame、Method、Method Debugger、DataQueue、DataStack、DataList、DataTable、Icon Editor） | 蓝色 | 可最大化/最小化/排列，始终在后台打开 |
| 对话框（物料流、移动、流体、资源、信息流、用户界面对象） | 绿色 | 始终在最前，不能最小化/最大化，可拖出程序窗口 |

- **停靠窗口**：右键标题栏切换 **Floating / Docking**，或拖动标题栏到停靠箭头；按住 **Ctrl** 拖动可防止浮动窗口停靠；双击标题栏可在停靠/浮动间切换。
- **对象窗口**：可通过 `openDialogBox` 方法在前台打开数据类窗口，用 `closeAllWindows` 关闭所有对象窗口，并可添加到 **Favorites** 快速访问。
- **窗口切换（Window Navigator）**：按 **Ctrl+Tab** 打开预览，用左右方向键切换“停靠窗口/对象窗口”两列，Tab 或上下方向键在列内切换，松开 Ctrl 激活所选窗口。

#### 2.2 选择设置（Select Settings）

- **模型专属设置**：`File > Model Settings`（保存在模型文件中）。
- **新模型设置**：`File > Preferences`（General / 3D / Editor 为模型无关设置；Simulation / User Interface / Units 为新模型专属设置）。
- **通用选项**：设置新模型使用的**语言**、**日期/时间格式**（`yyyy/mm/dd`、`yyyy-mm-dd`、`dd.mm.yyyy`）及**保存时注释类型**（无注释 / 带注释 / 不保存历史）。
- **单位与时间显示**：`File > Model Settings > Units` 或 `File > Preferences > Units`。
  - 支持**夏令时（DST）**规则（欧盟与美国规则不同）。
  - **时间标尺（Time Scale）**：可输入 0 到 86400，仅改变显示方式（无模型打开时才能更改时间标尺本身）。
  - 时间语句为 `days:hours:minutes:seconds` 四段冒号分隔，内部以秒存储。

#### 2.3 更改对象设置（Change the Settings of the Objects）

四种修改对象属性值的方式：

1. **对象对话框**：文本框输入、下拉选择、勾选/取消复选框；What's This 帮助会显示对应 SimTalk 属性名。
2. **SimTalk 赋值**：如 `MyStation.ProcTime := 180`（或 `:= 3:00`）。对象名与属性名用 `.` 分隔，赋值运算符为 `:=`；同 Frame 内无需完整绝对路径。字符串赋值不区分大小写，查询时按句首大写显示。
3. **Show Attributes and Methods 窗口**：按 **F8** 打开，双击属性修改，双击布尔属性切换 `true/false`。
4. **AttributeExplorer**：集中管理多个对象的属性，可导出为制表符分隔文本并导入其他模型，也可用于查找对象/属性并对齐。

#### 2.4 查找对象与文本（Find Objects and Text）

通过 Frame 功能区的 **Find Object**（或 Class Library 右键）查找对象名称、条件、属性表达式、方法源码或表格表达式。支持 **Match Whole Word Only**、**Match Case**、**Regular Expression**（通配符：`.`、`^`、`$`、`\<`、`\>`、`*`、`+`、`[]`、`\|` 等）以及 **Include Subframes**（搜索嵌套 Frame）。

- **按名称查找**：输入关键字（如 `Station`）可匹配 `Station1`、`MyStation` 等；双击结果打开对话框。
- **按条件查找**：输入 SimTalk 表达式（如 `proctime = 100`）。
- **按属性查找**：输入属性中包含的文本/值。
- **按源码查找**：在 Method 源码中查找文本，可勾选 **Ignore Inherited Name or Text** 仅搜索原始源码；双击结果跳转匹配位置，还支持右键 **Replace With** 批量替换。

---

## 目录结构

- `getting-started-ui-basic-operations.md` — 主文档：UI 与基本操作的完整说明。
- `getting-started-ui-basic-operations.txtx` — 源文档（原始素材）。

---

*Source: Plant Simulation Help — Unpublished work. © 2026 Siemens*
