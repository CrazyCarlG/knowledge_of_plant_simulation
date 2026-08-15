# Turntable Attributes — 目录说明

本目录汇总了 **Turntable（转台）** 对象的属性文档。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `attributes.md` | Turntable 属性的 Markdown 汇总文档（本目录唯一的 md 文件） |
| `attributes.txtx` | 同一文档的纯文本提取版（内容与 `attributes.md` 一致） |
| `Plant-Simulation-Help2606_5302-5316.pdf` | 源帮助文档 PDF |

> 本目录下没有子文件夹，因此没有其他 `README.md` 需要合并。

## 文档来源与结构

文档说明 Turntable 对象提供了以下属性来源：

- 目录中列出的本对象属性
- All Objects（所有对象）的属性
- Material Flow Objects（物流对象）的属性

可通过 **Show Attributes and Methods** 窗口查看对象的全部属性、方法和只读属性：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods** 查看选中类。
- 按 **F8** 键，或点击 Frame 的 Home 功能区选项卡中的 **Show Attributes and Methods** 查看选中实例。

属性的值既可以通过对话框窗口中的复选框、文本框和下拉列表设置/读取，也可以通过 SimTalk 给相应属性赋值/取值：

```simtalk
-- 设置属性值
MyTurntable.GoToDefaultPosition := false

-- 读取属性值
print MyTurntable.GoToDefaultPosition
posit := MyStation.Cont.XPos
```

## 属性清单

| 属性 | 语法 | 类型 | 功能摘要 |
| --- | --- | --- | --- |
| `StatRotationLoadedTime` | `<Path>.StatRotationLoadedTime → time` | `time`（只读） | 返回转台载货旋转（MU 在台面上）的总时间 |
| `AutomaticStop` | `<Path>.AutomaticStop:boolean` | `boolean` | 不输送 MU 时自动把当前速度设为 0（空载或阻塞）；速度为 0 时 Energy State 变为 operational |
| `DefaultAngle` | `<Path>.DefaultAngle:real` | `real` | 转到默认位置时端点侧面旋转到的角度（度）；转到起点一侧需加 180° |
| `GoToDefaultPosition` | `<Path>.GoToDefaultPosition:boolean` | `boolean` | MU 离开且无新 MU 待旋转时是否转回默认位置（true/false）；复位时使用 `DefaultAngle` |
| `Length` | `<Path>.Length:length` | `length`（watchable） | 转台长度 |
| `MURotationAttribute` | `<Path>.MURotationAttribute:string` | `string` | 触发 MU 旋转的用户自定义属性名（boolean 类型属性或返回 boolean 的方法）；仅当 Exit Angle Table 侧边选 Any 时评估 |
| `RotateWhen` | `<Path>.RotateWhen:string` | `string` | 转台何时朝目标工位旋转：`"Completely entered"` / `"Rotation point reached"` / `"Centered"` / `"User-defined with Sensor"` |
| `RotationPoint` | `<Path>.RotationPoint:length` | `length` | 旋转支点位置，取值 0 到 Length 之间，0 表示插入起点 |
| `RotationTimePer90Degrees` | `<Path>.RotationTimePer90Degrees:time` | `time` | 转台旋转 90° 所需时间 |
| `Speed` | `<Path>.Speed:speed` | `speed`（watchable） | 转台旋转速度，`-1` 表示无限速度 |
| `TargetCtrl` | `<Path>.TargetCtrl:method` | `method` | 指定 MU 完全移上转台或到达旋转中心时调用的 Method（Target Control），在方法中用 `setDestination` 设置目标 |
| `Width` | `<Path>.Width:length` | `length`（watchable） | 转台宽度 |

### 属性要点说明

- **StatRotationLoadedTime**：虽列于本属性文档中，但其类型为只读属性，只能查询、不能设置，对应 Statistics 选项卡中 Rotation Loaded 的统计项，另见 Statistics report、Rotation Time。
- **AutomaticStop**：对应对话框中的 Automatic Stop 复选框，另见 Operational [energy]。
- **DefaultAngle / GoToDefaultPosition**：二者配合使用，分别对应 Default Angle 文本框与 Go to Default Position 复选框；`GoToDefaultPosition` 设为 `true` 且复位模型时使用 `DefaultAngle` 作为实际角度。
- **Length / Width**：均为 `length` 类型且 watchable，在 SimTalk 2.0 中可直接跟单位（`m`、`mm`、`km`、`cm`、`yd`、`ft`、`in`），如 `10m`、`10.2m`。
- **MURotationAttribute**：对应属性页中的 MU Leaves Backwards Depends On 设置。
- **RotateWhen**：对应 Strategy 下拉列表（Turnplate）；选 `"User-defined with Sensor"` 时转台不会自动旋转，需在 Sensor Control 中调用 `setDestination`。
- **RotationPoint**：对应 Rotation Point 文本框。
- **RotationTimePer90Degrees**：对应 Rotation Time per 90° 文本框，输入 0 则瞬时旋转、不消耗时间。
- **Speed**：对应 Conveyor Speed 文本框；在 SimTalk 2.0 中可指定速度单位 `mps`、`fps`、`kmh`、`mph`。
- **TargetCtrl**：对应 Target Control（Turntable）；与 Exit Control 不同，调用时 MU 尚未准备离开对象。
- **Width**：对应 Width 文本框。

## 附：文档中同时出现的对象说明

本目录文档末尾还包含 **Turnplate [object]** 对象说明，用于建模旋转平台、旋转装载零件并保证离开零件方向一致（典型应用如包裹分拣中统一方向以便条码扫描）：

- 转台容量为 1，同一时刻只能有一个 MU 位于其上。
- 当 MU 的预订点（booking point）到达转台旋转中心时，MU 移上转台并开始旋转。
- 旋转完成后 MU 离开转台。
- 输送方向为单向，MU 不能先前进再后退。
- MU 长度不能超过转台自身的 Length。
- 旋转中心默认位于转台中心。
- 旋转耗时按 90° 步长设置，输入 0 则瞬时旋转。
- 旋转角度应为 90° 的倍数，否则 Plant Simulation 会取整到最接近的 90° 倍数；可输入大于 360° 的值（须能被 90 整除）以多次旋转，用于模拟收缩包装机等。
- 默认顺时针旋转 90°。
- MU 旋转并离开后，转台返回起始位置。
- 可在 Length-oriented Objects 的 Appearance 选项卡上选择不同配置。

## 相关对象与属性继承

Turntable 的属性体系继承自以下对象类别：

- All Objects（所有对象）的属性
- Material Flow Objects（物流对象）的属性

如需查看完整属性列表，请打开 **Show Attributes and Methods** 窗口。
