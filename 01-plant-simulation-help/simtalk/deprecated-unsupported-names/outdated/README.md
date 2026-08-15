# Outdated（过时的 SimTalk 名称）目录说明

本目录收录 Plant Simulation 帮助文档中 **「Outdated SimTalk Names」**（过时的 SimTalk 名称）一节的内容，用于说明旧版本 Plant Simulation 提供的、但当前版本已不再支持的 SimTalk 属性、只读属性和方法，以及它们对应的替代名称。

## 目录内容

| 文件 | 说明 |
|---|---|
| `outdated.md` | 经过格式化整理的 Markdown 版本（正文，推荐阅读） |
| `outdated.txtx` | 从帮助文档直接导出的纯文本版本（与 `outdated.md` 内容一致，含分页信息） |

> 本目录没有子文件夹，因此不存在子目录中的 `README.md`。

## 内容概要

### 1. 文档定位

旧版 Plant Simulation 提供了一批 SimTalk 属性、只读属性和方法，这些名称在当前版本中已被替换或完全移除。文档以字母顺序（A–Z）列出这些过时名称（英文与德文），并给出对应的替代项。

### 2. 处理过时函数的方法

文档开头的 **「Working with outdated functions」** 一节说明了如何在建模环境中定位和处理过时函数：

- **Find Outdated Functions（查找过时函数）**：位于 **Debugger（调试器）** 选项卡上，可查找模型中所有过时函数并显示在窗口中。
- **语法高亮**：Plant Simulation 会在源代码中以特定颜色显示过时函数（参见 *Colors for Syntax Highlighting*）。

### 3. 主参考表：过时名称 → 替代名称（A–Z）

文档主体是一张三列表格，列名为：

| 列 | 含义 |
|---|---|
| **Outdated English** | 过时的英文名称 |
| **Replaced by** | 替代名称（标注 `[SimTalk]` 表示对应的 SimTalk 名称，并注明适用范围/对象） |
| **Outdated German** | 过时的德文名称 |

该表包含约 **276** 个条目，涵盖属性、只读属性和方法的更名或移除。其中大量条目的替代列标注为 **"no longer supported"**（不再支持），表示该名称在当前版本中被彻底移除（部分条目注明相关的替代对象，如 EventController、Sorter、FlowControl、MUs、Exporter、Worker 等）。

常见替代模式包括：

- 更名类：如 `AnimIcon` → `animation`、`getFileName` → `FileName`、`getColor` 系列 → `getColor` 等。
- 统计属性规范化：如 `numIn` → `StatNumIn`、`numOut` → `StatNumOut`、`workingPercentage` → `StatWorkingPortion` 等。
- 明确移除类（`no longer supported`）：如 `closeFile`、`externCall`、`loadExternal`、`copyToClipboard` 等。
- 特殊语法替代：如 `increment` → SimTalk 的 `+=` 运算符、`read` → `[row]`。

### 4. 附加参考表：`_3D.*` 过时名称

文档末尾另有一张针对三维可视化（`_3D.*`）命名空间的过时名称表，列结构与主表相同，包含约 **114** 个条目，主要涉及：

- 三维图形的创建、删除、分组与变换（如 `_3D.createBox`、`_3D.setGraphicPosition`）。
- 三维材质与颜色（如 `_3D.AutoGraphicsDiffuseColor` → `_3D.MaterialDiffuseColor`）。
- 三维动画控制（如 `_3D.playAnimation` → `_3D.SelfAnimations.play` / `_3D.CameraAnimations.play`）。
- 大量已移除的 `_3D.*` 方法（标注为 `no longer supported`）。

### 5. 参见（See also）

文档末尾的「See also」指向两个相关主题：

- **Colors for Syntax Highlighting**（语法高亮的颜色设置）
- **No Longer Supported SimTalk Names of the 2D Visualization**（2D 可视化中不再支持的 SimTalk 名称）

---

## 源信息

- 来源：*Outdated SimTalk Names*，Plant Simulation Help 页码 12-1290 – 12-1308
- 版权：Unpublished work. © 2026 Siemens
