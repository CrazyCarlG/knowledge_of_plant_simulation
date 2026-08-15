# DismantleStation — Attributes（属性）

本目录存放 **DismantleStation**（拆卸站）对象的属性说明文档。内容来源为 `attributes.md`（`attributes.txtx` 为其原始提取文本，两者内容一致）。以下是对其内容的总结。

## 1. 概述

**DismantleStation** 提供：

- 本目录列出的属性；
- 所有对象的属性（Attributes of All Objects）；
- 物料流对象的属性（Attributes of the Material Flow Objects）。

要查看对象的全部方法、只读属性和属性，打开 **Show Attributes and Methods** 窗口：

- 在类库（Class Library）的上下文菜单中选择 **Show Attributes and Methods**，查看所选**类**的成员；
- 在插入实例的 Frame 中按 **F8** 键，或点击 Home 功能区标签页的 **Show Attributes and Methods**，查看所选**实例**的成员。

属性的值既可以通过对话框窗口中的复选框、文本框和下拉列表设置/获取，也可以通过为相应属性赋值来设置/获取：

- **设置属性值**，例如：

```simtalk
MyDismantleStation.NewMU := ".MUs.basicMU"
```

- **获取属性值**，例如：

```simtalk
print MyDismantleStation.Pause
posit := MyStation.Cont.XPos
```

## 2. 属性总览

| 属性 | 类型 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| `StatAverageDwellTime` | 只读属性 | `time` | 返回主部件在 DismantleStation 上停留的平均时间。 |
| `DismantleMode` | 只读属性 | `string` | 设置 DismantleStation 如何处理 MU（`"Create MUs"` / `"Detach MUs"`）。 |
| `DismantleTable` | 只读属性 | `table` | 设置 DismantleStation 拆卸表的名称（含 `MU` / `Number` / `Successor` 列）。 |
| `ExitingMUMode` | 只读属性 | `string` | 设置主 MU 移出对象，还是创建新 MU 后移出（`"Main MU"` / `"New MU"`）。 |
| `MainMU` | 属性 | `integer` | 设置 DismantleStation 将主 MU 移向的后继编号。 |
| `NewMU` | 属性 | `path` | 设置 DismantleStation 所创建 MU 的路径。 |
| `Sequence` | 属性 | `string` | 设置 DismantleStation 将 MU 分配给所连接后继的方式。 |

## 3. 属性详解

### 3.1 StatAverageDwellTime（只读属性）

返回 `<Path>` 所指定 DismantleStation 上**主部件停留的平均时间**。

- **类型：** Read-only attribute（只读属性）
- **语法：** `<Path>.StatAverageDwellTime → time`
- **返回值：** 数据类型为 `time`。

**示例：**

```simtalk
print MyDismantleStation.StatAverageDwellTime
```

**备注：** Plant Simulation 只统计 DismantleStation **未暂停**且**未处于 unplanned（未计划）状态**的时间。

**参见：** `Tab Statistics`、`Attributes of the DismantleStation`

---

### 3.2 DismantleMode

设置 `<Path>` 所指定 DismantleStation **如何处理 MU**。

- **类型：** Read-only attribute（只读属性）
- **语法：** `<Path>.DismantleMode:string`
- **赋值：** 可赋数据类型 `string` 的值。
  - `"Create MUs"`：DismantleStation 创建装配件（mounting parts）。
  - `"Detach MUs"`：DismantleStation 从主 MU 上拆卸装配件，并移向拆卸表中所填写的后继。

**示例：**

```simtalk
MyDismantleStation.DismantleMode := "Detach MUs"
```

**备注：** 若只想卸载拆卸表中填写的装配件，选择 `Sequence > MUs exiting independent of other MUs` 或 `Main MU after other MUs`，且 `Dismantle Mode > Detach MUs`。始终在 `MU` 列填入有效的 MU 类、在 `Number` 列填入正数。

**参见：** `Dismantle Table`、`Sequence`、`Dismantle Mode`

---

### 3.3 DismantleTable

设置 `<Path>` 所指定 DismantleStation **拆卸表的名称**。

- **类型：** Read-only attribute（只读属性）
- **语法：** `<Path>.DismantleTable:table`
- **赋值：** 可赋数据类型 `table` 的值。

拆卸表包含离开 DismantleStation 的 MU 名称及其后继：

- **`MU` 列** — MU 类的路径（如 `.MUs.Part`、`.MUs.Container`、`.MUs.Transporter`）；留空表示指定任意 MU 类。
- **`Number` 列** — 被拆卸的 MU 数量；未填写时默认为 `1`。
- **`Successor` 列** — 后继编号；未填写时，`Detach MUs` 模式下装配件移向 `1` 号后继，`Create MUs` 模式下移向主 MU 所去的后继。

**备注：**

- 若填写了 **MU Target**，Worker 会把所有部件搬运到该目标；否则由拆卸表或 `Main MU to successor with number` 设置决定。
- **按 MU 类自动移动所有部件**：在 `MU` 填入任意 MU 类，`Number` 填 `-1`（该类所有剩余部件），`Successor` 填后继编号；对其他类重复此操作。
- **将所有部件自动移到一个后继**：`MU` 留空，`Number` 填 `-1`，`Successor` 填后继编号。
- **继承**：若拆卸表被继承，写入其单元格时继承不会自动取消。将拆卸表赋值给自身即可取消继承。

**示例：**

```simtalk
var DismList:table[object,integer,integer]
DismList.create
DismList.writeRow(1,1, .MUs.MyPart,1,1)
DismList.writeRow(1,2, .MUs.MyPart,2,1)
MyDismantleStation.DismantleTable := DismList

-- 取消继承：
DismantleStation.DismantleTable := DismantleStation.DismantleTable

-- 入口控制示例（EntranceCtrlBeforeActions := true）：
?.DismantleList := ?.DismantleList    -- 取消继承
?.DismantleList[2, 1] := @.AmountOfParts
```

**参见：** `Dismantle Mode`、`Dismantle Table`、`Sequence`、`MU Target`、`Main MU to Successor with Number`

---

### 3.4 ExitingMUMode

设置 `<Path>` 所指定 DismantleStation 是让**主 MU 移出对象**，还是**创建一个新 MU 后移出对象**。

- **类型：** Read-only attribute（只读属性）
- **语法：** `<Path>.ExitingMUMode:string`
- **赋值：** 可赋数据类型 `string` 的值。
  - `"Main MU"`：DismantleStation 将主 MU 移向后继对象。
  - `"New MU"`：DismantleStation 删除主 MU、创建一个新 MU 并移向后继；此时 DismantleStation 显示 `MU` 文本框。

**示例：**

```simtalk
MyDismantleStation.ExitingMUMode := "New MU"
```

**参见：** `Exiting MU`

---

### 3.5 MainMU

设置 `<Path>` 所指定 DismantleStation **将主 MU 移向的后继编号**。

- **类型：** Attribute（属性）
- **语法：** `<Path>.MainMU:integer`
- **赋值：** 可赋数据类型 `integer` 的值。

**示例：**

```simtalk
MyDismantleStation.MainMU := 2
```

**备注：** 若填写了 **MU Target**，Worker 会把所有部件搬运到该目标；否则由拆卸表或 `Main MU to successor with number` 设置决定。

**参见：** `Main MU to Successor with Number`、`MU Target`、`Dismantle Table`

---

### 3.6 NewMU

设置 `<Path>` 所指定 DismantleStation **所创建 MU 的路径**。

- **类型：** Attribute（属性）
- **语法：** `<Path>.NewMU:path`
- **赋值：** 可赋一个路径。

**示例：**

```simtalk
MyDismantleStation.NewMU := .MUs.basicMU
```

**备注：** 当 DismantleStation 删除主 MU 并改创建新 MU 时，`NewMU` 生效。

**参见：** `Exiting MU`

---

### 3.7 Sequence

设置 `<Path>` 所指定 DismantleStation **将 MU 分配给所连接后继的方式**。

- **类型：** Attribute（属性）
- **语法：** `<Path>.Sequence:string`
- **赋值：** 可赋数据类型 `string` 的值。
  - `"MUs to all successors"`（将所有 MU 发送到所有后继）
  - `"MUs exiting independent of other MUs"`（MU 相互独立地移出）
  - `"Main MU after other MUs"`（主 MU 在其他 MU 之后移出）

**示例：**

```simtalk
MyDismantleStation.Sequence := "Main MU after other MUs"
```

**备注：**

- **MUs to all successors** — 配合 `Create MUs`：为每个后继创建一个新部件；主 MU 移向 `Main MU to Successor with Number` 指定的后继。配合 `Detach MUs`：MU 依次移向除接收主 MU 的后继之外的各后继。例如有四个后继、主 MU 移向 2 号后继时，新 MU 移向 1、3、4 号后继。
- **MUs exiting independent of other MUs** — DismantleStation 尽快将主 MU 及随后每个 MU 移向所定义的后继。
- **Main MU after other MUs** — 先把装配件移向后继，再移主 MU。

若只想卸载拆卸表中填写的装配件，选择 `MUs exiting independent of other MUs` 或 `Main MU after other MUs` 且 `Dismantle mode > Detach MUs`，并在 `MU` 列填入有效 MU 类、`Number` 列填入正数。

**参见：** `Sequence`、`DismantleMode`、`DismantleTable`

---

### 3.8 相关参考：PickAndPlace Robot

源文档末尾附带介绍了 **PickAndPlace robot**（拾放机器人）对象：用于在一个工位拾取部件、旋转并放置到另一个工位。

- 可通过 `Capacity` 设置一次拾取并递送一个或多个部件。
- 它按如下方式将部件传送给后继：
  1. 部件到达前驱的出口，通知机器人希望被拾取。
  2. 机器人判断是否拾取该部件：
     - 无 Pull Control 时，机器人收到通知并接受部件；
     - 有 Pull Control 时，机器人执行该控制，部件被选中时才被拾取。
  3. 机器人旋转到相应前驱并拾取部件。

## 目录说明

- `attributes.md`：DismantleStation 属性说明的 Markdown 版本（本总结的源文件）。
- `attributes.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。
