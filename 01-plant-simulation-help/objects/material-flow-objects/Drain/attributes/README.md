# Drain Attributes（Drain 对象属性）

本目录汇总了 Plant Simulation 中 **Drain（排水/移除）** 对象的属性（attributes），内容来源于 `attributes.md`，并参考了同级 `general/README.md` 中对 Drain 对象的概述。

> 说明：本目录下目前仅有一个内容文件 `attributes.md`，无子文件夹，故无子文件夹 README.md。

## 目录内容

- `attributes.md` — Drain 属性的说明文档（本总结的源文件）。
- `attributes.txtx` — 相同内容的文本提取版本（Siemens Plant Simulation Help 导出，含分页与 "See also" 交叉引用）。

## Drain 对象概述

**Drain** 用于在工件（MU）加工完成后将其从工厂中移除，通常代表工厂的发货部门。

- Drain 的内置属性与 **Station** 相同；与 Station 一样，它只有一个加工位置。
- 与 Station 的唯一区别在于：Drain 会将加工完成的工件**从工厂中移除**，而不是将其移动到后续物料流对象。
- Drain 本质上是 **Source** 的对应物（Source 生产工件，Drain 移除工件）。
- 添加到模型：Home 功能区标签页 → `Manage Class Library > Basic Objects > MaterialFlow > Drain`。

## 属性概述

Drain 提供：

- 本目录（`attributes.md`）中所列的属性。
- **Station** 的属性（Attributes of the Station）。
- **All Objects** 的属性（Attributes of All Objects）。
- **Material Flow Objects** 的属性（Attributes of the Material Flow Objects）。

## 属性列表

| 属性 | 类型 | 语法 | 说明 |
| --- | --- | --- | --- |
| `StatTranspWorkingPortion` | 只读属性 | `<Path>.StatTranspWorkingPortion → real` | 返回 MU 生命周期中停留在工作状态的 **Transport（运输类）** 物料流对象上的时间占比之和。 |
| `TypeStatOn` | Attribute | `<Path>.TypeStatOn:boolean` | 激活（`true`）或关闭（`false`）按 MU 类型收集统计值。 |

### StatTranspWorkingPortion [SimTalk] - Drain

返回由 `<Path>` 指定的 Drain 从工厂移除的所有 MU 的生命周期时间占比之和，即这些 MU 停留在资源类型为 **Transport** 的工作状态物料流对象上的时间占比。

- **类型**：只读属性（Read-only attribute）
- **语法**：`<Path>.StatTranspWorkingPortion -> real`
- **返回值**：数据类型为 `real`

```simtalk
print MyDrain.StatTranspWorkingPortion
```

- **参见**：Resource Type of the material flow objects、Detailed Statistics Table [FluidDrain] of the Drain、Statistics report, Cumulated Statistics of the Parts which the Drain Removed From the Plant。

### TypeStatOn [SimTalk]

激活（`true`）或关闭（`false`）由 `<Path>` 指定的 Drain 按 MU 类型收集统计值。

- **类型**：Attribute
- **语法**：`<Path>.TypeStatOn:boolean`
- **可赋值**：数据类型为 `boolean` 的值。

```simtalk
MyDrain.TypeStatOn := false
```

- **参见**：Type Dependent Statistics、`typeStatistics [SimTalk] - Drain`、`typeStatisticsCumulated [SimTalk]`。

## 获取与设置属性值（Getting and Setting Attribute Values）

既可以设置属性的值，也可以获取属性的值，方式有两种：通过对话框窗口中的复选框、文本框和下拉列表，或通过为相应属性赋值。

- **设置属性值**，例如：

```simtalk
MyDrain.Pause := true
```

- **获取属性值**，例如：

```simtalk
print MyDrain.Pause
posit := MyStation.Cont.XPos
```

要查看对象的全部方法、只读属性与属性，请打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可查看所选类的方法、只读属性与属性 [general description]。
- 按 **F8** 键，或点击插入实例的 Frame 中 Home 功能区标签页的 **Show Attributes and Methods**，可查看所选实例的方法、只读属性与属性 [general description]。

## 相关文档

- `../general/README.md` — Drain 对象概述、对话框与各选项卡说明。
- `../methods/README.md` — Drain 的方法（`typeStatistics`、`typeStatisticsCumulated`）与只读属性说明。
- `../read-only-attributes/README.md` — Drain 的只读属性文档（`StatAvgExitInterval`、`StatTranspWorkingPortion` 等）。
