# FluidSource Attributes 目录说明

本目录收录 **FluidSource（流体源）** 对象的属性文档，内容来源为 `attributes.md`。

## 概述

FluidSource 是 Plant Simulation 中用于**产生流体材料**的对象，它向物料流中注入自由流动材料（以升为单位），随后材料通过 `Pipe` 流向后续对象。

除本目录列出的属性外，FluidSource 还继承：

- 流体对象通用属性（Attributes of the Fluid Objects）
- 所有对象通用属性（Attributes of All Objects）

可通过 **Show Attributes and Methods** 窗口查看对象的全部方法、只读属性和属性（在类库中选中类，或在 Frame 中选中实例后按 `F8`）。

## 属性列表

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| `StatAmount` | 只读属性 | 返回该 FluidSource 已产生的材料总量（升），数据类型 `real` |
| `Material` | 属性 | 设置要生产的材料名称（或序列表路径），取值取决于 `MaterialSelection` |
| `MaterialSelection` | 属性 | 设置材料的选择方式：Constant / Sequence cyclical / Sequence |
| `MaterialsTable` | 属性 | 设置包含可生产材料数据的 MaterialsTable（数据类型 `path`） |
| `OutflowRate` | 属性 | 设置材料流出速率（升/秒），数据类型 `real` |

## 各属性要点

### StatAmount（只读）

- 语法：`<Path>.StatAmount → real`
- 返回 FluidSource 已生产的材料量（升）。

```simtalk
print MyFluidSource.StatAmount
```

### Material

- 语法：`<Path>.Material:string`
- 材料名称须已在 `MaterialsTable` 中定义。
- 赋值类型取决于 `MaterialSelection`：
  - **Constant**：赋 `string` 类型的材料名；
  - **Sequence Cyclical / Sequence**：赋 `DataTable` 对象或其路径。

```simtalk
MyFluidSource.Material := "MyMaterial"
MyFluidSource.MaterialSelection := "Sequence"
MyFluidSource.Material := .UserObjects.MySequenceTable
```

### MaterialSelection

- 语法：`<Path>.MaterialSelection:string`
- 三种取值：
  - **"Constant"**：只生产单一材料，材料名由 `Material` 指定；
  - **"Sequence cyclical"**：按序列表顺序循环生产材料，处理完整个序列后从头重新开始；
  - **"Sequence"**：按序列表顺序仅生产一次，处理完后不再生产。

```simtalk
MyFluidSource.MaterialSelection := "Sequence"
MyFluidSource.Material := .UserObjects.MySequenceTable
```

### MaterialsTable

- 语法：`<Path>.MaterialsTable:path`
- 设置包含不同材料数据的 MaterialsTable。

```simtalk
MyFluidSource.MaterialsTable := MyMaterialsTable
```

### OutflowRate

- 语法：`<Path>.OutflowRate:real`
- 设置材料流出速率（升/秒），材料经 `Pipe` 流向下一个对象。
- 注意：实际流出速率取决于所连接的 Pipe 数量——若连接了两根 Pipe，则每根 Pipe 都可能以该速率流出。若只想让指定量从对象流出，请先连接单根 Pipe，之后再分流。

```simtalk
MyFluidSource.OutflowRate := 1
```

## 相关对象：FluidDrain

`attributes.md` 末尾附带介绍了 **FluidDrain（流体排放口）**：它按材料名称区分并移除已混合、加工后的自由流动材料，与 FluidSource 形成物料的"注入—排放"闭环。可通过 **Manage Class Library > Basic Objects > Fluids > FluidDrain** 添加到模型。
