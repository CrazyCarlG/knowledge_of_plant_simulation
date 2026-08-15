# ParallelStation — Methods（方法）总览

本目录汇总了 **ParallelStation**（并行工位）对象的方法（Methods）与只读属性（Read-Only Attributes）文档。当前目录下包含以下文件：

- `methods.md` — Markdown 格式的方法说明文档
- `methods.txtx` — 纯文本格式的同内容说明文档

> 注：本目录下没有子文件夹。

---

## 一、方法（Methods）

### 1. `findPart [SimTalk]`

在由 `<Path>` 指定的 ParallelStation 上查找指定名称的零件（Part）并返回它。

- **类型（Type）：** Method
- **语法（Syntax）：** `<Path>.findPart(PartType:string) → object`
- **参数（Parameter）：** `PartType`（数据类型 `string`）用于指定零件类型。
- **返回值（Return Value）：** 数据类型 `object`

**示例：**

```simtalk
var o: object := MyParallelStation.findPart("Container")
// 例如赋值 .MUs.Container:1
```

---

### 2. `pe, [X,Y] [SimTalk]`

设置由 `<Path>` 指定的 ParallelStation 生产单元（PE）上指定的加工工位。

**备注（Remarks）：**

- 除了 `pe([X,Y])`，也可以直接使用 `[X,Y]`。
- 要访问该工位上的 MU（移动单元），可追加 `.Cont`。

- **类型（Type）：** Method
- **语法（Syntax）：**

  ```
  <Path>.pe([X:integer,Y:integer]) → any
  <Path>[X:integer,Y:integer] → any
  ```

**参数（Parameters）：**

- `X`（可选，数据类型 `integer`）— 加工工位的 X 维度。
- `Y`（可选，数据类型 `integer`）— 加工工位的 Y 维度。

若不指定参数，Plant Simulation 会返回第一个空闲的 PE；若无空闲 PE，则返回工位 `(1,1)` 上的 PE。

- **返回值（Return Value）：** 数据类型 `any`

**示例：**

```simtalk
@.move(ParallelStation[2,3])
@.move(ParallelStation.pe(2,3))
print ParallelStation[2,3].Cont.name
```

**另请参见：** X-Dimension [ParallelStation]

---

## 二、ParallelStation 的只读属性（Read-Only Attributes）

ParallelStation 提供以下只读属性：

- 只读属性 `Capacity [SimTalk] - ParallelStation`
- _所有对象的只读属性（Read-Only Attributes of All Objects）
- 物流对象（Material Flow Objects）的只读属性

只读属性的值只能查询、不能设置，因为 Plant Simulation 会在查询的时间点计算其值。大多数情况下，只读属性对应对象某个选项卡上不可用的对话框项，例如 **Statistics（统计）** 选项卡。

要查看对象的所有方法、只读属性与属性，可打开 **Show Attributes and Methods（显示属性与方法）** 窗口：

- 在 Class Library（类库）的上下文菜单中选择 **Show Attributes and Methods**，可查看所选 **Class（类）** 的方法、只读属性与属性。
- 在已插入实例的 Frame 上按 **F8** 键，或点击 Home 功能区选项卡上的 **Show Attributes and Methods**，可查看所选 **Instance（实例）** 的方法、只读属性与属性。

查询只读属性值的示例：

```simtalk
print ParallelStation.Capacity
```
