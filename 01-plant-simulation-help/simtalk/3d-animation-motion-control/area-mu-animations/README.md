# Animation Area & MU Animations — 目录说明

本目录收录了 Plant Simulation SimTalk 中用于访问 **3D 动画区域（Animation Area）** 以及操作 **MU 动画（MU Animations）** 的属性、方法与函数说明。

> 目录内没有子文件夹；内容主要来自以下两个文件，二者描述的是同一主题，其中 `.md` 为整理后的 Markdown 版本，`.txtx` 为 Plant Simulation Help 的原始文本导出。

## 文件清单

| 文件 | 说明 |
|---|---|
| `area-mu-animations.md` | 整理后的 Markdown 文档，按条目结构化列出了所有 `_3D.*` 动画区域属性/方法及 `MUAnimations.*` 动画函数 |
| `area-mu-animations.txtx` | Plant Simulation Help 的原始文本导出，包含相同的 API 参考内容 |

---

## 内容总结

SimTalk 提供以下两类能力：

1. **访问动画区域（Animation Area）**——面向具有矩阵装载空间的对象（`ParallelStation`、`Store`、`Transporter`、`Container`）、`PlaceBuffer` 以及 `Worker`。
2. **MU 动画（MU Animations）**——面向所有能接收部件（MU）或 Worker 的对象，包括除 `Connector`、`Interface` 外的所有物料流对象、纯动画对象（可通过 `_3D.getObject` 寻址）以及 Frame。

所有属性/方法均可通过 Method Editor 的 **Auto Complete**（Edit 功能区）查看与访问。

### 一、动画区域（Animation Area）

> 动画区域设置仅适用于具有矩阵装载空间的对象（`ParallelStation`、`Store`、`Transporter`、`Container`）、`PlaceBuffer` 和 `Worker`。除非预定义设置不满足需求，否则一般可直接使用预定义设置。

| 属性/方法 | 语法 | 类型 | 说明 |
|---|---|---|---|
| `_3D.convertMUAnimationAreaToPaths` | `<Path>._3D.convertMUAnimationAreaToPaths` | Method | 将动画区域转换为带存储位置的动画路径 |
| `_3D.createMUAnimationAreaFromPaths` | `<Path>._3D.createMUAnimationAreaFromPaths → boolean` | Method | 从动画路径为 MU 创建动画区域；`true` 表示有足够数据完成转换 |
| `_3D.MUAnimationAreaAbsoluteCenter` | `<Path>._3D.MUAnimationAreaAbsoluteCenter:real[3]` | Attribute | 以绝对值设置动画区域中心点（X/Y/Z），可取任意正负值 |
| `_3D.MUAnimationAreaAbsoluteSize` | `<Path>._3D.MUAnimationAreaAbsoluteSize:real[2]` | Attribute | 设置动画区域的绝对长度与绝对宽度（0 到任意大小） |
| `_3D.MUAnimationAreaEnabled` | `<Path>._3D.MUAnimationAreaEnabled:boolean` | Attribute | 激活（`true`）/关闭（`false`）动画区域 |
| `_3D.MUAnimationAreaMURotation` | `<Path>._3D.MUAnimationAreaMURotation:real/real[3]` | Attribute | 设置动画区域上 MU 的旋转；单值表示绕负 z 轴旋转，三值数组定义旋转轴分量 |
| `_3D.MUAnimationAreaOrientation` | `<Path>._3D.MUAnimationAreaOrientation:string` | Attribute | 设置动画区域朝向：`"XY-plane"`、`"XZ-plane"` 或 `"YZ-plane"` |
| `_3D.MUAnimationAreaRelativeCenter` | `<Path>._3D.MUAnimationAreaRelativeCenter:real[3]` | Attribute | 以相对值设置动画区域中心点（X/Y/Z），可取任意正负值 |
| `_3D.MUAnimationAreaRelativeSize` | `<Path>._3D.MUAnimationAreaRelativeSize:real[2]` | Attribute | 设置动画区域的相对长度与相对宽度（0 到任意大小） |
| `_3D.MUAnimationAreaShowMUsAsCuboids` | `<Path>._3D.MUAnimationAreaShowMUsAsCuboids:boolean` | Attribute | 以立方体（`true`）或 MU 实际图形（`false`）动画 MU；立方体动画明显更快 |

### 二、MU 动画（MU Animations）

- 可将某种类型的全部动画缓存到一个 `any` 类型变量中，例如 `var a : any := .Materialflow.PickAndPlace._3D.MUAnimations`。
- 动画路径类型包括 **Polycurve（曲线）**、**Spline（样条）**、**Lines（折线）** 与 **Point（单个锚点）**，可通过 `IsCurve` / `IsSpline` / `IsLine` / `IsPoint` 判断。
- 部分对象带有**自动生成动画**（如 `Conveyor` 的 `Default` 路径），不可删除、不可覆盖；若创建同名动画，则同名动画优先。

#### 单个动画路径（`_3D.MUAnimations.<AnimationPathName>.*`）

| 属性/方法 | 语法 | 类型 | 说明 |
|---|---|---|---|
| `.delete` | `<Path>._3D.MUAnimations.<AnimationPathName>.delete → boolean` | Method | 删除指定 MU 动画；不能删除自动生成动画 |
| `.getMUAnimationPosition` | `<Path>._3D.MUAnimations.<AnimationPathName>.getMUAnimationPosition(RelPos/AbsPos:real/length) → length[3]` | Method | 返回 MU 在指定位置的预期坐标；`real` 表示相对位置（0–1），`length` 表示距起点绝对距离 |
| `.getTable` | `<Path>._3D.MUAnimations.<AnimationPathName>.getTable(Target:table)` | Method | 将指定动画的全部已保存动画数据格式化后写入表格 |
| `.setTable` | `<Path>._3D.MUAnimations.<AnimationPathName>.setTable(Source:table)` | Method | 用传入表格数据覆盖指定动画；表格格式须正确，否则被取消 |
| `.IsCurve` | `<Path>._3D.MUAnimations.<AnimationPathName>.IsCurve → boolean` | Read-only | 是否为 Polycurve 类型 |
| `.IsGenerated` | `<Path>._3D.MUAnimations.<AnimationPathName>.IsGenerated → boolean` | Read-only | 是否自动生成 |
| `.IsLine` | `<Path>._3D.MUAnimations.<AnimationPathName>.IsLine → boolean` | Read-only | 是否为 Lines 类型 |
| `.IsPoint` | `<Path>._3D.MUAnimations.<AnimationPathName>.IsPoint → boolean` | Read-only | 是否为仅含单个锚点的 Lines 类型 |
| `.IsSpline` | `<Path>._3D.MUAnimations.<AnimationPathName>.IsSpline → boolean` | Read-only | 是否为 Spline 类型 |
| `.Length` | `<Path>._3D.MUAnimations.<AnimationPathName>.Length → length` | Read-only | 返回动画的物理长度 |
| `.PathAnchorPoint` | `<Path>._3D.MUAnimations.<AnimationPathName>.PathAnchorPoint:void/real[3/7]` | Attribute | 将动画设为单个点；3 值数组设置位置（旋转角 0、轴 `[0,0,-1]`），7 值数组设置位置 + 旋转角 + 旋转轴；读取返回 7 值数组，非单点折线返回 `void` |

#### 动画集合（`_3D.MUAnimations.*`）

| 属性/方法 | 语法 | 类型 | 说明 |
|---|---|---|---|
| `_3D.MUAnimations.Count` | `<Path>._3D.MUAnimations.Count → integer` | Read-only | 返回已保存动画路径的数量 |
| `createAnimationCurve` | `<Path>._3D.MUAnimations.createAnimationCurve(Name:string) → boolean` | Method | 创建 Polycurve 类型动画路径；`true` 表示名称未占用、创建成功 |
| `createAnimationLine` | `<Path>._3D.MUAnimations.createAnimationLine(Name:string) → boolean` | Method | 创建 Lines 类型动画路径 |
| `createAnimationPoint` | `<Path>._3D.MUAnimations.createAnimationPoint(IndexX:integer, IndexY:integer, Position:length[3]) → boolean` | Method | 在指定索引位置创建单个动画点（即仅含一点的 Lines 路径） |
| `createAnimationSpline` | `<Path>._3D.MUAnimations.createAnimationSpline(Name:string) → boolean` | Method | 创建 Spline 类型动画路径 |
| `getAnimation` | `<Path>._3D.MUAnimations.getAnimation(Name:string / Index:integer / PositionX:integer, PositionY:integer)` | Method | 按名称、序号或装载空间索引对返回指定动画；`getAnimation(1,1)` 等价于 `getAnimation("#0#0")`；名称或索引对不存在时返回 `void`（其余错误仍会打开调试器） |
| `getTable` | `<Path>._3D.MUAnimations.getTable(Target:table)` | Method | 查询所有已保存动画数据并写入表格（自动格式化） |
| `setTable` | `<Path>._3D.MUAnimations.setTable(Source:table)` | Method | 用表格数据覆盖已保存动画；自动生成动画不可覆盖 |

> **路径扩展访问**：若已保存动画的名称是合法的 SimTalk 标识符（如 `Default`），可通过路径扩展直接访问，例如 `Assembly._3D.MUAnimations.D...` 会由路径扩展提示补全。

#### 其他相关成员

| 属性/方法 | 语法 | 类型 | 说明 |
|---|---|---|---|
| `_3D.AnimationObject` | `<Path>._3D.AnimationObject:string` | Attribute | 设置替代动画对象；默认 `""` 表示对象自身承担动画与运输；`PickAndPlace` 机器人例外，其值包含动画轴 |
| `_3D.MUSideToAttach` | `<Path>._3D.MUSideToAttach:string` | Attribute | 设置 MU 附着到对象的侧面（`"Bottom"`、`"Top"`、`"Front"`、`"Back"`、`"Left"`、`"Right"`、`"Booking point"`、`"Center bottom"` 及各种 `"... bottom"` 组合） |
| `_3D.resetAnimationTime` | `<Path>._3D.resetAnimationTime` | Method | 将位于该对象上的 MU 的动画时间重置为 0；`Worker` 不支持 |
| `MUAnimations.copyFromSimulationObject` | `<Path>.MUAnimations.copyFromSimulationObject` | Method | 将拥有该可动画对象的仿真对象的所有 MU 动画（及动画区域设置）复制到该可动画对象 |

**`_3D.MUSideToAttach` 取值说明**：

- `"Bottom"` / `"Top"`：分别从负/正 z 方向附着，典型用于以重心承载 MU 的站。
- `"Front"` / `"Back"`：分别从正/负 x 方向附着。
- `"Left"` / `"Right"`：分别从负/正 y 方向附着。
- `"Booking point"`：从 MU 对话框 Attributes 页设置的局部位置 `(0,0,0)` 附着。
- `"Center bottom"`：以 MU 尺寸底板的中心置于运输对象的动画路径上。
- `"... bottom"` 组合：`Front bottom` / `Back bottom` / `Left bottom` / `Right bottom` 为对应方向与 Bottom 的组合。

计算附着侧时，Plant Simulation 还会考虑 MU 的**传送方向（Conveying Direction）**、**预约点高度（Booking Point Height）**、**MU 长/宽/高**。对 `PickAndPlace` 机器人及其可动画对象，附着侧还会改变所装部件的朝向（如 `Front` 绕 y 轴转 90° 再绕 z 轴转 180°）。

---

## 关联内容（See also）

- 对话框 **Edit 3D Properties** > **MU Animation** 页签 > **Animation Area**（动画区域设置）
- `_3D.getObject`、`_3D.InheritGraphics`、`_3D.getMUAnimationPosition`、`_3D.CameraAnimations.*`
- `rotateConveyingDirection`、Conveying Direction（传送方向）、Booking Point Height（预约点高度）
- 动画区域相关：Center / Length / Width / Orientation / MU Rotation / Show MUs as Cuboids 等设置
