# Self & Camera Animations — 摘要

本目录包含 SimTalk 中用于控制 **Self Animations（自身动画）** 与 **Camera Animations（相机动画）** 的 3D 动画属性与方法参考，完整内容见 [self-camera-animations.md](self-camera-animations.md)。

## 概览

- **Self Animations（自身动画）**：除 Folder、Connector、Interface 和 MU 之外的所有对象均可用。
- **Camera Animations（相机动画）**：仅 **Frame** 对象可用。

两者都可将全部（或某一类型的所有）动画缓冲到一个 `any` 类型的变量中：

```simtalk
var a : any := .Materialflow.PickAndPlace._3D.SelfAnimations
var a : any := .Models.Model._3D.CameraAnimations
```

---

## Self Animations（自身动画）

### 设置属性

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| `_3D.AniRotationAxis` | `real[3]` | 设置 `scheduleRotation` 的旋转轴（X/Y/Z 分量） |
| `_3D.AniRotationCenter` | `length[3]` | 设置 `scheduleRotation` 的旋转中心（X/Y/Z 位置） |
| `_3D.AniTranslationDirection` | `length[3]` | 设置 poses 动画的平移方向 |

### 每个已保存动画路径的方法

| 方法 | 返回 | 说明 |
| --- | --- | --- |
| `.delete` | `boolean` | 删除指定 Self Animation（生成的动画不可删除） |
| `.getTable` | — | 将动画数据写入表格（自动格式化） |
| `.IsCurve` / `.IsLine` / `.IsSpline` | `boolean` | 判断动画类型（Polycurve / Lines / Spline） |
| `.play([Backwards])` | `time` | 调度并播放已保存动画（隐式先 reset） |
| `.schedule([Backwards])` | — | 调度动画（不播放，需再调用 `playAnimation`/`play`） |
| `.setTable(Source)` | — | 用表格数据覆盖动画（表格须格式正确） |

### Self Animations 主要方法与属性

- **只读属性**：`AnimationTimeBlock`、`AnimationTimeTotal`（下一个/所有动画块预计所需时间）。
- **创建动画路径**：`createAnimationCurve` / `createAnimationLine` / `createAnimationSpline`（分别创建 Polycurve / Lines / Spline 类型，返回 `boolean`）。
- **动画块控制**：`deleteAllAnimationBlocks`、`deleteNextAnimationBlock`、`startNextAnimationBlock`。
- **播放控制**：`play`、`pause`、`resetAnimation`。
- **匿名动画（一键播放）**：
  - `playRotation(Start, Target, AngleVelocity) → time` / 简写 `_3D.playRotation(...)`
  - `playTranslation(Start, Target, Speed) → time` / 简写 `_3D.playTranslation(...)`
  - `scheduleRotation` / `scheduleTranslation`（仅调度，不播放）
- **数据访问**：`getAnimation(Name|Index)`（按名称或索引取动画）、`getTable` / `setTable`。

---

## Camera Animations（相机动画）

仅 **Frame** 提供。其方法与 Self Animations 高度对应，差异点如下：

### 每个已保存动画路径的方法

| 方法 | 说明 |
| --- | --- |
| `.delete` | 删除指定 Camera Animation |
| `.getTable` / `.setTable` | 读取 / 覆盖动画数据 |
| `.IsCurve` / `.IsLine` / `.IsSpline` | 判断动画类型 |
| `.play([Backwards, Factor])` | 播放动画，`Factor` 为速度倍率（0.5 更慢、2 更快） |
| `.schedule([Backwards, Factor])` | 调度动画（不播放） |

### Camera Animations 主要方法与属性

- **只读属性**：`AnimationTimeBlock`、`AnimationTimeTotal`，以及额外的 `Count`（已保存动画路径数量，`integer`）。
- **创建动画路径**：`createAnimationCurve` / `createAnimationLine` / `createAnimationSpline`。
- **播放控制**：`play`、`pause`、`resetAnimation`。
- **数据访问**：`getAnimation(Name|Index)`、`getTable` / `setTable`。

> 注意：Camera Animations 中一个 block 通常只包含单个动画（无重叠）。

---

## 关键区别速查

| 维度 | Self Animations | Camera Animations |
| --- | --- | --- |
| 可用对象 | 除 Folder/Connector/Interface/MU 外的所有对象 | 仅 Frame |
| 额外属性 | — | `Count` |
| 播放/调度额外参数 | — | `Factor`（速度倍率） |
| 一键匿名播放 | `playRotation` / `playTranslation`（含简写） | 无 |
| block 重叠 | 可能重叠 | 一般无重叠 |
