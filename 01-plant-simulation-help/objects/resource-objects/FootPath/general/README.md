# FootPath [object] — 目录说明

本目录 (`general`) 汇总了 Siemens Tecnomatix Plant Simulation 中 **FootPath** 资源对象的帮助文档。目录内包含以下文件：

- `general.md` — FootPath 对象的完整 Markdown 文档（正式帮助内容）。
- `general.txtx` — 同一帮助内容的原始文本提取版（包含页码、页眉页脚等排版痕迹，内容与 `general.md` 等价）。

> 本目录下没有子文件夹，因此没有额外的子级 `README.md` 内容。

---

## 内容概要

**FootPath** 对象用于建模一条路径，供 **Worker** 从 **WorkerPool** 走到 **Workplace**（工作站位）。

### 核心概念

- FootPath 细化了 **Broker–Importer–Exporter** 概念，形成 **Worker–WorkerPool–Workplace–FootPath** 概念。
- 在 WorkerPool 中可选择 Worker 前往工作站的 **Travel Mode（出行方式）**：
  - 在模型区域内自由行走（如同现实世界）。
  - 直接传送到指定的 Workplace。
  - 沿模型中的 FootPath 行走。
- Worker 通常作为容量为 1 的 Exporter。若需建模并仿真 WorkerPool 与工作站之间、或工作站之间的行走距离，使用 FootPath。
- Worker 在 FootPath 上移动时，Plant Simulation 会为其添加动画。

### FootPath 网络

- 可用 **Connector** 连接多条 FootPath 构成网络。
- 只要 WorkerPool 与 Workplace 连接在同一网络中，Worker 就会沿 **最短路径** 往返。
- 网络由所有被 Connector 相连的 FootPath，以及连接到这些 FootPath 的 WorkerPool 和 Workplace 共同组成。

### 行走时间

- 行走时间取决于 Worker 的 **Speed（速度）** 与所经过各 FootPath 的 **Length（长度）之和**。
- 只有 Worker 在 FootPath 上行走时才消耗时间；被直接传送或未走 FootPath 时不消耗时间。
- 注意：FootPath 可容纳任意数量的 Worker（因为 Worker 本身没有长度）。

### Broker 调度行为

Broker 将 Worker 分派到各个工作站，具体行为取决于建模方式：

1. 使用物料流对象 + Workplace 建模，且 WorkerPool 与 Workplace 用 FootPath 相连 → Worker 行走及工作时均有动画。
2. 插入了 Workplace，但 Worker 无法通过 FootPath 到达 → Worker 被直接传送到 Workplace 并在此处显示动画。
3. 未插入 Workplace、不存在支持该服务的 Workplace，或所有相关 Workplace 均被占用 → Worker 被传送到工作站本身执行任务，但不显示动画（仍继续在 WorkerPool 中显示）。

### 插入与外观

- FootPath 可插入 Frame：
  - 默认以**曲线对象**形式插入。
  - 可插入任意曲线段与直线段序列，真实建模传送系统上 Transporter 的运动。
- 可在 **Appearance** 选项卡选择不同配置。
- 鼠标悬停可显示对象信息 Tooltip。

### 操作提示

- **Show Manipulators（显示操纵点）**：在 Edit 功能区点击，或按 **M** 键，可修改对象图形的长度与锚点。
- **添加到模型**：Home 功能区 → **Manage Class Library > Basic Objects > Resources > FootPath**。
- **示例模型**：Window 功能区 → **Start Page > Getting Started > Example Models > Small Examples**。

---

## 对话框与属性

双击 FootPath 图标打开对话框，可编辑仿真属性与动画（3D）属性。

### Tab Attributes（属性选项卡）

- **Length [文本框]**：FootPath 的长度。Worker 从位置 0 进入，覆盖设定长度后离开。
- **Width [文本框]**：FootPath 的宽度。

### 其他选项卡与菜单

- **Tab User-defined**：自定义属性。
- **Navigate Menu / View Menu / Tools Menu / Help Menu**：提供刷新、显示属性与方法、编辑控件、编辑观察器等命令。

### 方法（Methods）

FootPath 提供 **Methods of All Objects（所有对象的通用方法）**。可通过 **Show Attributes and Methods** 窗口查看全部方法、只读属性与属性。

方法语法示例：

```simtalk
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

---

## 参见（See also）

- Worker Stays Here After Completing the Job
- Get Job Orders At Home Only
- Home Location
- FootPath
- Work with Length-oriented Objects
- Model Workers and the Jobs They Do
- Worker-WorkerPool-Workplace-FootPath concept
- Broker-Importer-Exporter concept
- 视频：<https://youtu.be/Rj5eYZu8pl4?si=eMS1tM55tJ4k9_ee&t=420>
- 视频：<https://youtu.be/Rj5eYZu8pl4?si=zfQFRHZgC336hXB7&t=1040>
