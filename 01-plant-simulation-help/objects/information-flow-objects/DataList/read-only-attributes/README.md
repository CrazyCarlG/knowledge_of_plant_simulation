# DataList — Read-Only Attributes（只读属性）

本目录汇总 DataList 对象的只读属性（Read-Only Attributes）文档。目录内容来源于 `read-only-attributes.md`（以及同内容的源文件 `read-only-attributes.txtx`），当前无子文件夹。

## 概述

DataList 提供以下只读属性：

- 列表与表格（Lists and Tables）的只读属性。
- 所有对象（All Objects）的只读属性。

只读属性只能**查询（query）**，不能**设置（set）**。其值由 Plant Simulation 在查询的时刻实时计算得出。在大多数情况下，只读属性对应于对象某个选项卡（例如 Statistics 选项卡）上不可用的对话框项。

## 查看属性与方法

要查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，显示所选**类（Class）**的方法、只读属性和属性。
- 按 **F8** 键，或在插入实例的 Frame 的 Home 功能区的 **Show Attributes and Methods** 按钮，显示所选**实例（Instance）**的方法、只读属性和属性。

## 查询只读属性

查询只读属性的值，示例：

```simtalk
print MyDataList.Full
```

## DataList 的属性

DataList 还提供：

- 列表与表格的属性。
- 所有对象的属性。

属性既可以设置也可以获取，方式包括对话框中的复选框、文本框、下拉列表，或通过赋值语句。

- 设置属性值，示例：

```simtalk
myDataList.InfoflowReadOnly := true
```

- 获取属性值，示例：

```simtalk
print myDataList.InfoflowReadOnly
```

- 从另一个对象读取坐标值，示例：

```simtalk
posit := Station.Cont.XPos
```

## 相关对象：DataStack

使用 **DataStack** 对象可按 LIFO（后进先出）方式访问数据。

**DataQueue** 与 **DataStack** 都是只有一列的列表，它们共享所有方法和属性，区别仅在于内置特性（DataQueue 为 FIFO，DataStack 为 LIFO）。
