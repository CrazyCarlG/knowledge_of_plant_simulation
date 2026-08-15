# Turntable Read-Only Attributes — 目录说明

本目录汇总了 **Turntable（转台）** 对象的只读属性文档。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `read-only-attributes.md` | Turntable 只读属性的 Markdown 汇总文档（本目录唯一的 md 文件） |
| `read-only-attributes.txtx` | 同一文档的纯文本提取版（内容与 `read-only-attributes.md` 一致） |
| `Plant-Simulation-Help2606_5295-5302.pdf` | 源帮助文档 PDF |

> 本目录下没有子文件夹，因此没有其他 `README.md` 需要合并。

## 文档来源与结构

文档说明 Turntable 对象提供了以下只读属性来源：

- 目录中列出的本对象只读属性
- All Objects（所有对象）的只读属性
- Material Flow Objects（物流对象）的只读属性

只读属性的值只能查询、不能设置，其值由 Plant Simulation 在查询时刻计算；在多数情况下，只读属性对应对象选项卡（如 Statistics 选项卡）上不可编辑的对话框项。

可通过 **Show Attributes and Methods** 窗口查看对象的全部方法、只读属性和属性：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods** 查看选中类。
- 按 **F8** 键，或点击 Frame 的 Home 功能区选项卡中的 **Show Attributes and Methods** 查看选中实例。

查询只读属性值的示例：

```simtalk
print Turntable.StatRotationEmptyPortion
```

## 只读属性清单

| 只读属性 | 语法 | 返回类型 | 功能摘要 |
| --- | --- | --- | --- |
| `CurrentAngle` | `<Path>.CurrentAngle → real` | `real` | 返回转台当前的旋转角度 |
| `CurrentDestinationAngle` | `<Path>.CurrentDestinationAngle → real` | `real` | 返回转台当前正在旋转到的目标角度 |
| `StatRotationEmptyPortion` | `<Path>.StatRotationEmptyPortion → real` | `real` | 统计收集期内转台空载旋转（无 MU 在台面上）的时间占比 |
| `StatRotationEmptyTime` | `<Path>.StatRotationEmptyTime → time` | `time` | 转台空载旋转（无 MU 在台面上）的总时间 |
| `StatRotationLoadedPortion` | `<Path>.StatRotationLoadedPortion → real` | `real` | 统计收集期内转台载货旋转（MU 在台面上）的时间占比 |
| `StatRotationLoadedTime` | `<Path>.StatRotationLoadedTime → time` | `time` | 转台载货旋转（MU 在台面上）的总时间 |

### 只读属性要点说明

- **CurrentAngle / CurrentDestinationAngle**：用于查询转台实时的当前角度与目标角度，例如 `print MyTurntable.CurrentAngle`。
- **StatRotationEmptyPortion / StatRotationLoadedPortion**：返回 `real` 类型的时间占比，对应 Statistics 选项卡中 Rotation Empty 与 Rotation Loaded 的统计项。
- **StatRotationEmptyTime / StatRotationLoadedTime**：返回 `time` 类型的总时长，可在 Statistics Report 的 Rotation Time 中查看。
- 上述统计类只读属性的另见条目为：Tab Statistics [Turnplate]、Statistics report, Rotation Time，以及 Empty [state, material flow objects]（空载相关）。

## 附：文档中同时出现的 Method

本目录文档开头还列出了 `stopMU`，其类型为 **Method**（方法），用于在转台仍旋转时停止 MU：

```simtalk
<Path>.stopMU
```

旋转结束后 MU 会自动继续移动；通常用于传感器控制中，在 MU 到达转台末端前停止以防碰撞。
