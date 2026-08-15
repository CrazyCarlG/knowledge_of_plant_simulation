# Turntable Methods — 目录说明

本目录汇总了 **Turntable（转台）** 对象的方法与只读属性文档。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `methods.md` | Turntable 方法与只读属性的 Markdown 汇总文档（本目录唯一的 md 文件） |
| `methods.txtx` | 同一文档的纯文本提取版（内容与 `methods.md` 一致） |
| `Plant-Simulation-Help2606_5281-5295.pdf` | 源帮助文档 PDF |

> 本目录下没有子文件夹，因此没有其他 `README.md` 需要合并。

## 文档来源与结构

文档说明 Turntable 对象提供了以下方法来源：

- 目录中列出的本对象方法
- Curved Objects（曲线对象）的方法
- Material Flow Objects（物流对象）的方法
- All Objects（所有对象）的方法

可通过 **Show Attributes and Methods** 窗口查看对象的全部方法、只读属性和属性：
- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods** 查看选中类。
- 按 **F8** 键，或点击 Frame 的 Home 功能区选项卡中的 **Show Attributes and Methods** 查看选中实例。

## 语法约定

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>`：方法所作用对象的路径。
- `(Parameter:string)`：参数名及数据类型，可用同类型变量或返回值匹配的方法替代常量。
- `[,Parameter:boolean]`：方括号内为可选参数。
- `:= false`：参数默认值。
- `→ boolean`：方法返回值的类型。

> 注意：表达式内部的括号 `(…)` 必须输入，否则可能导致意外结果并打开调试器。

## 方法清单

| 方法 | 语法 | 功能摘要 |
| --- | --- | --- |
| `calculateAngles` | `<Path>.calculateAngles` | 计算 Turntable 与其前驱、后继相连的角度，并写入入口角度表与出口角度表 |
| `getDestination` | `<Path>.getDestination → object` | 返回 Turntable 将 MU 移动到的目标对象 |
| `getEntryAngles` | `<Path>.getEntryAngles(EntryAnglesTable:table)` | 返回入口角度表并写入指定表格 |
| `getExitAngles` | `<Path>.getExitAngles(ExitAnglesTable:table)` | 返回出口角度表并写入指定表格 |
| `goToAngle` | `<Path>.goToAngle(Angle:real)` | 设置转台端点侧面旋转到的角度 |
| `setDestination` | `<Path>.setDestination(Destination:object)` | 设置 Turntable 将 MU 移动到的目标对象 |
| `setEntryAngles` | `<Path>.setEntryAngles(EntryAnglesTable:table)` | 设置要分配给 Turntable 的入口角度表 |
| `setExitAngles` | `<Path>.setExitAngles(ExitAnglesTable:table)` | 设置要分配给 Turntable 的出口角度表 |
| `stopMU` | `<Path>.stopMU` | 在转台仍旋转时停止 MU |

### 方法要点说明

- **calculateAngles**：计算后自动将入口角度写入 Entry Angles Table、出口角度写入 Exit Angles Table。
- **getDestination / setDestination**：通常在 Target Control（TargetCtrl）中使用，用于控制 MU 的移动目标。
- **getEntryAngles / setEntryAngles**：表格包含前驱编号、名称、连接角度以及朝向转台的哪一侧；`setEntryAngles` 的说明附有按插入方向（左→右、右→左、上→下、下→上）区分的入口角度位置图。
- **getExitAngles / setExitAngles**：表格包含后继编号、名称、连接角度以及朝向后继的哪一侧；`setExitAngles` 同样附有按插入方向区分的出口角度位置图。
- **goToAngle**：仅当转台上没有 MU 且没有 MU 等待时生效。
- **stopMU**：旋转结束后 MU 会自动继续移动；通常用于传感器控制中，在 MU 到达转台末端前停止以防碰撞。

## 只读属性（Read-Only Attributes）

Turntable 提供的只读属性包括：

- 目录中列出的本对象只读属性
- All Objects 的只读属性
- Material Flow Objects 的只读属性

只读属性只能查询、不能设置，其值由 Plant Simulation 在查询时刻计算；在多数情况下，只读属性对应对象选项卡（如 Statistics 选项卡）上不可编辑的对话框项。

## 相关对象与方法继承

Turntable 的方法体系继承自以下对象类别：

- Curved Objects（曲线对象）的方法
- Material Flow Objects（物流对象）的方法
- All Objects（所有对象）的方法

如需查看完整方法列表，请打开 **Show Attributes and Methods** 窗口。
