# Station（对象）— General 总结

本目录存放 **Station**（工位）对象的一般说明文档。内容来源为 `general.md`（`general.txtx` 为其原始提取文本，两者内容一致）。以下是对其内容的总结。

## 1. Station 对象概述

**Station** 用于在**单个加工位置**上加工工件（MU），是大多数机器的建模基础。

- Station 从前驱对象接收**单个** MU，加工后，在设置时间（set-up time）与加工时间（processing time）结束后，将其移动到某个后继对象。
- 若 MU 类型不同（即名称不同），Station 必须先**设置（set up）**才能加工新类型 MU。
- 当一个工件位于 Station 上时，它不再接收其他工件，而是将后续到达的工件放入其 **Blocking List（阻塞列表）**；待再次可用后，才逐个接受并加工这些被阻塞的 MU。
- 若 Station 有多个后继，它会逐个将 MU 移动到后继上。若目标后继被阻塞（已满或故障），Station **不会**选择其他可用后继，而是停止移动并进入阻塞状态，直到该后继重新可用。可通过 **Method** 设置不同的移动行为。

> **注：** Plant Simulation 总是将 MU **作为一个整体**移动（而非连续移动）——一旦 MU 的 booking point 位于 Station 上，整个 MU 即位于其上。

- 将鼠标悬停在 Station 上可显示工具提示；点击编辑功能区标签页的 **Show Manipulators**（或按 `M`）可更改图形长度和锚点。

**添加到模型：** Home 功能区标签页 → `Manage Class Library > Basic Objects > MaterialFlow > Station`。

**示例模型：** Window 功能区标签页 → `Start Page > Getting Started > Example Models > Small Examples`。

## 2. Station 对话框

双击 Station 图标打开对话框。共享仿真属性见 *Dialog Items of the Objects*。

### 编辑 3D 属性

- 点击仿真属性对话框左下角的 **Edit 3D Properties** 按钮。
- 或选中模型中的对象并按空格键。

**视频：** https://youtu.be/PQhEriOzVzU?si=HpfLhwtUyoiMFPzx&t=22

## 3. 选项卡 Times（时间）

定义时间（设置时间、加工时间、恢复时间、节拍时间等）。从下拉列表选择分布类型并输入所需值，参数显示在选项卡上边界；也可选择恒定时间（**Const**）。分布类型与参数可用方法 `setTypeAndAttr [SimTalk]` 设置。

## 4. 选项卡 Set-Up（设置）

定义设置对象（set-up）的相关属性。

## 5. 选项卡 Failures（故障）

定义故障。

## 6. 选项卡 Controls（控制）

提供修改对象内置行为的控制项。

- 选择已有 Method 的路径：点击省略号按钮，或将 Method 拖放到文本框；在文本框中按 `F2` 打开 Method。
- 创建用户自定义属性（数据类型为 Method）作为控制：通过 **Create Control** 完成，会插入 `self.<Name>`（如 `self.A1Ctrl`）或 `self.On<内置控制名>`（如 `self.OnEntrance`）。
- 删除控制：删除相应用户自定义属性（仅删除名称不会删除该属性）。

## 7. 选项卡 Exit（出口）

选择对象将 MU 移动到哪个后继。参见 *Blocking [exit strategy]* 和 *Strategy [material flow objects]*。

## 8. 选项卡 Statistics（统计）

统计按 *Tab Statistics* 说明描述。查看 Stationary Resources 的资源统计：`View > Show Statistics Report`，右键 Frame 选择 **Show Statistics Report**，或按 `F6`。

## 9. 选项卡 Importer（导入）

定义加工工件、为某种工件类型设置工位以及维修工位的服务。查看 Importer Statistics：按 `F6` 或点击 **Show Statistics Report**。

## 10. 选项卡 Energy（能源）

选择能源设置。

## 11. 选项卡 Costs（成本）

选择成本设置。Station 加工工件期间，成本由投资成本与运营成本之和累积：

- 投资成本仅在 **折旧期（Depreciation Period）** 内累积。
- 成本作为**应计成本（accrued costs）**分配到工件上。
- 若 Station 空闲，成本作为**一般成本（general costs）**保留在 Station 上。

## 12. 选项卡 User-defined（用户自定义）

定义自定义属性。

## 13. 菜单

- **Navigate 菜单：** 命令见 Navigate Menu 说明。
- **View 菜单：** 提供访问功能的命令（Refresh Exporters、Show Statistics Report、Show Attributes and Methods、Contents、Forward Blocking List、Exit Blocking List、Services、Associated Workplaces、Associated Lockout Zones、Associated Shift Calendar）。
- **Exporters [Station]：** 打开一张表，显示所有当前导出服务的 Exporters。参见 `getExporters [SimTalk]`。
- **Services [Station]：** 打开所有已导入服务的表。故障服务名称与子表名称相同。列：Exporter 名称、提供的服务数量。参见 `getImportedServices`、`getServices`、`setAlternativeServices`、`setServices`。
- **Unavailable Services [Station]：** 显示当前不可用的 Failure、Set-up、Processing 与 Transport 服务（名称以白字红底显示）。列：Exporter 名称、已定义数量、缺失数量、替代服务名称。
- **Associated Workplaces [Station]：** 列出分配给该 Station 的所有 Workplaces。参见 `assignedWorkplaces [SimTalk]`。
- **Tools 菜单：** 命令见 Tools Menu 说明。
- **Tabs 菜单：** 显示/隐藏所选物料流对象的各个选项卡；**Inherit** 命令切换显示/隐藏选项卡的继承。
- **Help 菜单：** 命令见 Help Menu 说明。

## 14. Station 的方法

Station 提供：

- 所有对象的通用方法（Methods of All Objects）；
- 物料流对象的方法（Methods of the Material Flow Objects）。

查看方式：打开 **Show Attributes and Methods**（在实例上按 `F8`，或通过类库的上下文菜单）查看全部方法、只读属性和属性。

## 15. 代码示例：TypeStatOn [SimTalk]

根据 MU 类型激活（`true`）或停用（`false`）由 `<Path>` 指定的 Drain 的统计值收集。

- **类型：** Attribute
- **语法：** `<Path>.TypeStatOn:boolean`

```simtalk
MyDrain.TypeStatOn := false
```

**参见：** Type Dependent Statistics、`typeStatistics [SimTalk] - Drain`、`typeStatisticsCumulated [SimTalk]`

## 目录说明

- `general.md`：Station 对象通用说明的 Markdown 版本（本总结的源文件）。
- `general.txtx`：相同内容的文本提取版本。
- `Plant-Simulation-Help2606_4625-4647.pdf`：对应帮助文档的 PDF 片段。
- 本目录无子文件夹，故无子文件夹 README.md。
