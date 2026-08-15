# HtmlReport — 方法

本目录包含 `methods.md`，记录了 Plant Simulation 用户界面对象 **HtmlReport** 提供的方法（Methods）。

> 本 README 为 `methods.md` 的内容总结，详细语法与示例请参阅 `methods.md`。

---

## 1. 概述

`HtmlReport` 提供：

- 本目录 `methods.md` 中列出的方法（见下方「方法一览」）。
- 所有对象的通用方法（Methods of All Objects）。

要查看对象的全部方法、只读属性与属性，可打开 **Show Attributes and Methods** 窗口：

- 在类库（Class Library）右键菜单中选择 **Show Attributes and Methods**，显示所选**类**的方法、只读属性与属性。
- 在插入实例的 Frame 中按 `F8`，或点击 Home 功能区上的 **Show Attributes and Methods**，显示所选**实例**的方法、只读属性与属性。

---

## 2. 语法行（Syntax Line）阅读说明

单个方法的语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示方法所作用对象的路径。
- 括号内为方法签名，由参数标识符与数据类型组成。例如 `(Parameter:string)` 表示一个 `string` 类型参数；除常量外，也可使用所需类型的变量或返回该类型的方法。
- 方括号 `[...]` 内为可选参数，例如 `[,Parameter:boolean]` 表示可以省略该布尔参数。
- 若参数有默认值，签名会在参数后显示默认值，如上例中的 `:= false`。
- 若方法有返回值，签名会在箭头 `→` 后显示返回值数据类型，如上例中的 `→ boolean`。

> **注意**：嵌套在括号内的表达式务必书写括号 `(…)`，否则可能导致意外结果并打开调试器（Debugger）。

---

## 3. 方法一览

| 方法 | 语法 | 说明 |
|---|---|---|
| `append` | `<Path>.append(Text:string)` | 向 Content 追加文本 |
| `appendLine` | `<Path>.appendLine(Text:string)` | 向 Content 追加一行文本 |
| `appendPlainText` | `<Path>.appendPlainText(PlainText:string)` | 将特殊字符按纯文本追加到 Content |
| `close` | `<Path>.close → boolean` | 关闭由 Show Report 打开的窗口 |
| `getHTMLCode` | `<Path>.getHTMLCode([WithButtonsAndLinks:boolean:=false]) → string` | 返回 HtmlReport 的 HTML 代码 |
| `refresh` | `<Path>.update → boolean` | 用当前值强制刷新显示的 HtmlReport |
| `save` | `<Path>.save(FileName:string)` | 将 HtmlReport 保存为 HTML 文件 |
| `show` | `<Path>.show([Anchor:string])` | 将 HtmlReport 显示为 HTML 页面 |

---

## 4. 方法详解

### 4.1 append [SimTalk]

向 `<Path>` 指定的 `HtmlReport` 的 Content 追加文本。

- **语法**：`<Path>.append(Text:string)`
- **参数**：`Text`（`string`）—— 要追加的文本。

**示例**

```simtalk
MyReport.Content := "#Heading"
   for var i := 1 to numNodes 
   MyReport.append(strChr(10))
   MyReport.append("Name: ")
   MyReport.append(object(i).name)
next
```

**参见**：Tab Content [HtmlReport]

---

### 4.2 appendLine [SimTalk]

向 `<Path>` 指定的 `HtmlReport` 的 Content 追加一行文本。

- **语法**：`<Path>.appendLine(Text:string)`
- **参数**：`Text`（`string`）—— 要追加的行的文本。

**示例**

```simtalk
MyReport.Content := "#Heading" + strChr(10)
for var i := 1 to numNodes 
   MyReport.appendLine(object(i).name)
next
```

**参见**：Tab Content [HtmlReport]

---

### 4.3 appendPlainText [SimTalk]

将特殊字符按纯文本追加到 `<Path>` 指定的 `HtmlReport` 的 Content。

- **语法**：`<Path>.appendPlainText(PlainText:string)`
- **参数**：`PlainText`（`string`）—— 要以纯文本追加的特殊字符。

**示例**

```simtalk
MyReport.Content := "#Heading" + strChr(10)
MyReport.appendPlainText("##**")
```

**参见**：Tab Content [HtmlReport]

---

### 4.4 close [SimTalk]

关闭通过点击 **Show Report** 打开的 `<Path>` 指定的 `HtmlReport` 窗口。

- **语法**：`<Path>.close → boolean`
- **返回值**：`boolean`。

**示例**

```simtalk
MyReport.close
```

**参见**：show [SimTalk]

---

### 4.5 getHTMLCode [SimTalk]

返回 `<Path>` 指定的 `HtmlReport` 的 HTML 代码。

- **语法**：`<Path>.getHTMLCode([WithButtonsAndLinks:boolean:=false]) → string`
- **参数**：`WithButtonsAndLinks`（`boolean`，可选）—— 设置返回的字符串是否包含显示窗口左上角按钮的 HTML 代码，以及对象链接（例如物流对象统计表中的链接）。
- **参数默认值**：`false`。
- **返回值**：`string`。

**示例**

```simtalk
print MyHtmlReport.getHTMLCode
```

**参见**：Display a HtmlReport

---

### 4.6 refresh [SimTalk]

用当前值强制刷新 `<Path>` 指定的已显示的 `HtmlReport`。

- **语法**：`<Path>.update → boolean`
- **返回值**：`boolean`：
  - `true` —— HtmlReport 已成功更新。
  - `false` —— 未更新。

> **说明**：`methods.md` 中该小节标题为 `refresh`，但语法与示例使用 `update`。

**示例**

```simtalk
MyHtmlReport.update
```

**参见**：Structure Pane of the Display Window > Refresh the report

---

### 4.7 save [SimTalk]

将 `<Path>` 指定的 `HtmlReport` 保存为 HTML 文件。

- **备注**：也可以指定文件在硬盘上的位置。
- **语法**：`<Path>.save(FileName:string)`
- **参数**：`FileName`（`string`）—— 要保存的 HTML 文件的路径与文件名。

**示例**

```simtalk
MyReport.save("C:\temp\MyReport.html")
```

---

### 4.8 show [SimTalk]

将 `<Path>` 指定的 `HtmlReport` 显示为 HTML 页面。

- **语法**：`<Path>.show([Anchor:string])`
- **参数**：`Anchor`（`string`，可选）—— 打开 HTML 页面时 Plant Simulation 要跳转到的锚点。

**示例**

```simtalk
MyHtmlReport.show("DrainStat")
// 跳转到 Content 选项卡上由以下代码定义的锚点：
// << <a id="DrainStat"> </a> >>
```

**参见**：Show Report

---

## 5. 只读属性（Read-Only Attributes）

`HtmlReport` 提供所有对象的通用只读属性（Read-Only Attributes of All Objects）。

只读属性的值可以查询，但不能设置——Plant Simulation 会在查询时计算该时刻的值。多数情况下，只读属性对应对象某选项卡上不可用的对话框项，例如 Statistics 选项卡。
