# Mixer 属性（Attributes）汇总

本目录包含 Mixer（混合器）对象的属性说明文档，来源为 Plant Simulation Help。Mixer 提供：

- 左侧目录（table of contents）中列出的属性
- Fluid Objects（流体对象）的属性
- All Objects（所有对象）的属性

可以通过 **Show Attributes and Methods** 窗口查看对象的全部方法、只读属性和属性。属性的值既可以通过对话框中的复选框、文本框、下拉列表设置，也可以通过 SimTalk 赋值来设置/获取，例如：

```simtalk
MyMixer.OutflowRate := 1          -- 设置属性值
print MyMixer.OutflowRate         -- 获取属性值
```

## 属性列表

| 属性 | 类型 | 语法 | 说明 |
| --- | --- | --- | --- |
| `TimeUntilEntranceOpen` | 只读属性 | `<Path>.TimeUntilEntranceOpen → real` | 返回 Mixer 入口在恢复时间（Recovery Time）结束后再次打开前的时间 |
| `IngredientCompleteCtrl` | 属性 | `<Path>.IngredientCompleteCtrl:method` | 指定一个 Method 对象作为“成分完成控制”，当配方中的某个成分完全到达 Mixer 时执行 |
| `MaterialsTable` | 属性 | `<Path>.MaterialsTable:path` | 设置包含 Mixer 可混合的各种材料数据的 MaterialsTable（材料表） |
| `OutflowRate` | 属性 | `<Path>.OutflowRate:real` | 设置 Mixer 所生产材料的流出速率（升/秒） |
| `ProcTime` | 属性 | `<Path>.ProcTime:time` | 设置 Mixer 的处理时间（Processing Time），即 Mixer 转化材料的时间 |
| `Product` | 属性 | `<Path>.Product:string` | 设置 Mixer 通过混合成分所生产的中间产品或最终产品的名称 |
| `ProductAmount` | 属性 | `<Path>.ProductAmount:real` | 设置 Mixer 通过混合成分所生产产品的数量（升） |
| `RecoveryTime` | 属性 | `<Path>.RecoveryTime:time` | 设置 Mixer 的恢复时间（Recovery Time），即冲洗、清洁并准备下一流程所需的时间 |
| `Volume` | 属性 | `<Path>.Volume:real` | 设置 Mixer 混合容器中可供成分或产品使用的体积（Volume） |

## 各属性详细说明

### TimeUntilEntranceOpen [SimTalk] - Mixer
- **类型**：只读属性（Read-only attribute）
- **语法**：`<Path>.TimeUntilEntranceOpen → real`
- **返回值**：数据类型为 `real`
- **说明**：返回 Mixer 入口在恢复时间结束后再次打开前的时间。

### IngredientCompleteCtrl [SimTalk]
- **类型**：属性（Attribute）
- **语法**：`<Path>.IngredientCompleteCtrl:method`
- **赋值类型**：`object` / `method`
- **说明**：当配方中的某个成分完全到达 Mixer 时，Plant Simulation 会执行“成分完成控制”（Ingredient Complete Control），从而可以通过 SimTalk 定义/启动仿真模型中所需的任何动作。当最后一个（或最后几个）成分与 Mixer 达到指定 Volume 同时到达时，该控制也会被调用。

### MaterialsTable [SimTalk] - Mixer
- **语法**：`<Path>.MaterialsTable:path`
- **赋值类型**：`path`
- **说明**：设置包含 Mixer 可混合的不同材料数据的 MaterialsTable。若在 MaterialsTable 的 Product Amount 列中为某配方指定 `-1`，Plant Simulation 会将所有成分之和作为 Product Amount；仅当混合成分会增大或减小体积（即 Product Amount 不等于成分之和）时，才需显式指定 Product Amount。

### OutflowRate [SimTalk] - Mixer
- **类型**：属性（Attribute）
- **语法**：`<Path>.OutflowRate:real`
- **赋值类型**：`real`
- **说明**：设置 Mixer 所生产材料的流出速率，材料随后通过 Pipe 对象流向材料流中的下一个对象。Outflow Rate 是每秒流出的材料升数。
- **注意**：实际流出速率取决于所连接的 Pipe 数量。例如连接两根 Pipe 时，只要 Pipe 的流出速率允许，指定的 Outflow Rate 会分别流经每根 Pipe。若只想让指定量从对象流出，应连接单根 Pipe，之后再将其拆分。

### ProcTime [SimTalk] - Mixer
- **类型**：属性（Attribute）
- **语法**：`<Path>.ProcTime:time`
- **赋值类型**：`time`
- **说明**：设置 Mixer 的处理时间，即 Mixer 转化材料的时间。

### Product [SimTalk]
- **类型**：属性（Attribute）
- **语法**：`<Path>.Product:string`
- **赋值类型**：`string`
- **说明**：设置 Mixer 通过混合成分所生产的中间产品或最终产品的名称。该产品名称必须在 MaterialsTable 中定义。

### ProductAmount [SimTalk]
- **类型**：属性（Attribute）
- **语法**：`<Path>.ProductAmount:real`
- **赋值类型**：`real`
- **说明**：设置 Mixer 通过混合成分所生产的中间产品或最终产品的数量，单位为升。默认值 `-1` 表示最终产品完全利用 Mixer 的体积。
- **注意**：
  - 若产品数量与 MaterialsTable 中填入的产品数量不同，Plant Simulation 会相应调整各成分的数量，以保持成分比例不变。
  - 若在 MaterialsTable 的 Product Amount 列中指定 `-1`，则 Plant Simulation 将所有成分之和作为 Product Amount；仅当混合会改变体积时才需显式指定。

### RecoveryTime [SimTalk] - Mixer
- **类型**：属性（Attribute）
- **语法**：`<Path>.RecoveryTime:time`
- **赋值类型**：`time`
- **说明**：设置 Mixer 的恢复时间，即冲洗、清洁 Mixer 并为下一流程做准备所需的时间。指定 `0` 可让材料持续进入。

### Volume [SimTalk] - Mixer
- **类型**：属性（Attribute）
- **语法**：`<Path>.Volume:real`
- **赋值类型**：`real`
- **说明**：设置 Mixer 混合容器中可供成分或产品使用的体积。

## 相关对象：ContinuousMixer

ContinuousMixer（连续混合器）用于通过混合将流程中的成分转化为中间产品或最终产品。成分可同时从多个上游流体对象流入。ContinuousMixer 仅在 MaterialsTable 中定义了产品与成分信息后才会处理流体。

## 本目录文件说明

- `attributes.md` — Mixer 属性的 Markdown 格式文档。
- `attributes.txtx` — Mixer 属性的纯文本格式文档（内容与 `attributes.md` 一致）。
