# Importing and Exporting Data in Text Format（以文本格式导入与导出数据）

本目录收录了 Plant Simulation 中 **List 与 Table** 对象用于**文本格式**（而非 `.pslist` 表格格式）读写数据的方法说明。

## 适用范围

本目录下的所有方法均适用于以下对象：

- **DataStack**
- **DataQueue**
- **DataList**
- **DataTable**
- **TimeSequence**

## 方法总览

共 9 个方法，分为「导入（Import）」与「导出（Export）」两类。所有方法均返回 `boolean`（成功返回 `true`），且写入类方法都会**覆盖目标文件中的已有数据**。

| 方法 | 方向 | 数据格式 | 说明 |
| --- | --- | --- | --- |
| `readExcelFile` | 导入 | Excel（`*.xls`） | 从 Excel 文件读取数据；需安装 MS Excel（COM 服务器） |
| `readFile` | 导入 | 文本（`*.txt`） | 读取文本文件，也可读取 `writeObjectFile` 导出的对象文件 |
| `readXMLFile` | 导入 | XML（`*.xml`） | 从 XML 文件读取数据；复杂 XML 建议改用 `XMLInterface` |
| `readXMLString` | 导入 | XML 字符串 | 从含合法 XML 语法的字符串读取数据 |
| `writeExcelFile` | 导出 | Excel（`.xls/.xlsx/.xlsm/.xlsb`） | 导出为 Excel 文件；需安装 MS Excel（COM 服务器） |
| `writeExcelXMLFile` | 导出 | Excel 2003 电子表格（`*.xml`） | 导出为 Excel 2003 格式；**无需**安装 Excel，速度更快 |
| `writeFile` | 导出 | 文本（`*.txt`） | 导出为文本文件 |
| `writeObjectFile` | 导出 | 对象文件（`*.pslist`） | 导出为 `.pslist` 对象文件 |
| `writeXMLFile` | 导出 | XML（`*.xml`） | 导出为 XML 文件（始终使用 Plant Simulation 专有格式） |

## 通用参数

大多数方法共享以下可选参数：

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| `FileName` | `string` | 文件路径与名称（必填） |
| `NoDebugger` | `boolean` | 访问失败时是否**不**打开 Method Debugger。默认 `false`（即默认会打开调试器）；设为 `true` 时出错直接返回 `false` |
| `Sheet` | `string` | Excel 方法专用，指定工作表名称 |
| `CodePage` | `string` | 文本方法（`readFile`/`writeFile`）专用，编码：`"ANSI"`/`"System"`、`"UTF-8"`、`"Unicode"`，默认 `"ANSI"` |
| `Password` | `string` | 仅 `readExcelFile` 使用，指定密码 |

## 重要注意事项（Remarks）

1. **覆盖行为**：所有导入/导出方法都会**覆盖**已有数据（`writeExcelFile` 还会覆盖 Excel 文件的格式）。
2. **Excel COM 服务器**：`readExcelFile` 与 `writeExcelFile` 通过 COM 服务器读写 Excel，**必须安装 MS Excel**。如需使用旧版接口，可用启动选项 `-NativeExcel`。
3. **`writeExcelXMLFile` 的优势**：不需要安装 Excel，且速度显著快于 `writeExcelFile`。
4. **DataTable 列/行索引**：`readExcelFile` 在对应 Excel 单元格为空时**不会**覆盖 DataTable 的列索引/行索引；如需覆盖请先删除原有内容。
5. **XML 专有格式**：`writeXMLFile` 始终使用 Plant Simulation 专有格式；`readXMLFile` 读取非专有格式时会尽力从任意 XML 数据构建列表/表格，复杂 XML 可能无法完整导入，应改用 `XMLInterface`。
6. **背景色**：若 DataTable 中定义了背景色，`writeExcelFile`/`writeExcelXMLFile` 会写入 Excel；否则不改变已有 Excel 文件的背景色。
7. **对象文件**：`readFile` 可同时导入文本文件（`writeFile` 导出）与对象文件（`writeObjectFile` 导出）。

## 关联方法（间接访问）

本目录末尾还提及 **Methods for Indirectly Accessing Lists and Tables**（间接访问 List 与 Table 的方法）。这些方法仅适用于数据类型为 `object` 的单元格范围——单元格内容为对象引用，需处理其属性。
