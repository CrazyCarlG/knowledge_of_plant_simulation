# Point Clouds (SimTalk Reference)

本目录汇总了 Plant Simulation SimTalk 中用于**状态图形（State Graphics）**、**点云（Point Clouds）** 和**视频录制设置（Video Recording）** 的相关属性与函数说明。详细内容见 `point-clouds.md`。

## 目录结构

- `point-clouds.md` — 完整参考文档（本 README 为其摘要）
- `point-clouds.txtx` — 原始导出文本

## 内容概览

### 1. 访问状态图形（Accessing State Graphics）

通过 `_3D.*` 属性控制物流对象 / 流体对象的状态图形。设置这些属性会**取消图形继承（deactivate graphic inheritance）**。

| 属性 | 类型 | 说明 |
|---|---|---|
| `_3D.StatesForColoring` | `string[]` | 指定参与状态着色的状态（如 Failed、Working、Blocked 等） |
| `_3D.StatesOrientation` | `string` | 设置状态图形方向与颜色：`"(Off)"`、`"Horizontal"`、`"Vertical"`、`"Color"` |
| `_3D.StatesPosition` | `length[]` | 设置状态图形参考点位置 `[x, y, z]` |
| `_3D.StatesScale` | `real` / `real[3]` | 设置状态图形缩放（可统一缩放或三轴分别缩放） |
| `_3D.StatesScaleWithObject` | `boolean` | 缩放对象时是否同步缩放状态图形（位置始终随对象缩放） |

状态与默认颜色映射（节选）：Unplanned=浅蓝、Failed=红、Stopped=粉、Working=绿、Blocked=黄、Paused=蓝、Setting-Up=棕、Waiting=橙 等。

### 2. 访问点云（Accessing Point Clouds）

通过 `_3D.*` 属性控制 Frame 的点云显示。

| 属性 | 类型 | 说明 |
|---|---|---|
| `_3D.PointCloudPath` | `string` | 点云文件路径（相对路径相对于模型所在文件夹） |
| `_3D.PointCloudPosition` | `array` | 点云位置 `[x, y, z]` |
| `_3D.PointCloudRotation` | `any` | 点云旋转：单个角度（绕负 z 轴）或 `[角度, 轴x, 轴y, 轴z]` |

### 3. 访问视频录制设置（Accessing Video Recording Settings）

通过 `F3D*` 函数录制、暂停、结束视频。

| 函数 | 说明 |
|---|---|
| `F3DfinishVideo` | 结束当前视频录制（若由 `F3DrecordSimulationVideo` 启动则同时停止仿真） |
| `F3DisRecordingAVideo` | 返回当前是否正在录制视频（`boolean`） |
| `F3DpauseVideo([StartPause:=true])` | 暂停（`true`）或继续（`false`）视频录制 |
| `F3DrecordSimulationVideo(...)` | 启动/恢复仿真并录制视频，参数丰富（路径、对象、时间比例、帧率、描述、起止时间、相机路径等） |
| `F3DrecordVideo(...)` | 录制 Plant Simulation 或活动窗口的视频（路径、帧率、描述、是否录制整个应用窗口） |

> 说明：录制相关函数受安全设置 *File > Model Settings > General > Prohibit Access to the Computer* 影响，启用该设置时无法从其他文件夹复制数据。
