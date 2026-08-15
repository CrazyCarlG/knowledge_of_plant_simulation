# Shape Methods

本目录收录了 SimTalk 中用于 3D 图形、建模、工人（Worker）外形以及外形属性的方法参考，涵盖创建与访问图形外形的属性与方法。

> 详细内容见同目录的 `shape-methods.md`。原始帮助源文件为 `shape-methods.txtx`。

## 内容概览

本文档分为三个部分：

1. **Worker 3D 属性**（`_3D.*`）—— 用于访问和设置工人在行走、搬运时的图形序列与障碍物行为。
2. **创建外形的方法**（`create*` 与 `importGraphics`）—— 用于在图形或图形组中创建各种 3D 图形。
3. **相关主题**（Related Topics）—— 交叉引用的其他帮助页面。

## Worker 3D 属性

| 属性 | 说明 | 类型 |
| --- | --- | --- |
| `_3D.SynchronizedJoints` | 设置朝向姿态移动时是否同步关节，使参与运动的所有关节同时到达目标状态 | Attribute (boolean) |
| `_3D.GraphicsWhenCarrying` | 设置工人搬运零件时循环使用的图形组序列 | Attribute (string[]) |
| `_3D.GraphicsWhenEmpty` | 设置工人未搬运零件时循环使用的图形组序列 | Attribute (string[]) |
| `_3D.ObstacleForWorker` | 设置对象的哪一部分是工人在模型中自由行走时的障碍物 | Attribute (string) |
| `_3D.VisibleWalkingGraphicGroup` | 返回工人当前用于可视化行走的图形组名称（未行走时返回 `""`） | Read-only Attribute (string) |

## 创建外形的方法

以下方法均通过 `<Path>` 指定的图形或图形组调用，通常通过 `_3D.getGraphic(...)` 获取目标图形组，返回值为创建的图形（`any`）。

| 方法 | 说明 |
| --- | --- |
| `createBarredArea` | 创建禁入区（Barred Area） |
| `createBox` | 创建箱体（Box） |
| `createConeFrustum` | 创建圆锥台（Cone Frustum） |
| `createCuboid` | 创建长方体/立方体（Cuboid），可设置边框线宽与颜色 |
| `createDimensioning` | 在两个测量点之间创建尺寸标注（Dimensioning） |
| `createExtrusionGraphic` | 沿三维向量拉伸二维轮廓创建图形 |
| `createFactoryWalls` | 创建厂房墙体（Factory Walls） |
| `createFence` | 创建围栏（Fence），可选网格与隔板 |
| `createIndexedFaceSet` | 创建索引面集（Indexed Face Set），用节点与面索引定义图形 |
| `createIndexedLineSet` | 创建索引线集（Indexed Line Set），用节点与线序列定义线 |
| `createMezzanine` | 创建夹层/平台（Mezzanine） |
| `createPicture` | 创建带纹理的图板，显示文件中的完整图片 |
| `createPolyLine` | 创建折线（Polyline），可显示方向 |
| `createRack` | 创建货架（Rack） |
| `createRectangle` | 在指定位置 (X,Y) 创建矩形 |
| `createSphere` | 创建球体（Sphere） |
| `createStairs` | 创建楼梯（Stairs） |
| `createText` | 创建文字（Text），可设置宽度、文字色、背景色与对齐方式 |
| `createTiledPlate` | 创建图板，将图片或纹理平铺显示 |
| `importGraphics` | 从文件导入图形并添加到现有图形/图形组中 |

### 常用返回图形属性

创建的图形（`any`）通常支持后续设置材质与位置，常见示例：

```simtalk
var box := _3D.getGraphic("deco").createBox([2.0, 2.5, 1], 0.15)
box.MaterialActive := true
box.MaterialDiffuseColor := makeRGBValue(255, 0, 0)
box.Position := [1.0, 2.0, 0.0]
```

## 相关主题

- `_Accessing Poses`
- `_Accessing the Worker`
- `_Accessing Methods of Graphic Shapes`
- `_Accessing Attributes of Graphic Shapes`
- `_Detailed Access To Graphics`
- `_3D.getGraphic`
- Auto Complete
- Insert Shape

> Source: Plant Simulation Help (Unpublished work. © 2026 Siemens)
