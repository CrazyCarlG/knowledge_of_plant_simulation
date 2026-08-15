# ShiftCalendar 对象 — 目录总结

本目录包含 Plant Simulation 帮助文档中 **ShiftCalendar（班次日历）** 资源对象的通用说明。以下是对本目录内 `general.md`（及对应原始文本 `general.txtx`）内容的总结。

## 概述

**ShiftCalendar** 对象用于在工厂仿真模型中建立班次系统并组织轮班工作。

- 可在模型中定义任意数量的班次。一个班次通过将相关物流对象的布尔属性 `Pause` 和 `Unplanned` 设为 `true` 来暂停一台或多台机器。
- 若在非计划（unplanned）时间取消 `Pause`（清除对话框中的 **Pause** 复选框，或将属性 `Pause` 设为 `false`），对象即开始工作。
- 使用 `schedule` 方法可让 ShiftCalendar 设置生产的开始/结束时间，分为：
  - **正向排程（Forward scheduling）**：从开始日期向未来推算。
  - **反向排程（Backward scheduling）**：从需求日期向过去推算开始日期。
  - 通常先从需求日期反向排程得到开始日期；若该开始日期已落在过去，则需从当前时间重新正向排程结束日期。
- 鼠标悬停可显示工具提示；点击 Edit 选项卡的 **Show Manipulators** 或按 **M** 可调整图形长度与锚点。

### 添加到模型

点击 Home 选项卡 **Manage Class Library > Basic Objects > Resources > ShiftCalendar** 即可将对象加入模型。

---

## 对话框（Dialog Box）

双击 ShiftCalendar 图标打开对话框：

- **编辑仿真属性**：共享属性参见 *Dialog Items of the Objects*。
- **编辑动画属性**：通过对话框左下角 **Edit 3D Properties** 按钮，或选中对象后按空格键打开 **Edit 3D Properties**。
- 输入数据前需先点击 **Inheritance** 复选框（使其关闭）。

---

## Active [复选框]

- 勾选后工厂按班次工作；清除则停用班次工作。
- 也可在 Frame 中右键 ShiftCalendar 选择 **Activate** / **Deactivate**。

---

## Tab Shift Times（班次时间选项卡）

在此选项卡中输入班次名称、开始时间、结束时间及休息（Pauses）时长。

- 在 **Mo, Tu, We, Th, Fr, Sa, Su** 下方勾选班次对应的工作日。
- 输入数据前先关闭 **Inheritance** 复选框。

### Shift（班次名称）
- 输入不同班次名称，例如 `Morning`、`Evening`、`Graveyard`。
- 状态图形：`Unplanned`、`Planned`。

### From / To（开始/结束时间）
- 输入 0:00–24:00 之间的小时和分钟（不支持秒）。
- 班次在一天内：结束时间大于开始时间（如 6:00–14:00）。
- 班次跨两天：结束时间小于开始时间（如 22:00–次日 6:00）。
- 不允许重叠的班次时间。

### Pauses（休息时间）
- 格式：`开始时:分-结束时:分`，多个休息用分号分隔，例如 `9:00-9:15;12:00-12:45`。
- 点击 **Apply** 可校验休息时间的格式与合理性。

---

## Tab Calendar（日历选项卡）

定义工厂全天停工或仅部分时间工作的日期，并为事件添加 **Comment** 描述。

- 使用前先关闭 **Inheritance** 复选框。
- 可右键列表字段选择 **Import** / **Export** 导入或导出日历。

### Date From / Date To
- 用日期选择器设置停工起止日期。
- 指定整日停工：仅填 **Date From**，不填 **Date To** 和 **Reduce Time To**。
- 指定连续多日停工：填写 **Date From** 与 **Date To**，不填 **Reduce Time To**。

### Reduce Time To（缩减工作时间）
- 格式：`开始时:分 - 结束时:分`，例如平安夜仅工作半天可填 `0:00 - 12:00`。
- 若缩减工作日的开始时间正好落在休息时段，则该工作日从休息开始。

### Comment
- 描述导致缩减工作时间的事件。

---

## Tab Resources（资源选项卡）

将资源（对象）分配给 ShiftCalendar。

- 资源可以是任何内置物流对象，或建模了机器的 Frame。
- 添加方式：从 Frame 窗口拖拽对象到 ShiftCalendar 图标（可多选拖拽），或直接输入路径与名称，或在物流对象的 **Controls** 选项卡 **Shift Calendar** 文本框中填写 ShiftCalendar 名称。
- 拖拽后会自动在物流对象 **Controls** 选项卡中填入 ShiftCalendar。
- 分配给班次的所有资源都会被暂停。

---

## Tab User-defined（用户自定义选项卡）

按 **Tab User-defined** 的说明定义自己的属性。

---

## 菜单

- **File 菜单**：`Import Shift Times` / `Export Shift Times`（导入/导出班次时间）、`Import Calendar` / `Export Calendar`（导入/导出日历），均基于制表符分隔的文本文件。
- **Navigate 菜单**：参见 Navigate Menu。
- **View 菜单**：`Refresh`、`Show Assigned Objects`（在 Frame 中选中分配给该 ShiftCalendar 的资源对象）、`Show Attributes and Methods`。
- **Tools 菜单**：`Edit Controls`、`Edit Observers`。
- **Help 菜单**：参见 Help Menu。

---

## 方法（Methods）

ShiftCalendar 提供：

- 目录中列出的方法；
- 所有对象的通用方法（Methods of All Objects）。

可通过窗口 **Show Attributes and Methods** 查看全部方法、只读属性与属性（类使用 Class Library 上下文菜单，实例使用 **F8** 或 Home 选项卡的 **Show Attributes and Methods**）。

---

## 相关 SimTalk 引用

文档中涉及的 SimTalk 相关项包括：`schedule`、`ShiftPlan`、`GetCurrShift`、`Calendar`、`Resources`、`Active`、`updateDialog` 等（详见各章节对应 SimTalk 说明）。
