# Tank — General（概述）摘要

本目录汇总了 Plant Simulation 流体对象 **Tank（储罐）** 的通用（General）说明。内容来源于本目录下的 `general.md`（其原始文本提取见 `general.txtx`）。

> 本目录没有子文件夹，因此没有其他子目录 `README.md` 需要汇总。

## 概述

使用 **Tank** 对象在加工前或加工后临时存储单一物料。物料可以从多个前驱对象流入 Tank，也可以从 Tank 流向多个后继对象。

## 描述

Tank 在任意时刻只能容纳一种物料。在 Tank 排空之前，新物料的流入会被阻止，因此不能在其完全排空之前让另一种物料流入。

- 将鼠标悬停在 Tank 上，可显示包含 Tank 相关信息的工具提示。
- 要更改图形的长度和锚点，点击 Edit 功能区选项卡上的 **Show Manipulators**，或按键盘 **M** 键。

### 将对象添加到仿真模型

要将 Tank 对象添加到仿真模型中，点击 Home 功能区选项卡上的 **Manage Class Library > Basic Objects > Fluids > Tank**。

比较示例模型：点击 Window 功能区选项卡，选择 **Start Page > Getting Started > Example Models > Small Examples**，然后在 *Examples Collection* 对话框中选择相应的 Category、Topic 和 Example，并点击 **Open Model**。

### 参见

- Simulate Free-flowing Materials and Fluids
- Configure the Tanks Storing the Materials
- Dialog Box of the Tank

## Tank 的对话框

双击 Tank 的图标可打开其对话框。

### Edit Simulation Properties（编辑仿真属性）

在对话框中可更改对象的仿真属性。共享属性见 *Dialog Items of the Objects*。

### Edit Animation Properties（编辑动画属性）

要在 *Edit 3D Properties* 对话框中编辑对象的 3D 属性：

- 点击仿真属性对话框左下角的 **Edit 3D Properties** 按钮。
- 选中模型中的对象并按空格键。

要操作对象的图形，点击 Edit 功能区选项卡上的 **Show Manipulators**，或按键盘 **M** 键。

## Tab Attributes（属性选项卡）

Tab Attributes 提供该对象所提供的设置。共享属性见 *Tab Attributes*。

### Outflow Rate（流出速率）[Tank]

在文本框中输入材料从 Tank 流出的 Outflow Rate。材料随后通过 Pipe 对象流向物料流中的下一个对象。

**备注：** Outflow Rate 是材料每秒流出的升数。

**注意：** 当前 Outflow Rate 取决于所连接的 Pipe 数量。例如，若连接了两个 Pipe，则在所连接 Pipe 的 Outflow Rate 允许的情况下，指定的 Outflow Rate 会流经每一条 Pipe。

若只想让指定数量从对象流出，请连接单条 Pipe，之后再将其拆分为多条 Pipe。

当空 Tank 的 Outflow Rate 大于 Inflow Rate，或满 Tank 的 Inflow Rate 大于 Outflow Rate 时，Plant Simulation 会显示错误消息。不要忽略这些错误消息，而应创建 Sensor 并编写处理这些情况的 Method。这些 Sensor 必须通过开启或关闭相连的 Pipe，防止 Tank 变满或变空。

**SimTalk：** `OutflowRate [SimTalk] - Tank`

### Volume（容积）[Tank]

在文本框中输入 Tank 的 Volume，即物料在储罐中所占的空间。

**SimTalk：** `Volume [SimTalk] - Tank`

### Shift Calendar（班次日历）[Tank]

选择 ShiftCalendar。它包含装置中的班次数据，并控制 Tank 在哪些班次工作。

**备注：**

- 点击省略号按钮，在 *Select Object* 对话框中选择 ShiftCalendar。
- 也可以不从省略号按钮选择，而是选中 Frame 中的 ShiftCalendar，将其拖放到文本框中。

这会自动将对象加入 ShiftCalendar 的 *Resources* 选项卡上的对象列表中。

**SimTalk：** `ShiftCalendarObject [SimTalk] - material flow objects`

**参见：** ShiftCalendar [object]、Associated Shift Calendar、Select Object [for controls]

### Current Material（当前材料）[Tank]

显示位于 Tank 中的 *Current Material* 的名称。

**备注：** 名称不区分大小写，与对象的属性和方法的名称一样。为节省内存并提高访问速度，所有使用这种不区分大小写字符串的位置都指向主内存中的同一个字符串。可见且意想不到的结果是：字符串的首次出现决定了该字符串的大小写写法。在 SimTalk 中可使用 `~=` 运算符以不区分大小写的方式比较字符串（见 *Relational Operators*）。

Tank 在任意时刻只能容纳一种物料。在 Tank 排空之前，新物料的流入会被阻止，因此不能在其完全排空之前让另一种物料流入。

**SimTalk：** `CurrentMaterial [SimTalk] - Tank`

### Current Fill Level（当前液位）[Tank]

显示 Tank 中物料的 *Current Fill Level*。Tank 在流出侧显示当前液位。

**SimTalk：** `CurrentFillLevel [SimTalk] - Tank`

### Current Amount（当前数量）[Tank]

显示位于 Tank 中的物料的 *Current Amount*。

**SimTalk：** `CurrentAmount [SimTalk] - Tank`

### Current Inflow Rate（当前流入速率）[Tank]

显示 *Current Inflow Rate*，即每秒流入 Tank 的物料升数。

**SimTalk：** `CurrentInFlowrate [SimTalk]`

### Current Outflow Rate（当前流出速率）[Tank]

显示 *Current Outflow Rate*，即每秒流出 Tank 的物料升数。

**SimTalk：** `CurrentOutFlowrate [SimTalk]`

## Sensors（传感器）[Tank]

要在 Tank 中创建传感器，点击 **Sensors**。该按钮会打开 *Sensor List* 对话框，可在其中新建传感器，或修改、删除现有传感器。

操作步骤如下：

- 要新建传感器，点击 **New**。
- 要编辑传感器的设置，点击 **Edit** 或双击传感器列表中的传感器名称。
- 要删除在传感器列表中选中的传感器，点击 **Delete**。

对于 Tank，可以：

- 选择传感器在 Tank 中的 *Position* 是相对位置还是绝对位置。
- 选择当物料数量 *Exceeded*（超过）传感器位置时是否触发传感器。
- 选择当物料数量低于该位置，即 *Underrun*（低于）时是否触发传感器。
- 选择或创建传感器触发的 *Control*。

**参见：** _Methods of the Sensors of the Tank、_Attributes of the Sensors of the Tank

### Position（位置）[Tank]

从下拉列表中选择传感器在 Tank 中的 *Position* 类型，然后在 *Position* 文本框中输入传感器位置。

**备注：** 可选择以下设置之一：

- **Relative（相对）**：输入 0 到 1 之间的值，即 0% 到 100%。Plant Simulation 以 0..1 为单位显示。
- **Absolute（绝对）**：输入 0 到所指定 Volume 之间的值。Plant Simulation 以 `l`（升）为单位显示。

**SimTalk：** `Position [SimTalk] - Tank`、`PositionType [SimTalk]`

### Exceeded（超过）[复选框]

若要在 Tank 中的物料数量 *Exceeded*（超过）该数量，即位于传感器位置之上时触发传感器，请选中此复选框。

**SimTalk：** `Exceeded [SimTalk]`

### Underrun（低于）[复选框]

若要在 Tank 中的物料数量 *Underrun*（低于）该数量，即位于传感器位置之下时触发传感器，请选中此复选框。

**SimTalk：** `Underrun [SimTalk]`

### Control（控制）[Tank]

修改对象的内置行为。对象会根据所选设置调用 Control。

输入 Sensor Control 后，Frame 中对象的上下文菜单会显示 *Controls* 命令，然后可在子菜单上选择传感器控制的名称进行编辑。

**选择现有 Method 的路径**

- 点击省略号按钮，在 *Select Object [for controls]* 对话框中导航到 Method 的位置并点击 OK。这会把 Method 名称插入 Control 文本框。
- 在文本框中按 F2 打开 Method，然后输入 Control 的源代码。
- 也可以不选择 Select Object，而是选中 Frame 中的 Method，将其拖放到文本框中。

**创建作为对象 Method 的控制**

按如下步骤将控制创建为数据类型为 Method 的用户自定义属性：

- 在文本框中输入一个有意义的名称，并选择 *Create Control* [context menu]。Plant Simulation 会插入 `self.你输入的控制名称`，例如 `self.A1Ctrl`。
- 在空文本框上选择 *Create Control*。Plant Simulation 会插入 `self.On内置控制名称`，例如 `self.OnEntrance`。

在弹出的 Method 中输入该控制的源代码。

之后要编辑源代码：

- 按 F2。
- 或按住 Shift 并双击文本框。
- 或在上下文菜单中选择 *Open Object*。
- 或点击 *User-defined* 选项卡并双击列表中的 Method 名称。

要删除此控制，删除用户自定义属性即可。若只从文本框中删除名称，用户自定义属性会被保留。

标准传感器控制作为用户自定义属性如下所示：

```simtalk
self.OnEntrance
```

**参数**

可以指定以下参数：

- 传感器调用此 Method 时，会把 Sensor-ID 作为可选参数传入。若 Method 期望一个数据类型为 integer 的参数，传感器会把 Sensor-ID 传给 Method。若不指定 integer 参数，Method 会被无参调用。
- 数据类型为 boolean 的可选参数 *Exceeded* 向用户显示传感器位置是 Exceeded 还是 Underrun。

**SimTalk：** `sensorID(sensorID).Control [SimTalk] - sensor, Tank`、`ID [SimTalk] - Tank`

**参见：** Select Object [for controls]

## Tab Times（时间选项卡）

按 *Tab Times* 中的说明定义时间。

从下拉列表中选择一个分布并输入该分布所需的值。Plant Simulation 会沿选项卡上边框显示参数。也可以选择常量时间（`Const`）。

可使用方法 `setTypeAndAttr [SimTalk]` 设置分布类型和完整的参数集。

**参见：** Set-up Time [general description]、`SetupTime [SimTalk] - fluid objects`、Select the Set-Up Time

## Tab Failures（故障选项卡）

按 *Tab Failures* 中的说明定义故障。

## Tab Statistics（统计选项卡）[Tank]

除 *Tab Statistics* 中所述的值外，Tank 的 *Statistics* 选项卡还显示以下对象特定值。

| Item（英文） | 描述 | 只读属性 |
| --- | --- | --- |
| Total Throughput | 显示流经 Tank 的物料数量。 | `StatDeleted [SimTalk] - Drain` |
| Relatively Empty | 显示在统计采集期间 Tank 处于 Empty 状态的时间占 Tank 可用时间的比例。 | `StatRelativeEmptyPortion [SimTalk]` |
| Relatively Full | 显示在统计采集期间 Tank 处于满状态的时间占 Tank 可用时间的比例。 | `StatRelativeFullPortion [SimTalk]` |
| Relative Occupation | 显示在统计采集期间 Tank 未暂停且未故障时，所有物料停留时间的总和。 | `Name [SimTalk] - MUs` |

## Tab Importer（导入器选项卡）

在 *Tab Importer* 上可以定义用于加工零件、为某类型零件进行换装设置以及维修该站点的服务。

要在 Statistics Report 中查看 Importer Statistics，可执行以下任一操作：

- 在对象的对话框中选择 **View > Show Statistics Report**。
- 在 Frame 中右键点击对象，选择 *Show Statistics Report*，或按 F6。
- 点击 Home 功能区选项卡上的 *Show Statistics Report*。

**参见：** Processing Importer、Set-up Importer、Failure Importer

## Tab User-defined（用户自定义选项卡）

按 *Tab User-defined* 中的说明定义自己的属性。

## Navigate Menu（导航菜单）

相关命令见 *Navigate Menu*。

## View Menu（视图菜单）

View Menu 提供访问其功能的命令，也提供与 Transport Importer 相关的命令。

- Exporters [on View menu]
- Unavailable Services [on View menu]
- Services [on View menu]
- Associated Workplaces [on View menu]

**参见：** View Menu [general description]、Transport Importer

## Tools Menu（工具菜单）

相关命令见 *Tools Menu*。

## Help Menu（帮助菜单）

相关命令见 *Help Menu*。

## Tank 的方法（Methods of the Tank）

Tank 提供：

- The General Methods of the Tank（Tank 的通用方法）。
- The Methods of the Sensors of the Tank（Tank 传感器的方法）。
- The Methods of the Fluid Objects（流体对象的方法）。
- The Methods of All Objects（所有对象的方法）。

要查看对象的所有方法、只读属性和属性，请打开 *Show Attributes and Methods* 窗口（图以 Station 对象为例进行说明）。

- 选择 Class Library 上下文菜单上的 *Show Attributes and Methods*，可显示所选 Class 的方法、只读属性和属性（见 Class [general description]）。
- 按 F8 键，或点击插入了实例的 Frame 的 Home 功能区选项卡上的 *Show Attributes and Methods*，可显示所选 Instance 的方法、只读属性和属性（见 Instance [general description]）。

可以通过对话框中的复选框、文本框和下拉列表，或通过给相应属性赋值来设置和获取属性值。

例如，设置属性值：

```simtalk
MyFluidDrain.Pause := true
```

获取属性值：

```simtalk
print MyFluidDrain.Pause
posit := MyStation.Cont.XPos
```
