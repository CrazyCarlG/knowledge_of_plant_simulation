# 传输系统、AGV 与电池驱动运输车建模

> 本目录总结自 `conveyor-track-agv-battery.md`，内容来源于 Plant Simulation Help 中关于传输系统（Transport Systems）、AGV 系统以及电池驱动运输车（Battery-powered Transporters）的建模指南。

---

## 目录概览

本目录包含一个 Markdown 文件：

| 文件 | 内容 |
| --- | --- |
| `conveyor-track-agv-battery.md` | 传输系统、AGV 与电池驱动运输车建模的完整帮助文档 |

---

## 1. 建模传输系统

仿真模型中传输系统的多种用途：简单输送机、复杂电动单轨、叉车、起重机以及自动导引车（AGV）系统。核心对象位于 Class Library 的 `MaterialFlow` 文件夹：

| 对象 | 类型 | 说明 |
| --- | --- | --- |
| **Conveyor** | 主动（active） | 自带推进系统，运输无自身动力的被动零件。 |
| **Track** | 被动（passive） | 无自身动力，作为主动 **Transporter** 前进/后退的路线。 |
| **TwoLaneTrack** | 被动（passive） | 同 Track，但为双车道。 |

**关键特性：**

- 三者均为**长度导向**对象，通过 `Length` 与 `MU Length` 决定可同时容纳的 MU 数量；点导向对象（Station、ParallelStation 等）不使用长度。
- 可为其创建 **Controls** 和 **Sensors**。
- 零件从点导向对象转移到长度导向对象时是**整体转移**。
- 两个长度导向对象之间按长度导向对象对话框中输入的 **Speed** 转移。
- 简单传输用 **Conveyor**；交叉转运、AGV、起重机等用 **Track** / **TwoLaneTrack**。
- 激活 Transporter、Part、Container 的 **Automatic Routing** 可使其沿最短路径自动寻址。

---

## 2. 主动对象传输系统（Conveyor）

Conveyor 用于建模固定带式/辊式输送机，可建模：

- 两工位之间的简单输送机
- 累积式 / 非累积式传输系统
- 固定间距 / 无间距输送机
- 多重间距 / 多重节距输送机
- 带被动对象的传输系统

### 简单输送机
零件在两个加工工位 SP1、SP2 之间移动。**Speed、Length、Transport Time** 三者相互依赖：改 Speed 或 Length 会重算 Transport Time，改 Transport Time 会改 Speed。

### 累积式 / 非累积式
- **累积式**（勾选）：出口堵塞时 MU 首尾相接继续前进。
- **非累积式**（不勾选）：前面 MU 无法出口时后续 MU 全部停止并保持间距。
- 默认 `Capacity = -1` 表示无限容量，实际由输送机长度与零件长度决定。
- 累积式类似**辊式输送机**，非累积式类似**带式输送机**。

### 固定间距 / 无间距
- `MU Distance = -1`：停用间距功能。
- `MU Distance = 0`：无间距。
- **Fixed gap**：零件间距恒定（导致频繁停线）。
- **Minimum Gap**：间距不小于最小值，可避免停机。
- **Minimum Pitch** / **Pitch**：基于前件前端与后件前端的最小/固定距离。
- **Enforce MU distance** 勾选与否决定是否强制保持间距。

### 多重间距 / 多重节距
- **Multiple Gap**：间距为 MU Distance 的整数倍。
- **Multiple Pitch**：前端间距为整数倍，类似**链式输送机**。
- 可用 **EventDebugger** 逐步查看 `CheckMUDistance`、`CreateMU`、`Out` 事件。

---

## 3. 被动对象传输系统（Track）

Track/TwoLaneTrack 上的主动 **Transporter** 驱动。因 Track 被动，需：

1. 确保有 Transporter 可用；
2. 装载/卸载 Transporter；
3. **不要**用 Connector 连接前一工位与 Track（防止 MU 自动转移）。

### 创建并插入 Transporter
- 通过 **Source**：`Attributes > Time of Creation > Number Adjustable`，`Amount = 1`，选择 `MU > .MUs.Transporter`。
- 通过 SimTalk 在 `init` 方法中创建：
  ```simtalk
  .MUs.Transporter.create(Track)        // 插入 Track 末端
  .MUs.Transporter.create(Track, 5.5)   // 插入指定位置（如 5.5 m）
  ```

### 装载/卸载示例
- 无控制时 Transporter 驶到 Track 末端停止；需在 Front/Rear 出口控制中设置 `@.Backwards` 实现往返。
- 装载：`waituntil SP1.occupied and SP1.cont.finished` → `SP1.cont.move(@)` → `@.Backwards := false`。
- 卸载：等待 SP2 空 → `@.cont.move(SP2)` → `@.Backwards := true`。

---

## 4. 牵引列车（Tugger Train）

由**牵引车（tractor）**与若干**拖车（trailer）**组成。

### 定义 Tractor
1. 复制 Transporter 并重命名为 **Tractor**。
2. 勾选 **Is Tractor**。
3. 设置 `X-Dimension`/`Y-Dimension` 为 0（避免载货），对 Track/Line 装载空间设置 `Capacity = 0`。

### 创建牵引列车 Source
- 在 Frame `SourceTuggerTrains` 中用 Source 按序列表创建牵引车和拖车。
- Track 长度需容纳整车（1 拖头 + 4 拖车，各 1.5 m → 10 m）。
- 通过 Method 编程拖车碰撞挂接逻辑。

### 序列表与碰撞控制
- Source 选择 `MU Selection > Sequence`，序列表中 1 个 Tractor + 4 个 Transporter（拖车）。
- 拖车速度略快（如 1.1 m/s）使其追上前车，`CollisionCtrl` 设为挂接方法：
  ```simtalk
  if @.isTractor = false then
  @.hitchFront(@.FrontMU)
  end
  ```

### 轨道与装卸站
- 主线 + 支线（分流后回流），用 4 段 Track 与 Connector 连接。
- 装卸站使用 **TransferStation**，在 `Attributes` 标签配置零件来源、运行对象及触发传感器位置。

---

## 5. 在目的地停车（Stop the Transporter at Its Destination）

演示 Transporter 在目的地停车、等待零件、再启动。Transporter 属性在 SourceT 的 **Entrance Control** 中设置：

```simtalk
@.XDim = 1
@.YDim = 1
@.StopAtDestination = true
@.AccelerationEnabled = true
@.Acceleration = 0.2
@.Deceleration = 0.2
@.Destination = Station1
```

- Sensor1 控制：等待 Station1 有已加工完成的零件 → `station.Cont.move(@)` → 设目的地 Station2 → `@.Stopped := false`。
- Sensor2 控制：`part.move(station)` → 等待卸载完成 → 设目的地 Station1。

---

## 6. 使用自动路由（Automatic Routing）

自动路由保证零件沿最短/最快路径到达目的地。

- **Transporter 的自动路由**（Routing 标签）：沿**最短**路径寻址。
- **Part/Container 的自动路由**：沿**最快**路径寻址。

### Transporter 自动路由
- 路线网络由三条环路拼接，装卸点命名为 LoadingStation、Unload1/2/3。
- 装载控制根据 `@.ID mod 2` / `mod 3` 分配目的地，并设 `@.DestCtrl := "unload"`。
- 卸载方法 `unload`：`@.deleteMovables` → 设新目的地 LoadingStation → `@.move`。
- 3D 优化：New Standard Graphics、车道配色、显示 Captions、Tooltip、`View > Route to Destination`。

### Part/Container 自动路由
- 演示 **Pallet（Container）** 在 Conveyor 上自动寻址。
- 可通过 `Alt` 拖拽将 Track 批量替换为 Conveyor（`MyConveyor` 拖到 `MyTrack` 上）。
- 卸载站传感器选 **Only when Destination**，只有目的地匹配才触发。
- Conveyor 因带支腿需设 `Base Height = 1`。

---

## 7. 自动导引车系统（AGVS）

使用 **AGVPool** 和 **Marker** 建模 AGV 系统。AGV 从 AGVPool 出发，沿插入的标记点覆盖指定路线。

> 注意：保持 Marker **对齐**；通过 **Show Connections** 显示/隐藏 Marker。

AGV 功能：
- 沿**全向标记点（Omnidirectional Markers）**覆盖路线：`AGV.setRoute([M1,M2,M3,M4])`，用 `DestinationWasReached` 判断到达。
- 沿**方向标记点（Directional Markers）**覆盖路线：勾选 **Use Rotation of Marker**。
- 沿**方向标记点 + 指定角度**：在 3D 属性中设置旋转角度。
- 沿**段表（Segments Table）**覆盖路线：`setRouteSegments`，表列为长度、角度、半径、速度。
- 装载零件并旋转、精定位、防碰撞。

### 装载并旋转零件
- AGV 驶到 Conveyor 下方装载托盘，行驶中旋转托盘并放置到另一输送机。
- 通过可动画对象（`Plate`）与 Revolute Joint 实现旋转。

### 精定位
- 使用 `rotate` 和 `drive` 方法进行自由驾驶的精定位。

### 防碰撞
- 使用 Transporter 的 **Distance Control** 与 **Safety Zones**：后方 AGV 在对方进入安全区 2 时减速、进入安全区 1 时停止，通过后继续。

---

## 8. 电池驱动运输车（基础）

快速建模电池驱动 Transporter：Track 的 **Exit Control** 检测电量，电量充足则继续运料，不足则驶往充电站。

1. 复制 Transporter 重命名为 **TransporterBattery**。
2. 配置 **Battery** 标签。
3. 输入 **Charge Control**：
   ```simtalk
   if @.BatCharge >= @.BatCapacity
      @.Stopped := false
   end
   ```
4. Track 的 **Exit Control**：`@.BatCharge <= @.BatReserve` 则驶向 `ChargeBattery`，否则正常运输。
5. 两个传感器：一个由 TransferStation 装料，一个由 PickAndPlace 卸料到 Conveyor。
6. 充电 Track `ChargeBattery` 的传感器控制：
   ```simtalk
   @.Stopped := true
   @.BatCharging := true
   NumberOfBatteryCharges += 1
   ```

---

## 9. 电池驱动运输车（扩展）

电池相关规则：
- 电量低于 **Reserve Charge** 时必须充电。
- 运行功耗 = **Driving Consumption** + **Base Consumption**。
- 在 **Charge Control** 中防止电池完全放电停机。
- 充电需要 **Charge Current**；充电时间 =（Capacity − 当前电量）/ 充电站充电电流。
- 达到 Reserve Charge（行驶中）或 battery capacity（充电结束）时调用 Charge Control，可用 `BatCharge` 区分。

### 建模步骤
1. **建模物料流**：Source → Buffer → Track（闭环，连接首尾）→ Station → Drain；另建 `ChargingStation` 和 `ParkingPosition`；`init` 中创建两个 Transporter。
2. **编程装卸传感器控制**：sensorID=1 从 Buffer 装料到 Transporter（`repeat ... until @.Full`）；sensorID=2 从 Transporter 卸料到 Station。
3. **配置电池运行**：设置 Battery 标签、Transporter 速度 0.5 m/s、ChargingStation 的 Entrance Control 为 `startCharging`。
4. **编程电池控制**：
   - **Charge Control** `myBatteryChargeControl`：电量低则 `@.BatCharging := true` 并 `@.transfer(ChargingStation)`；充满则 `@.move(ParkingPosition)`。
   - **Entrance Control**：等待 ParkingPosition 有 MU，再将其移到 Track。

### 相对路径 vs 绝对路径
- 仅输入方法名时可能因命名空间内找不到而标红，但因 Transporter 与 Charge Control 位于同一 Frame 命名空间内，可正常使用。
- 通过对话框选择会插入**相对路径**（前缀 `~`）；选择 **Absolute Path** 插入**绝对路径**（前缀 `*`）。
- **多数情况推荐相对路径**，因为重命名 Frame 会破坏绝对路径。

---

## 核心要点速查

| 主题 | 关键对象/方法 |
| --- | --- |
| 主动传输 | `Conveyor`（Speed/Length/Transport Time 关联） |
| 被动传输 | `Track`、`TwoLaneTrack` + `Transporter`（`create`、`Backwards`） |
| 牵引列车 | `Transporter`（勾选 Is Tractor）+ `hitchFront` |
| 停车等待 | `StopAtDestination`、`AccelerationEnabled`、传感器控制 |
| 自动路由 | `Automatic Routing`、`DestCtrl`、`Destination` |
| AGV | `AGVPool`、`Marker`、`setRoute`、`setRouteSegments`、`rotate`、`drive`、`Distance Control` |
| 电池运输车 | `Battery` 标签、`BatCharge`、`BatReserve`、`BatCapacity`、`BatCharging`、Charge Control |
