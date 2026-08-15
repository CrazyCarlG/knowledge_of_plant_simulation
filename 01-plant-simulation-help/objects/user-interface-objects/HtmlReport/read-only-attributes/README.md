# Read-Only Attributes of the HtmlReport

本目录介绍 HtmlReport 对象的只读属性（Read-Only Attributes）。

## 目录内容

- `read-only-attributes.md` — HtmlReport 只读属性的 Markdown 说明文档
- `read-only-attributes.txtx` — 相同内容的文本版本

## 内容摘要

HtmlReport 提供所有对象的只读属性（_Read-Only Attributes of All Objects）。这些属性只能查询其值，不能对其进行设置，因为 Plant Simulation 会在查询时实时计算对应的值。在大多数情况下，只读属性对应对象某个选项卡（如 Statistics 选项卡）上不可用的对话框项。

### 查询只读属性

```simtalk
print MyHtmlReport.UUID
```

### 查看方法与属性

要查看对象的所有方法、只读属性和属性，打开 **Show Attributes and Methods** 窗口：

- 在类库（Class Library）的上下文菜单中选择 **Show Attributes and Methods**，可查看所选类的方法、只读属性和属性。
- 按 **F8** 键，或点击插入实例所在 Frame 的 Home 功能区选项卡上的 **Show Attributes and Methods**，可查看所选实例的方法、只读属性和属性。

### 方法

#### show

将 `<Path>` 指定的 HtmlReport 作为 HTML 页面显示。

- **类型：** Method
- **语法：** `<Path>.show([Anchor:string])`

**参数：** 可选参数 `Anchor`（字符串类型）指定 Plant Simulation 打开 HTML 页面时导航到的锚点。

**示例：**

```simtalk
MyHtmlReport.show("DrainStat")
// 跳转到 Content 选项卡上由以下代码定义的锚点：
// << <a id="DrainStat"> </a> >>
```

### 属性

HtmlReport 提供：

- 所有对象的只读属性。
- 所有对象的属性。
