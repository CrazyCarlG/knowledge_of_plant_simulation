# PlaceBuffer（对象）— Methods 总结

本目录存放 **PlaceBuffer**（缓冲区工位）对象的**方法（Methods）**说明文档。内容来源为 `methods.md`（`methods.txtx` 为其原始提取文本，两者内容一致）。以下是对其内容的总结。

## 1. 方法概述

**PlaceBuffer** 提供以下方法：

- 方法 `pe, [X Y]`；
- 物料流对象的方法（Methods of the Material Flow Objects）；
- 所有对象的通用方法（Methods of All Objects）。

查看全部方法、只读属性和属性：打开 **Show Attributes and Methods** 窗口。

- 在**类库（Class Library）**中选中某个类后，右键上下文菜单选择 **Show Attributes and Methods**，可查看该类的方法、只读属性和属性。
- 在插入实例的 **Frame** 中按 **F8**，或点击 Home 功能区标签页的 **Show Attributes and Methods**，可查看该实例的方法、只读属性和属性。

## 2. 语法行约定

单个方法的语法行示例如下：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- 表达式 `<Path>` 表示该方法所应用对象的路径。
- 括号内列出方法的签名（参数标识符及数据类型）。例如 `(Parameter:string)` 表示一个 `string` 类型参数。除常量外，也可使用所需类型的变量或返回所需类型的方法。

> **注意：** 嵌套在括号中的表达式 `(…)` 必须输入括号，否则可能产生意外结果并打开调试器（Debugger）。

- 可选参数写在方括号内。例如 `[,Parameter:boolean]` 表示可以省略该布尔参数。
- 若参数有默认值，签名在参数后显示默认值，如示例中的 `:= false`。
- 若方法有返回值，签名在箭头 `→` 后显示其数据类型，如示例中的 `→ boolean`。

## 3. 方法 pe(1) / [1] [SimTalk] — PlaceBuffer

设置由 `<Path>` 指定的 PlaceBuffer 的指定位置（生产单元 / production element）。

### 备注（Remarks）

PlaceBuffer 有若干存储位置，这些位置排成一排、前后依次排列。

> **注意：** 若激活了 **Sequentially Indexing**（顺序索引），则不支持方法 `pe`。

### 类型（Type）

Method（方法）

### 语法（Syntax）

```
<Path>.pe([Index:integer:=1]) → any
<Path>[Index:integer] → any
```

### 参数（Parameter）

可选参数 `Index`（数据类型 `integer`）指定位置。

### 参数默认值（Default Value of the Parameter）

默认值为 `1`。

### 返回值（Return Value）

返回值的数据类型为 `any`。

### 示例（Example）

```
@.move(MyPlaceBuffer[2])
@.move(MyPlaceBuffer.pe(2))
```

### 参见（See also）

- Sequentially Indexing [check box]（顺序索引复选框）

## 4. 只读属性（Read-Only Attributes）

PlaceBuffer 提供：

- 所有对象的只读属性（Read-Only Attributes of All Objects）；
- 物料流对象的只读属性（Read-Only Attributes of the Material Flow Objects）。

只能查询只读属性的值，不能设置——Plant Simulation 会在你查询的时刻计算其值。多数情况下，只读属性对应对象某个选项卡（例如 **Statistics**）上不可用的对话框项。

查询只读属性的值，例如：

```
print MyPlaceBuffer.UUID
```

## 5. 属性（Attributes）

PlaceBuffer 提供：

- PlaceBuffer 的属性（Attributes of the PlaceBuffer）。

## 目录说明

- `methods.md`：PlaceBuffer 方法说明的 Markdown 版本（本总结的源文件）。
- `methods.txtx`：相同内容的文本提取版本。
- `Plant-Simulation-Help2606_4994-4997.pdf`：对应帮助文档的 PDF 摘录。
- 本目录无子文件夹，故无子文件夹 README.md。
