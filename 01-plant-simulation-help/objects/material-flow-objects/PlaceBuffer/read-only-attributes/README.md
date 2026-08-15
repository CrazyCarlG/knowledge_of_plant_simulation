# README — PlaceBuffer Read-Only Attributes

本目录汇总 **PlaceBuffer（暂存区）对象**的只读属性（Read-Only Attributes）相关内容。

## 目录内容概览

- `read-only-attributes.md` — PlaceBuffer 只读属性与属性的说明（主要来源）。
- `read-only-attributes.txtx` — 与 `read-only-attributes.md` 内容对应的纯文本版本。
- `Plant-Simulation-Help2606_4997-4998.pdf` — 对应帮助文档的 PDF 页面（11-2067 / 11-2068）。

> 当前目录下无子文件夹，因此无其他 `README.md` 需要合并。

## 内容总结

### 1. PlaceBuffer 的只读属性（Read-Only Attributes）

PlaceBuffer 提供以下只读属性来源：

- 所有对象的只读属性（_Read-Only Attributes of All Objects）。
- 物流对象（Material Flow Objects）的只读属性。

**使用要点：**

- 只读属性**只能查询、不能赋值**。Plant Simulation 会在查询的时间点实时计算其值。
- 大多数只读属性对应对象某个选项卡（例如 **Statistics** 选项卡）上不可编辑的对话框项。

**查询示例：**

```simtalk
print MyPlaceBuffer.UUID
```

### 2. 查看方法与属性

要查看对象的全部方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：

- 在 Class Library（类库）的上下文菜单中选择 **Show Attributes and Methods**，可查看所选类的信息。
- 在 Frame（框架）中选中实例后，按 **F8** 键，或点击 Home 功能区选项卡上的 **Show Attributes and Methods**，可查看所选实例的信息。

### 3. PlaceBuffer 的属性（Attributes）

PlaceBuffer 提供：

- 左侧目录（table of contents）中列出的属性。
- 所有对象的属性（Attributes of All Objects）。
- 物流对象的属性（Attributes of the Material Flow Objects）。

属性**既可读取也可设置**，可通过对话框中的复选框、文本框、下拉列表，或直接给属性赋值。

**设置属性示例：**

```simtalk
MyPlaceBuffer.Accumulating := true
```

**读取属性示例：**

```simtalk
print MyPlaceBuffer.Accumulating
posit := MyStation.Cont.XPos
```

## 参考来源

- Plant Simulation Help 11-2067 / 11-2068
- Unpublished work. © 2026 Siemens
