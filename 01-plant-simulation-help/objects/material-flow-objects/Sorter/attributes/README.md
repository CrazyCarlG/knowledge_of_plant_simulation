# Sorter / attributes — 内容总结

> **说明：** 本目录虽然位于 `Sorter/attributes` 路径下，但其中的文档（`attributes.md` 与 `attributes.txtx`）实际记录的是 **Store（仓库/存储）** 对象的属性（Attributes）与一个只读属性（`Stock.MyPartName`），并在文件末尾附带 `PlaceBuffer` 对象的简短说明。本 README 忠实按照源文件内容进行总结。

本目录包含以下文件：

- `attributes.md` — Store 对象属性帮助文档（Markdown 格式）
- `attributes.txtx` — 与 `attributes.md` 内容对应的纯文本源文件
- `Plant-Simulation-Help2606_4964-4972.pdf` — 对应的 PDF 参考文件（Plant Simulation Help 11-2034 至 11-2042）

目录下没有子文件夹，因此不存在子文件夹中的 README.md 需要合并。`Sorter` 下相邻的 `general/`、`methods/` 与 `read-only-attributes/` 目录各有 README.md，均同样记录 Store 对象，可交叉参考（见文末第 4 节）。

---

## 1. 属性总览

`attributes.md` 中记录的 Store 属性汇总如下：

| 属性 | 类型 | 数据类型 | 可监视 | 作用 |
| --- | --- | --- | --- | --- |
| `Stock.MyPartName` | 只读属性 | `integer` | 否 | 返回指定零件的当前库存 |
| `FillWholeLayer` | 属性 | `boolean` | 否 | 设置 Z-Dimension 大于 1 时是否始终整层填充 |
| `Supermarket` | 属性 | `boolean` | 否 | 设置 Store 是否作为超市（Supermarket）工作 |
| `XDim` | 属性 | `integer` | 是 | 设置 x 轴上的存储位数量 |
| `YDim` | 属性 | `integer` | 是 | 设置 y 轴上的存储位数量 |
| `ZDim` | 属性 | `integer` | 是 | 设置 z 轴上的存储位数量（用于堆叠零件） |

此外，文件末尾附有 **PlaceBuffer** 对象的简介（见第 3 节）。

---

## 2. 各属性详解

### 2.1 Stock.MyPartName [SimTalk]

返回 `<Path>` 所指定的 Store 中，由 `MyPartName` 指定的零件的当前库存。

- **类型：** 只读属性（Read-only attribute）
- **语法：**

  ```simtalk
  <Path>.Stock.MyPartName → integer
  ```

- **返回值：** `integer`
- **备注：** `MyPartName` 是相应零件的名称，在 Store 的 **Configuration Table（配置表）** 中设置。
- **示例：**

  ```simtalk
  print MyStore.Stock.PartRed
  // 例如可能返回 1
  ```

- **参见：** Configuration（按钮）

---

### 2.2 Attributes of the Store（Store 的属性总说明）

Store 提供：

- 目录左侧列出的属性。
- 所有对象的属性（Attributes of All Objects）。
- 物料流对象的属性（Attributes of the Material Flow Objects）。

查看对象的所有方法、只读属性与属性，可打开 **Show Attributes and Methods** 窗口：

- 在 **Class Library（类库）** 的上下文菜单中选择 **Show Attributes and Methods**，查看所选 Class 的方法、只读属性与属性。
- 在插入实例的 Frame 的 Home 功能区选项卡上按 **F8**，或点击 **Show Attributes and Methods**，查看所选 Instance 的方法、只读属性与属性。

可以通过对话框窗口中的复选框、文本框与下拉列表，或通过给相应属性赋值来设置属性值；也可以获取属性值：

```simtalk
// 设置属性值：
MyStore.YDim := 10
// 获取属性值：
print MyStore.YDim
posit := MyStation.Cont.XPos
```

---

### 2.3 FillWholeLayer [SimTalk] — Store

设置 `<Path>` 所指定的 Store，在 Z-Dimension 大于 1 时是否始终填满整层（`true`）或不填满整层（`false`）。

- **类型：** 属性（Attribute）
- **语法：**

  ```simtalk
  <Path>.FillWholeLayer:boolean
  ```

- **赋值：** `boolean`
- **备注：** Plant Simulation 总是先开始新的一层，然后才把零件堆放到下面一层。指定 `false` 会在开始新层之前，先把每个存储位填充到其最大 Z-Dimension。
- **示例：**

  ```simtalk
  MyStore.XDim := 2
  MyStore.YDim := 2
  MyStore.ZDim := 2
  MyStore.FillWholeLayer := true
  ```

- **参见：** Fill Whole Layer [check box] - Store

---

### 2.4 Supermarket [SimTalk]

设置 `<Path>` 所指定的 Store 是否作为超市（Supermarket）工作（`true`）或不作为超市工作（`false`）。

- **类型：** 属性（Attribute）
- **语法：**

  ```simtalk
  <Path>.Supermarket:boolean
  ```

- **赋值：** `boolean`
- **示例：**

  ```simtalk
  MyStore.Supermarket := true
  ```

- **参见：** Supermarket [check box]、Configuration [button]、Source > MU selection [drop-down list] > Order Controlled [MU selection]

---

### 2.5 XDim [SimTalk] — Store

设置 `<Path>` 所指定的 Store 在 x 轴上的存储位数量。

- **类型：** 属性（Attribute）
- **语法：**

  ```simtalk
  <Path>.XDim:integer
  ```

- **可监视（Watchable）：** 是
- **赋值：** `integer`
- **备注：**
  - 容量（Capacity）等于 `XDim × YDim × ZDim` 的乘积，最大允许值为一千万（10,000,000）。
  - 若缩小 Store 的尺寸，请确保没有 MU 位于将被删除的存储位上——应先删除这些 MU，或把它们移动到更小存储空间上的其他存储位。
- **示例：**

  ```simtalk
  MyStore.XDim := 10
  ```

- **参见：** X-Dimension [Store]

---

### 2.6 YDim [SimTalk] — Store

设置 `<Path>` 所指定的 Store 在 y 轴上的存储位数量。

- **类型：** 属性（Attribute）
- **语法：**

  ```simtalk
  <Path>.YDim:integer
  ```

- **可监视（Watchable）：** 是
- **赋值：** `integer`
- **备注：**
  - 容量（Capacity）等于 `XDim × YDim × ZDim` 的乘积，最大允许值为一千万（10,000,000）。
  - 若缩小 Store 的尺寸，请确保没有 MU 位于将被删除的存储位上——应先删除这些 MU，或把它们移动到更小存储空间上的其他存储位。
- **示例：**

  ```simtalk
  MyStore.YDim := 10
  ```

- **参见：** Y-Dimension [Store]

---

### 2.7 ZDim [SimTalk] — Store

设置 `<Path>` 所指定的 Store 在 z 轴上的存储位数量。

- **类型：** 属性（Attribute）
- **语法：**

  ```simtalk
  <Path>.ZDim:integer
  ```

- **可监视（Watchable）：** 是
- **赋值：** `integer`
- **备注：**
  - `ZDim` 允许把零件堆叠到其他零件之上。
  - 容量（Capacity）等于 `XDim × YDim × ZDim` 的乘积，最大允许值为一千万（10,000,000）。
  - 若缩小 Store 的尺寸，请确保没有 MU 位于将被删除的存储位上——应先删除这些 MU，或把它们移动到更小存储空间上的其他存储位。
- **示例：**

  ```simtalk
  MyStore.ZDim := 4
  // 枚举存储位 (1,1) 上的所有 MU：
  var place := Store[1,1]
  for var i := 1 to place.NumMU
     print place.MU(i)
  next
  // 返回该堆叠最顶层的 MU：
  Store[1,1].Cont
  // 返回存储位 (1,2) 上自顶向下第二个 MU：
  Store[1,2].MU(2)
  ```

- **参见：** Z-Dimension [Store]、Stack Parts in the Store、Unload Stacked Parts、mu [SimTalk] - PE, Store

---

## 3. 文件末尾附带的 PlaceBuffer 简介

文件末尾附有一小段 **PlaceBuffer** 对象的说明：

- **PlaceBuffer** 对象用于在若干缓冲位（buffer places）上处理零件，这些缓冲位排成一排、一个接一个。
- 它不是 Toolbox 默认提供的内置对象之一。
- **说明：** PlaceBuffer 处理的 MU 必须从一个缓冲位前进到下一个缓冲位，只有经过最后一个缓冲位后才能离开 PlaceBuffer。这样可以对每个缓冲位单独调用与访问。

---

## 4. 相关目录交叉参考

`Sorter` 目录下的相邻子目录同样记录 Store 对象：

- `../general/README.md` — Store 对象的总体说明（概述、对话框、各选项卡、菜单、方法等）。
- `../methods/README.md` — Store 中 PE（库位/生产元素）的方法与只读属性：`Cont`、`exitBlockList`、`getStackHeight`、`mu`、`NumMU`。
- `../read-only-attributes/README.md` — Store 的只读属性：`Capacity`、`XDim`/`YDim`/`ZDim`、`Stock.MyPartName` 等。

---

*Source: Plant Simulation Help (11-2034 / 11-2042). Unpublished work. © 2026 Siemens.*
