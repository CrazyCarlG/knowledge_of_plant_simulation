# Icon Behavior（图标行为）目录总结

本目录汇总了 Plant Simulation 帮助文档中「图标行为」相关章节的内容。目录内包含以下 Markdown 文件：

- `icon-behavior.md`：主内容文件（英文原文的 Markdown 版本），主题为 **在 Omniverse 中可视化仿真模型** 与 **动画仿真模型并查看结果**。

> 目录内无子文件夹，因此不存在子文件夹 README.md。

---

## 内容概览

`icon-behavior.md` 涵盖两个相互关联的主题：

1. 创建并管理到 Omniverse 的 **Live Connection（实时连接）** 与 **Filesystem Connection（文件系统连接）**（通过 `MVA_WriteUSD`）。
2. **动画仿真模型** 以及 **使用对象图标**（Icon Editor）。

---

## 1. Live Connection 与 Filesystem Connection

### 创建并激活连接

对于 **Live Connection**，项目文件与系统根文件夹通常是 Omniverse Nucleus 项目文件夹中由 Omniverse Nucleus 服务器管理的子文件夹。

使用以下代码创建并激活带 `MVA_WriteUSD` 的 **Filesystem Connection**：

```javascript
var system_root_path:string = "D:/USD_DataFiles/My_Project01/Library"
var output_path:string = "file://d:/USD_DataFiles/My_Project01A/myExport.usd"
MVA_writeUSD(output_path+"?sysroot="+system_root_path)
```

### 终止连接

输入空字符串即可终止已打开的 Live Connection 或 Filesystem Connection：

```javascript
MVA_writeUSD("")
```

### 注意事项

- 当从 Plant Simulation 以相同的项目文件和系统根启动新的导出时，请确保 Omniverse Composer 没有对先前导出的仿真保持打开连接。
- 对于 **Nucleus Live Connection**，函数 `MVA_writeUSD()` 尚不受支持。

---

## 2. 动画仿真模型并查看结果

本部分介绍动画仿真模型以及查看仿真运行结果，包含：

- 动画仿真模型（Animate the Simulation Model）
- 查看与可视化统计（View and Visualize Statistics）
- 切换状态与执行动作（Switch States and Execute Actions）

### 动画设置位置

Plant Simulation 在对话框 **Edit 3D Properties** 的 **Tab MU Animation** 上以 3D 形式显示动画设置。

### 激活与停用动画

仿真运行期间，动画会显示：

- 对象的状态。
- MU 在仿真模型中的位置和运动。

> **注意：** 动画化零件和对象图标会减慢仿真速度，因此仅在确实要展示模型或检查模型行为是否正确时才激活。对于过夜批处理运行（overnight batch runs），建议停用动画。

- **MU** 与 **State Animation** 只能一起激活或停用，不能单独操作。
- **激活 MUs and States** 时，会立即看到零件流动以及 MU 堆积的阻塞站点。
- **停用 MUs and States** 后，若某对象打算改变其状态，Plant Simulation 会延迟其在屏幕上的显示，直到再次激活动画或选中该对象。
- 要停用 MUs and States，点击 **Home** 选项卡上的相应按钮。
- 要以所选设置运行仿真，点击 EventController 中的 **Start/Stop Simulation**。

> **注意：** 点击 **Home** 选项卡上的按钮会激活 MU 与 State Animation。要在不动画化对象和 MU 的情况下启动仿真，请点击另一个动画按钮。

---

## 3. 使用对象图标（Working with Object Icons）

### 概览

**Icon Editor（图标编辑器）** 是为了向后兼容而提供的编辑图标的工具。

在早期版本中，Plant Simulation 的 2D 可视化使用对象的图标，在 Class Library、Toolbox 和 Frame 中显示对象。图标还可以显示对象的运行状态，如 failed（故障）、paused（暂停）、unplanned（未计划）等。

对于旧版本创建的仿真模型，仍可通过点击 **Edit Icons [Home ribbon]** 打开 Icon Editor 来修改图标。

> Plant Simulation 2606 的 3D 可视化不再使用图标。

### 创建图标（Create an Icon）

可以创建新图标，然后打开现有图形使用。可执行以下任一操作：

- 点击 **Edit** 选项卡上的 **New Icon**。若打开的图形大于默认图标尺寸 **41 × 41 像素**，输入其他宽度和/或高度。
- 点击 **Import > Import Bitmap File / Import Icon Resource**，导航到包含所用图形的文件夹，选择文件并点击 **Open**。
- 将图形文件（`.gif`、`.bmp`、`.ppm`、`.ppm raw`、`.dxf` 或 `.dwg`）从 Windows 资源管理器拖到绘图窗口上并放下。
- 为图标输入有意义的 **Name**。
- 要绘制线条或形状，在 **Edit** 选项卡上选择绘图颜色和一种绘图工具，然后在绘图窗口中绘制形状。
- 更改颜色：
  - **一个或多个像素**：在调色板中选择颜色，然后用某种绘图工具点击要改色的像素。
  - **连续颜色区域**：在调色板中选择颜色，然后点击要改色的区域。
- 用两种颜色绘图时，分别给左右鼠标键分配颜色：
  - 用鼠标左键点击调色板中的颜色，把它添加到顶部绘图颜色字段；或
  - 双击颜色字段，在 **Colors** 对话框中自定义颜色。
  - 然后点击相应的鼠标键用该颜色绘图。
- 可使像素或区域透明：
  - **一个或多个像素**：点击透明字段，然后用某种绘图工具点击要设为透明的像素。
  - **连续颜色区域**：点击透明字段，然后点击要设为透明的区域。

> **注意：** Frame 的背景会透过任何标记为透明的区域显示出来。

- 点击应用按钮应用更改并关闭 Icon Editor。

### 编辑图标（Edit an Icon）

可以编辑对象的图标，可执行以下任一操作：

- 在 Frame 中右键对象并选择 **Edit Icons**。
- 在 Frame 中选中对象，点击 **Home** 选项卡上的 **Edit Icons**。
- 在 Class Library 中右键对象并选择 **Edit Icons**。
- 点击 **Home** 选项卡上的相应按钮以编辑所选 Frame 的图标。
- 点击 **Home** 选项卡上的相应按钮以编辑所选对象的图标。
- 然后使用 Icon Editor 的 **Edit Ribbon Tab** 上的功能实际编辑图标。
- 点击应用按钮应用更改。

### 使图标区域透明（Make Areas of an Icon Transparent）

可使打开的图形文件的连续区域透明，以便 Frame 的背景色透出。步骤如下：

1. 点击 **Home** 选项卡上的 **Edit Icons** 打开 Icon Editor。
2. 点击导航按钮，导航到要设为透明的图标。
3. 点击 **color picker（取色器）** 并点击图标背景，使该颜色成为要替换的活动绘图颜色。
4. 在 **Color Palette proper（调色板本体）** 中（而非透明颜色字段中）选择替换活动绘图颜色的透明色。

> 若透明色不在调色板本体中，双击调色板中任一含不需要颜色的字段，在 **Colors > Custom** 对话框中输入 `0, 128, 128` 并点击 OK。

- 确保 **Icon > Activate Transparency** 已激活。
- 点击 **Apply Changes** 使该区域透明。
- 要使用更改后的图标作为对象的当前图标，确保选中相应选项。

---

## 目录文件说明

| 文件 | 说明 |
| --- | --- |
| `icon-behavior.md` | 图标行为章节（Live/Filesystem Connection、动画与对象图标）的 Markdown 版本，为本总结的源文件。 |
| `README.md` | 本文件，目录内容的中文总结。 |

*来源：Plant Simulation Help — "Visualize the Simulation Model in Omniverse" 与 "Animating the Simulation Model and Viewing the Results"。Unpublished work. © 2026 Siemens.*
