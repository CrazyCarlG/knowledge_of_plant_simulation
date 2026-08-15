# Tank 的方法（Methods of the Tank）

本目录汇总了 Plant Simulation 中 **Tank（储罐）** 对象的方法说明，内容源自 `methods.md`（原始帮助文本见 `methods.txtx`）。

## 概述

Tank 提供以下几组方法：

- **Tank 的通用方法（General Methods of the Tank）**
- **Tank 的传感器方法（Methods of the Sensors of the Tank）**
- **流体对象的方法（Methods of the Fluid Objects）**
- **所有对象的方法（Methods of All Objects）**

> 查看对象的所有方法、只读属性和属性：在类库的上下文菜单中选择 **Show Attributes and Methods**，或选中实例后按 **F8** / 点击 Home 选项卡上的 **Show Attributes and Methods**。

### 语法行示例

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` 表示方法所作用对象的路径。
- 括号内为方法签名（标识符 + 各参数的数据类型），如 `(Parameter:string)`。
- 方括号内为可选参数，如 `[,Parameter:boolean]`。
- 默认值写在参数后，如 `:= false`。
- 返回值的类型写在箭头 `→` 后，如 `→ boolean`。

> **注意**：表达式内的括号 `(…)` 必须输入，否则可能产生意外结果并打开调试器（Debugger）。

---

## 通用方法（General Methods）

### setCurrentContent

设置 `<Path>` 所指定 Tank 中材料的当前量（Current Amount）。

- **类型**：Method
- **语法**：

```
<Path>.setCurrentContent(Amount:real[, Material:string, MaterialsTable:path])
```

**参数**：

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| `Amount` | real | 材料数量 |
| `Material` | string（可选） | 材料本身 |
| `MaterialsTable` | path（可选） | MaterialsTable 的路径 |

**备注**：新内容会替换之前的内容。通常用该方法设置对象的初始状态。

**注意**：若 Tank 已含有某种材料，只需输入新的 `Amount` 单个参数；否则还需指定 `Material` 和 `MaterialsTable`。

**示例**：

```simtalk
Tank1.setCurrentContent(3, "MyProduct", .Fluids.MaterialsTable)
MyTank.setCurrentContent(5) -- MyTank already contains a material
```

---

## 传感器方法（Methods of the Sensors）

Tank 提供以下传感器方法：`createSensor`、`deleteSensor`、`existsSensorID`、`sensorID`、`sensorNo`、`sensors.ID`。

### createSensor

为 `<Path>` 指定的 Tank 创建一个新传感器。

- **类型**：Method
- **语法**：

```
<Path>.createSensor([Position:real, Control:method, Exceeded:boolean, Underrun:boolean, PositionType:string]) → integer
```

**参数**（用于定义传感器）：

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| `Position` | real（可选） | 相对位置 |
| `Control` | method（可选） | 传感器触发的方法对象名称，可为字符串 `"myMethod"` 或 `&myMethod` |
| `Exceeded` | boolean（可选） | 材料量超过传感器位置（位于上方）时是否触发 |
| `Underrun` | boolean（可选） | 材料量低于传感器位置（位于下方）时是否触发 |
| `PositionType` | string（可选） | 位置类型：`Relative` 或 `Absolute` |

**返回值**：`integer` — 传感器的唯一编号，可用于访问该传感器。

**示例**：

```simtalk
var ID1,ID2: integer
ID1 := MyTank.createSensor(0.5,"SensorCtrl",true,false)
ID2 := MyTank.createSensor(0.7,&myMethod,false,true)
ID3 := MyTank.createSensor(3,"SensorCtrl",true,false,"absolute")
```

### deleteSensor

删除 `<Path>` 指定的 Tank 中的指定传感器。

- **类型**：Method
- **语法**：`<Path>.deleteSensor(SensorID:integer)`
- **参数**：`SensorID`（integer）— 指定 SensorID。
- **示例**：`MyTank.deleteSensor(2)`

### existsSensorID

返回指定传感器在 `<Path>` 指定的 Tank 中是否存在（`true`）或不存在（`false`）。

- **类型**：Method
- **语法**：`<Path>.existsSensorID(SensorID:integer) → boolean`
- **参数**：`SensorID`（integer）— 指定 SensorID。
- **返回值**：`boolean`。
- **示例**：`print MyTank.existsSensorID(2)`

### sensorID

返回 `<Path>` 指定的 Tank 中指定编号的传感器。

- **类型**：Method
- **语法**：`<Path>.sensorID(SensorID:integer) → any`
- **参数**：`SensorID`（integer）— 创建传感器时 Plant Simulation 分配的唯一 Sensor-ID。
- **返回值**：`any`。
- **备注**：`sensorNo(SensorID:integer)` 与 `sensorID(SensorID:integer)` 可能引用不同的传感器。

**示例**：

```simtalk
MyTank.SensorID(3).Exceeded := true
if MyTank.SensorID(3).Exceeded = true then
   ?.EntranceLocked := true
end
```

### sensorNo

返回 `<Path>` 指定的 Tank 中一个传感器（当你不知道其唯一标识符时使用）。

- **类型**：Method
- **语法**：`<Path>.sensorNo(SensorNumber:integer) → object`
- **参数**：`SensorNumber`（integer）— 取值在 1 到传感器数量之间。Plant Simulation 返回哪个传感器可能在仿真过程中变化（例如删除了现有传感器时）。因此仅当方法调用需要遍历对象的所有传感器时才使用 `sensorNo`。
- **返回值**：`object`。
- **备注**：`sensorNo` 与 `sensorID` 可能引用不同的传感器。

**示例**：`MyTank.sensorNo(1).Underrun := true`

### sensors.ID

返回 `<Path>` 指定的 Tank 中指定编号的传感器。

- **类型**：Method
- **语法**：`<Path>.sensors.ID(<Number>) → any`
- **返回值**：`any`。ID 后面的数字表示创建传感器时 Plant Simulation 分配的唯一标识符。

**示例**：

```simtalk
MyTank.sensors.ID3.Front := true
var sensor := MyTank.sensors.ID2
sensor.Front := true
```

---

## 只读属性（Read-Only Attributes）

Tank 提供只读属性，包括 `sensors.ID`。

---

## 方法速查表

| 方法 | 语法 | 返回值 | 说明 |
| --- | --- | --- | --- |
| `setCurrentContent` | `<Path>.setCurrentContent(Amount:real[, Material:string, MaterialsTable:path])` | — | 设置材料当前量 |
| `createSensor` | `<Path>.createSensor([...])` | integer | 创建新传感器 |
| `deleteSensor` | `<Path>.deleteSensor(SensorID:integer)` | — | 删除传感器 |
| `existsSensorID` | `<Path>.existsSensorID(SensorID:integer)` | boolean | 传感器是否存在 |
| `sensorID` | `<Path>.sensorID(SensorID:integer)` | any | 按唯一 ID 返回传感器 |
| `sensorNo` | `<Path>.sensorNo(SensorNumber:integer)` | object | 按序号返回传感器 |
| `sensors.ID` | `<Path>.sensors.ID(<Number>)` | any | 按 ID 返回传感器 |
