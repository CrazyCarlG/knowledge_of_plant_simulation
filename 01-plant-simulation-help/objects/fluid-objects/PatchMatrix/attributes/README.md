# PatchMatrix Attributes

本文件汇总了 `attributes` 目录下 Markdown 文档（`attributes.md`）的内容。该目录无子文件夹，因此不包含子目录中的 README.md。

`attributes.md` 同时涵盖了 **PatchMatrix**（流体对象）的**只读属性（Read-Only Attributes）**与**属性（Attributes）**两部分说明，并附带 **MaterialsTable** 的说明。

## 只读属性（Read-Only Attributes）

PatchMatrix 提供：

- **流体对象（Fluid Objects）的只读属性**。
- **所有对象（All Objects）的只读属性**。

只读属性**只能查询、不能设置**——其值由 Plant Simulation 在查询的时间点即时计算得出。多数情况下，只读属性对应对象某个选项卡（例如 **Statistics** 选项卡）上不可用的对话框项。

查看对象全部方法、只读属性和属性的方式：打开 **Show Attributes and Methods** 窗口。

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，查看所选类（Class）的方法、只读属性和属性。
- 按 **F8** 键，或点击插入实例所在 Frame 的 Home 功能区 **Show Attributes and Methods**，查看所选实例（Instance）的方法、只读属性和属性。

查询只读属性示例：

```simtalk
print MyPatchMatrix.UUID
```

## 属性（Attributes）

PatchMatrix 提供：

- **流体对象（Fluid Objects）的属性**。
- **所有对象（All Objects）的属性**。

查看对象全部方法、只读属性和属性的方式同上：打开 **Show Attributes and Methods** 窗口。

属性**可以设置、也可以读取**，既可通过对话框窗口中的复选框、文本框和下拉列表，也可通过给相应属性赋值来实现。

- 设置属性值示例：

```simtalk
PatchMatrix.Name := "MyPatchMatrix"
```

- 读取属性值示例：

```simtalk
print PatchMatrix.Name
posit := MyStation.Cont.XPos
```

## MaterialsTable

使用对象 **MaterialsTable** 来定义工厂中要创建和加工的原料（ingredients）与产品（products）。

## 目录内文件

- `attributes.md` — PatchMatrix 只读属性与属性的帮助页文本。
- `attributes.txtx` — 同一帮助页的纯文本导出，内容一致。

---

Plant Simulation Help · Unpublished work. © 2026 Siemens
