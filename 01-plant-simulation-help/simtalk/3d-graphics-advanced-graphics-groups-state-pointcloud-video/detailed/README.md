# 图形访问详解（Accessing Graphics · SimTalk）

本目录汇总 SimTalk 中用于**访问仿真对象图形**的属性与方法。所有成员均可通过 Method Editor 的 **Auto Complete**（Edit 功能区）查看。

> 说明：本 README 是对同目录下 `detailed.md` 的内容摘要。当前目录下没有子文件夹，也没有其他 README.md，因此仅汇总 `detailed.md` 一个文档。

---

## 一、对象级图形访问（`_3D`）

以 `_3D.` 前缀访问仿真对象（`<Path>`）的图形级能力。

| 名称 | 类型 | 作用 |
|------|------|------|
| `_3D.calculateMUDimensions([OnlyVisibleGroups])` | 方法 | 根据图形计算 MU 的长/宽/高 |
| `_3D.exchangeGraphic(FilePath[, UseNewGraphicMeasurement])` | 方法 | 用文件导入的图形整体替换对象图形 |
| `_3D.ExcludeFromShowContentOfLocation` | 属性 | 隐藏/显示对象在其所在位置之外的“外部表示” |
| `_3D.exportAsJt(FilePath[, OptimizeForCAD, ExcludeInvisibleParts])` | 方法 | 导出为 `.JT` 文件 |
| `_3D.exportAsS3D(FilePath)` | 方法 | 导出为 `.s3D` 文件（含外观/动画属性与嵌入对象） |
| `_3D.exportModelingViewBitmap(...)` | 方法 | 将 3D 建模视图场景导出为 `.PNG` |
| `_3D.exportPlanningViewBitmap(...)` | 方法 | 将 3D 规划视图场景导出为 `.PNG` |
| `_3D.getGraphic(GraphicGroupName[, Path])` | 方法 | 返回指定的 graphic 或 graphic group |
| `_3D.InheritGraphics` | 属性 | 开启/关闭图形继承 |
| `_3D.optimizeObject(WithContainedObjects, OptimizeInheritance, OptimizeGraphicStructure)` | 方法 | 优化 3D 对象结构（不可逆，建议先另存模型） |
| `_3D.ShowContent` | 属性 | 显示/隐藏所包含对象的外部表示 |

要点：
- `_3D.getGraphic` 的 `Path` 参数用一维数组表示层级，支持**一基数字索引**或**名称**两种写法（不能混用）；`[]` 表示整个组，`[1]` 表示第一个直接子图形，`[1,4]` 表示第一个子图形的第 4 个子图形。缩写写法示例：`Machine._3D.default([1])`。
- `exportAsJt` 开启 `OptimizeForCAD` 时会排除标签与逻辑对象（EventController、FlowControl、所有 InformationFlow / UserInterface / GA 对象等）。
- `optimizeObject` 会丢弃数据且**不可恢复**。

---

## 二、图形级详细访问（Detailed Access To Graphics）

作用于 `getGraphic` 返回的 graphic / graphic group（`<Path>`）上，可精细控制变换、材质、命名与优化。

### 变换（Transform）

| 名称 | 类型 | 作用 |
|------|------|------|
| `Position` | 属性 | 设置图形位置 `length[3]`（X/Y/Z） |
| `Rotation` | 属性 | 设置旋转：单个 `real`（绕负 Z 轴）或 `real[4]`（角度 + 轴向量） |
| `Scale` | 属性 | 设置缩放：单个 `real`（均匀）或 `real[3]`（各轴） |
| `TransformationMatrix` | 属性 | 设置完整变换矩阵 `real[4,4]` 或 `real[16]` |
| `addGraphicTransformation(Position, RotationAngle, RotationAxis, Scale)` | 方法 | 在已有变换上叠加一个变换（顺序敏感，按顺序依次应用） |

### 结构与访问（Structure & Access）

| 名称 | 类型 | 作用 |
|------|------|------|
| `graphic(Name/Index)` | 方法 | 返回复合图形内部的子 graphic/group |
| `groupGraphics(Children)` | 方法 | 将指定图形合并为一个组，返回新组 |
| `deleteGraphic` | 方法 | 删除指定图形 |
| `Index` | 只读属性 | 返回图形的一基数字索引 |
| `InternalGraphicType` | 只读属性 | 返回图形/组的内部类型字符串 |
| `NumGraphics` | 只读属性 | 返回直接子图形的数量 |
| `Name` | 属性 | 设置/读取图形或组的名称（`default` 组不可重命名） |
| `makeAnimatableObject(ObjectName, ExtractAtBoundingBoxBase[, ExtractionOffset, SwapXAndZAxis])` | 方法 | 从图形创建可动画对象并返回 |

`InternalGraphicType` 常见取值：
- 复合图形：`GraphicGroup`、`GroupNode`、`Instance`、`Switch`、`Rack`、`Stairs`、`Fence`、`FactoryWalls`
- 简单图形：`Shape`、`Box`、`BarredArea`、`Dimensionings`

### 材质（Material）

设置任一材质属性都会自动将 `MaterialActive` 置为 `true`。

| 名称 | 类型 | 作用 |
|------|------|------|
| `MaterialActive` | 属性 | 激活/停用材质 |
| `MaterialAmbientColor` | 属性 | 环境光颜色（`makeRGBValue`） |
| `MaterialDiffuseColor` | 属性 | 漫反射颜色 |
| `MaterialEmissiveColor` | 属性 | 自发光颜色 |
| `MaterialSpecularColor` | 属性 | 镜面反射颜色（需材质已激活） |
| `MaterialShininess` | 属性 | 光泽度（0–1） |
| `MaterialTransparency` | 属性 | 透明度（0–1；多层透明图形可能渲染异常） |

### 障碍物（Worker Obstacle）

| 名称 | 类型 | 作用 |
|------|------|------|
| `ObstacleForWorker` | 属性 | 设置该图形对 Worker 的障碍属性 |

取值随图形类型不同：`"(None)"`（无障碍）、`"Bounding box"`（包围盒为障碍）、`"Sides"`（仅 Stairs）、`"Graphics"`（仅复合图形）。

### 优化（Optimize）

| 名称 | 类型 | 作用 |
|------|------|------|
| `optimizeByPruningTinyGraphics(BoundingCubeSideLength)` | 方法 | 删除小于指定立方体的微小图形 |
| `optimizeByStructureFlattening(KeepGrouping, PreserveObstacles, RemovePolylinesAndPointSets[, PreserveReferences])` | 方法 | 展平图形结构 |
| `optimizeByVisibilityFilter(CullGranularity, ReductionLevel)` | 方法 | 删除从外部不可见的组件 |

### 纹理（Texture）

| 名称 | 类型 | 作用 |
|------|------|------|
| `removeTexture` | 方法 | 删除图形上已有的纹理 |

---

## 三、完整成员速查表

| 名称 | 类型 | 用途 |
|------|------|------|
| `_3D.calculateMUDimensions` | 方法 | 根据图形计算 MU 尺寸 |
| `_3D.exchangeGraphic` | 方法 | 从文件替换图形 |
| `_3D.ExcludeFromShowContentOfLocation` | 属性 | 隐藏外部表示 |
| `_3D.exportAsJt` | 方法 | 导出 `.JT` |
| `_3D.exportAsS3D` | 方法 | 导出 `.s3D` |
| `_3D.exportModelingViewBitmap` | 方法 | 导出建模视图 `.PNG` |
| `_3D.exportPlanningViewBitmap` | 方法 | 导出规划视图 `.PNG` |
| `_3D.getGraphic` | 方法 | 访问 graphic/graphic group |
| `_3D.InheritGraphics` | 属性 | 切换图形继承 |
| `_3D.optimizeObject` | 方法 | 优化 3D 对象结构 |
| `_3D.ShowContent` | 属性 | 显示/隐藏所包含对象 |
| `addGraphicTransformation` | 方法 | 叠加图形变换 |
| `deleteGraphic` | 方法 | 删除图形 |
| `graphic` | 方法 | 访问内部图形（复合） |
| `groupGraphics` | 方法 | 合并图形为组 |
| `Index` | 只读属性 | 图形数字索引 |
| `InternalGraphicType` | 只读属性 | 图形/组类型 |
| `makeAnimatableObject` | 方法 | 创建可动画对象 |
| `MaterialActive` | 属性 | 激活/停用材质 |
| `MaterialAmbientColor` | 属性 | 环境光颜色 |
| `MaterialDiffuseColor` | 属性 | 漫反射颜色 |
| `MaterialEmissiveColor` | 属性 | 自发光颜色 |
| `MaterialShininess` | 属性 | 光泽度（0–1） |
| `MaterialSpecularColor` | 属性 | 镜面反射颜色 |
| `MaterialTransparency` | 属性 | 透明度（0–1） |
| `Name` | 属性 | 图形/组名称 |
| `NumGraphics` | 只读属性 | 直接子图形数量 |
| `ObstacleForWorker` | 属性 | Worker 障碍设置 |
| `optimizeByPruningTinyGraphics` | 方法 | 删除微小图形 |
| `optimizeByStructureFlattening` | 方法 | 展平图形结构 |
| `optimizeByVisibilityFilter` | 方法 | 删除不可见组件 |
| `Position` | 属性 | 图形位置 |
| `removeTexture` | 方法 | 删除纹理 |
| `Rotation` | 属性 | 图形旋转 |
| `Scale` | 属性 | 图形缩放 |
| `TransformationMatrix` | 属性 | 完整变换矩阵 |
