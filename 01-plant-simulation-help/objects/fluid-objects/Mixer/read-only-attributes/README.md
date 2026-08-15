# Read-Only Attributes of the Mixer

本目录汇总了 Mixer（混合器）对象的只读属性（Read-Only Attributes）。

## 概述

Mixer 提供以下只读属性：

- 本目录"目录"（table of contents）中所列的只读属性。
- _Read-Only Attributes of the Fluid Objects（流体对象的只读属性）。
- _Read-Only Attributes of All Objects（所有对象的只读属性）。

可以查询只读属性的值，但**不能设置**它们，因为 Plant Simulation 会在查询的时间点实时计算这些值。在大多数情况下，只读属性对应对象某个选项卡（例如 Statistics 选项卡）上不可编辑的对话框项。

要查看对象的全部方法、只读属性和属性，可打开 Show Attributes and Methods 窗口：

- 在类库（Class Library）的上下文菜单中选择 **Show Attributes and Methods**，可显示所选类的方法、只读属性和属性。
- 在插入了实例的 Frame 的 Home 功能区选项卡上，按 **F8** 键或点击 **Show Attributes and Methods**，可显示所选实例的方法、只读属性和属性。

查询只读属性值的示例：

```simtalk
print Mixer.Full
```

## 只读属性列表

| 属性 | 返回类型 | 说明 | 可监视 |
| --- | --- | --- | --- |
| `CurrentAmount` | `real` | 返回 Mixer 混合容器中物料的当前量（单位：升） | 否 |
| `CurrentFillLevel` | `real` | 返回 Mixer 混合容器中物料的当前填充水平（单位：百分比） | 否 |
| `Empty` | `boolean` | 返回 Mixer 是否为空 | 是 |
| `EntranceOpen` | `boolean` | 返回物料是否因当前恢复时间而可以进入 Mixer | 否 |
| `Full` | `boolean` | 返回 Mixer 是否已满 | 是 |
| `Ready` | `boolean` | 返回 Mixer 是否已完成配料混合并准备好进行新的混合过程 | 是 |
| `StatThroughput` | `real` | 返回 Mixer 使用配料混合出的产品通过量（单位：升） | 否 |
| `TimeUntilEntranceOpen` | `real` | 返回恢复时间结束后 Mixer 入口再次打开所需的时间 | 否 |

## 各属性说明

### CurrentAmount [SimTalk] - Mixer

返回由 `<Path>` 指定的 Mixer 混合容器中物料的当前量。

- **类型：** 只读属性
- **语法：** `<Path>.CurrentAmount → real`
- **返回值：** 数据类型为 `real`，当前量以升为单位。

```simtalk
print MyMixer.CurrentAmount
```

**参见：** Current Amount [Mixer]

---

### CurrentFillLevel [SimTalk] - Mixer

返回由 `<Path>` 指定的 Mixer 混合容器中物料的当前填充水平。

- **类型：** 只读属性
- **语法：** `<Path>.CurrentFillLevel → real`
- **返回值：** 数据类型为 `real`，当前量以百分比为单位。

```simtalk
print MyMixer.CurrentFillLevel
```

**参见：** Current Fill Level [Mixer]

---

### Empty [SimTalk] - Mixer

返回由 `<Path>` 指定的 Mixer 是否为空。

- **类型：** 只读属性
- **语法：** `<Path>.Empty → boolean`
- **可监视：** 该只读属性可被监视（watchable）。
- **返回值：** 数据类型为 `boolean`。

```simtalk
print MyMixer.Empty
```

**参见：** Full [SimTalk] - Mixer

---

### EntranceOpen [SimTalk] - Mixer

返回物料是否因当前恢复时间而可以进入由 `<Path>` 指定的 Mixer。

- **类型：** 只读属性
- **语法：** `<Path>.EntranceOpen → boolean`
- **返回值：** 数据类型为 `boolean`。

```simtalk
print MyMixer.EntranceOpen
```

**参见：**
- Entrance Locked [material flow objects]
- TimeUntilEntranceOpen [SimTalk] - Mixer

---

### Full [SimTalk] - Mixer

返回由 `<Path>` 指定的 Mixer 是否已满。

- **类型：** 只读属性
- **语法：** `<Path>.Full → boolean`
- **可监视：** 该只读属性可被监视（watchable）。
- **返回值：** 数据类型为 `boolean`。

```simtalk
print MyMixer.Full
```

**参见：** Empty [SimTalk] - Mixer

---

### Ready [SimTalk] - Mixer

返回由 `<Path>` 指定的 Mixer 是否已完成配料混合，并准备好进行新的混合过程。

- **类型：** 只读属性
- **语法：** `<Path>.Ready → boolean`
- **可监视：** 该只读属性可被监视（watchable）。
- **返回值：** 数据类型为 `boolean`。

```simtalk
print MyMixer.Ready
```

---

### StatThroughput [SimTalk] - Mixer

返回由 `<Path>` 指定的 Mixer 使用配料混合出的产品的通过量。

- **类型：** 只读属性
- **语法：** `<Path>.StatThroughput → real`
- **返回值：** 数据类型为 `real`，通过量以升为单位。

```simtalk
print MyMixer.StatThroughput
```

**参见：** Tab Statistics [FluidDrain]

---

### TimeUntilEntranceOpen [SimTalk] - Mixer

返回恢复时间结束后，由 `<Path>` 指定的 Mixer 入口再次打开所需的时间。

- **类型：** 只读属性
- **语法：** `<Path>.TimeUntilEntranceOpen → real`
- **返回值：** 数据类型为 `real`。

```simtalk
print MyMixer.TimeUntilEntranceOpen
```

**参见：** EntranceOpen [SimTalk] - Mixer
