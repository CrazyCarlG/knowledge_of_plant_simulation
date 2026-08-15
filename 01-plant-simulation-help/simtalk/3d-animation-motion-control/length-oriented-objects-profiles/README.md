# Length-oriented Objects & Profiles — 目录说明

本目录收录了 Plant Simulation SimTalk 中用于定义 **3D 长度导向对象（length-oriented objects）** 以及访问 **挤出轮廓（extrusion profiles）** 的属性、方法与函数说明。

> 目录内没有子文件夹；内容主要来自以下两个文件，二者描述的是同一主题，其中 `.md` 为整理后的 Markdown 版本，`.txtx` 为 Plant Simulation Help 的原始文本导出。

## 文件清单

| 文件 | 说明 |
|---|---|
| `length-oriented-objects-profiles.md` | 整理后的 Markdown 文档，按条目结构化列出了所有 `_3D.*` 属性/方法及 `F3Dgenerate*` 轮廓函数 |
| `length-oriented-objects-profiles.txtx` | Plant Simulation Help 的原始文本导出，包含相同的 API 参考内容 |

---

## 内容总结

SimTalk 提供了以下能力：定义长度导向对象的外观与动画行为，以及通过函数生成用户自定义的挤出轮廓。所有属性/方法均可通过 Method Editor 的 **Auto Complete**（Edit 功能区）查看与访问。

### 一、长度导向对象的属性（Attributes）

| 属性 | 语法 | 类型 | 说明 |
|---|---|---|---|
| `_3D.StoreType` | `<Path>._3D.StoreType:string` | Attribute | 设置 Store 的类型（如 `"Floorspace"`、`"Rack with round posts"`、各种 `(dynamic)` 变体等） |
| `_3D.AniGravityMode` | `<Path>._3D.AniGravityMode:boolean` | Attribute | 激活/关闭重力模式；仅影响自动动画，对悬挂轨道等尤其有用 |
| `_3D.AnimationOffset` | `<Path>._3D.AnimationOffset:length[3]` | Attribute | 设置动画路径相对对象表面在 X/Y/Z 方向的偏移 |
| `_3D.AniSmoothRotation` | `<Path>._3D.AniSmoothRotation:boolean` | Attribute | 激活/关闭平滑旋转；仅影响自动动画，控制 MU 在锚点处的旋转过渡 |
| `_3D.BaseHeight` | `<Path>._3D.BaseHeight:length` | Attribute | 设置基座高度（插入高度与 ΔZ=0 段之间的高度差），可在类中继承 |
| `_3D.ExtConfiguration` | `<Path>._3D.ExtConfiguration:table` | Attribute | 设置挤出配置（extrusion configuration），详见下方配置类型表 |
| `_3D.ShowMaterialFlowDirection` | `<Path>._3D.ShowMaterialFlowDirection:boolean` | Attribute | 显示/隐藏物料流方向箭头（仅对有意义的流向对象生效） |
| `_3D.ShowSensors` | `<Path>._3D.ShowSensors:boolean` | Attribute | 在 3D 中显示/隐藏传感器 |
| `_3D.Width` | `<Path>._3D.Width:real` | Attribute | 设置长度导向对象的宽度 |

### 二、长度导向对象的方法（Methods）

| 方法 | 语法 | 说明 |
|---|---|---|
| `_3D.getExtSegments` | `<Path>._3D.getExtSegments(Table:table)` | 读取长度导向对象的 Segments 表到指定 table |
| `_3D.setExtSegments` | `<Path>._3D.setExtSegments(Table:table)` | 从指定 table 导入 Segments 表设置 |

### 三、挤出配置（`_3D.ExtConfiguration`）

该属性接收一个 table，用于定义沿路径挤出的轮廓。其参数包括：

- **Index Name**：挤出组名称，仅在每组第一列（列 0）填写一次。
- **Extrusion Profile**：`[2 × 点数]` 子表，定义待挤出的轮廓；数值应按 1 米宽度来定义。
- **Configuration Type**：挤出方式，取值 `0`–`47`（共 48 种），涵盖 Path/Horizontal/Vertical/Forward 等类型 × z 取值方式（z max / Floor / Ceiling / z 1/5 等）× 锚点/间隔 × 宽度变化时的 Move/Scale/Fix 等行为组合。
- **Start Offset / End Offset**：挤出方向上的起止参考偏移。
- **Repetition Interval**：对于配置类型 14–19、22、23，`0` 表示仅在起点生成一次；大于 0 表示每隔该米数重复生成（如 `0.5` 表示每 50 cm）。
- **Graphic Group ID**：默认 `0`；0–10 之间可生成额外图形组（如 Fluid 对象 Pipe 使用此特性）。
- **Material**：子表，可设置 Diffuse/Ambient/Specular/Emissive 颜色、Transparency、Shininess（参见 `makeRGBValue`）。

**注意**：`_3D.ExtConfiguration` 返回的是值的副本。直接对属性下标赋值（如 `Conveyor._3D.ExtConfiguration[2,1] := 2`）无效，须先读取到局部变量、修改后再整体赋值回去。拷贝到 Frame 中的 DataTable 也需用 `copyFormatTo` + `copyRangeTo` 而非简单 `:=`。

### 四、挤出轮廓访问函数（`F3Dgenerate*`）

以下函数用于生成二维轮廓，供用户自定义挤出配置使用，均返回一个二维数组：

| 函数 | 语法 | 说明 |
|---|---|---|
| `F3DgenerateEllipse` | `F3DgenerateEllipse(BasePoint:length[2], Width, Height, CurvePrecision)` | 生成二维椭圆轮廓 |
| `F3DgenerateHollowEllipse` | `F3DgenerateHollowEllipse(BasePoint:length[2], Width, Height, BarThickness, CurvePrecision)` | 生成二维空心椭圆轮廓 |
| `F3DgenerateHollowRectangle` | `F3DgenerateHollowRectangle(BasePoint:length[2], Width, Height, BarThickness)` | 生成二维空心矩形轮廓 |
| `F3DgenerateRectangle` | `F3DgenerateRectangle(BasePoint:length[2], Width, Height)` | 生成二维矩形轮廓 |

---

## 关联内容（See also）

- `_3D.InheritGraphics`、`createExtrusionGraphic`、`makeRGBValue`
- `Length [SimTalk] - animatable object`、`Segments [tab Appearance]`
- 对话框 **Edit 3D Properties** 中的 Store 外观、Width、Base Height 等设置
