# environment — SimTalk 访问 3D 功能（窗口与环境）

本目录总结 `environment.md` 与 `environment.txtx`（两者内容一致，后者为带帮助页码与版权标记的纯文本版本）的内容。该目录下无子文件夹，故无子目录 README.md。

主题为 **SimTalk Access to 3D Functions**：Plant Simulation 在通用 SimTalk 函数之外，还提供一组用于访问 3D 对象的专用函数/属性。本目录聚焦 3D 窗口、视图选项与通用访问入口。

## 关键注意事项

- SimTalk 对方法、属性、只读属性的名称不区分大小写。
- 可在 Method 编辑器的 Edit 选项卡中点击 **Auto Complete** 查看 3D 对象的属性与方法。
- 访问 3D 对象时，在指令中输入 `_3D.`（后接句点）。
- 目录中列出的多数 3D 属性/方法使用数组数据类型进行读写。

## 通用访问目录（General Access）

文档给出的整体目录如下，本目录重点覆盖其中「3D 窗口」与「视图选项」两部分：

- **基础访问**：3D 窗口、视图选项、包围盒（Bounding Box）、长度导向对象（Length-oriented Objects）、对象与 MU 外观、Store 外观、Frame/Folder 背景色、对象标题（Captions）、Buffer 填充量、3D 中对象、点云（Point Clouds）、变换设置（Transformation Settings）
- **动画访问**：MU 动画、自主动画、相机动画、机械臂动画、关节（Joints）、姿态（Poses）、Worker
- **图形访问**：图形形状的方法与属性、图形组的属性/只读属性与方法、图形（Graphics）、详细图形访问、状态图形（State Graphics）
- **PLMXML 运动学文件访问**：见下文

## 将对象设置复制到 Method

可将仿真对象、可动画对象及图形的设置复制到 Method：

- **复制对象路径**：在 Frame 中 `Ctrl+C`，到 Method 中 `Ctrl+V`（如 `EventController`、`Source`、`Frame`）。
- **复制形状路径**：同上（如 `Cuboid`）。
- **复制当前材质设置**：在 Frame 中按 `Spacebar` → 切到 Material 选项卡 → 激活材质并点击复制按钮 → 到 Method 中 `Ctrl+V`（如 `Cuboid`）。
- **复制可动画对象路径**：`Ctrl+C`/`Ctrl+V`（如 `Sphere`）。

复制后可输入句点并按 `Ctrl+Spacebar` 扩展路径（等价于 Auto Complete）。示例中括号数字如 `("deco", [1])` 表示对应编号的图形节点，该编号同样显示在 **Show Graphic Structure** 对话框中。

## PLMXML 运动学文件访问

- `applyPLMXMLKinematicStructure [SimTalk]`（方法）：将指定 PLMXML 文件中的运动学结构应用到 `<Path>` 指定的图形上，并在其中创建带运动学设置的可动画对象。
  - 语法：`<Path>.applyPLMXMLKinematicStructure(FilePath:string[, PreferFirstEntryPoint:boolean:=true, PreferredEntryPointName:string:=""]) -> boolean`
  - 参数：`FilePath`（PLMXML 路径）、`PreferFirstEntryPoint`（`true` 用第一个 / `false` 用最后一个结构，默认 `true`）、`PreferredEntryPointName`（指定根名称，默认空串 `""`；两者同时给出时名称优先）。
  - 返回 `boolean`：找到并应用结构为 `true`，否则 `false`。
- `getPotentialPLMXMLKinematicRoots [SimTalk]`（方法）：读取 PLMXML 文件的运动学信息，列出所有潜在运动学结构的根。
  - 语法：`getPotentialPLMXMLKinematicRoots(FilePath:string) -> string[]`
  - 返回 `string[]`：空数组表示未找到根；单个名称表示唯一根；多个名称表示存在多种无法区分上下文的解释（同名可能出现多次）。

## 访问 3D 窗口

- `_3D.closeWindows [SimTalk]`（方法）：关闭为 `<Path>` 对象打开的所有窗口。例：`MyStation._3D.closeWindows`。
- `F3DactivateCameraMark [SimTalk]`（函数）：在当前活动的 3D 窗口中激活指定相机标记（CameraMark），改变视点与关注对象。例：`F3DactivateCameraMark("MyCameraMark")`。
- `F3DattachCamera [SimTalk]`（函数）：将活动 3D 窗口的相机附着到指定对象或解除附着；传入 `void` 解除。无 3D 窗口或处于 Planning View 时不生效。例：`F3DattachCamera(.MUs.Part:1)`。
- `F3DconfigurePlanningView [SimTalk]`（函数）：按参数将视图设为 Planning View。参数 `ViewPosition:real[2]`、`Zoom:real`、可选 `ObjectOfInterest`。例：`F3DconfigurePlanningView([-14, -15], 16, .Models.MyWarehouse)`。
- `F3DconfigureView [SimTalk]`（函数）：按参数将视图设为 Modeling View。参数 `CameraPosition:real[3]`、`CameraRotationX:real`、`CameraRotationZ:real`、可选 `ObjectOfInterest`。例：`F3DconfigureView([-8.129, -3.707, 7.832], 45.000, -15.000, .Models.MyWarehouse)`。

## 访问视图选项（View Options）

以下均为 `<Path>._3D.<属性>:boolean` 形式的布尔属性，用于显示/隐藏 Frame 的各类 3D 显示项：

| 属性 | 作用 |
| --- | --- |
| `_3D.PlanningView` | 启用/停用 Planning View |
| `_3D.ShowBasePlate` | 显示/隐藏网格下方的底板 |
| `_3D.ShowConnections` | 显示/隐藏连接器/接口/标记 |
| `_3D.ShowExternalGraphics` | 显示/隐藏外部图形组 |
| `_3D.ShowGrid` | 显示/隐藏网格 |
| `_3D.ShowLabels` | 显示/隐藏对象标签 |
| `_3D.ShowMaterialFlowDirections` | 显示/隐藏长度导向对象的物流方向箭头 |
| `_3D.ShowNames` | 显示/隐藏对象名称 |
| `_3D.ShowPointClouds` | 显示/隐藏点云 |
| `_3D.ShowShadows` | 显示/隐藏阴影（标题、操纵器、路径可视化及部分显示对象通常不产生阴影） |
| `_3D.ShowSky` | 显示/隐藏天空 |

## 相关参考

- 3D Properties — Visualizing the Simulation
- Copy Object Settings to a Method
- General Access to SimTalk
- View Ribbon Tab（视图选项卡）
- `_3D.getGraphic [SimTalk]`、`_3D.getObject [SimTalk]`
- Camera Marks、Attach Camera、Use Planning View
- Auto Complete、Show Graphic Structure [context menu]
