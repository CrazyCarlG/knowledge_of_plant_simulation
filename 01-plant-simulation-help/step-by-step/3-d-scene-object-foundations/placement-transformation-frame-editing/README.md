# Placement, Transformation & Frame Editing（放置、变换与框架编辑）总结

本目录包含 `placement-transformation-frame-editing.md`（以及同名文本提取文件 `placement-transformation-frame-editing.txtx`），内容为 Plant Simulation 帮助文档中 **Working with Objects in the Frame（在框架中操作对象）** 相关章节的说明——如何在 3D 场景中插入、选择、移动、旋转、缩放和编辑对象，尤其侧重长度导向对象（Length-oriented Objects）与精确变换编辑。以下是对其内容的总结。

## 1. 总览（Overview）

Plant Simulation 提供了多种在 3D 场景中操作对象的方式，主要包括：

- 将对象插入场景
- 选择对象
- 同时粘贴多个副本
- 用连接器（Connector）连接对象
- 用键盘 / 鼠标移动对象
- 在框架中旋转对象
- 在框架中缩放对象
- 编辑组合图形、设置图形材质、为对象更换图形
- 添加 JT 布局文件
- 处理长度导向对象
- 设置物流对象容量、设置对象的显示方式
- 将 3D 模型适配到 2D 模型、创建自定义对象

## 2. 将对象插入场景（Insert Objects into the Scene）

对象可从 **Toolbox（工具箱）** 或 **Class Library（类库）** 插入（两者默认包含相同对象）。

- **Toolbox**：左键点击对象，拖到 3D 窗口目标位置后点击插入；右键或 `Esc` 取消。
- **Class Library**：左键点击并按住拖到目标位置后松开；按住期间显示预览，在 3D 窗口外松开可取消。
- **粘贴副本**：用 `Home > Copy` 或 `Ctrl+C` 复制，再到 3D 窗口按 `Ctrl+V`；副本被粘贴到被复制对象在其位置内的相同位置。

**吸附（Snapping）**：点击 Edit 选项卡上的 snap 按钮可将对象吸附到最近的网格线交点；不点击则按网格/对象对齐设置自由放置。

> 注意：插入 Marker 时要保持对齐，避免不必要的舍入。若在关闭 *Show Grid* 时插入，可能产生未对齐的 Marker。

可在 **3D Properties** 对话框（由 Home 选项卡打开）中微调位置；通过其左下角按钮或双击对象打开仿真对象的对话框。

**连续插入多个相同对象**：按住 `Ctrl` 在 Toolbox 中选择对象，插入后它保持选中，可连续插入多个；右键或 `Esc` 退出。

插入后可对齐网格、吸附网格、吸附对象或在网格上排列（需开启 *Show Grid*）。

## 3. 选择对象（Select Objects）

左键点击对象即可选中。选中颜色表示元素类型：

| 对象类型 | 选中后颜色 |
|---|---|
| 仿真对象（直接位于打开的对象中） | 绿色 |
| 可动画对象（属于仿真对象） | 紫色 |
| 图形（可视化仿真对象） | 黄绿色 |
| 显示的操作器（manipulator） | — |

选择技巧：

- 按住 `Shift` 或 `Ctrl` 点击可多选。
- 拖拽选框：不按 `Shift`/`Ctrl` 时取消原选择；按住 `Shift`/`Ctrl` 时新选择加入原选择。
- `Ctrl+A` 全选场景对象。
- 用 `+` 和 `-` 键修改选择。
- 按住 `Shift` 依次点击对象可记录选择顺序（例如用于统计报告的顺序）。

## 4. 同时粘贴多个副本（Simultaneously Paste Multiple Copies）

例如创建一个带多个货架的 Store：

1. 插入对象（如 Station）。
2. 选中并 `Ctrl+C` 复制。
3. 点击 Home 选项卡上的 `Paste > Multiple Paste`。
4. 在 **Count** 组合框中输入副本数量。
5. 输入相对原对象的 **Offset**（偏移量）。

> 示例：一个宽 2.0 m 的 Station，在 X 轴上偏移 2.0 m，向右粘贴 4 个副本。存在初始预定义偏移（向右、向下），以避免副本相互重叠。

点击 **Paste**；如需要，粘贴后再移动副本。

## 5. 移动对象（Move Objects in the Frame）

移动对象有三种方式：鼠标、键盘、精确输入。

### 用鼠标移动

- 左键拖拽：在网格平面上自由移动（隐藏网格时参照视图平面）。
- 按住 `Alt`/`Alt Gr` + 左键拖拽：垂直上下移动。

> 注意：在内容可见的 Frame 中，先按 `Alt`/`Alt Gr` 再点击会选中 Frame 内的仿真对象；按住该键仍会垂直移动选中对象。若键盘无 `Alt Gr`，用 `Ctrl-right + Alt-right`。

### 用键盘移动

使用 `Ctrl` 或 `Shift` 加方向键：

- 单独方向键：移动网格吸附距离的 **10%**。
- `Shift` + 方向键：移动完整网格吸附距离。
- `Ctrl` + 上/下：沿 z 方向垂直移动（10% 步长；`Shift+Ctrl` 为完整步长）。
- `Ctrl` + 左/右：逆/顺时针旋转 1°。
- `Shift+Ctrl` + 左/右：旋转 45°。

### 精确移动

在 **3D Properties > Tab Transformation** 中输入精确值：

1. 选中对象。
2. 按空格键（或 Home 选项卡按钮）并点击 **Transformation** 选项卡。
3. 在文本框中滚动滚轮以 0.1 m 步长调整；按住 `Shift` 滚动以 1 m 步长调整。
4. 点击 **Apply** 预览，满意后点击 **OK**。

## 6. 旋转对象（Rotate Objects in the Scene）

### 用键盘旋转

键盘旋转使用 **3D Properties > Transformation > Settings for the Rotation** 下的设置。

- `Ctrl` + 左/右：左/右旋转 1°。
- `Ctrl+Shift` + 左/右：左/右旋转 45°。
- 数字键盘：`7`/`8` = x 轴 10°，`4`/`5` = y 轴 10°，`1`/`2` = z 轴 10°。

定义旋转设置：选择 **3D Properties > Transformation > Settings for the Rotation**，点击轴按钮或输入任意旋转轴的 x/y/z 分量，然后点击 **Apply** 激活。

### 精确旋转

在 **3D Properties > Tab Transformation** 中输入精确值：

1. 选中对象。
2. 按空格键或点击 Home 选项卡按钮。
3. 输入旋转轴的 x/y/z 分量。
4. 输入相对对象中心的旋转偏移 x/y/z（默认 `0, 0, 0`，即绕中心旋转）。
5. 输入旋转角度（度）。
6. 点击 **Apply**。

> 注意：在一个 3D 窗口中的变换（移动/旋转/缩放）不会立即更新到其他 3D 窗口，只有在取消选中该对象后才会更新。

## 7. 缩放对象（Scale Objects in the Frame）

在 **3D Properties > Tab Transformation > Scale** 中输入精确值：

1. 选中对象并按空格键（或 Home 选项卡按钮）。
2. **Uniform（统一缩放）**：三个维度使用相同系数（输入一个值会自动填充其余，避免变形）。
3. 输入 x/y/z 轴的系数（如 `0.5` 减半、`2` 加倍）。仅允许非零值。
4. 清除 **Uniform** 可为各维度输入不同系数（会变形）。
5. **Set Dimensions**：输入缩放后对象的物理尺寸。

## 8. 处理长度导向对象（Work with Length-oriented Objects）

长度导向对象在仿真中使用其长度和尺寸，包括 **Conveyor、Track、TwoLaneTrack、Footpath、Container、Transporter 和 Pipe**。Plant Simulation 还会为 **Turnplate、Turntable、Converter、AngularConverter 和 Store** 自动生成图形。

要从 Conveyor、Turntable、Track、TwoLaneTrack 或 FootPath 创建类，先在 Frame 中建模再拖入 Class Library。

涵盖的主题：

- 插入曲线与直线段
- 自动连接长度导向对象
- 以 90° 角绘制直线与曲线段
- 不使用固定值绘制直线与曲线段
- 修改线段形状
- 用 SimTalk 命令创建曲线对象
- 重用长度导向对象的线段
- 键盘快捷键
- 用鼠标 / 键盘 / 精确编辑长度导向对象
- 建模输送元素之间的高度差
- 建模螺旋输送机

### 插入曲线与直线段

1. 缩放 Frame 以容纳对象。
2. 点击 Toolbox 中的长度导向对象并拖到 Frame；点击起点（打开 **Edit Parameters of Curve**）。
3. 绘制**直线段**：在终点位置再次点击。
4. 绘制**曲线段**：按住 `Ctrl` 拖动鼠标并点击一次以设置曲线。
5. 松开 `Ctrl` 并点击以绘制下一直线段。
6. 点击已有的末端线段可开始新的连接序列（Plant Simulation 自动连接；按住 `Alt` 可阻止）。
7. 右键或点击 **Finish** 退出插入模式；按 `Esc` 或点击 **Abort** 终止而不插入；点击 **Delete Last Point** 删除最后一个锚点。

**固定值**（输入对话框并勾选 *fixed* 框）：

- 直线段：**Line Length**（线长）和 **Tangential Angle**（相对上一段的切向角）。
- 曲线段：**Arc Length**（弧长）、**Radius**（半径）和 **Curve Angle**（正=顺时针、负=逆时针；360° 自动首尾相连）。
- 两种段：**Anchor Point Height**（锚点高度，即到下一个锚点的地板距离——用于坡道）。

> 网格激活时，点尽可能放在网格点上；固定值优先。不符合网格的值（如半径 2.5 m）会导致非切向过渡。
>
> 在曲线段后插入直线段时，Plant Simulation 总是强制切向角为 0°。

**起始切向角规则**：

- 点击已有对象后，采用上一对象的角度作为起始切向角（对图标同样适用）。
- 在已有对象上点击设置直线段时，根据鼠标位置使用对象角度或 ±90°。
- 未点击已有对象而设置曲线段时：为直线段输入的角度被用作起始切向角；按住 `Ctrl` 时，根据鼠标位置使用 0/±90/180°。

挤出路径最初只包含起始点（插入点或所选对象的终点）。左键插入直线段，`Shift`+左键插入曲线段。若完成后少于两个线段/点，则不插入该对象。

### 自动连接长度导向对象

当点击另一对象作为长度导向对象的后续时，Plant Simulation 尝试用额外的直线/曲线段桥接间隙，使连接相切。

- 方向由最后/第一段（长度导向）、点导向对象的 X 轴或场景的 X 轴决定。
- 最后一段的高度差会自动修正。

闭合间隙的条件：

- 曲线角固定为 90° 且半径固定。
- 对象平行或垂直对齐。
- 间隙最多用两个直角曲线段闭合。
- 对象只绕 z 轴旋转（不绕其他轴）。

支持的情况（对象无需对齐网格）：

- 对象对齐且指向同一方向。
- 对象平行且同向（切向和垂直距离 ≥ 双倍半径）。
- 对象平行但反向（垂直距离 ≥ 双倍半径）。
- 对象成直角（切向和垂直距离 ≥ 半径）。

若无法闭合间隙，Plant Simulation 建议一条指向后续对象的直线（除非按住 `Ctrl`）。可接受它（点击后续对象）或手动定义单独的切向段。

### 以 90° 角绘制直线与曲线段

1. 点击 Toolbox 中的 Conveyor 图标。
2. 拖到 Frame 并点击设置起点。
3. 在 **Edit Parameters of Curve** 中设置 90° 曲线默认值（固定切向角 0°、固定曲线角 90°、固定半径 2 m），可输入不同半径。
4. 绘制曲线：按住 `Ctrl` 向下拖动并点击一次。
5. 向左弯曲的曲线：保持曲线角 *Fixed* 激活并输入 `90`，再拖动点击。
6. 松开 `Ctrl` 并点击下一段直线。
7. 右键退出插入模式。

> Plant Simulation 保存最后一组对话框设置以供复用。

若吸附导致不对齐，可按住 `Alt` 点击取消吸附网格，或为该段输入固定切向角 0°。

不使用固定值绘制曲线段：左键点击三次（第一次按住 `Ctrl` 激活曲线模式）——第一击设起点、第二击设半径、第三击设弧长/曲线角。

### 不使用固定值绘制直线与曲线段

**直线段**：
1. 点击一次设起点（Connector 图标附着到光标；文本框显示实时值）。
2. 朝目标方向拖动并点击设第一个锚点。
3. 继续直到对象达到所需长度/形状。
4. 右键设终点并退出插入模式。

**曲线段**：
1. 按住 `Ctrl` 点击一次设起点。
2. 拖动设切向角。
3. 继续拖动并点击设半径。
4. 继续拖动并点击设弧长。
5. 右键设终点。
6. 用对话框中的 **Delete Last Point** 删除最后一个锚点。

### 修改线段形状

- 修改直线段形状：点击 **Show Manipulators** 并拖动操作器。
- 删除锚点：右键选择 **Delete Anchor Point**。
- 不新增锚点而延长曲线段：拖动拖拽点。
- 追加锚点：右键曲线选择 **Segments > Append [segment]**。
- 编辑/插入线段：选择 **Segments > Edit [segment]** 打开 **Segments Table**（也可在开头插入线段，鼠标无法做到）。示例：在 Pipe 开头插入曲线段以无缝连接 FluidSource（按 `F7` 打开 Segments 表，插入行）。
- 修改方向（如从右到左）：在 Segments 表中编辑 **Curve angle**。
- 用曲线替换直角：在 Segments 表中插入行并输入曲线值（可从模板对象复制）。
- 反转运动方向：右键对象选择 **Reverse [segment]**。
- 将对象拆分为独立线段：点击某点选择 **Split Up [segment]**。
- 移动整个对象：点击拖拽，或用方向键（一次一个像素；`Shift`+方向键 = 一个网格单位）。
- 删除整个对象：点击一次并按 `Delete`。
- 不新增锚点延长：抓住手柄拖动。
- 连接两个长度导向对象：插入 **Connector**。
- 将新的直线对象连接到已有对象：点击第一个对象末端，移到第二个对象开头再点击。

### 用 SimTalk 命令创建曲线对象

使用 `derive` 和 `duplicate` 方法：

```simtalk
var obj := .Materialflow.Conveyor.derive(.Models.Frame)
obj.Coordinate3D := [5, 5, 0]
var obj1 := .Materialflow.Conveyor.derive(.Models.Frame)
obj1.Coordinate3D := [1, 1, 0]
```

另见方法 `getCurveSegments` 和 `setCurveSegments`（下文）。

### 重用长度导向对象的线段

对于较小的线段表，可同时打开两个模型，直接在表间复制/粘贴值（右键行索引选择 **Append Row** 添加行）。

**导出线段表**（用 Method 通过 `getCurveSegments` 将坐标写入 Variable）：

```simtalk
Conveyor.getCurveSegments(MySegmentsVariable)
```

**导入线段表**（用 `setCurveSegments` 覆盖 Conveyor 的设置）：

```simtalk
Conveyor.setCurveSegments(MySegmentsVariable)
```

要在另一仿真模型中重用设置，插入 DataTable 并将线段表保存为对象文件（`.psobj`），再导入到另一模型的 DataTable 中。

### 插入直线与曲线段的键盘快捷键

| 操作 | 按键/点击 |
| --- | --- |
| 设直线段起点 | 左键 |
| 设曲线段起点 | `Ctrl` + 左键 |
| 取消吸附网格 | `Alt` + 左键 |
| 取消最后一点的吸附网格 | `Alt` + 右键 |
| 水平/垂直绘制直线段并取消吸附网格 | `Shift` + 左键 |
| 终止插入模式 | 右键 |
| 插入同类新曲线对象（无需在 Toolbox 中再次选择） | `Ctrl` + 右键，然后左键 |
| 水平/垂直绘制最后一段直线并取消吸附网格 | `Shift` + 右键 |
| 取消默认设置 | `Shift` + `Alt` |
| 按默认值插入图标 | `Shift` + 第一次左键点击 |
| 打开对话框 Sensor | `Alt` + 双击红色 Sensor 线 |
| 3D：插入上升曲线 | 上方向键，然后左键 |
| 3D：插入下降曲线 | 下方向键，然后左键 |

### 用鼠标编辑长度导向对象

点击 Edit 选项卡上的 **Show Manipulators** 显示所有操作器，然后左键拖动操作器到新位置。

- 操作器外观因对象而异；长度导向对象的起点/终点操作器是"截断"的（两个相连对象组成完整操作器）。
- 悬停操作器时会显示提示（tooltip）。

示例：

- 选择锚点并拖动以缩短线段。
- 选择锚点，按住 `Ctrl` 按上方向键抬升线段（可逐步重复——让工人/叉车从下方通过）。
- 拖动 Store 的右上角调整其图形尺寸（反映在宽/深及动画区域）。
- 使用旋转操作器绕 Store 中心旋转。

### 用键盘编辑长度导向对象

**操作器**：`Page Up` 加长、`Page Down` 缩短选中的操作器。

- 选择**第一个**操作器按 `Page Up`：加长相邻直线段，增加水平曲线段的曲线角（对垂直曲线无影响）。
- 选择**最后一个**操作器按 `Page Up`：缩短相邻段，减小水平曲线段的曲线角。
- 选择**第一个**操作器按 `Page Down`：缩短线段，减小水平曲线的曲线角。
- 选择**最后一个**操作器按 `Page Down`：加长线段，增大水平曲线的曲线角。

**传感器（Sensors）**：`Page Up`（或左方向键）左移；`Page Down`（或右方向键）右移。

### 精确编辑长度导向对象

1. 选中对象。
2. 按空格键或点击 Home 选项卡按钮，再点击 **Transformation** 选项卡。
3. 编辑位置、旋转和缩放值。
4. 点击 **Apply**。
5. 如需，在 **Appearance** 选项卡上编辑额外设置。

### 建模输送元素之间的高度差

**直线上升/下降坡道**：
1. 插入长度导向对象（如 4 m 的 Conveyor）并点击 **Show Manipulators**。
2. 右键点击右侧操作器，按住 `Ctrl` 按上方向键直到该侧达到所需高度。
3. 追加线段：右键 Conveyor 选择 **Segments > Append**；在 **Line/Arc Parameters** 中输入半径/角度，点击场景，点击 **Finish**。

**曲线上升/下降坡道**：
1. 插入长度导向对象（如 Conveyor）。
2. 按上方向键插入上升曲线（z 方向向上）或下方向键插入下降曲线。
3. 在 **Line/Arc Parameters** 中输入半径和角度（最大曲线角为 90°）。
4. 在场景中点击插入，再点击 **Finish**。

Segments 对话框中的勾选框表示 Conveyor 包含垂直曲线。

### 建模螺旋输送机

1. 点击 Toolbox 的 MaterialFlow 选项卡上的 Conveyor 并拖入。
2. 使用 **Line/Arc Parameters** 的标准设置（更大的半径对应更宽的弧）。
3. 按住 `Ctrl` 连续点击插入弧线段（初始放置在同一层、彼此正上方）。示例：一段直线、13 段弧线，再一段直线。
4. 按 `F7` 打开 Segments 表。
5. 在 **ΔZ** 单元格中输入相对前一段基础高度的额外偏移（如 0.5 m）。
6. 点击 OK。

在 **Appearance** 选项卡上修改螺旋设置。

## 9. 设置物流对象容量（Set the Capacity of a Material Flow Object）

- **容量**（ParallelStation、Sorter、Store、Transporter、Container 可容纳的零件数）在 **Attributes** 选项卡上以两个维度设置（X-Dimension 和 Y-Dimension）。
- **动画区域**（零件的 3D 放置）通过 **Edit 3D Properties > MU Animation > Area > Animation Area** 设置，适用于矩阵装载空间的对象（Store 类型：ParallelStation、Sorter、Store、Transporter、Container）、PlaceBuffer 和 Worker。

### 定义仿真对象的动画区域

示例：将圆柱形容器放入储物箱（装瓶工厂）。

1. 插入两个 Source、一个 AssemblyStation、一个 Conveyor、一个 Station 和一个 Drain，并用 Connector 连接。
2. 在 Class Library 的 MUs 文件夹中复制 `Part` 和 `Container` 以创建自定义 MU 类型。
3. 将复制的 container 重命名为 `StorageBox`（F2）；打开并用 **Exchange Graphics** 选择储物箱图形（s3D 文件也包含尺寸和动画数据）。
4. 在 X/Y/Z-Dimension 中配置尺寸以设定容量。
5. 将复制的 part 重命名为 `Canister`；删除其默认图形并创建自定义圆柱图形（Edit 选项卡 > Cylinder）。
6. 定义 Canister 的长、宽、高。
7. 运行仿真——AssemblyStation 在每个储物箱中放置 12 个容器；激活的动画区域使其均匀分布。

动画区域设置说明：

- **Show/Hide** 显示动画区域（红色，中心带红色方向指示器）。
- **Orientation > XY plane** 在 x-y 方向分布容器。
- Plant Simulation 使用图形长度的 94% 和宽度的 92%（扣除壁厚），基于 s3D 图形的区域设置。
- 中心的 Z 位置可能自动设置（如 5 cm 底部高度对应 0.05 m）。

## 10. 场景背景的上下文菜单（Context Menu of the Background of the Scene）

右键点击窗口空白区域打开上下文菜单；点击其边框可让迷你工具栏保持打开。

命令包括：

- Reset Simulation、Show Structure、Start/Stop Simulation、Start Fast Forward Simulation、Open Location、Open Origin、Open Class
- Show Graphic Structure、Show Inheritance、Show Attributes and Methods、Edit User-defined Attributes、Create User-defined Attribute
- Snap to Grid、Snap to Objects、Lock Structure、Exchange Graphics、Apply Changes (MUs)、Paste Contents of the Clipboard / Multiple Paste、Unhide Objects、Find Object
- Previous Scene、View All、Edit 3D Properties、View Options

> 不要把选中的对象与选中对象的图形混淆。

## 11. 创建用户自定义属性（Create User-defined Attribute）

选择此命令可在鼠标点击位置创建用户自定义属性（不适用于 Frame 或文件夹）。对话框 **User-defined Attribute** 以最后一次使用的 Transformation 和 Display Settings 打开；**Show in 3D** 默认选中。输入设置并点击 OK。

## 12. 上一场景（Previous Scene）

返回之前激活的层次级别或相机标记。

## 13. 将 3D 模型适配到 2D 模型（Adapt the 3D Model to the 2D Model）

当在 3D 激活的情况下创建 2D 模型、且模型包含带对象的 Frame 时，默认设置下的 3D 视图可能看起来出乎意料。

若 **Show Content** 激活，Frame 的内容（如 Interfaces 和 Station）会与其他物流对象显示在同一层。要使 3D 模型匹配 2D 模型，清除 **Show Content** 复选框即可。

## 目录说明

- `placement-transformation-frame-editing.md`：放置、变换与框架编辑章节的 Markdown 版本（本总结的源文件）。
- `placement-transformation-frame-editing.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。

*来源：Plant Simulation Help — "Working with Objects in the Frame"（10-920 及以下）。Unpublished work. © 2026 Siemens.*
