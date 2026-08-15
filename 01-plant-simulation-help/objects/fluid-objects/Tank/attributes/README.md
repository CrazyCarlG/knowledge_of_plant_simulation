# Tank Attributes — 摘要

本目录包含 Tank（流体对象）的属性说明，来源文件为 `attributes.md`。

Tank 提供以下属性：

- Tank 的通用属性（General Attributes）
- Tank 传感器的属性（Attributes of the Sensors）
- 流体对象的属性（Attributes of the Fluid Objects）
- 所有对象的属性（Attributes of All Objects）

属性值可通过对话框（复选框、文本框、下拉列表）或直接赋值来设置与获取。例如：

```simtalk
MyTank.OutflowRate := 1        -- 设置属性值
print MyTank.OutflowRate       -- 获取属性值
```

## Tank 通用属性

| 属性 | 类型 | 语法 | 说明 |
| --- | --- | --- | --- |
| **Origin** | 只读属性 | `<Path>.Sensor.Origin → integer` | 返回 `<Path>` 指定传感器在 Tank 上的原点位置；无原点时返回 `VOID`。 |
| **OutflowRate** | 属性 | `<Path>.OutflowRate:real` | 设置 Tank 所存储材料的流出速率（升/秒）。 |
| **Volume** | 属性 | `<Path>.Volume:real` | 设置 Tank 所能容纳的原料量（容积）。 |

### OutflowRate 备注
- 材料通过 Pipe 类型对象流向物料流中的下一个对象。
- 当前流出速率取决于连接的 Pipe 数量：若连接两根 Pipe，则在 Pipe 流出速率允许的情况下，指定的流出速率会流经每根 Pipe；若只想让指定量从对象流出，则连接单根 Pipe，之后再进行拆分。
- 空 Tank 的流出速率大于流入速率，或满 Tank 的流入速率大于流出速率时，Plant Simulation 会输出错误消息。应通过创建传感器并编写 Method 来处理这些情况，由传感器开闭连接的 Pipe，防止 Tank 变空或变满。

## Tank 传感器属性

Tank 的传感器相关属性如下（语法中 `<Number>` 为传感器编号 ID）。

| 属性 | 类型 | 语法 | 说明 |
| --- | --- | --- | --- |
| **Control** | 属性 | `<Path>.Sensors.ID<Number>.Control:string` | 指定传感器触发时运行的 Method 对象（引用或名称）。触发时传感器将 Sensor-ID 作为可选参数传入；另有可选布尔参数 `Exceeded` 指示传感器位置是超出还是低于。 |
| **Exceeded** | 属性 | `<Path>.Sensors.ID<Number>.Exceeded:boolean` | 设置材料量超过传感器位置（位于其上方）时是否触发传感器。 |
| **Position** | 属性 | `<Path>.Sensors.ID<Number>.Position:real` | 设置传感器在 Tank 上的位置，取值取决于 PositionType。 |
| **PositionType** | 属性 | `<Path>.Sensors.ID<Number>.PositionType:string` | 设置传感器位置类型，可为 `"absolute"` 或 `"relative"`。 |
| **Underrun** | 属性 | `<Path>.Sensors.ID<Number>.Underrun:boolean` | 设置材料量低于传感器位置（位于其下方）时是否触发传感器。 |

### Position 取值说明
- `relative`：取值范围 0 到 1（即 0% 到 100%）。
- `absolute`：取值范围 0 到所设置的 Volume。

## 使用示例

```simtalk
MyTank.OutflowRate := 1
MyTank.Volume := 10

MyTank.Sensors.ID2.Control := &mySensorCtrl
MyTank.Sensors.ID2.Control := "mySensorCtrl"

MyTank.Sensors.id1.Exceeded := true
MyTank.Sensors.id2.Position := 0.1
MyTank.Sensors.ID2.PositionType := "absolute"
MyTank.Sensors.id1.Underrun := true
```
