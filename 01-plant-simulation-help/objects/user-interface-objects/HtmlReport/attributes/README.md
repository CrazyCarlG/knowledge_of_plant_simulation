# HtmlReport — 属性

本目录包含 `attributes.md`，记录了 Plant Simulation 用户界面对象 **HtmlReport** 提供的属性（Attributes）。

> 本 README 为 `attributes.md` 的内容总结，详细语法与示例请参阅 `attributes.md`。

---

## 1. 概述

HtmlReport 提供：

- 本目录 `attributes.md` 中列出的属性（见下方「属性一览」）。
- 所有对象的通用属性（Attributes of All Objects）。

要查看对象的全部方法、只读属性与属性，可打开 **Show Attributes and Methods** 窗口：

- 在类库（Class Library）右键菜单中选择 **Show Attributes and Methods**，显示所选**类**的方法、只读属性与属性。
- 在插入实例的 Frame 中按 `F8`，或点击 Home 功能区上的 **Show Attributes and Methods**，显示所选**实例**的方法、只读属性与属性。

---

## 2. 读取与设置属性

属性的值既可以通过对话框中的复选框、文本框和下拉列表设置，也可以通过为相应属性赋值来设置与获取。

- 查询只读属性的示例：

```simtalk
print MyHtmlReport.UUID
```

- 设置属性的示例：

```simtalk
MyReport.TocLevels := 3
```

- 获取属性的示例：

```simtalk
print MyReport.TocLevel
```

---

## 3. 属性一览

| 属性 | 数据类型 | 语法 | 说明 |
|---|---|---|---|
| `Content` | string | `<Path>.Content:string` | 设置 HtmlReport 显示的内容 |
| `IsShown` | boolean | `<Path>.IsShown:boolean` | 设置 HtmlReport 是否显示在插入它的 Frame 窗口中 |
| `TocLevels` | integer | `<Path>.TocLevels:integer` | 设置目录显示的层级数（1–4） |
| `WindowHeight` | integer | `<Path>.WindowHeight:integer` | 设置显示窗口打开时的高度（像素） |
| `WindowWidth` | integer | `<Path>.WindowWidth:integer` | 设置显示窗口打开时的宽度（像素） |

---

## 4. 属性详解

### 4.1 Content [SimTalk]

设置 `<Path>` 指定的 `HtmlReport` 显示的内容（Content）。

- **类型**：Attribute
- **语法**：`<Path>.Content:string`
- **赋值**：可赋值 `string` 类型的数据。

**示例**

```simtalk
HtmlReport.Content := "[!self, Header, *]\
# General Information\
[Receiving, \"Statistics of the Source named 'Receiving' and the station 
named 'MyStation'\"]\
[MyStation]\
Created on [=day(sysdate)].[=month(sysdate)].[=year(sysdate)+1900]"
```

**参见**：Tab Content [HtmlReport]

---

### 4.2 IsShown [SimTalk]

设置 `<Path>` 指定的 `HtmlReport` 是否显示在插入它的 Frame 窗口中（`true`）或不显示（`false`）。

- **类型**：boolean（`attributes.md` 中将本小节类型标为 Method，但提供的是属性式赋值语法）
- **语法**：`<Path>.IsShown:boolean`
- **赋值**：可赋值 `boolean` 类型的数据。

**示例**

```simtalk
MyReport.IsShown := true
```

**参见**：Show Report

---

### 4.3 TocLevels [SimTalk]

设置 `<Path>` 指定的 `HtmlReport` 显示的目录层级数。

- **类型**：Attribute
- **语法**：`<Path>.TocLevels:integer`
- **赋值**：可赋值 `integer` 类型的数据。

取值范围为 1 到 4；若指定大于 4 的值，Plant Simulation 会将其按 4 处理。

**示例**

```simtalk
MyReport.TocLevels := 4
```

**参见**：Study the HtmlReport

---

### 4.4 WindowHeight [SimTalk]

设置 `<Path>` 指定的 `HtmlReport` 显示窗口打开时的高度（单位：像素）。

- **语法**：`<Path>.WindowHeight:integer`
- **赋值**：可赋值 `integer` 类型的数据。

**示例**

```simtalk
MyHtmlReport.WindowHeight := 600 // pixels
```

**参见**：Show Report

---

### 4.5 WindowWidth [SimTalk]

设置 `<Path>` 指定的 `HtmlReport` 显示窗口打开时的宽度（单位：像素）。

- **语法**：`<Path>.WindowWidth:integer`
- **赋值**：可赋值 `integer` 类型的数据。

**示例**

```simtalk
MyHtmlReport.WindowWidth :=  800 // pixels
```

**参见**：Show Report
