# Step-by-Step Help — 目录说明

本目录及同级目录（`onboarding-plant-simulation/` 下）收录了 Plant Simulation Help 中「入门（Onboarding）」相关的帮助文档，涵盖从**认识 Plant Simulation**、**用户界面与基本操作**，到**仿真建模理论基础**的内容。

## 目录结构

```
onboarding-plant-simulation/
├── step-by-step-help/
│   ├── step-by-step-help.md    # Step-by-Step Help 总览
│   └── step-by-step-help.txtx  # 原始帮助文本
├── getting-started-ui-basic-operations/
│   ├── getting-started-ui-basic-operations.md    # UI 与基本操作
│   └── getting-started-ui-basic-operations.txtx  # 原始帮助文本
└── modeling/
    ├── modeling.md    # 仿真建模概念
    └── modeling.txtx  # 原始帮助文本
```

---

## 文档摘要

### 1. Step-by-Step Help（本目录 `step-by-step-help.md`）

介绍最常见的建模任务，说明如何创建仿真模型、如何使用内置对象解决问题，帮助用户快速掌握建模流程。

**涵盖主题：**

- Getting to Know Plant Simulation（认识 Plant Simulation）
- Modeling the Material Flow（物料流建模）
- Visualizing the Material Flow（物料流可视化）
- Animate the Simulation Model and View the Results（动画与结果查看）
- Import Data for the Simulation（仿真数据导入）
- Set Parameters in the Model（模型中设置参数）

**另请参阅（Also Consult）：** What's New、Introducing Plant Simulation、Update Arbitrary Old Models、The User Interface Components、The Objects Reference Help、The SimTalk Reference、Outdated SimTalk Names、The Add-Ins Reference Help、The Libraries Reference。

---

### 2. Getting Started: UI & Basic Operations（`getting-started-ui-basic-operations.md`）

总结 Plant Simulation 的用户界面与基本操作，帮助新手快速上手。

#### 认识 Plant Simulation（Getting to Know Plant Simulation）

- **观看 YouTube 视频** — 从 Start Page 访问，快速了解常用建模任务；帮助主题中的链接会通过时间码（如 `=18`）跳转到对应片段，使用 YouTube 短链接。
- **查看示例模型** — 在 Start Page 的 `Example Models > Small Examples` 下打开，演示各类问题的建模思路；可搜索示例模型 ReadMe 文件中的描述。
- **查阅 Step-by-Step Help** — 通过 `File > Help > Contents` 打开，或阅读官网下载的 PDF 文档，也推荐用 Copilot 搜索在线帮助。

#### 窗口类型（Work with Window Types）

Plant Simulation 是一个**多文档界面（MDI）** 应用，窗口显示在公共父窗口中：

- **Docking Windows（停靠窗口，红框）** — Class Library、Favorites、Toolbox、Console，始终在前台；可浮动（Floating）、重新停靠（Docking）、自动隐藏（Auto Hide），用 **Ctrl+Tab** 切换。
- **Object Windows（对象窗口，蓝框）** — Frame、Method、Method Debugger、DataQueue、DataStack、DataList、DataTable 与 Icon Editor 的窗口，始终在后台；可用 `openDialogBox` 前台打开、`closeAllWindows` 关闭所有。
- **Dialog Boxes（对话框，绿框）** — 各类对象的属性对话框，始终在最前、不可最小化/最大化，可拖出程序窗口。
- 按 **Ctrl+Tab** 打开 **Window Navigator** 在停靠窗口与对象窗口间切换。

#### 设置选择（Select Settings in Plant Simulation）

- **模型级设置**：`File > Model Settings`（保存在模型文件中）。
- **新模型设置**：`File > Preferences`，其中 General、3D、Editor 为模型无关设置；Simulation、User Interface、Units 为新模型专用的模型相关设置。
- **常规选项**：选择新建模型的语言（影响文件夹/对象命名、下拉项、属性返回值等）、日期时间格式、保存时的注释类型。
- **单位与时间显示**：设置夏令时（欧盟/美国默认规则）、Time Scale（0–86400）与 Transfer If；时间语句格式为 `days:hours:minutes:seconds`，内部以秒存储。

#### 修改对象设置（Change the Settings of the Objects）

- 在对象对话框内修改值（文本框、下拉框、复选框）。
- 通过 SimTalk 赋值（如 `MyStation.ProcTime := 180` 或 `MyStation.ProcTime := 3:00`）；路径语法为 `对象.属性 := 值`。
- 在 Show Attributes and Methods 窗口中修改（按 F8 打开）。
- 用 AttributeExplorer 集中管理多个对象的属性，可导出/导入制表符分隔的文本文件。

#### 查找对象与文本（Find Objects and Text）

通过 **Find Object** 查找对象名称、条件（SimTalk 表达式）、属性值、Method 源代码或表格表达式；支持 **Match Whole Word Only**、**Match Case**、**Regular Expression（正则表达式）** 等选项，并可替换 Method 中的源代码。

---

### 3. Modeling（`modeling.md`）

介绍仿真的理论基础与建模概念，以及开始建模前需要了解的内容。

#### 仿真与建模概念（Simulation and Modeling Concepts）

仿真通过动态分析得出客观决策，帮助管理者安全规划并降低成本。当真实系统/工厂实验成本过高、试验时间受限时，建模、仿真与动画是分析与优化时间动态过程的优秀工具。

#### 什么是仿真（What is Simulation?）

VDI 3633 将仿真定义为**在一个可实验的模型中对系统及其动态过程的模拟**，目标是将结果迁移到真实工厂。典型仿真研究步骤：检查真实工厂 → 抽象建模 → 运行实验 → 解释数据 → 作出决策。模型开发是**循环且演进**的过程。

#### 时间导向仿真与事件控制仿真（Time-Oriented vs. Event-Controlled Simulation）

Plant Simulation 是**离散、事件控制**的仿真程序，只在事件发生的时刻进行考察（如零件进入/离开站点）。零件进入物料流对象时，Plant Simulation 计算离开时间并将离开事件插入 EventController 的调度事件列表，因此仿真时间从一个事件跳到下一个事件。

#### 为什么使用仿真（Why Use Simulation?）

- **规划新工厂**：在投产前发现并消除问题，确定并优化时间与产能，确定缓冲区大小与机器数量，考察故障影响，确定所需工人数，评估备选方案，降低投资成本。
- **优化现有工厂**：先在仿真环境中验证再实施优化措施，优化控制策略与订单顺序，测试日常流程。
- **总体收益**：提高生产率、减少投资、降低库存与周转时间、优化系统尺寸、降低投资风险、最大化资源利用、改进产线设计与排程。

#### 实施仿真项目（Implement a Simulation Project）

项目实施流程：**描述项目 → 规划项目 → 确定所需数据及获取方式 → 构建仿真模型 → 验证模型并检查有效性 → 执行仿真实验并收集结果 → 分析实验结果 → 撰写最终文档**。整个过程同样是循环演进的。

---

## 说明

- 以上文档均源自 *Plant Simulation Help*，未发表作品，© 2026 Siemens。
- 每个 `.md` 文件对应一个 `.txtx` 原始帮助文本，内容一致，前者为整理后的 Markdown 版本。
