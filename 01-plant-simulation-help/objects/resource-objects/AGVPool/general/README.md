# AGVPool (General)

本目录包含 AGVPool 对象的通用帮助文档。内容源自 `general.md`（结构化 Markdown 版本）与 `general.txtx`（帮助系统的原始提取文本）。二者描述同一对象，此处合并总结。

## 概述

**AGVPool** 对象用于创建自动导引车（AGV，Automated Guided Vehicles），从而在工厂中建模 **不依赖固定路线网络** 的 AGV 系统（AGVS）。

- 可用它来建模工厂的调度员或车间的领班。
- 尤其适用于在单一生产线上生产**小批量、多品种**的产品：AGV 在模块化布局的工位间运输已装载的产品，并可根据情况创建和改变虚拟行驶轨迹。
- AGVPool 初始不显示任何 AGV。要显示它们：在 AGVPool 的 **Graphics** 选项卡中勾选 **Show Content**，然后点击 **Start Simulation**。
- 使用 **Marker** 对象设置路径点，让 AGV 从 AGVPool 驶向目的地。
- 将鼠标悬停在对象上可显示提示；点击 Edit 功能区选项卡上的 **Show Manipulators** 或按 **M** 键可修改图形长度和锚点。

### 添加到仿真模型

点击 Home 功能区选项卡上的 **Manage Class Library > Basic Objects > Resources > AGVPool**。

## 对话框（Dialog Box）

双击 AGVPool 图标打开对话框。

- **编辑仿真属性**：共享属性见 *Dialog Items of the Objects*。
- **编辑动画属性**：点击仿真属性对话框左下角的 **Edit 3D Properties**，或选中对象后按空格键；点击 **Show Manipulators** 或按 **M** 操作图形。

## 选项卡 Attributes

| 设置项 | 说明 |
|--------|------|
| **AGV** | 选择 AGVS 所用车辆类型。默认使用 Class Library 的 *MUs* 文件夹中的 **Transporter**，因此 Transporter 的方法、属性与只读属性同样适用于 AGV。自由行驶的 AGV 还可定义 Distance Control 参数：Length Zone 1、ΔWidth Zone 1、Length Zone 2、ΔWidth Zone 2。SimTalk：`AGV`、`AGVPool`、`StoppingCounter`；另见 `setRoute`、`setRouteSegments`。 |
| **Amount** | 设置 AGVS 使用的车辆数量，仿真初始化阶段创建对应数量的 AGV。SimTalk：`Amount`。 |
| **Shift Calendar** | 选择包含班次数据、控制 AGVPool 工作班次的 **ShiftCalendar**（点击省略号按钮选择，或从 Frame 中拖入）。SimTalk：`ShiftCalendarObject`。 |

## 选项卡 Statistics

| 统计项 | 说明 | 只读属性 |
|--------|------|----------|
| Paused | 统计周期内 AGVPool 处于暂停状态的时间占比 | `StatPausingCount` |
| Unplanned | 统计周期内 AGVPool 未计划（未排班）工作的时间占比 | `StatUnplannedPortion` |
| Average Traveled Distance | AGV 从 AGVPool 到目的地行驶的平均距离（米） | `StatAverageTraveledDistance` |

查看统计报告：在对话框中选择 **View > Show Statistics Report**，或点击 Home 功能区选项卡的 **Show Statistics Report**，或右键对象选择 **Show Statistics Report**。

## 选项卡 User-defined

自定义属性，见 *Tab User-defined*。

## Navigate Menu

命令见 *Navigate Menu*。

## View Menu

提供以下命令：Refresh、Show Attributes and Methods、Assigned AGVs、Associated Shift Calendar。SimTalk：`updateDialog`。

- **Assigned AGVs**：打开列表，显示 AGVPool 管理的所有 AGV。SimTalk：`getAssignedAGVsTable`。

## Tools Menu

- Edit Controls > Init control
- Edit Observers

## Help Menu

命令见 *Help Menu*。

## AGVPool 的方法

AGVPool 提供：
- 目录中列出的方法
- 所有对象共有的方法（*Methods of All Objects*）

查看全部方法、只读属性与属性：在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**（查看所选 Class），或按 **F8** / 点击 Frame 的 **Show Attributes and Methods**（查看所选 Instance）。

## 代码示例（SimTalk）

以下示例通过 Broker 的 Importer Request Control 将零件分配给可用的 worker/AGV：

```simtalk
t.create
obj.imp.getAlternativeServices(t)
service := t[1,1][1,1]
part := @ --if part.id = 4 then debug 
end
tab.create; allWorker := WorkerPartAssignment
if part /= void 
    j := allWorker.getRowNo(part)
    if j = -1 
        j := 1
        while j<= allWorker.yDim AND allWorker[0,j]/=void 
            j := j + 1
        end
        if j<= allWorker.yDim 
            allWorker[0,j] := part
            expObj := allWorker[1,j]
            tab.writeRow(1,1, expObj, service, 1 )
            broker.engage( obj, type, tab )
        end
    else
        expObj := allWorker[1,j]
        tab.writeRow(1,1, expObj, service, 1 )
        broker.engage( obj, type, tab )
    end
end
```

相关：`engage` [SimTalk]，另见 **Importer Request Control [Broker]**。
