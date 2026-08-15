# Model Optimization, Video Recording, and Omniverse Output（模型优化、视频录制与 Omniverse 输出）总结

本目录包含 `model-optimization-video-publishing.md`（以及同名文本提取文件 `model-optimization-video-publishing.txtx`），内容为 Plant Simulation 帮助文档中 **模型优化、视频录制与 Omniverse 输出** 相关章节的说明。以下是对其内容的总结。

## 1. 优化模型（Optimizing the Model）

只有在完成模型的创建与修改之后再进行优化，因为被丢弃的数据无法恢复；优化可提升性能。

- 优化前请以不同名称另存模型，以便在优化后的模型报错或不符合预期时回到之前的状态。
- 点击 **Home** 功能区选项卡上的 **Optimize Model**。
- 选择要执行的优化；可选择单个设置或任意组合。

可用设置及其效果（以 `MyTurnplateShrinkwrapper3D.spp` 为例）：

| 设置 | 效果 |
|---|---|
| **Clean Up Class Library** | 从 Class Library 中删除模型中未使用的对象类，文件大小缩减最多；之后可用 **Start > Manage Class Library** 重新添加缺失对象 |
| **Optimize 3D Attribute Inheritance** | 示例中仅略微减小文件大小 |
| **Optimize 3D Graphic Structure** | 示例中仅略微减小文件大小；若之后还想编辑图形，不要启用此项 |

组合所有设置可得到最小文件大小，但仅比单独使用 **Clean Up Class Library** 略小。

### 优化可动画对象的层级结构

在 **Show Graphic Structure** 对话框中，可展平可动画对象的层级结构以获得更好的运行时性能。外观不变，仅展平图形结构。

> **注意：** 由于被丢弃的数据无法恢复，只有在完成对象建模后再展平结构。只有当优化后的图形在外观和结构上都符合你的意图时才接受结果。

## 2. 录制视频（Recording a Video）

录制器会生成任何多媒体播放器都能播放的 AVI 文件。**Video** 功能区选项卡提供所有录制与播放视频的工具。

### 选择视频设置

| 录制方式 | 说明 |
|---|---|
| **Start Simple Recording** | 以实时方式录制 Plant Simulation 或活动的 3D 窗口（物理时间一分钟等于播放一分钟），适用于演示如何操作模型 |
| **Start Simulation Recording** | 以缩放后的仿真时间录制仿真；作为 *Real-time x [video]* 输入的仿真时间分钟数对应一分钟播放，适用于展示真实的生产行为 |

> **注意：** 为防止覆盖上一次录制的 AVI 文件，录制另一段视频前请重命名输出文件。

### 布置录制场景

- 调整窗口大小，只显示观看者需要的内容。
- 对于 720p 或 1080p 视频，在 **Start Simple Recording** 和 **Start Simulation Recording** 对话框中设置录制窗口尺寸。
- 场景越大，需要的处理器时间越多，动画速度越慢，生成的视频文件也越大。
- 先选择位置和角度，再在开始前旋转、缩放场景。
- 对于仿真视频，可通过选择 **Play Camera Path** 自动将录制与相机动画关联。

### 录制视频

- 若要在仿真中途开始，先运行动画到所需时间，再点击开始录制。
- 必要时重置模型，然后启动仿真。
- 录制器捕获当前活动窗口的内容。避免点击其他窗口或将鼠标悬停在按钮上（否则提示会出现在视频中）。
- 可用功能区选项卡按钮取消、暂停和停止录制。
- 录制结束时，会弹出一个对话框显示 AVI 文件的保存位置，点击 **OK** 继续。
- 之后若要查看视频，请先停止仿真，因为仿真会占用大量资源。

### 播放视频

点击 **Video** 功能区选项卡上的播放按钮，默认的 Windows 媒体播放器会播放视频。也可用 Adobe Premiere 或 Camtasia 等数字视频应用程序进行编辑。

## 3. 在 Omniverse 中可视化仿真模型（Visualizing the Simulation Model in Omniverse）

Omniverse Connector 仅在订阅了该可选产品时可用。要在 Omniverse 中可视化 Plant Simulation 2606 模型：

1. 启动 Omniverse Connector。
2. 设置新的文件系统连接。
3. 建立到 Omniverse 的实时连接。
4. 在 NVIDIA Omniverse Composer 的 **Live data** 区域打开项目并增强模型外观。
5. 可选地使用 `MVA_WriteUSD` 函数。

### 启动 Omniverse Connector

- 启动 Plant Simulation 2606，并打开包含要导出或实时连接的模型的 Frame。
- 在 **Edit** 功能区选项卡上点击 **Omniverse Connector**，打开 **LiveConnect** 窗口。

### 设置新的文件系统连接

- 在 LiveConnect 窗口中点击 **Omniverse** 节点并选择 **New Filesystem connection**。
- 在文件浏览器中新建一个文件夹（或选择已有文件夹）。
- 在 **Add new Filesystem connection** 对话框中输入 **Description**。
- 点击数据文件夹并选择 **Connect**，然后选择数据文件夹链接。
- 在 LiveConnect 窗口底部的 **File name** 框中输入文件名。**Frames per second** 设置目前未使用，可留空。

#### 以 USD 格式导出仿真

设置好文件系统连接后，将正在运行的仿真导出为 USD（Universal Scene Description）文件：

1. 点击 **Export**，让 Omniverse 在配置的数据文件夹中创建所需的 usd 文件。
2. 启动要录制的仿真。
3. 录制完所有想展示的内容后停止仿真。
4. 再次点击 **Export** 以停止 usd 录制。
5. Plant Simulation 在数据文件夹中创建一个 library 文件夹和一个 usd 文件。
6. 在 NVIDIA Omniverse Composer 中打开导出的项目进行可视化。

### 建立到 Omniverse 的实时连接

- 确保 Omniverse Nucleus Server 正在运行。
- 在 LiveConnect 窗口中右键 **Omniverse** 节点并选择 **New Nucleus connection**。
- 输入 **Description**、Omniverse Nucleus 计算机的 IP 地址或服务器名，以及配置的 **Port** 端口号。
- 右键新的服务器节点并选择 **Connect**，以查看 Omniverse 数据文件夹。
- 在 NVIDIA Omniverse Composer 的 **Projects** 文件夹下创建文件夹结构。
- 右键项目中的 **Library** 文件夹并选择 **Set System root folder**。
- 选择项目文件夹，并在 **File name** 框中输入项目名称。
- 点击 **Connect** 并在 Frame 中启动仿真。
- 在 Omniverse Composer 的 **Live data** 区域打开项目。
- 在 Plant Simulation 中停止仿真，然后通过点击 LiveConnect 窗口中的 **Connect** 终止实时连接。

参考视频：`https://support.sw.siemens.com/en-US/knowledge-base/KB000179496_EN_US`

### 使用 MVA_WriteUSD 函数

`MVA_WriteUSD` 通过 SimTalk 创建并激活 Nucleus 连接、创建并激活文件系统连接，或终止实时/文件系统连接。

**备注** — 使用 `MVA_WriteUSD` 之前，需要：

- 通过 SimTalk 加载 Omniverse DLL：

```simtalk
loadLibrary(applicationHome + "PlantSimOmniverse.dll")
```

- 或点击 **Edit** 功能区选项卡上的 **Omniverse Connector** 手动启动 Omniverse 连接。

**类型：** Function

**语法：**

```simtalk
MVA_WriteUSD("parameter string")
```

**创建并激活 Nucleus 连接：**

```simtalk
var system_root_path:string = "/Projects/My_Project01/Library"
var output_path:string = "omniverse://127.0.0.1:80/Projects/My_Project01/myExport.live"
MVA_writeUSD(output_path+"?sysroot="+system_root_path)
```

**参数** — 参数字符串第一部分指定项目文件路径，第二部分指定 Omniverse 系统根文件夹，用于 USD 导出或实时连接：

```simtalk
MVA_writeUSD(<project file path>?systemroot=<system root path>)
```

## 目录说明

- `model-optimization-video-publishing.md`：模型优化、视频录制与 Omniverse 输出章节的 Markdown 版本（本总结的源文件）。
- `model-optimization-video-publishing.txtx`：相同内容的文本提取版本。
- 本目录无子文件夹，故无子文件夹 README.md。

*来源：Plant Simulation Help — "Model Optimization, Video Recording, and Omniverse Output"（10-1150 – 10-1163）。Unpublished work. © 2026 Siemens.*
