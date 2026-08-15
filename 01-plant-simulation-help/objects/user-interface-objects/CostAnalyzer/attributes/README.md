# CostAnalyzer 对象 — Attributes（属性）

> 本目录 `attributes/` 下只有一个 Markdown 文件 `attributes.md`（以及同名源文本 `attributes.txtx`），没有子文件夹，也没有子文件夹的 README.md。本文件是对 `attributes.md` 内容的总结。

## 目录内容

| 文件 | 说明 |
|------|------|
| `attributes.md` | CostAnalyzer 属性（Attributes）的 Markdown 文档（主要内容） |
| `attributes.txtx` | 相同内容的原始文本导出（Plant Simulation Help 导出） |

> 注：当前目录下没有子文件夹，因此没有子文件夹的 README.md 需要汇总。

## 概述（Overview）

CostAnalyzer 的**只读属性（read-only attributes）**可以查询其值，但**无法设置**——Plant Simulation 会在你查询的那个时间点即时计算其值。大多数情况下，只读属性对应对象某个选项卡（例如 **Statistics** 选项卡）上不可用的对话框项。

要查看对象的所有方法、只读属性和属性，打开 **Show Attributes and Methods** 窗口：

- 在 **Class Library** 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选**类（Class）**的方法、只读属性和属性。
- 按 **F8** 键，或点击插入实例的 Frame 的 **Home** 功能区选项卡中的 **Show Attributes and Methods**，可显示所选**实例（Instance）**的方法、只读属性和属性。

查询只读属性值的示例：

```simtalk
print MyCostAnalyzer.UUID
```

## 提供的属性（Provided Attributes）

CostAnalyzer 提供：

- 属性 `CollectData`。
- **所有对象的通用属性（Attributes of All Objects）**。

属性值既可以设置，也可以获取——通过对话框中的复选框、文本框和下拉列表，或通过给相应属性赋值来实现。

- **设置属性值**示例：

```simtalk
MyCostAnalyzer.CollectData := false
```

- **获取属性值**示例：

```simtalk
MyCostAnalyzer.CollectData
posit := Station.Cont.XPos
```

## CollectData [SimTalk] — CostAnalyzer

设置由 `<Path>` 指定的 CostAnalyzer 是否收集数据：`true` 表示收集数据，`false` 表示不收集数据。

- **类型（Type）：** 属性（Attribute）
- **语法（Syntax）：** `<Path>.CollectData:boolean`
- **赋值（Assignment Value）：** 可赋一个 `boolean` 类型的数据值。

**示例：**

```simtalk
MyCostAnalyzer.CollectData := true
```

**另请参阅（See also）：** Collect Data [复选框] — CostAnalyzer

## HtmlReport [对象]

对象 **HtmlReport** 用于将仿真运行的当前数据和结果以报告形式呈现，便于与同事和客户共享。

- 可将 HtmlReport 保存为 `.htm` 文件，并在 HTML 浏览器（如 Microsoft Edge、Firefox、Google Chrome 等）中打开。
- 在外部浏览器中打开 HtmlReport **无需安装 Plant Simulation**，因此 HtmlReport 可在任何安装了 HTML 浏览器的计算机上显示。

## 与同级目录的关系

本目录（`attributes/`）是 CostAnalyzer 对象文档的一部分。CostAnalyzer 的其他文档分布在以下同级子目录中（各自都有独立的 README.md）：

- `general/` —— CostAnalyzer 总览，涵盖成本分配方式、成本报告、对话框等内容。
- `methods/` —— CostAnalyzer 的 4 个方法：`getInvestmentCostsTable`、`getPieceCostsTable`、`putInvestmentCostsIntoTable`、`putPieceCostsIntoTable`。
- `read-only-attributes/` —— CostAnalyzer 的只读属性（提供所有对象的通用只读属性）。

---

*来源：Plant Simulation Help 11-4909–11-4911。未发表作品。© 2026 Siemens。*
