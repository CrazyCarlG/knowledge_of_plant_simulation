# Factory51 建模思路

> 模型来源：`02-offcial-psfm-model/Factory51/Factory51.psfm`
> 分析依据：`Models/Factory51/**` 各对象 `.yaml` 的 `$CustomAttributes`/`$Failures`/`ProcTime`/`EntranceCtrl`/`ExitCtrl` 等字段，以及 Method 的 `Program` 源码；`UserObjects/**` 自定义类定义。

---

## 一、模型定位与目标

Factory51 是一个**离散事件制造 + 仓储物流的一体化演示模型**，模拟一个从原材料进货、高架立体仓库（HBW）暂存、双生产线加工（机加工 → 抛光 → 喷漆 → 烘干 → 后处理 → 质检）到成品仓储与出货的完整工厂。

它要回答/展示的核心问题与关键绩效指标（KPI）：

| 关注点 | 对应指标 / 对象 |
| --- | --- |
| 生产节拍 / 吞吐量 | `TPH`（每小时产出）、`PlatesInProduction`（在制品板件数） |
| 设备利用率与故障影响 | `Milling` 等 Station 的 `$Failures`（故障间隔/时长分布）、`ResStatOn` |
| 库存水平 | `StorageArea`（Store）、WMS `Inventory`、RackLane `OccupancyLeft/Right`、`NumFreePlaces`/`NumOccupiedPlaces` |
| 物流效率 / 等待 | `TrucksMissed`（错过卡车数）、`TrucksArrived`、AGV/叉车路径 |
| 成本分析 | `CostAnalyzer`、`Milling.InvestmentCosts`、`OperatingCosts`、`Part.MaterialCostsPerPiece` |

一句话概括：**用"类库 + 参数化 + 拉式分流 + 资源协作"的方式，演示一个可配置的双产品、双生产线、带立体仓库和 AGV 物流的制造系统。**

---

## 二、建模方法与建模范式

### 2.1 建模范式（Paradigm）

- **推拉结合（Push + Pull）**：
  - **Push（推式）**：`Source`、`TruckArrivals` 按到达间隔/数量主动生成 MU，推入下游（如 Source → 传送网）。
  - **Pull（拉式）**：`StoreExit.Init` 用 `stopuntil not StorageArea.Empty ... StorageArea.&removeProductTo` 在需要时从仓库"拉"产品；`Production/Line.OnExit` 根据下游 `Polishing1.Polishing.Empty` 决定去向——下游空才走抛光，体现按下游状态拉料。
- **组件化/类继承建模**：一条 `Production` 类定义两条生产线 P1、P2（`Origin=Production`）；工序单元（Painting/PolishingCell/PostProcess/Drying）做成 Frame 类再派生多份同构实例（Polishing1..3、PostProcess1..3）。
- **外部库复用（Library Reuse）**：立体仓库直接引用 `HBW3D`（RackLane/WMS）与 `CranesAndMore`（MultiPortalCrane/StorageArea）库，WMS 逻辑（placeIntoStock、reserveBox 等）继承自库（派生 Method 无 Program，`Origin` 指向库内方法）。
- **资源协作建模**：`Workplace` + `WorkerPool` + `Broker`（`root.Broker`）表达工人资源协作；`Milling` 的 `$ProcImp.BrokerPath = root.Broker` 绑定经纪人调度。
- **实时/演示导向**：`EventController.Realtime=true`、`RealtimeScale=3`、`StartDate=2016-1-4 6:00`，配合 3D 动画（`Milling` 的 `TurnPlate`/`FrontDoor`/`Tool` 姿态动画）用于实时可视化演示。

### 2.2 对象选型逻辑（为什么用 X 而不是 Y）

| 选型 | 理由（基于文件证据） |
| --- | --- |
| 用 `Station`（Milling/Polishing/PostProcess）而非 `ParallelStation` | 单工位单件加工，`Capacity=1`、`ProcTime=8/13/5`，且需要故障/成本/3D 动画/工人服务，Station 足够 |
| 用 `Buffer`（StoreEntry/StoreExit）而非 `Store` 做线边暂存 | `StoreEntry`/`StoreExit` 容量小（StoreExit `Capacity=1`）、`ProcTime=2`，仅作交接缓冲；大容量存储用 `StorageArea`（Store） |
| 用 `Conveyor`（Line 系列）做主线 | 传送带 `Accumulating=true`、`Speed=1`、`Length` 可调，适合连续流；`Line` 类挂 `ExitCtrl` 实现分流 |
| 用 `Converter`/`AngularConverter` 做分合流/转向 | 生产网中 73 个 Converter + 26 个 AngularConverter，构建传送网的拓扑分支与转向 |
| 用自定义 Frame 类（Production 等） | 实现"一条线定义、多实例复用"，避免 P1/P2 重复建模 |
| 用 `PickAndPlace` 做产品分流/上下料 | `PickAndPlaceAubergine`/`PickAndPlaceStrawberry` 按产品类型拾取分流 |
| 用 `Store` + `Track` 堆垛机做立体仓库 | `StorageArea`（Store）+ `MultiPortalCrane`（Track）实现 HBW 存取 |
| 用 `Interface` 做跨 Frame 边界 | P1/P2 的 `PartEntrance`/`BoxEntrance`/`AGV_Entrance`/`AGV_Exit`、Warehouse 的 `Entry`/`Exit` 明确 Frame 进出边界 |

### 2.3 关键参数来源

| 参数 | 来源 | 说明 |
| --- | --- | --- |
| 加工时间 `ProcTime` | 常量 | Milling=8、Polishing=13、PostProcessStation=5、StoreExit=2 |
| 卡车到达间隔 `Interval` | 概率分布 | TruckArrivals `[Normal,15:00,4:00,2:00,30:00]`（均值 15 分钟，σ 4 分钟） |
| 故障间隔 / 时长 | 概率分布 | Milling `$Failures`：间隔 `[Negexp,3:22.22]`、时长 `[Erlang,20,14.14]` |
| 源生产数量 `Number` | 常量 | Source `Number=120`（两产品各半） |
| 初始 AGV 数 `NumAGVs` | 变量 | Production/Init 按 `NumAGVs` 创建 AGV |
| 成本数据 | 常量 | Milling `InvestmentCosts=25000`、`OperatingCosts=3000`；Part `MaterialCostsPerPiece=3` |
| 仿真时钟 | 常量 | EventController `StartDate=2016-1-4 6:00`、`RealtimeScale=3` |

---

## 三、控制逻辑梳理

> 按"触发时机 → 触发条件 → 执行动作 → 产生影响"结构描述，并给出关键生命周期方法。

### 3.1 进货：卡车到达与卸货

**TruckArrivals（Source）— OnEntrance**
- 触发时机：卡车源按 `Interval` 生成卡车 MU 时。
- 触发条件：`if SupplyRoad.NumMU > 1`（道路上已有 >1 辆等待卡车）。
- 执行动作：条件成立 → `TrucksMissed += 1`、`@.delete`、`return`（拒绝进入，限流）；否则 → 创建 Truck，内装 `Pallet → Box → Part`（每托盘容量 `palette.Capacity`，每箱容量 `container.Capacity`）。
- 产生影响：限制等待卡车数量，统计 `TrucksMissed`；生成满载零件卡车进入 `SupplyRoad`。

**UnloadTruck（Method）**
```
param CurrentTruck:object
TrucksArrived += 1
var forklift := AGVPool.Cont          // 从 AGV 池取叉车
while not CurrentTruck.Empty
    forklift.Backwards := true
    forklift.setRoute([M_RoadTurn, M_Road])
    forklift.moveFork(0.4)
    waituntil forklift.DestinationWasReached
    ...
    CurrentTruck.Cont.move(forklift)   // 叉车搬运到 StoreEntry
    ...
end
CurrentTruck.Stopped := false
```
- 触发时机：卡车到达卸货点。
- 触发条件：`not CurrentTruck.Empty`（卡车仍有货物）。
- 执行动作：叉车沿标记点往返 `M_RoadTurn → M_Road → M_Truck`，`moveFork` 调整叉臂，`move` 搬运 MU 到 `StoreEntry`。
- 产生影响：货物从卡车转移到入库缓冲，叉车被占用/释放。

### 3.2 入库与立体仓库

- `StoreEntry（Buffer）` 的 `ExitCtrl = StorageArea.storing`：MU 离开 StoreEntry 时，触发 `StorageArea.storing`（CranesAndMore Store 的入库方法），由 `MultiPortalCrane`/`SmallCrane` 堆垛机存入 `StorageArea`。
- `StorageArea（Store）`：`StoreType=Floorspace`，`XDim/YDim/ZDim=4/5/2`，维护 `Content`/`Layout` 数据表，记录 `StoreEntrance`/`StoreExit`/`crane` 引用。

### 3.3 出库与配送（拉式）

**StoreExit（Buffer）— Init**
```
while true
    stopuntil not StorageArea.Empty and self.~.Empty
    StorageArea.&removeProductTo.executeNewCallChain(1, @)   // 从仓库拉一个产品
    stopuntil self.~.Full
end
```
- 触发时机：仿真初始化后循环执行。
- 触发条件：仓库非空且自身空。
- 执行动作：调用 `StorageArea.removeProductTo` 把产品拉入 StoreExit。
- 产生影响：实现"需要时才取"的拉式补料。

**StoreExit — OnExit**
```
self.~.&Unload.executeNewCallChain(1, PickAndPlaceTop, @, ?)
self.~.&Unload.executeNewCallChain(2, PickAndPlaceBottom, @, ?)
stopuntil @.Empty
wait 4
@.delete
```
- 触发时机：MU 离开 StoreExit。
- 执行动作：并行调用 `Unload` 方法（`executeNewCallChain` 并发），把箱体分发给上下两个 `PickAndPlace`（Top/Bottom）。
- 产生影响：箱体分发到生产线入口，空托盘等待后删除。

**StoreExit — Unload**
```
param ypos:integer, target:object
for var i := 1 to 2
    box := @[2, ypos].cont ; box.move(target) ; stopuntil box.Location /= @
    box := @[1, ypos].cont ; box.move(target) ; stopuntil box.Location /= @
next
```
- 执行动作：按坐标 `[行, 列]` 从托盘取箱体 `move` 到目标 `PickAndPlace`。

### 3.4 生产线内部（P1/P2）

**Production/Init（Method）**
```
var startPos:length := 12
for var i := 1 to NumAGVs
    var agv := .UserObjects.MUs.AGV.create(Track, startPos)
    startPos -= agv.Length + 0.1
next
```
- 触发时机：Production Frame 初始化。
- 执行动作：按 `NumAGVs` 在 `Track` 上等间距创建 AGV。
- 产生影响：初始化线内 AGV 车队。

**Production/Line（Conveyor）— OnExit（分流核心）**
```
PlatesInProduction += 1
if Polishing1.Polishing.Empty
    @.move(2)   // 抛光站空 → 走抛光分支
else
    @.move(1)   // 抛光站忙 → 走其它分支
end
```
- 触发时机：板件离开主线传送带。
- 触发条件：`Polishing1.Polishing.Empty`（下游抛光站是否为空）。
- 执行动作：`@.move(n)` 选择后继出口。
- 产生影响：按下游状态动态分流（拉式），并累计在制品数。

**Milling（Station）— OnEntrance / OnExit（3D 动画 + 加工）**
```
// OnEntrance
var poses := ?._3D.Poses
poses.moveTo("DoorClosed")
waituntil poses.EndPoseWasReached
?.startProcessing
if ?._3D.ExistsWithAnimation
    ?._3D.getObject("Tool").SelfAnimations.Work.play
    ?._3D.getObject("TurnPlate").SelfAnimations.playRotation(0, 360, 360/?.procTime)
end
// OnExit（分支：forward blocking / rear / 正常出料）
... poses.moveTo("DoorOpen") ... @._3D.VisibleGraphicGroups := ["Milled"] ... @.move
```
- 触发时机：MU 进入/离开 Milling。
- 执行动作：关门 → 开始加工 → 播放刀具/转台动画；出料时开门 → 设置图形组 `Milled` → 移动。
- 产生影响：加工可视化 + 状态着色（`VisibleGraphicGroups` 切换零件外观）。

### 3.5 成品入库与 WMS

- 生产线成品经 AGV（沿 `Track`）送往 `Warehouse/WMS`。
- `WMS` 继承 HBW3D 库逻辑：`placeIntoStock`/`getFreePlace`/`reserveBox`/`removeProduct`/`autoRemove` 等 Method 由库提供（派生 Method 无 Program，`Origin` 指向库内方法）。
- `RackLane1..5`：每个巷道含 `IN`/`OUT`/`MainEntrance`/`SideEntrance` 接口、`RackLeft`/`RackRight` 货架、`RSU` 巷道堆垛机，及 `NumberOfRows/Columns`、`OccupancyLeft/Right` 等参数变量。
- 成品最终从 `Shipment1..3`（Drain）或 `TruckDepartures`（Drain）离开系统。

### 3.6 生命周期方法（init / endSim / reset）

| 生命周期 | 对象/方法 | 职责 |
| --- | --- | --- |
| init | `TruckArrivals.Init` | `self.~.Path.create(self.~)` 创建卡车路径 |
| init | `Production/Init` | 创建 AGV 车队 |
| init | `StoreExit.Init` | 启动拉式补料循环 |
| reset | `Milling.Reset`（`$CustomAttributes`） | `self.~.IsAvailable := true` 复位可用标志 |
| reset/统计 | 各 `Variable`（TrucksArrived/Missed、PlatesInProduction、ChargeCount 等） | 累计统计量 |

> 注：模型中未显式看到独立的 `endSim` Method（文件未体现），仿真结束统计可能依赖 `HtmlReport`、`CostAnalyzer`、`SankeyDiagram` 等内置报告对象自动汇总。

---

## 四、建模亮点与可复用模式

### 4.1 值得借鉴的建模模式

1. **类继承 + 组件化生产线**：`Production` 一个类定义两条线，工序单元（Painting/Polishing/PostProcess/Drying）再做 Frame 类并派生多份同构实例。这是最核心的可复用模式——"定义一次，实例化多次"。
2. **外部库复用**：立体仓库/堆垛机直接引用 `HBW3D`、`CranesAndMore` 成熟库，WMS 全部逻辑继承自库，避免重复造轮子。
3. **拉式分流**：`Production/Line.OnExit` 用 `@.move(n)` 按下游空满动态选路，是典型的 Pull 控制；`StoreExit.Init` 的 `stopuntil ... removeProductTo` 是拉式补料范本。
4. **`executeNewCallChain` 并行委托**：StoreExit.OnExit 用该方法并发启动两个 Unload 分支（上/下 PickAndPlace），体现 SimTalk 并行调用技巧。
5. **叉车/AGV 路径点导航**：`UnloadTruck` 用 `setRoute([M_RoadTurn, M_Road, M_Truck])` + `moveFork` + `waituntil DestinationWasReached`，是资源小车点对点搬运的清晰范式。
6. **3D 动画与加工耦合**：`Milling.OnEntrance/OnExit` 通过 `?_3D.Poses`、`SelfAnimations.play`、`playRotation` 把姿态/动画与加工状态联动，并切换 `VisibleGraphicGroups` 呈现零件加工状态。
7. **故障与成本建模**：`Milling.$Failures`（Negexp 间隔 + Erlang 时长）、`CostAnalyzer` + `InvestmentCosts`/`OperatingCosts`/`MaterialCostsPerPiece` 让模型具备可用性/成本分析能力。

### 4.2 可能的简化假设 / 局限

- **加工时间为常量**（Milling=8、Polishing=13、PostProcessStation=5），未用分布表达波动（除故障/到达间隔外）。
- **产品仅两类**（Aubergine / Strawberry），通过 Source.OnEntrance 的颜色与数量对半区分，产品差异集中在颜色/图形，未体现更复杂的工艺路径差异（推测：为演示简洁而简化）。
- **WMS 逻辑依赖外部 HBW3D 库**，库内方法体不在本模型文件中（派生 Method 无 Program），逆向时无法在本文件内读到完整仓储算法。
- **班次日历（ShiftCalendar）未显式使用**：模型中虽有 WorkerPool/Workplace/Broker 资源对象，但 `Milling.ShiftcalendarObject` 为空、`$ModelInfo` 中 `TimeScale` 为默认，未见明确的排班表（文件未体现换班逻辑）。
- **P2 与 P1 完全同构**，两条线之间是否独立、共享何种资源（如共用工人池/AGV）未在本文件明确体现。
