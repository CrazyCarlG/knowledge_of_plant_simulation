# Shape Materials（图形形状属性）— 目录说明

本目录收录 **Siemens Plant Simulation** 帮助文档中关于 **Graphic Shapes（图形形状）** 的 SimTalk 属性参考。

## 内容来源

- `shape-materials.md` — 主文档，整理自 `shape-materials.txtx`（Plant Simulation Help，第 12-1010 至 12-1191 页），记录了通过 `Insert Shape` 创建的 3D 图形（如 Factory Walls、Fence、Mezzanine、Rack、Stairs、Dimensioning）的外观与几何属性。
- `shape-materials.txtx` — 原始帮助文件（源数据）。

## 概述

SimTalk 提供一系列属性用于设置 3D 图形形状的材质与几何参数。图形通过 `_3D.getGraphic("deco", [n])` 引用。

### 材质属性通用模式

大多数材质组都遵循相同的七属性结构：

| 属性 | 数据类型 | 含义 |
|---|---|---|
| `...MaterialActive` | `boolean` | 激活/停用材质 |
| `...MaterialAmbientColor` | `integer` | 环境光颜色（`makeRGBValue`） |
| `...MaterialDiffuseColor` | `integer` | 漫反射颜色（`makeRGBValue`） |
| `...MaterialEmissiveColor` | `integer` | 自发光颜色（`makeRGBValue`） |
| `...MaterialShininess` | `real` | 光泽度（0–1） |
| `...MaterialSpecularColor` | `integer` | 镜面反射颜色（`makeRGBValue`） |
| `...MaterialTransparency` | `real` | 透明度（0–1） |

**通用规则**：
- 为颜色属性赋值会自动将材质设为激活（`MaterialActive := true`）。
- 颜色/透明度/光泽度属性只有在材质激活时才能访问。
- 赋值任意属性会**取消图形继承**。
- 当图形是自动生成的图形组（或其位于其中）时，无法赋值。
- 颜色通常用 `makeRGBValue` 方法设置。

## 属性分组（按图形类型）

| 图形类型 | 属性组 |
|---|---|
| **Factory Walls（工厂墙）** | Factory Walls Attributes、Frame Material、Pane Material、Wall Material |
| **Fence（围栏）** | Fence Attributes、Mesh Material、Pane Material、Post Material、Profile Material |
| **Mezzanine（夹层平台）** | Border Line Material、Floor Material、Mezzanine Attributes、Post Material、Railing Material |
| **Rack（货架）** | Board Material、Post Material、Rack Attributes |
| **Stairs（楼梯）** | Stairs Attributes、Stringer Material、Tread Material |
| **Dimensioning（尺寸标注）** | Dimensioning Attributes |

## 非材质（几何）属性速览

- **Dimensioning**：`DimensioningSpace`、`MeasuredLength`（只读）、`MeasuringPoint1`、`MeasuringPoint2`、`TextPosition`
- **Factory Walls**：`WallElementWidth`
- **Fence**：`FenceElementWidth`、`MeshActive`、`PanesActive`
- **Mezzanine**：`BorderLineActive`、`FloorThickness`、`PostDiameter`、`RailingsActive`、`RailingSegmentWidth`
- **Rack**：`BayDepth`、`BaySize`、`BoardDepth`、`BoardThickness`、`Capacity`、`GroundClearance`、`MinimalStructure`、`PostDiameter`、`SquarePosts`
- **Stairs**：`Rise`、`Run`（只读）、`TreadWidth`

## 相关条目

`_3D.getGraphic`、`createFactoryWalls`、`createFence`、`createMezzanine`、`createRack`、`createStairs`、`createDimensioning`、`InternalGraphicType`、`makeRGBValue`、`Dimensions`（graphic）。
