# Controls, Sensors, Observers, Distance Control（控制、传感器、观察器与距离控制）

> 本目录整理了 Plant Simulation 帮助文档中关于**高级物料流建模**的内容，来源为 *Plant Simulation Help — Modeling the Flow of Materials, Advanced*（第 10-309 至 10-372 页）。主题覆盖：用控制（controls）与用户自定义属性定制对象行为、入口/出口控制、传感器、观察器以及距离控制。

## 目录说明

- `controls-sensors-observers-distance-control.md` — 本主题的整理版总结（Markdown）。
- `controls-sensors-observers-distance-control.txtx` — 帮助文档原文的文本提取（含页眉页码与版权信息）。

## 内容概览

### 1. 定制对象行为（Customizing the Behavior of Objects）

可通过两种方式定制大多数 Plant Simulation 对象的行为：

- **控制方法（control methods）**：编程并分配给对象，使其对特定用户操作（插入、删除对象等）作出反应。
- **用户自定义属性（user-defined attributes）**：创建对象默认不提供的属性。

#### 定义控制（Defining Controls）

控制方法可让对象执行期望的动作：

- **共享控制（Method 对象）**：将动作编程到 Method 对象中，插入到 Frame 或类库（Class Library）的文件夹里，供多个对象复用。
- **对象专属控制**：以数据类型为 `method` 的用户自定义属性实现，只作用于该对象，并随对象一起插入到其他 Frame 中。

**分配 Method 对象控制**：编程 Method → 点击目标对象 → **Tools > Edit Controls** → 在 *Controls* 对话框中选择要激活的 Method。

**创建属于对象的控制**（数据类型为 `method` 的用户自定义属性）：在文本框中输入名称后右键 **Create Control**（插入 `self.名称`，如 `self.mySelectControl`），或直接右键 **Create Control**（插入 `self.On内置名`，如 `self.OnCreate`）。

打开/修改控制：按 **F2**，或 **Shift + 双击**文本框，或在 **User-defined** 选项卡双击 Method 名称。

#### 手动创建用户自定义属性

在 **User-defined** 选项卡点击 **New** → 输入有意义的**唯一**名称（不能与内置或已有的用户自定义属性/方法重名）→ 选择**数据类型** → 输入与类型兼容的值 → 点击 **OK**。

> **注意**：若数据类型为 `method` 的用户自定义属性在执行中被删除（例如其 MU 在 Drain 中被删除），执行会立即终止；`waituntil` 之后的指令不再执行。若该属性方法被其他 Method 调用，调用方会继续执行并返回一个部分设置的 `result` 值。

#### 在仿真过程中动态创建用户自定义属性

可通过 Method 在仿真中动态创建/删除属性，而不必手动创建。

**示例模型**：带 `Bad` 属性的零件在喷漆车间后剔除，送往返工站重新喷漆后送回产线。关键步骤：

1. **Source** 每两分钟产生一个 `MyPart` 类型的零件。
2. **可视化**：创建图形组 `Good` 与 `Bad`（*Open in 3D* → *Edit 3D Properties* → *Graphics*）。
3. **动态创建属性**（Station1 的 Entrance Control，方法 `createMyAttr`）：

```simtalk
@.createAttr("Paint","boolean")
```

4. **检查喷漆结果**（PaintShop 的 Entrance Control，方法 `checkPaintJob`），用 `z_uniform(1,0,1)` 生成 0 到 1 之间的随机值，低于 0.1 判为次品（约每 10 个零件 1 个次品），并切换图标。

5. **按属性分支**（`BranchOff` 的 Exit Control，方法 `checkMyAttr`）：

```simtalk
if @.Paint
   @.move(1)   // 好零件走 Connector1
else
   @.move(2)   // 次品走 Connector2
end
```

6. **删除属性**（Station2 的 Entrance Control，方法 `deleteMyAttr`）：

```simtalk
@.deleteAttr("Paint")
```

#### 创建提示框（Tooltip）作为用户自定义属性

在 **User-defined** 选项卡 **New** → 名称 `Tooltip`、数据类型 `string`、在 **Value** 输入提示文本。标准提示框显示：对象名（加粗）→ 来源（`Origin: .MaterialFlow.Station`）→ 自定义文本。若只想显示自定义文本，可在文本前加冒号（`:`）；对子 Frame 需勾选 **Show Externally** 才能在 3D 窗口中显示。

### 2. 创建入口与出口控制（Entrance / Exit Controls）

通过编程**入口控制（Entrance Control）**与**出口控制（Exit Control）**可修改物料流对象的默认转移行为。对象在 MU 打算进入/离开时调用对应 Method，这些控制**覆盖**标准转移行为，因此必须自行确保 MU 移动到正确工位。典型用途：统计进入的 MU 数量，达到指定数量后将后续 MU 路由到其他后继对象。

控制 Method 可以是 Frame/文件夹中的 **Method 对象**（同一 Frame 内用 Frame，跨 Frame 用 Class Library），也可以是数据类型为 `method` 的**用户自定义属性**（仅该对象可用，通常在类中创建供所有实例共享）。

指定 Method 的几种方式（入口/出口/反向入口/反向出口控制通用）：

- 点击按钮在 Frame 中选择 Method → 输入**相对路径**。
- 勾选 **Before Actions** 使入口控制在标准动作（加工时间、准备时间、导入器服务、装配表等）开始前激活。
- **Shift+Ctrl** 拖拽 Method 到文本框 → 输入**绝对路径**。
- 右键文本框 **Create Control** → 创建为用户自定义属性（输入名称则插入 `self.名称`；直接创建则插入 `self.On内置名`，如 `self.OnEntrance`）。

> **注意**：用 *Create Control* 创建的控制是对象的用户自定义属性，**不是** Method 对象；删除它需删除对应的用户自定义属性（仅从文本框删除名称不会删除属性本身）。

> **注意**：Exit Control 可有一个数据类型为 `object` 的可选参数。当存在时，把 MU 拉走（因 MU 在该对象的阻塞列表中）的后继对象会被赋给该参数。

### 3. 面向点对象的控制（Point-Oriented Objects）

**面向点对象**提供加工工位，但无长度且不考虑 MU 长度：`Station`、`ParallelStation`、`AssemblyStation`、`DismantleStation`、`Buffer`、`PlaceBuffer`、`Store`、`Sorter`、`Source`、`Drain`。

- **Entrance Control**：MU 完全进入对象后激活（默认；*Before Actions* 未勾选）。勾选 **Before Actions** 则在标准动作开始前激活，可改变影响进入零件的加工时间等。
- **Exit Control**：MU 离开时激活。
- **Front / Rear 复选框**决定 MU 触发 Method 的时机：
  - **Front**：MU 一旦准备离开即激活；Exit Control 必须自行将零件移走（覆盖内置行为）。
  - **Rear**：MU 后部完全离开后激活；**不**覆盖内置行为。
  - Front 与 Rear 可同时勾选。

> **注意**：若 MU 无法离开并进入目标对象的阻塞列表，前部触发的 Exit Control 可能被同一 MU 多次调用（新的 `Out` 事件再次触发）；后部触发的 Exit Control 只调用一次。

四种典型应用：

- **在 Entrance Control 中改变加工时间**：`ParallelStation` + `MyEntranceControl`（勾选 Before Actions），按 `@.Name` 用 `switch/case` 为不同零件设置 `?.ProcTime`。
- **在 Entrance Control 中改变导入器服务**：`Station` 的 `MyEntranceControl` 通过 `Station.imp.getServices/setServices` 按零件名重写服务表（`table[string,integer,string]`）。
- **在 Entrance Control 中改变装配表**：`AssemblyStation`（Assembly Mode > Attach MUs）的 `MyEntranceControl` 按容器名构建装配清单并赋给 `Assembly.AssemblyTable`。
- **用 Exit Control 分配零件**：Source 生产 1000 个零件到 Station，Exit Control 依据 `Station.StatNumIn` 计数，把前 100 个送 Station1、之后 200 个送 Station2、其余 700 个送 Station3（用 `@.move(...)`，`@` 标识被移动的零件）。

### 4. 面向长度对象的控制（Length-Oriented Objects）

**面向长度对象**考虑自身长度与 MU 长度：`Track`、`TwoLaneTrack`、`Conveyor`、`Turnplate`、`Turntable`、`AngularConverter`、`Converter`。

除正向入口/出口控制外，还提供**反向入口控制**与**反向出口控制**，当 `Transporter` 倒车时激活。

> **注意**：Transporter 在 Track 上是**倒退**而非掉头，其前端仍指向物料流方向；零件的 Front 始终指向长度对象在你插入方向上的一端，倒车时亦然。

- **Entrance Control**：**Front**（MU 前部进入时；此处改加工时间不影响已进入的 MU，需用公式实现逐 MU 加工时间）或 **Rear**（MU 后部进入时）。
- **Backward Entrance Control**（倒车进入）：Rear（后部进入）与 Front（前部进入）均可选。
- **Backward Exit Control**（倒车离开）：**Rear**（调用一次，不覆盖默认离开策略）或 **Front**（覆盖内置行为，须自行移走零件）。

### 5. 创建传感器（Sensor，物料流对象）

面向长度对象（`Track`、`TwoLaneTrack`、`Turntable`、`Conveyor`）、`Transporter` 与 `Tank` 除入口/出口控制外，还可在对象任意位置定义**传感器控制**。MU 经过传感器时对象激活对应 Method（类似光栅）。示例用途：设置转移条件，或在 Transporter 前端到达传感器时改变其目标速度/图标。

创建方式：右键对象上的位置 → **Create Sensor**，或点击 **Controls** 选项卡（Transporter 为 *Load Bay* 选项卡上的 **Sensors** 按钮，选中 Track/Line 并点击 Apply 后可见）。

*Sensor* 对话框参数：

- **ID**：自动分配的唯一编号，供 Method 访问传感器。
- **位置类型**：`Relative`（0..1）或 `Length`（0..对象长度，单位取自 *File > Model Settings/Preferences > Units > Length*；无效值显示为红色）。
- **触发条件**：始终触发，或仅当 MU 的 **Destination** 与传感器中填写的目的地相同（自动路由使用该目的地；当有更短可达路线时 MU 驶向最近的传感器）。
- **Method**：传感器调用的 Method。若 Method 声明了整数参数，传感器传入 **Sensor ID**；否则无参调用。也可用 **Create Control** 做成用户自定义属性。
- **Front / Rear**：由 MU 前部、后部或两者触发。
- **Booking Point**：MU 的预订点长度触发 Method。

示例 Method `accelerate`：`@.Speed := 50`、`@.currIcon := "car_fast"`。传感器在对象图标上显示为红线（双击或右键 → *Open Sensor* 编辑；悬停显示提示框）。

### 6. 创建与删除观察器（Observer）

为大多数内置对象创建**观察器**，当可监视（watchable）的属性、只读属性或方法的值发生变化时触发动作。观察器在值变化时执行一个或多个 Method（Method 对象或数据类型为 `method` 的用户自定义属性）。

> **注意**：仅当值可监视时才有效——在 *Show Attributes and Methods* 中查看 **Watchable** 列。

> **注意**：观察器 Method 在**所有其他控制之后**调用。要在其他控制之前响应，应改用 `stopuntil` 或 `waituntil`。

示例用途：监视 `NumMUs`（对象上的 MU 数量）或 `Empty`（对象是否为空）。

**示例**：当 Station1 的只读属性 `Occupied` 变化时，把 Station1 的内容移到 Station2。

1. 打开 Station1 → **Tools > Edit Observers** → **New**。
2. 选择要监视的 **Attribute**（如 `Occupied`）。
3. 选择要执行的 **Method**（如 `occupiedObserver`），或用 **Create Control** 创建用户自定义属性方法。

```simtalk
param attribute: string, oldValue: any
if ?.occupied
   ?.cont.move(Station2)
end
```

- `attribute`：被监视值的名称（使单个 Method 可服务多个属性）。
- `oldValue`：变化前的值（变化后可访问）。
- Method 内 `?` 与 `@` 指向值发生变化的对象（此处为 Station1）。

删除观察器：在对话框中点击 **Remove**，或编程删除：

```simtalk
Station1.removeObserver("Occupied","OccupiedObserver")
```

### 7. 使用距离控制（Distance Control，无 AGVPool）

为防止减速的 Transporter 被追尾，后车须及时减速，这通过 Transporter 的**距离控制**实现。示例：制动距离 5 m，距离控制设为 6 m，保留 1 m 安全距离。

模型搭建步骤：

1. **配置 Source**：通过 Delivery Table（第 0 分钟、第 2 分钟）生产 `MyTransporter1`（在类库文件夹 `MUs` 中复制并重命名为 `MyTransporter`）。
2. **配置 Track**：在 10 m 处添加传感器，其控制令第一个 Transporter 停下（`param sensorID: integer, Front: boolean`，`if @.ID = 1` 时 `@.Speed := 0`）。
3. **配置 Transporter**：在类库 `MUs` 中激活 **Acceleration**，加速度/减速度各 10 m/s²；在 *Controls* 选项卡选择 **Distance Control** 并设置调用距离 6 m。

> **注意**：在对象的类中选择控制时，须在 *Select Object* 对话框中激活 **Absolute Path**，否则实例找不到该控制。

距离控制 `myDistanceControl`：

```simtalk
param DistanceObjectBelowLimit: boolean
if DistanceObjectBelowLimit   // 间距小于 6 m 时后车停车
   ?.Speed := 0
else                          // 间距再次大于 6 m 时后车加速
   ?.Speed := 10
end
```

- `?` 是填写距离控制的 Transporter（后车），`@` 是间距变得过大或过小的那个 Transporter。
- 无加速度的 Transporter 需在重设速度前用 `wait 0.01` 延迟，以免距离再次超限导致距离控制被重复调用。

用 `init` 方法（`&reStart.methCall(10)` 延时 10 秒）与 `reStart` 方法（`Track.MU(1).Speed := 10`）重启第一个 Transporter；间距再次超过 6 m 时后车也会加速。Plant Simulation 在间距变得过小和过大时都会调用距离控制。

## 关键术语

| 英文 | 中文 |
| --- | --- |
| control | 控制 |
| control method | 控制方法 |
| user-defined attribute | 用户自定义属性 |
| entrance control | 入口控制 |
| exit control | 出口控制 |
| backward entrance / exit control | 反向入口 / 出口控制 |
| Before Actions | 在标准动作之前 |
| point-oriented object | 面向点对象 |
| length-oriented object | 面向长度对象 |
| sensor | 传感器 |
| sensor ID | 传感器编号 |
| booking point | 预订点 |
| observer | 观察器 |
| watchable | 可监视（属性） |
| read-only attribute | 只读属性 |
| distance control | 距离控制 |
| blocking list | 阻塞列表 |
| delivery table | 交付表 |
| absolute / relative path | 绝对 / 相对路径 |
