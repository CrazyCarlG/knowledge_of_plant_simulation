# DePortioner — Attributes（属性）

本目录汇总了 Plant Simulation 中 **DePortioner（分配器）** 对象的属性（Attributes）文档。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `attributes.md` | 主文档，包含属性概述以及各属性的完整描述 |
| `attributes.txtx` | 同内容的文本格式来源（Siemens 帮助文档导出的原始文本） |

> 注：本目录无子文件夹，因此没有子目录的 README.md 可汇总。

## 内容摘要

### 概述（Overview）

DePortioner 提供：

- 左侧目录表中列出的属性；
- _Attributes of the Fluid Objects（流体对象的属性）；
- _Attributes of All Objects（所有对象的属性）。

查看对象全部方法、只读属性与属性的方式：

- 在类库（Class Library）上下文菜单中选择 **Show Attributes and Methods** 查看所选类；
- 按 **F8** 或点击 Frame 的 Home 功能区 **Show Attributes and Methods** 查看所选实例。

设置与获取属性值既可通过对话框（复选框、文本框、下拉列表），也可通过为相应属性赋值：

- 设置值，例如：`MyDePortioner.AmountPerMU := 10`
- 获取值，例如：`print MyDePortioner.AmountPerMU` 或 `posit := MyStation.Cont.XPos`

### 属性（Attributes）

#### CurrentAmount [SimTalk] — 只读属性

返回 `<Path>` 指定的 DePortioner 中当前流体的量。

- **类型**：只读属性（Read-only attribute）
- **语法**：`<Path>.CurrentAmount → real`
- **返回值**：数据类型 `real`，单位为升（liters）
- **示例**：`print MyDePortioner.CurrentAmount`

#### AmountPerMU [SimTalk]

设置 DePortioner 生成的物料总量（升）。仅当 *Fluid Depends On* 选择 **Fixed** 时适用。

- **类型**：属性
- **语法**：`<Path>.AmountPerMU:real`
- **赋值**：`real`
- **示例**：`MyDePortioner.AmountPerMU := 20`

#### AttrNameAmount [SimTalk]

设置用户自定义 **数量属性（Amount Attribute）** 的名称，用于定义 DePortioner 生成的流体数量。仅当 `FluidDependsOn` 选择 **MU Attribute** 时适用。

- **类型**：属性
- **语法**：`<Path>.AttrNameAmount:string`
- **赋值**：`string`
- **示例**：`MyDePortioner.AttrNameAmount := "Amount"`

#### AttrNameMaterial [SimTalk]

设置用户自定义 **物料属性（Material Attribute）** 的名称，用于定义 DePortioner 生成的流体物料。仅当 `FluidDependsOn` 选择 **MU Attribute** 时适用。

- **类型**：属性
- **语法**：`<Path>.AttrNameMaterial:string`
- **赋值**：`string`
- **示例**：`MyDePortioner.AttrNameMaterial := "Material"`

#### FluidDependsOn [SimTalk]

设置 DePortioner 如何定义待生成流体的物料与数量。

- 每个待使用的物料名称都必须在 `MaterialsTable` 中定义。
- 可选值：
  - `"Fixed"`：在 *Material*（`Material`）与 *Amount per MU*（`AmountPerMU`）中设置物料与每 MU 数量。
  - `"MU Name"`：在 *Mapping Table*（`MappingTable`）中设置物料与每 MU 数量。
  - `"MU Attribute"`：在 *Material Attribute*（`AttrNameMaterial`）与 *Amount Attribute*（`AttrNameAmount`）中设置物料与每 MU 数量；这些为需自行创建的 MU 用户自定义属性。
- **类型**：属性
- **语法**：`<Path>.FluidDependsOn:string`
- **赋值**：`string`
- **示例**：`MyDePortioner.FluidDependsOn := "Fixed"`

#### MappingTable [SimTalk]

设置数据表名称，该表包含到达 MU 的 MU Name、物料以及 DePortioner 生成的流体数量。仅当 `FluidDependsOn` 选择 **MU Name** 时适用。

- **类型**：属性
- **语法**：`<Path>.MappingTable:path`
- **赋值**：`path`
- **示例**：`MyDePortioner.MappingTable := MyMappingTable`

#### Material [SimTalk]

设置 DePortioner 生成的物料名称。仅当 `FluidDependsOn` 选择 **Fixed** 时适用。

- **类型**：属性
- **语法**：`<Path>.Material:string`
- **赋值**：`string`
- **示例**：`MyDePortioner.Material := "StandardMaterial"`

#### MaterialsTable [SimTalk]

设置 MaterialsTable，其中包含 DePortioner 可生成的各种物料数据。

- **类型**：属性
- **语法**：`<Path>.MaterialsTable:path`
- **赋值**：`path`
- **示例**：`MyDePortioner.MaterialsTable := MyMaterialsTable`

#### OutflowRate [SimTalk]

设置流体流出 DePortioner 的出流速率（升/秒）。

- 物料随后经 `Pipe` 类型的对象流向物料流中的下一对象。
- **注意**：当前出流速率取决于所连接的 Pipe 数量——连接两条 Pipe 时，每条 Pipe 都按该速率流出（前提是连接 Pipe 的出流速率允许）。若只想让指定量流出对象，则连接一条 Pipe，之后再拆分。
- **类型**：属性
- **语法**：`<Path>.OutflowRate:real`
- **赋值**：`real`
- **示例**：`MyDePortioner.OutflowRate := 1`

#### RecoveryTime [SimTalk]

设置 DePortioner 的恢复时间（Recovery Time）时长。

- 恢复时间指倒空并清洗 DePortioner、为下一流程做准备所需的时间；在此期间，MU 离开对象后不会再接收物料。
- 指定 `0` 可让物料持续进入。
- **类型**：属性
- **语法**：`<Path>.RecoveryTime:time`
- **赋值**：`time`
- **示例**：`MyDePortioner.RecoveryTime := 1:00:00`
