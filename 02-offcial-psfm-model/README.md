# 02-offcial-psfm-model

Siemens Tecnomatix Plant Simulation 的**官方示例模型**（Factory 51）及其逆向分析文档。模型以 PSFM 文本格式保存，配套的 `model-knwo-how/` 目录是对该模型结构、逻辑与代码的逐层解读。

**English:** The **official example model** (Factory 51) of Siemens Tecnomatix Plant Simulation, plus reverse-engineering notes. The model is stored in PSFM text format; the accompanying `model-knwo-how/` directory explains its structure, logic, and code layer by layer.

> 模型版权归 Siemens 所有，本目录仅用于学习与知识管理。
> **English:** The model is © Siemens; this directory is for learning and knowledge management only.

## 目录结构 / Directory Structure

```
02-offcial-psfm-model/
└── Factory51/
    ├── Factory51.psfm/          # 官方示例模型（PSFM 文本格式，约 1592 个对象）
    │   ├── $ModelInfo.yaml      # 模型版本与设置（Plant Simulation 26.6.2.3599）
    │   ├── Models/              # 根 Frame 与 P1/P2/Warehouse 各实例对象
    │   ├── UserObjects/         # 自定义类库（Production、Milling、AGV、Box 等）
    │   ├── ApplicationObjects/  # 外部应用库（CranesAndMore、HBW3D）
    │   └── MaterialFlow/ Resources/ InformationFlow/ MUs/ UserInterface/
    │                            # 标准基础类（Built-in 对象的父类模板）
    └── model-knwo-how/          # 逆向分析文档（Markdown）
        ├── Factory51-建模思路.md         # 模型定位、建模范式与控制逻辑梳理
        ├── Factory51-模型结构.md         # Frame 层级、对象清单与物料流拓扑
        ├── Factory51-类结构与继承关系.md  # 类继承树与实例化映射
        └── Factory51-代码样例.md         # SimTalk 代码清单与逐段注释
```

## 模型概述 / Model Overview

**Factory 51** 是一个**离散事件制造 + 仓储物流的一体化演示模型**：原材料由卡车送达 → 高架立体仓库（HBW）暂存 → 配送至两条平行生产线（P1/P2）完成机加工、抛光、喷漆、烘干、后处理、质检 → 成品入库（WMS + RackLane）→ 出货。

核心要点：

- **产品**：两类零件（Aubergine 紫 / Strawberry 粉），各 60 件，共 120 件。
- **生产线**：`Production` 一个类定义两条线 P1、P2（同构复用），内部再派生 Polishing/PostProcess/Painting/Drying 等工序单元。
- **仓储**：复用 `CranesAndMore`（堆垛机/存储区）与 `HBW3D`（高架立体仓库 WMS/巷道）外部库。
- **物流**：叉车/AGV 沿标记点路径搬运；入库为推式、出库为拉式（`StoreExit.Init` 按需拉料）。
- **控制**：`EntranceCtrl`/`ExitCtrl` 挂载自定义 Method；`Production/Line.OnExit` 按下游抛光站空满动态分流。
- **可视化**：实时仿真（`Realtime=true`）、3D 加工动画、`CostAnalyzer` 成本分析与 `SankeyDiagram` 桑基图。

## 分析文档索引 / Analysis Docs

| 文档 | 内容 |
|---|---|
| `Factory51-建模思路.md` | 模型定位、推拉结合范式、对象选型理由、关键参数来源、控制逻辑（进货→入库→生产线→出货）与可复用模式 |
| `Factory51-模型结构.md` | Frame 层级树、1592 个对象的类型分布清单、物料流拓扑、控制与数据流关系 |
| `Factory51-类结构与继承关系.md` | 三层层级类继承树（内置 → 类 → 派生 → 实例）、类/实例映射、继承/引用/委托/属性绑定关系 |
| `Factory51-代码样例.md` | SimTalk 源码清单（Source/TruckArrivals/UnloadTruck/WMS/StoreExit/Production/Milling 等）与逐段注释解读 |

## 如何打开模型 / How to Open

模型为 PSFM 文本格式（`ModelFormat: 1`），可在 Siemens Tecnomatix Plant Simulation 中打开：

1. 启动 Plant Simulation（本模型基于 `26.6.2.3599`）。
2. `File → Open` 选择 `Factory51/Factory51.psfm` 目录。
3. 运行仿真即可观察实时 3D 演示与 KPI 统计。

> 注：PSFM 中 `.jt` 文件为 Siemens JT 二进制格式（3D 图形 + 编译后源码），非明文 SimTalk；明文源码位于同目录对象 `.yaml` 的 `$CustomAttributes` 或 `Program` 字段。
