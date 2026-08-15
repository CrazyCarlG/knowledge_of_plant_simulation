# Building Capable Simulation Objects（构建功能强大的仿真对象）总结

本目录包含 `building-capable-simulation-objects.md`（以及同名文本提取文件 `building-capable-simulation-objects.txtx`），内容为 Plant Simulation 帮助文档中两个分步教程 **Creating a Simulation Object with Animation（创建带动画的仿真对象）** 与 **Modeling a Complex Receiving Department（建模复杂收货部门）** 的总结。二者都演示了如何构建可在 3D 中动画化工作流程的仿真对象。

## 目录结构

```
building-capable-simulation-objects/
├── building-capable-simulation-objects.md     # 源文件（Markdown 总结）
├── building-capable-simulation-objects.txtx   # 相同内容的文本提取版
└── README.md                                  # 本总结文件
```

> 本目录**无子文件夹**，故无子文件夹 README.md 需要合并。

---

## 1. 创建带动画的仿真对象（Creating a Simulation Object with Animation）

本教程在一个 Frame 中自定义建模一个螺丝刀工站（screwdriver station），涵盖创建仿真对象、添加动画与交互、测试与微调。

### 1.1 创建仿真对象（Create the Simulation Object）

1. 新建 Frame 并打开。打开 **Edit 3D Properties** → **Graphics** 选项卡，勾选 **Show Content** 以显示所含对象。
2. 在 **View** 功能区选项卡点击 **Show External Graphic Groups**，删除名为 `default` 的图形组中的图形。
3. 在 **Edit** 功能区选项卡点击 **Import Graphics**，将 JT 文件（如 `Screwdriver.jt`）导入 `default` 图形组。
4. 提取第一个仿真对象：
   - 点击工站的底板，反复按 `+` 直到只选中底板（呈黄绿色）。
   - 右键该图形选择 **Make Simulation Object**。
   - 选择类 `.MaterialFlow.Station`，命名为 `PartCarrierStation`，调整 **Object Position** 坐标使其居中于螺丝刀。
5. 选中支撑螺丝刀的支架。深绿色 = 选中对象；黄绿色 = 选中图形（可按 `+` 收缩选择）。
6. 创建第二个仿真对象：`.MaterialFlow.Station`，命名 `Trestle`，定位于螺丝刀中心。

### 1.2 添加动画与交互（Add Animations and Interactions）

1. 右键支架 → **Open in New Window**（打开 `.Models.MyScrewdriver.Trestle`）。按 `+` 直到只选中螺丝臂图形。
2. 右键图形 → **Make Animatable Object**，命名 `Arm`，将 **Object Position** 设为螺丝臂中心。
3. 右键可动画对象 → **Use as Animation Object**，将 MU 动画转发给 `Arm`。
4. 关闭 Trestle Frame。右键 `Trestle` → **Edit 3D Properties** → **MU Animation** 选项卡，`Arm` 现在显示为动画对象（也可手动输入其名称）。

**配置 Arm 的自动画：**

- 在新窗口打开 Trestle，右键 `Arm` → **Self Animation**。
- 添加四条 **Lines** 类型动画路径：`Setup`、`DownAdvance`、`Reset`、`DownFinal`。
- 对每条路径点击 **Edit** 并定义两个锚点（在 *Path Anchor Points* 中点击 **Add**，选中点后点击 **Edit Values**）：

  ```
  Setup:       0, 0, 0    to  0, 0, 0.9
  DownAdvance: 0, 0, 0.9  to  0, 0, -0.1
  DownFinal:   0, 0, -0.1 to  0, 0, -0.22
  Reset:       0, 0, -0.22 to 0, 0, 0
  ```

- 转到 **MU Animation** 选项卡，添加名为 `Default` 的路径，动画点设为 `0, 0, -0.38`。

**配置仿真侧：**

- `PartCarrierStation`：处理时间 `0:10`（10 秒）。
  - Exit Control `self.OnExit`：

    ```simtalk
    if ?.ExitCtrlFront 
       self.~.~.Trestle.EntranceLocked := false
       @.move
    end
    ```

  - 用户自定义属性 `init`（方法）：

    ```simtalk
    self.~.EntranceLocked := true
    ```

- `Trestle`：准备时间 `0:06`（6 秒）。
  - Entrance Control `self.OnEntrance`：

    ```simtalk
    var animations : any := self.~._3D.getObject("Arm").SelfAnimations 
    animations.resetAnimation
    animations.DownAdvance.schedule
    animations.startNextAnimationBlock
    animations.DownFinal.schedule
    animations.scheduleRotation(0, 360, 90)
    @.outIn(animations.AnimationTimeTotal)
    animations.playAnimation
    ```

  - Exit Control `self.OnExit`：

    ```simtalk
    if ?.ExitCtrlFront
       @.deleteObject
       var animations : any := self.~._3D.getObject("Arm").SelfAnimations
       animations.resetAnimation
       animations.Reset.schedule
       animations.playAnimation
       self.~.EntranceLocked := true
    end
    ```

  - Setup Control `self.OnSetup`：

    ```simtalk
    param setupStart: boolean 
    if setupStart 
       var animations : any := self.~._3D.getObject("Arm").SelfAnimations
       animations.resetAnimation
       animations.Setup.schedule
       animations.playAnimation
    else
       self.~.~.PartCarrierStation.EntranceLocked := false
    end
    ```

  - 用户自定义属性 `init`（方法）：

    ```simtalk
    self.~.EntranceLocked := false
    ```

### 1.3 在仿真模型中测试工站（Test the Station in the Simulation Model）

- 插入一个 `Source`（`SourcePallets`）生产托盘，再插入第二个 `Source`（`SourceScrews`）供应螺丝（JT 文件来自同事）。
- 插入一个 `Drain` 接收完工托盘。
- 插入螺丝刀工站和三个 `Conveyors`。
- 用 **Connectors** 连接所有对象：
  - `SourcePallets`（生产 `MU > PartsCarrier`）→ `ConveyorPallets` → 螺丝刀工站的 `InterfaceInPallet`。
  - `SourceScrews`（生产 `MU > Screw`）→ `ConveyorScrews` → 接口 `InScrew`。
  - `ConveyorOut` → 接口 `Out` → `Drain`。

**传送带倾斜设置：**

- `ConveyorPallets`：在 **Line/Arc Parameters** 中设锚点高度第一个 `1 m`、第二个 `0.15 m`，以匹配 `SourcePallets`。
- `ConveyorOut`：**Edit 3D Properties → Appearance**，Base Height `0.15 m`；再用 **Segments** 将 Z 尺寸设为 `1 m` 以连接到 Drain。
- 以较低实时因子运行以观察拧螺丝动作。

### 1.4 微调工站（Fine-tune the Station）

1. **托盘在顶部而非底部**：打开螺丝刀类，`PartCarrierStation` → **Edit 3D Properties → MU Animation**，显示 `Default` 路径。选中路径标记（向下的楔形），按住 `Ctrl`，用下箭头键将其下移直到与 `PartCarrierStation` 齐平。
2. **螺丝未附着到臂尖**：打开螺丝刀类 → Trestle → `Arm` → **Edit 3D Properties → MU Animation**，可视化 `Default`。选中路径标记，按住 `Ctrl` 下移直到与 Arm 尖端齐平。
3. **螺丝附着在错误一侧**：打开螺丝刀类 → Trestle → **Edit 3D Properties → MU Animation**，可视化 `Default`，选择 **Top** 作为附着 MU 的一侧。

再次运行仿真以确认行为正确。

---

## 2. 建模复杂收货部门（Modeling a Complex Receiving Department）

该示例模型用三个 Source 生产砖块、玻璃砖和砖块载体。砖块与玻璃砖装载到载体上，送到 `ParallelStation`，再由 `TransferStation` 装载到第四个 Source 生产的卡车上。

### 2.1 插入建模 Source 所需的对象（Insert the Objects Required for Modeling the Source）

1. 在 Class Library 中新建 Frame，命名 `MySourceTruckLoadedWithBricks`。
2. 在左侧插入三个 `Source` 对象（类 `MySource`，修改了 3D 图形）：`SourceGlassBricks`、`SourceBricksCarrier`、`SourceBricks`。
3. 在右侧插入两个 `AssemblyStation`：`AssemblyGlassBricks` 和 `AssemblyBricks`（各自把 50 块砖放到托盘上）。
4. 插入一个 `TransferStation`、一段短 `Track` 和一个名为 `SourceTrucks` 的 `Source`（生产卡车）。
5. 插入一个 `Interface` 将收货部门连接到模型其余部分。

> **注意：** 由于 AssemblyStation 连接到两个工站，连接前驱的顺序很重要。若装配失败，检查前驱编号。Plant Simulation 在悬停 Connector 时以工具提示显示前驱/后继，请在 **Main MU from Predecessor** 中输入正确的前驱编号。

### 2.2 配置各工站（Configure the Individual Stations）

**配置 MU：**

- **Truck**：复制 `.MUs.Transporter`，重命名为 `Truck`。删除其图形并导入 `Truck.jt`。尺寸 `6.3 × 2.2 × 1.6 m`。
- **BricksCarrier**：复制 `.MUs.Container`，重命名为 `BricksCarrier`。导入 `BricksCarrier.jt`。尺寸 `1.1 × 1.1 × 0.15 m`，容量 50 个零件（X 方向 5 × Y 方向 10）。
- **Brick** 与 **GlassBrick**：复制 `.MUs.Part` 两次并重命名，尺寸均为 `0.2 × 0.1 × 0.05 m`。

对砖块使用自动生成的图形而非 JT 文件：

- 打开类 → **Edit 3D Properties → Transformation**，激活 **Scale Automatically**。
- 对 `GlassBrick`：激活 **Material Active**，选择蓝灰色 **Diffuse Color**，**Transparency** 因子 `0.6` 以获得半透明效果。（同样激活 **Material Active** 并选择橙色作为 Diffuse Color。）

**配置其他对象：**

- 配置每个 Source 生产与其名称匹配的 MU（无其他改动）。
  > **注意：** MU 使用绝对路径（以 `*` 开头）；相对路径以 `~` 开头。
- 配置 AssemblyStation 附着 MU 并让 Main MU 离开。点击 **Assembly Table** 旁的 **Open**，在 **Number** 列输入 `50` 将 50 个零件装载到载体上。
- 将 `ParallelStation` 拖到 `TransferStation` 上，用作 **Part Source**（默认设置）。
- 将 `Track` 拖到 `TransferStation` 上作为 **Target Station**，接受 `0` 作为 Sensor Position。为使卡车停下等待装完，在 **Advanced Attributes** 选项卡选择 **Always Stop Container**。
- 打开 `MySourceTruckLoadedWithBricks` → **Edit 3D Properties → Graphics**，取消 **Show Content**。

将收货工站插入模型，用 Track 和 Drain 连接并运行。它生产运输两种载体的卡车——一种装载普通砖，一种装载玻璃砖。

### 2.3 在砖块载体的动画区域上动画化砖块（Animate Bricks on the Animation Area of the Brick Carrier）

Plant Simulation 会根据对象尺寸与载体尺寸/维度，自动将放置对象（装载到载体上的砖块）均匀分布到动画区域。

示例：载体在 110 × 110 cm 区域承载 50 块砖（每块 20 cm 长 × 10 cm 宽）。x 维度 5 时五块砖并排沿 x 方向排列；y 维度 10 时十块沿 y 方向排列。使用默认容器设置。

### 2.4 在卡车的动画区域上动画化砖块载体（Animate Brick Carriers on the Animation Area of the Truck）

Plant Simulation 将对象放置到卡车的装载空间（动画区域）。动画区域为 `ParallelStation`、`Sorter`、`Store`、`Transporter` 和 `Container` 预定义。

由于卡车图形被修改（派生自 `Transporter`），必须调整动画区域：

1. 在 Class Library 中右键 `MUs > Truck` → **Open In 3D**。
2. 右键 `.MUs.Truck` → **Edit 3D Properties → MU Animation**。
3. 调整 **animation area** 设置，使砖块载体均匀分布到装载空间。点击 **Apply** 时 Plant Simulation 计算该区域。

**替换卡车图形（TruckDumper）：**

- 复制 `Transporter`，重命名为 `TruckDumper`，更换其图形。
- 在 `SourceTruck` 中将 dumper 输入为 MU。
- 现在只装载 6 个砖块载体而非 8 个——通过将装载空间的 **X-Dimension** 从 `3` 增加到 `4` 修复。
- 调整车厢动画区域：在新窗口打开 `TruckDumper`，点击背景，按空格键，在 **MU Animation** 选项卡激活并显示 **Animation Area**，然后点击文本框滚动滚轮直到区域正确。

### 2.5 显示 Frame 的内容（Show the Content of the Frame）

在 `MyPlant` 内显示 `MySourceTruckLoadedWithBricks` 的内容而非 Frame 图标：

1. 选中 Frame，按空格键。
2. 选择 **Show Content**。
3. 调整内容：
   - 清除图形组 `default` 的 **Visible**，使 Frame 的默认图形不覆盖内容。
   - 删除类型为 `Exit` 的 `Interface`（子 Frame 只有一个外部物料流对象，故不需要）。将子 Frame 与 Track 连接。
4. 调整对象位置并运行仿真。

---

## 目录说明

- `building-capable-simulation-objects.md`：本目录源文件（Markdown 版本），总结"创建带动画的仿真对象"与"建模复杂收货部门"两个教程。
- `building-capable-simulation-objects.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。

*来源：Plant Simulation Help — "Creating a Simulation Object with Animation" and "Modeling a Complex Receiving Department"。Unpublished work. © 2026 Siemens.*
