# Access Transformation (3D API Fundamentals — Window, Object & Appearance)

本目录收录 Plant Simulation SimTalk 3D API 中关于**访问对象**与**变换设置**的参考文档，源自
`access-transformation.txtx`（Plant Simulation Help，页码 12-666 至 12-729）。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `access-transformation.txtx` | 原始帮助文档文本（Plant Simulation Help 12-666 ~ 12-729） |
| `access-transformation.md` | 从原始文本整理出的结构化 Markdown 总结 |

> 注：本目录下没有子文件夹，因此无子级 README 需要合并。

## 内容概要

文档涵盖通过 SimTalk 的 `_3D` 前缀访问 3D 对象与变换设置的属性和方法，共分为六大主题：

### 1. 访问 3D 中的对象 (Accessing Objects in 3D)
在 3D 中访问对象的核心属性和方法：

- **存在性/数量判断**
  - `_3D.Exists`、`_3D.existsObject`、`_3D.ExistsWithAnimation` — 判断对象/可动画对象是否存在于 3D、动画功能是否激活。
  - `_3D.NumObjects` — 返回对象所含可动画对象的数量（配合 `_3D.getObject` 遍历）。
- **对象访问与检索**
  - `_3D.getObject` — 按名称或索引返回内部可动画对象。
  - `_3D.getAttribute` / `_3D.hasAttribute` / `_3D.inheritAttribute` — 读取/检查属性值、开启属性继承。
  - `_3D.InternalClassType` — 返回长度导向/点导向对象的内置英文类名。
  - `_3D.ShowUserDefinedAttributes`、`_3D.Selected` — 显示用户自定义属性、选中/取消选中对象。
- **可动画对象的增删**
  - `_3D.addObject` — 创建可动画对象。
  - `delete`（可动画对象） — 删除可动画对象。
  - `Name`、`Length`（可动画对象） — 设置可动画对象的名称与长度。
- **方向与内存**
  - `_3D.addLengthOrientation` / `_3D.removeLengthOrientation` — 设置/取消长度导向。
  - `_3D.memUsage` — 计算对象的 3D 部分占用内存。
- **界面操作**
  - `_3D.openDialog`（打开“编辑 3D 属性”对话框）、`_3D.openWindow`（在新窗口中以 3D 打开）。
- **MU 动画位置/旋转推算**
  - `_3D.getMUAnimationPosition` / `_3D.getMUAnimationRotation` — 计算 MU 在长度导向/点导向对象上的预期动画位置与旋转。
- **坐标换算**
  - `_3D.getPositionOfObject` / `_3D.getRotationOfObject` — 返回指定对象在调用对象坐标系中的位置/旋转。

### 2. 访问变换设置 (Accessing Transformation Settings)
通过 `<Path>._3D.属性名` 读取、`<Path>._3D.属性名 := 值` 设置对象的变换：

- **位置/旋转/缩放/镜像**
  - `_3D.Position`（`length[3]`）、`_3D.Rotation`（`real`/`real[4]`）、`_3D.Scale`（`real`/`real[3]`）。
  - `_3D.Mirror` — 在一个或三个平面上镜像对象（不适用于长度导向对象、MU、Connector）。
  - `_3D.Dimensions` — 设置缩放图形的尺寸（`length[3]`）。
  - `_3D.ScaleAutomatically` — MU 图形自动缩放（`boolean`）。
- **全局坐标/世界坐标**
  - `_3D.getWorldCoordinate` / `_3D.getWorldRotation` — 返回对象在最顶层 Frame 中的位置/旋转。
- **完整变换矩阵**
  - `_3D.TransformationMatrix` — 设置/获取对象的完整变换矩阵（16 值或 4×4 数组）。
  - `F3DconcatenateRotations` — 将两个旋转拼接为一个。
- **Connector 中间锚点**
  - `_3D.CornerPoints` — 设置 Connector 的中间锚点（二维 `length` 数组）。

### 3. 访问对象标题 (Accessing Object Captions)
- `_3D.NameLabelEnabled` — 显示/隐藏名称与标签。
- `_3D.NameLabelPosition` — 设置名称与标签的参考点。
- `_3D.NameLabelRotation` — 设置名称与标签的旋转。
- `_3D.NameLabelScale` — 设置名称与标签的缩放。

### 4. 访问 Frame 与 Folder 的背景色 (Background Color of Frame and Folder)
- `_3D.BackgroundColor` — 设置背景色（`integer`，通常用 `makeRGBValue`，`-1` 表示无色）。
- `_3D.BackgroundBrightness` — 设置背景四个角的亮度（`real[4]`，-1 到 1）。

### 5. 访问 Buffer 的填充水平 (Fill Level of the Buffer)
- `_3D.FillLevelDimensions`（`length[2]`）、`_3D.FillLevelPosition`（`length[3]`）、`_3D.FillLevelRotation`（`real`/`real[4]`）。
- `_3D.ShowContentsAs` — 设置 Buffer 内容显示方式（`"MUs"` / `"Fill level"` / `"Both"`）。

### 6. 访问包围盒 (Accessing the Bounding Box)
只读属性，用于测量对象可见图形的包围盒（局部对象坐标系，排除不可见图形）：

- `_3D.BoundingBoxCenter` — 包围盒中心（`length[3]`）。
- `_3D.BoundingBoxMax` — 右上顶点（`length[3]`）。
- `_3D.BoundingBoxMin` — 左下顶点（`length[3]`）。
- `_3D.BoundingBoxSize` — 包围盒尺寸，即长(X)/宽(Y)/高(Z)。

**包围盒关系：**
- `(BoundingBoxMin + BoundingBoxMax) / 2 = BoundingBoxCenter`
- `BoundingBoxMax - BoundingBoxMin = BoundingBoxSize`
- `BoundingBoxMax ≥ BoundingBoxMin`

## 来源

- `Plant Simulation Help` — 页码 12-666 至 12-729
- 文件：`access-transformation.txtx`
