# Connector — General（概述）

本目录存放 **Connector**（连接器）对象的一般说明文档。内容来源为 `general.md`（`general.txtx` 为其原始提取文本，两者内容一致）。

## 对象用途

**Connector** 用于在对象之间建立物料流连接，工件（MU）沿这些连接在设备中移动。

## 核心说明

- Connector 的**名称不可更改**。
- 它连接物料流对象或流体对象（MU 在其上移动）。
- 在层级化建模（Frame 内嵌套 Frame）时，它也能将一个对象与某个 Frame 的入口/出口（通过 **Interface** 建模）相连。
- Connector 通过连接线中部的**箭头**显示连接方向。
- 将鼠标悬停在 Connector 上，可通过工具提示查看其**前驱/后继对象**；悬停在 Frame 中的 Connector 上可查看其**源对象与目标对象**。

## 显示连接 / 连接器的锚点

- 两个对象之间**只能建立一条连接**。
- 右键对象并选择 **Reorder Successors**（重排后继）可调整后继顺序；也可通过编辑功能区标签页的 **Show Manipulators**（显示操纵器）重排连接。
- 通过起点/终点锚点的操纵器可更改 Connector 的前驱/后继，把锚点从当前对象拖到其他对象即可。
- 若场景中未选中任何对象，该命令也会显示 Connector 的位置操纵器（前提是场景中显示了 Connector）。
- 锚点（含起点与终点）可通过位置操纵器进行编辑。
- Plant Simulation 将 Connector 的起点/终点锚点显示为**半切**形状，以便清晰区分无自身长度的 Connector，并便于逐个选择。

## 添加到仿真模型

在 Home 功能区标签页点击 **Manage Class Library > Basic Objects > MaterialFlow > Connector**。

## Connector 对话框

双击插入到 Frame 中的 Connector 即可打开其对话框。

### 选项卡 Attributes（属性）

#### Width（线宽，文本框）

输入 Connector 的线宽。取值可为 `-1` 到 `100` 之间的实数：

| 值 | 含义 |
| --- | --- |
| `1` | 在缩放因子为 100% 的 Frame 窗口中为 1 像素线宽 |
| `0` | 无论 Frame 窗口是否缩放，线宽恒为 1 像素 |
| `-1` | 使 Connector 不可见 |

- Width 的数据类型为 `real`。
- 对于 3D Only 模型，可用 `0` 到 `1` 之间的值将默认线宽缩小为其分数倍。

#### Color（颜色）

点击 Color 旁的字段设置颜色：可选预定义颜色，或点击 **More Colors** → **Select** 在颜色矩阵中选取，然后点击 OK。

### 选项卡 User-defined（用户自定义）

在此定义自定义属性。

## 菜单

- **Navigate 菜单**：命令见 Navigate Menu 说明。
- **View 菜单**：提供 `Refresh`、`Show Attributes and Methods`（SimTalk：`updateDialog`）。
- **Tools 菜单**：提供 `Edit Controls`、`Edit Observers`。
- **Help 菜单**：命令见 Help Menu 说明。

## Connector 的方法

Connector 提供：
- 左侧目录中列出的方法；
- 所有对象的通用方法（Methods of All Objects）。

查看方式：打开 **Show Attributes and Methods** 窗口（在类库上下文菜单中选择，或按 F8 / 点击 Home 标签页上的 **Show Attributes and Methods**）。

## 参见

- Dialog Box of the Connector
- Connect Objects with the Connector
- Navigate Menu
- View Menu
- Tab User-defined
