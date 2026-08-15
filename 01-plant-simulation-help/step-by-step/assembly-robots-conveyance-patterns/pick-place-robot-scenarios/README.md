# Pick and Place Parts with the PickAndPlace Robot

本目录介绍如何使用 **PickAndPlace 机器人** 完成零件的抓取（Pick）、旋转（Rotate）与放置（Place）操作。该机器人可一次抓取并投递一个或多个零件，多个零件时通过设置 **Capacity**（容量）实现。

机器人可从 **Class Library** 的 **MaterialFlow** 文件夹，或 **Toolbox** 的 **Material Flow** 工具栏插入模型。

示例模型位置：**Window ribbon tab → Start Page → Getting Started → Example Models → Small Examples**，在 *Examples Collection* 对话框中选择 Category、Topic 和 Example 后点击 **Open Model**。

本目录共包含 8 个场景：

---

## 1. Pick Up Parts and Place Them with the Robot
用默认设置演示 PickAndPlace 机器人的基本抓取与放置，无需修改任何参数。

- **流程**：`Source`（产生 `MyPart`）→ `Station`（加工）→ `PickAndPlace`（抓取）→ 旋转到 `Station1` → 放置 → `Station1` 移送到 `Drain`。
- 移动目标站后，可右键机器人 → **Calculate Angles** 重新计算连接角度，**Angles Table** 会随之更新。

## 2. Pick Up Several Parts and Place Them with the Robot
演示机器人一次抓取并放置多个零件。

- **流程**：`SourceContainers` 将容器直接送到 `AssemblyStation`；`SourceParts` 将零件送到机器人，机器人抓取后旋转并投递到 `AssemblyStation`；装载完成后 `AssemblyStation` 将容器送上 `Conveyor` → `Drain`。
- **Sources/容器/零件配置**：设置 `SourceContainers` 类型（如 `MyContainer`）、`SourceParts` 类型（如 `MyNewPart`，Interval `0:01`）；容器 x/y/z 维为 `4/2/1`（两排四列）。
- **机器人配置**：Capacity 设为 `8`；连接 `SourceParts` 与 `AssemblyStation` 后自动计算角度与时间；设置 X-Dimension 与 Z-Dimension 各为 `2`。
- **AssemblyStation 配置**：Assembly Table → Predecessors 输入前任编号 `2` 与装载数量 `8`，机器人按 FIFO 顺序装载。
- 常见问题：空托盘与已装载托盘重叠时按 **M** 键调整边界或设置 Transformation 缩放；零件突出时更换 3D 图形并缩放（如 `BoxFor2x1x2Entities.s3d`、scale `0.55`）。

## 3. Place Parts with a Target Control
演示用 **Target Control**（目标控制）决定零件去向。

- **流程**：`Source` → 机器人 → `Drain`；`Source1` → 机器人 → `Station` → 回到机器人 → `Drain1`。
- 为每个 Source 与 Station 定义 **Entrance Control** 记录零件最后所在工位：`@.LastStation := ?`；并创建零件用户属性 `LastStation`（类型 `object`）。
- 机器人 **Target Control** 根据 `LastStation` 判断目标：

```simtalk
if ?.empty
   return
end
if @.LastStation = Source
   ?.setDestination(Drain)
elseif @.LastStation = Source1
   ?.setDestination(Station, true)
else
    ?.setDestination(Drain1)
end
```

## 4. Load Parts with an Exit Control
演示用 **Exit Control**（出口控制）与变量 `WaitingBasket` 配合，将零件装入正确的篮子。

- **流程**：机器人从 `Source` 抓取 `Part` 放入 `Basket` → `Conveyor1` 运送 → `Station` 加工 → `Conveyor2` 反向运送 → 停止后机器人抓取零件放入 `Drain`。
- 复制内置类：`Part` → `MyPart`，`Container` → `Basket`；`SourceParts` 每 30 秒产生一个 `MyPart`，`SourceBasket` 每 10 秒产生 4 个篮子。
- **SourceParts 的 Exit Control**（`exitSourcePart`）设置目标并等待篮子可用。
- **Conveyor1 传感器控制**：停车、设置 `WaitingBasket`、等待篮子非空。
- **Conveyor2 传感器控制**：从篮子卸载零件并送往 `Drain`。
- **机器人 Exit Control**（`loadCtrl`）与 **Target Control**（`targetCtrlRobot`）配合将零件装入正确的篮子，**Target Selection** 选 *Exit strategy or target control*。

## 5. Load and Unload Parts at the Sensor of a Conveyor
演示三台机器人协同：放置零件到传送带、把零件装载到托盘、从托盘卸载零件。

- 支持两种配置方式：**拖放**（机器人自动创建传感器、控制并写入 Angles Table）或 **手动**（Exit 标签页自行创建传感器与控制）。
- **物料流**：`SourceParts` → `Station1` → `PlacePartOnConveyor` → `Conveyor`；`SourcePallets` 产生托盘；`LoadPallets` 将零件装载到托盘；`UnloadPallets` 卸载到 `Station2` → `Drain`（`PartsOut`）。
- 关键操作：**Operation → Place part / Pick part / Load part / Unload part**；传送带起点与终点相连形成循环。
- 3D 托盘标准图形只有 4 个装载位，需用 `BoxFor3Entities.s3d` 更换图形并设 Z-Dimension `3`。

## 6. Set the Conveying Direction of the Parts
演示在 PickAndPlace 机器人中设置 **MU 传送方向**。

- `Turnplate`、`Turntable`、`AngularConverter`、`Conveyor` 会改变 MU 传送方向（原长度变新宽度、原宽度变新长度），机器人也可任意旋转零件。
- **流程**：`Source` → `Conveyor`（6 米，非积放，间隔 1 米）→ `AngularConverter`（Forward → Lateral right，出入长度各 2 米）→ 机器人（**MU Conveying Direction → Forwards**）→ `Conveyor1`（5 米，积放）→ `Drain`。

## 7. Unload Stacked Parts
演示利用 Z-Dimension 堆叠零件，并用三台机器人逐级卸载。

- **结构**：`Transporter` 运送托盘，托盘上堆叠箱子，箱内堆叠 3 个零件。
  - 第一台机器人从 `Transporter` 卸载托盘到传送带；
  - 第二台机器人从托盘卸载箱子到第二条传送带；
  - 第三台机器人从箱子卸载堆叠零件到第三条传送带。
- **配置**：`Transporter` 存储区 Z-Dimension `1`（不堆叠托盘）；托盘 Z-Dimension `3`（堆 3 箱）；箱（复制 Container）Z-Dimension `3`，长宽使托盘可放 4 箱。
- **Source/Track**：每 40 秒产生 10 个 Transporter；用 **Entrance Control** 装载托盘、箱子与零件（先设 Transporter 长度 3.2 m，再创建托盘→箱→零件）；在 Track 上创建传感器及停车控制，直到完全卸载。
- **传送带**：左侧两条各 2 个传感器，右侧 1 个；卸载传感器由零件后缘光栅触发；三条传送带传感器控制相同，仅 `Destination`（`PickAndPlace1`/`PickAndPlace2`）不同。
- **机器人**：三台机器人 Loading/Unloading Time 各 2 秒；第一台机器人图形 Uniform Scaling Factor 设为 `2`。

## 8. Animate the Robot Arm in 3D
演示如何在 3D 中设置 **Robot Arm Animation**。

- **物料流**（默认设置）：`Source` → `Station` 加工 → 机器人抓取 → 旋转到 `Station1` 放置 → 加工 → `Drain`。
- **更换图形**：右键机器人 → **Exchange Graphics**，选择 Comau 的 PickAndPlace 机器人。
- **机械臂运动**：**Real-time Factor** 设为 `1` 便于观察；空格键打开 **Edit 3D Properties** → **Robot Arm Animation [PickAndPlace]** 标签页。
  - 添加路径 **From 'Station' to 'Station1'**：点击 **Show** 显示路径，点击 **Extend** 添加 3 个锚点，各锚点 elevation 设为 `2.2`（工位高 2 米），再拖动锚点到正确位置（抓取、离开工位、进入下一工位、放置）。
  - 添加路径 **Default Orientation to Station**（elevation `3.8`），避免机械臂穿过零件架、防护笼及指示灯。

---

*来源：Siemens Plant Simulation Help —— "Pick and Place Parts with the PickAndPlace Robot"。*
