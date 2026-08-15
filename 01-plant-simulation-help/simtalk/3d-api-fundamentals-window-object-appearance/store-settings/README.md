# Store Settings（Store 设置 / 外观）

本目录内容来自 Plant Simulation SimTalk 3D API 帮助，主题为「Store Settings」。核心内容为 `store-settings.md`，介绍如何通过 SimTalk 设置 3D 中**对象与 MU 的对象材质（object material）**，以及**Store（仓储对象）的外观**。

## 概述

- SimTalk 提供了一系列 `_3D.*` 属性，用于在 3D 中访问和设置对象、MU 以及 Store 的材质与外观。
- 本主题分为两大部分：
  1. **对象与 MU 的外观**（Accessing the Appearance of Objects and MUs）
  2. **Store 的外观**（Accessing the Appearance of the Store）

## 一、对象与 MU 的外观（Object Material）

SimTalk 通过 `_3D.Material*` 属性设置对象/MU 的对象材质。

### 不提供对象材质的对象类型

以下对象不提供对象材质：

- 具有对象专属外观设置的对象，例如**长度方向对象（length-oriented objects）**与 **Store**。
- 用于连接其他对象的对象，例如 **Connector**、**Interface**、**Marker**。
- 用于显示文本/数值或用于选择设置的对象，例如 **Comment**、**Variable**、**Display**、**Button**、**DropDownList**、**Checkbox**、**Chart**、**Tank**、**Mixer**。

### 材质的应用范围

Plant Simulation 将这些属性应用到指定对象上所有**未定义自身材质**的图形上，例如：

- Worker 的 T-Shirt。
- Transporter 的车身（body）。
- Container 与 Part 的整个图形。
- 点向对象（point-oriented objects）的蓝色图形，如 Station、Buffer 等。
- 逻辑对象图标下方的浅灰色底板，如信息流对象 Method、DataTable 等，以及用户界面对象 SankeyDiagram、CostAnalyzer 等。

### 对象材质属性一览

| 属性 | 数据类型 | 说明 |
|------|----------|------|
| `_3D.MaterialActive` | boolean | 设置对象/MU 是否具有对象范围材质（`true`/`false`）。 |
| `_3D.MaterialAmbientColor` | integer | 设置环境光颜色（ambient color）。 |
| `_3D.MaterialDiffuseColor` | integer | 设置漫反射颜色（diffuse color）。 |
| `_3D.MaterialEmissiveColor` | integer | 设置自发光颜色（emissive color）。 |
| `_3D.MaterialShininess` | real | 设置光泽度（shininess），取值 0 到 1。 |
| `_3D.MaterialSpecularColor` | integer | 设置镜面反射颜色（specular color）。 |
| `_3D.MaterialTransparency` | real | 设置透明度（transparency），取值 0 到 1。 |
| `_3D.ShowSafetyZones` | boolean | 显示（`true`）或隐藏（`false`）Transporter 已定义的安全区。 |

**通用语法：**

```
<Path>.<属性>:类型
<MU-Path>.<属性>:类型
```

**注意：**

- 颜色类属性通常使用 `makeRGBValue(r,g,b)` 方法设置 RGB 颜色值。
- 给颜色、光泽度、透明度属性赋值时，会自动将材质设为激活（`MaterialActive := true`）。
- `_3D.ShowSafetyZones` 仅用于 Transporter（安全区）。

**示例：**

```
MyStation._3D.MaterialActive := true
MyStation._3D.MaterialDiffuseColor := makeRGBValue(0,0,255)
MyPortioner._3D.MaterialShininess := 0.8
.MUs.Part._3D.MaterialTransparency := 0.85
Station._3D.ShowSafetyZones := true
```

## 二、Store 的外观（Appearance of the Store）

SimTalk 通过 `_3D.*` 属性设置 Store 在 3D 中的外观，分为几何尺寸属性与材质属性两类。

### 几何 / 尺寸属性

| 属性 | 数据类型 | 说明 |
|------|----------|------|
| `_3D.Dimensions` | length[3] | 设置 Store 存储区域的尺寸（X/宽度、Y/深度、Z/高度）。动态类型表示槽位尺寸；非动态类型表示 Store 整体尺寸。 |
| `_3D.FloorThickness` | any | 设置地板空间（Floorspace，动态）基础板厚度；对带圆/方立柱的货架（Rack，动态）则设置各层搁板厚度。`void` 表示使用默认厚度。 |
| `_3D.Gap` | any | 设置动态 Store 类型各货架隔间之间的间距。仅适用于动态类型；`void` 表示无间距，取值须 ≥ 0。 |
| `_3D.GroundClearance` | any | 设置最低搁板下缘到地面的距离（Rack with round/square posts，动态）。`void` 表示默认离地高度；`0` 表示最低搁板平放于地面。 |
| `_3D.OriginX` | string | 设置 Store 自动生成图形及 MU 动画在 X 方向的原点，可选 `"Left"`、`"Center"`、`"Right"`。 |
| `_3D.OriginY` | string | 设置 Store 自动生成图形及 MU 动画在 Y 方向的原点，可选 `"Top"`、`"Center"`、`"Bottom"`。 |

### 材质属性

Store 的自动图形分为两类材质：**立柱/支架材质（PostMaterial）**与**存储区域材质（StorageAreaMaterial）**，各自都提供完整的一组材质属性。

#### 立柱材质（Post Material）

| 属性 | 数据类型 | 说明 |
|------|----------|------|
| `_3D.PostMaterialActive` | boolean | 激活/停用立柱自动图形的材质。 |
| `_3D.PostMaterialAmbientColor` | integer | 设置立柱环境光颜色。 |
| `_3D.PostMaterialDiffuseColor` | integer | 设置立柱漫反射颜色。 |
| `_3D.PostMaterialEmissiveColor` | integer | 设置立柱自发光颜色。 |
| `_3D.PostMaterialShininess` | real | 设置立柱光泽度，取值 0 到 1。 |
| `_3D.PostMaterialSpecularColor` | integer | 设置立柱镜面反射颜色。 |
| `_3D.PostMaterialTransparency` | real | 设置立柱透明度，取值 0 到 1。 |

#### 存储区域材质（Storage Area Material）

| 属性 | 数据类型 | 说明 |
|------|----------|------|
| `_3D.StorageAreaMaterialActive` | boolean | 激活/停用存储区域自动图形的材质。 |
| `_3D.StorageAreaMaterialAmbientColor` | integer | 设置存储区域环境光颜色。 |
| `_3D.StorageAreaMaterialDiffuseColor` | integer | 设置存储区域漫反射颜色。 |
| `_3D.StorageAreaMaterialEmissiveColor` | integer | 设置存储区域自发光颜色。 |
| `_3D.StorageAreaMaterialShininess` | integer | 设置存储区域光泽度。 |
| `_3D.StorageAreaMaterialSpecularColor` | integer | 设置存储区域镜面反射颜色。 |
| `_3D.StorageAreaMaterialTransparency` | real | 设置存储区域透明度，取值 0 到 1。 |

**注意：**

- 立柱与存储区域的颜色、光泽度、透明度属性，通常在赋值时自动将对应材质设为激活。
- 立柱颜色类属性只能在材质已激活时访问。
- 颜色类属性通常使用 `makeRGBValue(r,g,b)` 设置。

**示例：**

```
MyStore._3D.Dimensions := [2, 2, 0.01]
MyStore._3D.FloorThickness := 0.24

Store3._3D.StoreType := "Rack with round posts (dynamic)"
Store3._3D.Gap := 0.1
Store3._3D.FloorThickness := 0.15
Store3._3D.GroundClearance := 0.3

Store3._3D.OriginX := "Left"
Store3._3D.OriginY := "Top"

MyStore._3D.PostMaterialActive := true
MyStore._3D.PostMaterialDiffuseColor := makeRGBValue(255,0,0)
MyStore._3D.StorageAreaMaterialActive := true
MyStore._3D.StorageAreaMaterialTransparency := 0.9
```

## 相关引用

- 对话框：**Edit 3D Properties** > Appearance of Objects and MUs / Appearance of the Store。
- SimTalk 方法：`makeRGBValue`。
- 相关属性：`_3D.StoreType`。
