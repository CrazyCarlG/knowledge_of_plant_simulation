# Converter、Turntable 类物料流对象（基于转台/转向的路由）

本目录介绍会改变零件输送方向、朝向以及路径的物料流对象：

- **Converter**（转换器）
- **AngularConverter**（角向转换器）
- **Turnplate**（转盘）
- **Turntable**（转台）

这些对象均可从 Class Library 的 `MaterialFlow` 文件夹，或 Toolbox 的 `Material Flow` 工具栏插入。

---

## 一、用 Converter 横向输送零件

**Converter** 可将零件沿直线（直行）、向左或向右输送。

### 涵盖示例

1. 直线输送零件（Convey Parts Straight Through）
2. 按零件名称横向输送（Convey Parts Laterally According to Their Name）
3. 按策略控制输送零件（Convey Parts According to a Strategy Control）
4. 发送零件到默认出口（Send Parts to the Default Exit）
5. 从支线向主线喂入零件（Feed Parts from a Branch Line into the Main Line）

### 1. 直线输送零件

- Converter 使用默认设置即可。
- Source 产生零件并移动到相连的 Conveyor 上，Converter 将其直行传给后续 Conveyor。
- 为限制零件数量，Source 只生产 5 个零件。
- 零件先自右向左移动，再自下向上移动；零件缺口位于其右侧。

### 2. 按零件名称横向输送

Source 以不同频率生产 6 种零件，零件经多条 Conveyor 到达两对 Converter，按名称横向送入/移出两个加工站。

- **配置 Source**：设置生产时间与间隔（可调间隔 + 正态分布时间）；选择零件类型与生产频率（随机频率，选用频率表 DataTable `MyParts`）。
- **配置 ProcessingA 的进/出 Converter**：
  - `ConverterToA`：`Strategy > MU Name`，在列表中为 `A1/A2/A3` 选择 **side 3**（向左出口）。
  - `ConverterFromA`：`Strategy > MU Name`，为 `A1/A2/A3` 选择 **side 0**（直行）。
- **配置 ProcessingA / ProcessingB 两站**：类型为 `ParallelStation`，容量 X/Y 各为 5（各 25 个加工位），设置正态分布 Processing Time。
- **配置 ProcessingB 的进/出 Converter**：`ConverterToB` 用 `B1/B2/B3` 选 side 3；`ConverterFromB` 用 `B1/B2/B3` 选 side 0。

> **注意**：向左横向移动会使零件顺时针旋转 90°；第二次横向移动再旋转 90°，因此零件会倒着朝 Drain 移动。

### 3. 按策略控制输送零件

Source 各生产 3 种零件每种 10 个，Converter 按名称决定左横、右横或直行，由 **Strategy Control**（方法）控制。

- **配置 Source**：选择 Delivery Table（DataTable）自动套用格式。
- **配置 Converter**：`Strategy > Method`，右键 `Strategy Method` 文本框 → `Create Control`，Plant Simulation 自动输入 `self.OnStrategy` 并打开方法，输入代码：

```simtalk
param entranceNo: integer
if @.name = "C" 
   ?.ExitForMU := 0 /* number of the exit of the converter*/
elseif @.name = "A" 
  if entranceNo = 2 
       ?.ExitForMU := 3
   else
       ?.ExitForMU := 0
   end
else
   if entranceNo = 2
       ?.ExitForMU := 1
   else
       ?.ExitForMU := 0
   end
end
```

- 名称 `A` 向左（出口 3）、`B` 向右（出口 1）、`C` 直行（出口 0）。

### 4. 发送零件到默认出口

- Converter 将所有到达零件发送到选定的 **Default Exit**。
- `Strategy > Default Exit`，选择默认出口编号（例如 `3` 表示向上出口）。

### 5. 从支线向主线喂入零件

- Converter 在主线间隙足够大时，把支线零件喂入主线。
- **配置主线 Source**：恒定间隔 `30` 秒；零件类型 `Part`（图标添加方向箭头）。
- **配置 Converter**：`Strategy > Feed in`，输入间隙大小（Free Space，例如 `5` 米）。
- 零件以喂入时的朝向从支线进入主线。

---

## 二、用 AngularConverter 改变输送方向

**AngularConverter** 在纵向输送与横向输送之间切换（或反向切换），同一时间只能容纳一个零件。

- Source `PartsIn` 生产 `MyCarbody` 零件，AngularConverter 改变其输送方向，占用长度从 **MU Length** 变为 **MU Width**，并消耗 **Moving Time**；零件离开后 AngularConverter 复位，准备接收下一个 MU。

### 配置步骤

- 配置 Source：命名 `PartsIn`，选择 `UserObjects` 中的 `MyCarbody`。
- 插入进料 Conveyor（例如 10 米长）。
- 插入第一个 AngularConverter：Entry Length 与 Exit Length 各 `5` 米。
- 插入 `ProcessingConveyor`：长度 `2.5` 米，速度 `0.001` m/s（使零件停留在线上，对应时间 41 分 40 秒）。
- 插入第二个 AngularConverter、另一条 Conveyor 和 Drain，用 Connector 连接所有对象。

> 零件的 Conveying Direction 依次为：`forward` →（变向点后）`lateral right` →（再次变向后）`backward`，直到 Drain。

---

## 三、用 Turnplate 对齐与裹膜零件

**Turnplate** 模拟旋转平台，旋转装载的零件并保证出料方向一致（例如包裹配送中让条形码朝向扫描器）。

### 涵盖示例

1. 用 Turnplate 对齐零件（Align Parts）
2. 模拟裹膜机（Model a Shrink Wrapper）

### 1. 用 Turnplate 对齐零件

Source 生产 4 个 `MyPart` 零件，Turnplate 将每个零件向右旋转 90° 后继续输送。

- Source：`Time of Creation > Number Adjustable`，Amount `4`，零件 `MyPartColored`（来自 `UserObjects`）。
- 插入进料 Conveyor、Turnplate，以及通往 Drain 的 Conveyor。
- Turnplate 默认设置：`Strategy > Angle`，旋转 Angle `90` 度。
- 降低仿真速度（调整 EventController 的 Simulation Time，或左拖滑块）以观察旋转。

### 2. 模拟裹膜机

流程：`SourceParts` 产生 9 个零件 → `Conveyor1` 送入 Turnplate（右转 90°）→ 后继线 → `ParallelStation`（加工 2 分钟）→ `TransferStation`（装载到托盘）→ `ConveyorPallet` 将托盘送回 Turnplate（裹膜）→ Drain。

#### 配置 Source 与进料线

- Source：`Number Adjustable`，Amount `9`，零件 `MyPart`（`UserObjects`）。
- 进料线：默认设置 Conveyor。

#### 配置 Turnplate

Turnplate 有双重任务：右转零件 90°，以及旋转托盘模拟裹膜。

- `Strategy > Method`，右键 `Strategy Method` → `Create Control`（自动输入 `self.OnStrategy`），输入代码：

```simtalk
var rotAngle: integer
if @.typeOf(.UserObjects.MyPart)           // rotates the part
   rotAngle := 90
else
   if @.typeOf(.UserObjects.MyPallet)      // rotates the pallet
       rotAngle := -(4 * 360)              // minus (-) designates 
counterclockwise rotation
   end
end
?.rotatePart(rotAngle)
```

- 正负号决定旋转方向：`+` 顺时针，`-` 逆时针；示例让托盘逆时针旋转 4 次各 360°。

#### 配置转运零件的 Conveyor

- `Controls` 页定义长度方向、**front triggered** 的传感器；右键 `Control` → `Create Control`，输入代码：

```simtalk
param sensorID: integer, front: boolean
if @.typeOf(.UserObjects.MyPart)
   @.move(ParallelStation)
end
```

#### 配置处理托盘的站点

- 托盘 Source：`Number Adjustable`，Amount `1`，Creation Times `10:00`，MU `MyPallet`。
- 插入 `ParallelStation`（无需改设置）。
- 插入并配置 `TransferStation`：
  - 将 ParallelStation 拖到 TransferStation（写入 Exit Control）。
  - 将 `ConveyorPallet` 拖到 TransferStation，选择 station type **Load** 并设置传感器位置。
- 用 reset 方法降低仿真速度：

```simtalk
EventController.Speed := 60
```

#### 调整裹膜机与零件

- 零件高度设为 `0.1` m（长宽保持 `0.8` m）。
- 若零件显示偏移，检查 **Booking Point Length** 与 **Booking Point Width**（居中 vs. 偏移）。
- 替换托盘 3D 图形（`MyPallet` → 3D → `Exchange Graphics`，如 EUR-pallet）。
- 缩小零件 3D：右键 `MyPart` → `Edit 3D Properties` → `Transformation`，减小缩放（如均匀缩放 `0.5`），必要时取消 `Scale automatically`。
- 将 ParallelStation 旋转 90°，避免零件穿透玻璃板。
- 另存为 **3D Only** 模型。
- EventController 的 **Real-time factor** 设为 `10`（使 reset 方法冗余）。
- 将托盘 Creation Times 缩短为 `1` 分钟，并调整 ParallelStation 加工时间。
- 可选：将托盘 Z 方向容量从 `1` 增到 `3`，同时将 Source 零件数增至三倍。

---

## 四、用 Turntable 转运零件

**Turntable** 模拟旋转平台，将零件移动到多个相连物料流对象之一。

- Source `PartsIn` 生产 `MyPart` 零件，逐个送到 Turntable 进料线；Turntable 循环地将零件移到后继对象（Drain `OutA` 与 `OutB` 的进料线）。

### 配置步骤

- 配置 Source：负指数分布，参数 `0:10, 0, 1:40`；零件 `MyPart`（`UserObjects`）。
- 插入进料 Conveyor。
- 插入 Turntable 及其直接后继（Drain 的进料线）并连接；Turntable 需要后继才能配置 **Entry Angle Table** 与 **Exit Angle Table**。
- Turntable 长度 `4` 米，**Rotation Point** 居中（`2` 米）。
- 用 Connector 从 Turntable 末端拖到后继起点；Plant Simulation 自动计算后继所在角度，可在 `Exit Angles Table` 查看。
- 配置 Drain 并运行仿真。
- 若要在移上顶部进料线前调转零件方向，打开 **Exit Angle Table**，对 `FeederPartA` 选择 `Which Side > MU leaves backward`。

### 3D 中添加固定底座

默认 Turntable 在 3D 中悬空（无支腿）；若定义支腿，整个 Turntable（含支腿）都会旋转。为此创建不旋转的圆柱底座：

- 在新窗口打开 Turntable。
- 右键 → `Edit 3D Properties` → `Graphics` → `Add`，新建图形组 `base`。
- 在 `Edit` 功能区点击 `Cylinder` 创建底座圆柱。
- 将底座插入 Turntable 中心下方的网格交点。
- 右键底座 → `Make Animatable Object`，命名为 `base`。
- 在 `Edit 3D Properties` 的 `Joint` 页选择 `Revolute Joint`，`Velocity` 输入 `0`，使 Turntable 旋转时底座保持静止。

---

## 快速对照表

| 对象 | 主要用途 | 关键配置/策略 |
| --- | --- | --- |
| **Converter** | 直行 / 左横 / 右横输送；支线喂入 | `MU Name`、`Method`（Strategy Control）、`Default Exit`、`Feed in`（Free Space） |
| **AngularConverter** | 纵向 ↔ 横向输送方向切换 | Entry/Exit Length、Moving Time |
| **Turnplate** | 旋转并对齐零件；模拟裹膜机 | `Angle`、`Method`（`rotatePart`） |
| **Turntable** | 在多个后继间循环转运零件 | Entry/Exit Angle Table、Rotation Point、`MU leaves backward` |

> 示例模型的对照查看方式：`Window` 功能区 → `Start Page` → `Getting Started` → `Example Models` → `Small Examples`，选择 Category / Topic / Example 后点击 `Open Model`。
