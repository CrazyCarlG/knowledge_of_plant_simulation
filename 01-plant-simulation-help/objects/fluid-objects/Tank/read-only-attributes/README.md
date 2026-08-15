# Read-Only Attributes of the Tank

本目录汇总了 Plant Simulation 中 **Tank（流体对象/罐体）** 的只读属性（Read-Only Attributes）文档。

## 目录内容说明

| 文件 | 说明 |
| --- | --- |
| `read-only-attributes.md` | Tank 只读属性的 Markdown 文档（主文档） |
| `read-only-attributes.txtx` | 同一内容的纯文本提取版本 |

本目录不包含子文件夹，因此没有子目录下的 README.md 需要合并。

## 文档内容概要

Tank 提供以下只读属性分组：

- **General Read-Only Attributes of the Tank**（Tank 的通用只读属性）
- **Read-Only Attributes of the Sensors of the Tank**（Tank 传感器的只读属性）
- **Read-Only Attributes of the Fluid Objects**（流体对象的只读属性）
- **Read-Only Attributes of All Objects**（所有对象的只读属性）

只读属性可以查询其值，但**不能设置**——Plant Simulation 会在你查询的时间点计算该值。在大多数情况下，只读属性对应对象某个选项卡（如 **Statistics** 选项卡）上不可用的对话框条目。

查看对象所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口。查询只读属性值示例：

```simtalk
print Tank.Full
```

---

## General Read-Only Attributes of the Tank

### CurrentAmount
返回由 `<Path>` 指定的 Tank 中材料的 **Current Amount（当前量）**。

- **类型：** 只读属性
- **语法：** `<Path>.CurrentAmount → real`
- **返回值：** `real`，单位为升（liters）

```simtalk
print MyTank.CurrentAmount
```

**参见：** Current Amount [Tank]

### CurrentFillLevel
返回由 `<Path>` 指定的 Tank 中材料的 **Current Fill Level（当前液位）**。

- **类型：** 只读属性
- **语法：** `<Path>.CurrentFillLevel → real`
- **返回值：** `real`，单位为百分比（percent）

```simtalk
print MyTank.CurrentFillLevel
```

**参见：** Current Fill Level [Tank]

### CurrentMaterial
返回由 `<Path>` 指定的 Tank 中的 **Current Material（当前材料）**。

> **备注：** Tank 在任意时刻只能容纳一种材料。在 Tank 排空之前，新材料的流入会被阻止，因此必须先排空 Tank 才能让另一种材料流入。
>
> **注意：** 名称不区分大小写（与对象的属性和方法名一样）。为节省内存并提高访问速度，所有使用此类不区分大小写字符串的位置都指向主内存中的同一个字符串。可见且意外的结果是，字符串的首次出现决定了其大小写写法。在 SimTalk 中可使用 `~=` 运算符对字符串进行不区分大小写的比较。

- **类型：** 只读属性（可监视 / watchable）
- **语法：** `<Path>.CurrentMaterial → string`
- **返回值：** `string`

```simtalk
print MyTank.CurrentMaterial
```

**参见：** Current Material [Tank], Relational Operators

### Empty
返回由 `<Path>` 指定的 Tank 是否为 **Empty（空）**（`true`）或非空（`false`）。

- **类型：** 只读属性（可监视 / watchable）
- **语法：** `<Path>.Empty → boolean`
- **返回值：** `boolean`

```simtalk
print MyTank.Empty
```

### Full
返回由 `<Path>` 指定的 Tank 是否为 **Full（满）**（`true`）或非满（`false`）。

- **类型：** 只读属性（可监视 / watchable）
- **语法：** `<Path>.Full → boolean`
- **返回值：** `boolean`

```simtalk
print MyTank.Full
```

### StatRelativeOccupation
返回由 `<Path>` 指定的 Tank 的 **Relative Occupancy（相对占用率）**。

- **类型：** 只读属性
- **语法：** `<Path>.StatRelativeOccupation → real`
- **返回值：** `real`

```simtalk
print MyTank.StatRelativeOccupation
```

**参见：** Tab Statistics [Tank]

### StatThroughput
返回 **Throughput（吞吐量）**，即流经由 `<Path>` 指定的 Tank 的材料量。

- **类型：** 只读属性
- **语法：** `<Path>.StatThroughput → real`
- **返回值：** `real`，单位为升（liters）

```simtalk
print MyTank.StatThroughput
```

**参见：** Tab Statistics [Tank]

---

## Read-Only Attributes of the Sensors of the Tank

### ID
返回由 `<Path>` 指定的 Tank 某个传感器的唯一标识符，用于访问该传感器。

- **类型：** 只读属性
- **语法：** `<Path>.Sensor.ID → integer`
- **返回值：** `integer`

```simtalk
// 删除所有在材料量超过传感器位置时被触发的传感器
for i := MyTank.numSensors downto 1
   if MyTank.sensorNo(i).Exceeded = true
      sensorID := MyTank.sensorNo(i).ID
      MyTank.deleteSensor(sensorID)
   end
next
```

**参见：** Sensors [Tank]

### NumSensors
返回由 `<Path>` 指定的 Tank 已定义的传感器数量。

- **类型：** 只读属性
- **语法：** `<Path>.NumSensors → integer`
- **返回值：** `integer`

```simtalk
print MyTank.NumSensors
```

**参见：** Sensors [Tank]

### Origin
返回由 `<Path>` 指定的 Tank 传感器的来源（origin）。

- **类型：** 只读属性
- **语法：** `<Path>.Sensor.Origin → integer`
- **返回值：** `integer`；如果传感器没有来源，则返回 `VOID`

```simtalk
print MyTank.Sensors.id1.Origin
```

**参见：** Sensors [Tank]

---

## Related Methods

### sensors.ID
返回由 `<Path>` 指定的 Tank 的指定传感器。

- **类型：** 方法（Method）
- **语法：** `<Path>.sensors.ID(<Number>) → any`
- **返回值：** `any`；ID 后面的数字指定了 Plant Simulation 在创建该传感器时分配的唯一标识符。

```simtalk
MyTank.sensors.ID3.Front := true

var sensor := MyTank.sensors.ID2
sensor.Front := true
```

**参见：** Sensors [Tank], New [sensor]
