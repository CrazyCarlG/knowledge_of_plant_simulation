# CostAnalyzer Methods

本目录包含 CostAnalyzer 对象（用户界面对象）的方法文档。

## 目录内容

| 文件 | 说明 |
|------|------|
| `methods.md` | CostAnalyzer 方法的 Markdown 文档（主要内容） |
| `methods.txtx` | 相同内容的原始文本导出（Plant Simulation Help 导出） |

> 注：当前目录下没有子文件夹，因此没有子文件夹的 README.md 需要汇总。

## 内容概述

CostAnalyzer 提供：

- 左侧目录中列出的方法（即本目录中记录的 4 个方法）。
- 所有对象的通用方法（Methods of All Objects）。

要查看对象的全部方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的右键菜单选择 **Show Attributes and Methods**，查看所选**类（Class）** 的方法与属性。
- 在 Frame 的 Home 功能区选项卡中按 **F8** 键或点击 **Show Attributes and Methods**，查看所选**实例（Instance）** 的方法与属性。

## 语法行（Syntax Line）说明

方法语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示方法所应用对象的路径。
- 括号内为方法签名，由参数标识符和数据类型组成。例如 `(Parameter:string)` 表示一个 `string` 类型的参数。除常量值外，也可使用所需类型的变量或返回所需类型的方法。
- **注意**：嵌套括号 `(…)` 内的表达式必须输入括号，否则可能产生意外结果并打开调试器（Debugger）。
- 可选参数列在方括号 `[…]` 内。例如 `[,Parameter:boolean]` 表示可以（但不是必须）输入该布尔参数。
- 若参数有默认值，签名会在参数后显示 `:=` 默认值（如上例中的 `:= false`）。
- 若方法有返回值，签名会在箭头 `->` / `→` 后显示返回类型（如上例中的 `→ boolean`）。

## 方法列表

CostAnalyzer 提供以下 4 个方法：

| 方法 | 说明 | 语法 | 返回/参数 |
|------|------|------|-----------|
| `getInvestmentCostsTable` | 返回 CostAnalyzer 计算出的 **Investment costs（投资成本）** 表 | `<Path>.getInvestmentCostsTable → table` | 返回值类型 `table` |
| `getPieceCostsTable` | 返回 CostAnalyzer 计算出的 **Piece costs（单件成本）** 表 | `<Path>.getPieceCostsTable → table` | 返回值类型 `table` |
| `putInvestmentCostsIntoTable` | 将计算出的 **Investment costs（投资成本）**、**Depreciation period（折旧期）** 和 **Operating costs（运营成本）** 写入指定的 DataTable | `<Path>.putInvestmentCostsIntoTable(DataTable:table)` | 参数 `DataTable`（类型 `table`） |
| `putPieceCostsIntoTable` | 将计算出的 **Piece costs（单件成本）** 写入指定的 DataTable | `<Path>.putPieceCostsIntoTable(DataTable:table)` | 参数 `DataTable`（类型 `table`） |

### 方法详解

#### getInvestmentCostsTable

返回由 `<Path>` 指定的 CostAnalyzer 所计算的 **Investment costs** 表。

- **类型**：Method
- **语法**：`<Path>.getInvestmentCostsTable → table`
- **返回值**：数据类型 `table`

**示例**：

```
CostAnalyzer.getInvestmentCostsTable.openDialog
// open the table as a dialog
```

**参见**：Investment Costs、putInvestmentCostsIntoTable、Costs Shown in the Costs Report

---

#### getPieceCostsTable

返回由 `<Path>` 指定的 CostAnalyzer 所计算的 **Piece costs** 表。

- **类型**：Method
- **语法**：`<Path>.getPieceCostsTable → table`
- **返回值**：数据类型 `table`

**示例**：

```
CostAnalyzer.getPieceCostsTable.openDialog
// open the table as a dialog
```

**参见**：Costs Shown in the Costs Report、Piece Costs、putPieceCostsIntoTable

---

#### putInvestmentCostsIntoTable

将由 `<Path>` 指定的 CostAnalyzer 所计算的 **Investment costs**、**Depreciation period** 和 **Operating costs** 写入指定的 DataTable。

- **类型**：Method
- **语法**：`<Path>.putInvestmentCostsIntoTable(DataTable:table)`
- **参数**：`DataTable`（数据类型 `table`）—— 指定 Plant Simulation 写入投资成本的 DataTable。

**示例**：

```
CostAnalyzer.putInvestmentCostsIntoTable(MyInvestmentCosts)
```

**参见**：Costs Shown in the Costs Report、getInvestmentCostsTable

---

#### putPieceCostsIntoTable

将由 `<Path>` 指定的 CostAnalyzer 所计算的 **Piece costs** 写入指定的 DataTable。

- **类型**：Method
- **语法**：`<Path>.putPieceCostsIntoTable(DataTable:table)`
- **参数**：`DataTable`（数据类型 `table`）—— 指定 Plant Simulation 写入单件成本的 DataTable。

**示例**：

```
CostAnalyzer.putPieceCostsIntoTable(MyPieceCosts)
```

**参见**：Costs Shown in the Costs Report、getPieceCostsTable

## 只读属性（Read-Only Attributes）

CostAnalyzer 提供所有对象的通用只读属性（**Read-Only Attributes of All Objects**）。
