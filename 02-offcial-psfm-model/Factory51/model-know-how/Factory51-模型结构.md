# Factory51 模型结构分析

> 模型来源：`02-offcial-psfm-model/Factory51/Factory51.psfm`（Folder Model，PSFM 文本格式）
> 模型版本：Tecnomatix Plant Simulation `26.6.2.3599`，`ModelFormat: 1`
> 对象总数：`1592`（来自 `.UserSettings.yaml` 的 `NumberOfObjects`）

本模型是 Siemens 官方的 Factory 51 演示/示例模型，展示了一个完整的离散事件生产与仓储系统：原材料由卡车送达，经高架立体仓库（HBW）暂存，再配送至两条平行生产线（P1、P2）完成机加工、抛光、喷漆、后处理等工序，成品进入成品仓库（WMS + RackLane）并通过 AGV / 叉车流转。以下按五部分逆向解析其结构。

---

## 一、Frame 层级树

> 说明：PSFM 目录中每个 Frame 由 `$.yaml` 定义，`InternalClassType: Frame` 表示 Frame 对象。`Origin` 字段指向其所属的自定义类（UserObjects）或类库（ApplicationObjects/标准库）。`isClass`（类定义，位于 UserObjects/ApplicationObjects）与 `isInstance`（实例，位于 Models 下）由所在目录区分。

```
Factory51                                (根Frame，Models/Factory51，isInstance)
├── P1                                   (Frame，Production 类实例)
│   ├── ClearPaint                       (Frame，Painting 类派生 → 实例)
│   ├── Drying                           (Frame，Drying 类派生 → 实例)
│   ├── Drying1                          (Frame，Drying 类派生 → 实例)
│   ├── Drying2                          (Frame，Drying 类派生 → 实例)
│   ├── Painting1                        (Frame，Painting 类派生 → 实例)
│   ├── Painting2                        (Frame，Painting 类派生 → 实例)
│   ├── Polishing1                       (Frame，PolishingCell 类派生 → 实例)
│   ├── Polishing2                       (Frame，PolishingCell 类派生 → 实例)
│   ├── Polishing3                       (Frame，PolishingCell 类派生 → 实例)
│   ├── PostProcess1                     (Frame，PostProcess 类派生 → 实例)
│   ├── PostProcess2                     (Frame，PostProcess 类派生 → 实例)
│   └── PostProcess3                     (Frame，PostProcess 类派生 → 实例)
├── P2                                   (Frame，Production 类实例，与 P1 结构相同)
│   └── (同 P1 的 11 个子 Frame)
├── Warehouse                            (Frame，Warehouse 类实例)
│   ├── RackLane1..RackLane5             (Frame，RackLane 类[HBW3D]派生 → 实例，共 5 个)
│   └── WMS                              (Frame，WMS 类[HBW3D]派生 → 实例)
└── (根 Frame 直属对象，见下)
    Source, TruckArrivals, StoreEntry, StoreExit, StorageArea, EmptyPalletsStore,
    MultiPortalCrane, SmallCrane, PaletteLine, Track/Track1..3, ChargeTrack1..2,
    SupplyRoad, PickAndPlace(1..5/Top/Bottom), AngularConverter1, Converter(1..3/11/111/112),
    Line(1..17/71/711/712/81/82/...), UpperStoreExit, Shipment1..3, TruckDepartures,
    UnloadTruck, userSetTarget, EventController, HtmlReport, CostAnalyzer,
    PartSankey, WorkerSankey, AGVPool, M_* Marker, 变量/按钮/显示 等
```

**Frame 层级要点：**

| Frame | 类型来源 | 是否自定义类实例 | 对象数量说明 |
| --- | --- | --- | --- |
| Factory51 | Frame（根） | 是（模型主 Frame） | 根 Frame 直属约 100+ 对象 + 3 个子 Frame |
| P1 / P2 | Production（自定义 Frame 类） | 是 | 各含 11 个子 Frame + 约 90 个直属对象 |
| P1/ClearPaint | Painting 类派生 | 是 | 含 Line/Station/Workplace/LockoutZone/Comment |
| P1/Drying(1/2) | Drying 类派生 | 是 | 仅含 Line（Conveyor） |
| P1/Painting1/2 | Painting 类派生 | 是 | 含 Line/Station/Workplace/LockoutZone/PaintColor |
| P1/Polishing1..3 | PolishingCell 类派生 | 是 | 含 Polishing/Buffer/DisplayBuffer/Display/Workplace |
| P1/PostProcess1..3 | PostProcess 类派生 | 是 | 含 Line1..3/Step1..3/Workplace(1/2)/Display |
| Warehouse | Warehouse（自定义 Frame 类） | 是 | 含 WMS + RackLane1..5 |
| Warehouse/RackLane1..5 | HBW3D RackLane 派生 | 是 | 每 RackLane 约 60 个对象（货架巷道单元） |
| Warehouse/WMS | HBW3D WMS 派生 | 是 | 约 54 个对象（仓库管理系统逻辑） |

> 注：P2 与 P1 完全同构，文件目录中两者的子 Frame 清单一致。

---

## 二、对象清单表

### 2.1 全模型对象类型分布（共 1592 个对象，按 `InternalClassType` 统计）

| 对象类型(英文) | 所属大类 | 数量 | 说明 |
| --- | --- | --- | --- |
| Variable | InformationFlow | 350 | 全局变量与自定义属性，WMS/RackLane 中最多 |
| Method | InformationFlow | 233 | 控制逻辑方法 |
| Conveyor | MaterialFlow | 224 | 传送带（Line 系列为主） |
| Comment | UI | 92 | 注释 |
| Station | MaterialFlow | 88 | 加工站（Milling/Polishing/PostProcess 等） |
| Workplace | Resource | 78 | 工位（与 Worker 协作） |
| Converter | MaterialFlow | 73 | 转换器（分/合流） |
| Frame | — | 60 | 各层 Frame |
| Interface | MaterialFlow | 52 | 跨 Frame 接口 |
| Display | UI | 52 | 显示对象 |
| DataTable | InformationFlow | 36 | 数据表 |
| Store | MaterialFlow | 28 | 仓库/暂存 |
| AngularConverter | MaterialFlow | 26 | 转角转换器 |
| Dialog | UI | 24 | 对话框 |
| Folder | — | 20 | 文件夹（类库组织） |
| PickAndPlace | MaterialFlow | 18 | 机械手/拾取放置 |
| Track | MaterialFlow | 16 | 轨道（含 MultiPortalCrane/SmallCrane） |
| Buffer | MaterialFlow | 13 | 缓冲 |
| LockoutZone | Resource | 11 | 锁定区（安全） |
| HtmlReport | UI | 11 | HTML 报告 |
| Drain | MaterialFlow | 9 | 出口/消散 |
| Transporter | MaterialFlow | 8 | 运输 MU（AGV/叉车/卡车） |
| WorkerPool | Resource | 7 | 工人池 |
| Toolbar | UI | 7 | 工具栏 |
| Checkbox | UI | 7 | 复选框 |
| Marker | Resource | 5 | 标记点（AGV/叉车路径点） |
| Part | MaterialFlow | 4 | 零件 MU 类 |
| DataList | InformationFlow | 4 | 数据列表 |
| Container | MaterialFlow | 4 | 容器 MU 类（Box/Pallet） |
| Chart | UI | 4 | 图表 |
| Broker | Resource | 4 | 经纪人（工人调度） |
| Source | MaterialFlow | 3 | 源头（Source/TruckArrivals） |
| SankeyDiagram | UI | 3 | 桑基图 |
| Connector | MaterialFlow | 3 | 连接器 |
| Button | UI | 3 | 按钮 |
| Worker | Resource | 2 | 工人 |
| TwoLaneTrack | MaterialFlow | 2 | 双向轨道（SupplyRoad） |
| EventController | InformationFlow | 2 | 事件控制器 |
| CostAnalyzer | UI | 2 | 成本分析 |
| AGVPool | Resource | 2 | AGV 池 |
| FootPath | Resource | 1 | 步道 |

### 2.2 根 Frame（Models/Factory51）关键对象

| 所属Frame | 对象名称 | 对象类型(英文) | 所属大类 | 关键属性(名称=值) |
| --- | --- | --- | --- | --- |
| Factory51 | Source | Source | MaterialFlow | `EntranceCtrl= self.OnEntrance`；`Number=120`；每次生成 1 托盘→4 箱→4 零件/箱 |
| Factory51 | TruckArrivals | Source | MaterialFlow | `Interval= [Normal,15:00,4:00,2:00,30:00]`；`Start=40`；OnEntrance 生成卡车载荷 |
| Factory51 | SupplyRoad | TwoLaneTrack | MaterialFlow | 卡车行进道路 |
| Factory51 | StoreEntry | Buffer | MaterialFlow | `ExitCtrl= StorageArea.storing` |
| Factory51 | StoreExit | Buffer | MaterialFlow | `ExitCtrl= self.OnExit` |
| Factory51 | UpperStoreExit | Station | MaterialFlow | 上层出库站 |
| Factory51 | StorageArea | Store | MaterialFlow | `StoreType= Floorspace`；`XDim/YDim/ZDim=4/5/2`（CranesAndMore StorageArea） |
| Factory51 | EmptyPalletsStore | Store | MaterialFlow | 空托盘存储 |
| Factory51 | MultiPortalCrane | Track | MaterialFlow | CranesAndMore MultiPortalCrane 类（高架堆垛机） |
| Factory51 | SmallCrane | Track | MaterialFlow | CranesAndMore MultiPortalCrane 类（小型堆垛机） |
| Factory51 | Track / Track1..3 | Track | MaterialFlow | AGV/堆垛机轨道 |
| Factory51 | ChargeTrack1/2 | Track | MaterialFlow | 充电轨道 |
| Factory51 | PaletteLine | Conveyor | MaterialFlow | `ExitCtrl= self.OnExit` |
| Factory51 | PickAndPlace(1..5/Top/Bottom) | PickAndPlace | MaterialFlow | 拾取/放置机器人 |
| Factory51 | AngularConverter1 | AngularConverter | MaterialFlow | 转角转换器 |
| Factory51 | Converter(1..3/11/111/112) | Converter | MaterialFlow | 分/合流转换器 |
| Factory51 | Line(1..17 等) | Conveyor | MaterialFlow | 传送线，多处挂 `ExitCtrl` |
| Factory51 | Shipment1..3 | Drain | MaterialFlow | 成品出货出口 |
| Factory51 | TruckDepartures | Drain | MaterialFlow | 卡车离场出口 |
| Factory51 | UnloadTruck | Method | InformationFlow | `param CurrentTruck:object`；叉车卸货逻辑 |
| Factory51 | userSetTarget | Method | InformationFlow | HBW3D 目标设定 |
| Factory51 | EventController | EventController | InformationFlow | 仿真事件控制 |
| Factory51 | CostAnalyzer | CostAnalyzer | UI | 成本分析 |
| Factory51 | PartSankey / WorkerSankey | SankeyDiagram | UI | 零件/工人桑基图 |
| Factory51 | HtmlReport | HtmlReport | UI | HTML 报告 |
| Factory51 | AGVPool | AGVPool | Resource | AGV 池（UnloadTruck 取 `AGVPool.Cont` 叉车） |
| Factory51 | M_Road / M_RoadTurn / M_StoreEntry / M_Truck | Marker | Resource | 叉车/AGV 路径标记点 |
| Factory51 | ChargeCount1/2, TrucksArrived, TrucksMissed, PalDeliveryInterval | Variable | InformationFlow | 统计与参数变量 |

### 2.3 生产线 P1/P2 关键对象（Production 类实例内）

| 所属Frame | 对象名称 | 对象类型(英文) | 所属大类 | 关键属性(名称=值) |
| --- | --- | --- | --- | --- |
| P1/P2 | PartEntrance / BoxEntrance | Interface | MaterialFlow | 零件/箱体进入接口 |
| P1/P2 | AGV_Entrance / AGV_Exit | Interface | MaterialFlow | AGV 进出接口 |
| P1/P2 | Line, Line1..31, Lift | Conveyor | MaterialFlow | 传送网，多处挂 `ExitCtrl`（如 `Line` 的 OnExit 按 Polishing 空满分流） |
| P1/P2 | Converter1..13, AngularConverter1..9 | Converter / AngularConverter | MaterialFlow | 分流/合流/转向 |
| P1/P2 | Milling1..3 | Station | MaterialFlow | 机加工站（Milling 类） |
| P1/P2 | Inspection1..3 | Station | MaterialFlow | 质检站 |
| P1/P2 | PickAndPlaceAGV / Aubergine / Strawberry | PickAndPlace | MaterialFlow | 按产品类型（Aubergine/Strawberry）拾取 |
| P1/P2 | QualityControlDrain | Drain | MaterialFlow | 质检不合格出口 |
| P1/P2 | Track | Track | MaterialFlow | 线内轨道 |
| P1/P2 | WorkerPool / ServiceTeam | WorkerPool | Resource | 工人池 |
| P1/P2 | Workplace1..8 / Workplace51/52 | Workplace | Resource | 工位 |
| P1/P2 | Broker | Broker | Resource | 工人调度经纪人 |
| P1/P2 | NumAGVs, PlatesInProduction, TPH | Variable | InformationFlow | 生产参数/统计变量 |
| P1/P2 | Init | Method | InformationFlow | 按 NumAGVs 创建 AGV 于 Track |

### 2.4 仓储 Warehouse 关键对象

| 所属Frame | 对象名称 | 对象类型(英文) | 所属大类 | 说明 |
| --- | --- | --- | --- | --- |
| Warehouse/RackLane1..5 | RSU, RackLeft, RackRight | Track/货架 | MaterialFlow | 巷道堆垛机与左右货架 |
| Warehouse/RackLane1..5 | IN / OUT / MainEntrance / SideEntrance | Interface | MaterialFlow | 巷道出入接口 |
| Warehouse/RackLane1..5 | Line, Converter1/2 | Conveyor/Converter | MaterialFlow | 巷道传送与分合流 |
| Warehouse/RackLane1..5 | InitRackLane / createRack / RSU 等 | Method | InformationFlow | 巷道初始化与 RSU 控制 |
| Warehouse/RackLane1..5 | NumberOfRows/Columns, OccupancyLeft/Right 等 | Variable | InformationFlow | 巷道参数变量 |
| Warehouse/WMS | WMS_Init / INIT / placeIntoStock / addProduct / removeProduct / reserveBox / getFreePlace / getStock 等 | Method | InformationFlow | 仓库管理核心逻辑 |
| Warehouse/WMS | RackLanes / PredefinedRacks / ProductRanges / Inventory / Content | Variable/DataTable | InformationFlow | WMS 数据表与参数 |

---

## 三、类结构与继承关系

### 3.1 类继承树（父类 → 子类）

> 标准库基础类（MaterialFlow/Resources/InformationFlow/UserInterface 目录中的 `.yaml`）是自定义类的 `Origin` 指向对象，即"父类"。

```
标准库基础类（Basic Objects，作为父类）
├── Frame（标准库）
│   ├── Production            (UserObjects/Production，自定义 Frame 类)
│   │    └── P1 / P2          (Models/Factory51/P1、P2，实例)
│   ├── Drying                (UserObjects/Drying，自定义 Frame 类)
│   │    └── Drying(派生)     (UserObjects/Production/Drying，Origin=Drying)
│   │         └── P1/Drying、Drying1、Drying2  (实例)
│   ├── Painting              (UserObjects/Painting，自定义 Frame 类)
│   │    ├── ClearPaint(派生) (UserObjects/Production/ClearPaint)
│   │    ├── Painting1(派生)  (UserObjects/Production/Painting1)
│   │    └── Painting2(派生)  (UserObjects/Production/Painting2)
│   │         └── P1/ClearPaint、Painting1、Painting2  (实例)
│   ├── PolishingCell         (UserObjects/PolishingCell，自定义 Frame 类)
│   │    ├── Polishing1/2/3(派生) (UserObjects/Production/Polishing1..3)
│   │    └── P1/Polishing1..3 (实例)
│   ├── PostProcess           (UserObjects/PostProcess，自定义 Frame 类)
│   │    ├── PostProcess1/2/3(派生) (UserObjects/Production/PostProcess1..3)
│   │    └── P1/PostProcess1..3 (实例)
│   ├── Warehouse             (UserObjects/Warehouse，自定义 Frame 类)
│   │    └── Warehouse        (Models/Factory51/Warehouse，实例)
│   └── RackLane              (ApplicationObjects/HBW3D/RackLane，HBW3D 库 Frame 类)
│        └── RackLane1..5     (UserObjects/Warehouse/RackLane1..5，派生)
│             └── Warehouse/RackLane1..5 (实例)
│        └── WMS              (ApplicationObjects/HBW3D/WMS，HBW3D 库 Frame 类)
│             └── WMS(派生)   (UserObjects/Warehouse/WMS)
│                  └── Warehouse/WMS (实例)
├── Conveyor（标准库）
│   └── Line                  (UserObjects/Line，自定义 Conveyor 类)
│        ├── Line1/Line2/Line3 (UserObjects/PostProcess/Line1..3，派生)
│        └── (众多 Line 实例，Origin 指向 Line)
├── Station（标准库）
│   ├── Milling               (UserObjects/Milling，自定义 Station 类)
│   ├── Polishing             (UserObjects/Polishing，自定义 Station 类)
│   └── PostProcessStation    (UserObjects/PostProcessStation，自定义 Station 类)
│        └── Step1/Step2/Step3 (UserObjects/PostProcess/Step1..3，派生)
├── Container（标准库）
│   ├── Box                   (UserObjects/MUs/Box，自定义 Container 类)
│   ├── Pallet / PalletSmall  (UserObjects/MUs，自定义 Container 类)
├── Part（标准库）
│   ├── Part                  (UserObjects/MUs/Part，自定义 Part 类)
│   └── DummyPart             (UserObjects/MUs/DummyPart，Origin=Part，派生)
├── Transporter（标准库）
│   ├── AGV / Forklift / Truck (UserObjects/MUs，自定义 Transporter 类)
├── Track（标准库）
│   ├── MultiPortalCrane      (ApplicationObjects/CranesAndMore/MultiPortalCrane，Track 类)
│   │    └── MultiPortalCrane / SmallCrane (实例)
├── Store（标准库）
│   └── StorageArea           (ApplicationObjects/CranesAndMore/StorageArea，Store 类)
└── 其他标准库基础类（Buffer/Interface/Converter/AngularConverter/PickAndPlace/Drain/Source/Workplace/WorkerPool/Worker/Variable/Method/Display/Comment 等）
     └── 对应实例对象的 Origin 直接指向这些标准库类文件
```

### 3.2 实例对象 → 对应类映射表

| 实例对象 | 所属Frame | 对应类(Class) | 类来源 |
| --- | --- | --- | --- |
| P1、P2 | Factory51 | Production | UserObjects/Production |
| P1/ClearPaint, Painting1/2 | P1 | ClearPaint/Painting1/Painting2 | UserObjects/Production（Origin=Painting） |
| P1/Drying, Drying1, Drying2 | P1 | Drying 派生 | UserObjects/Production（Origin=Drying） |
| P1/Polishing1..3 | P1 | Polishing1..3 | UserObjects/Production（Origin=PolishingCell） |
| P1/PostProcess1..3 | P1 | PostProcess1..3 | UserObjects/Production（Origin=PostProcess） |
| Warehouse | Factory51 | Warehouse | UserObjects/Warehouse |
| Warehouse/RackLane1..5 | Warehouse | RackLane1..5 | UserObjects/Warehouse（Origin=HBW3D RackLane） |
| Warehouse/WMS | Warehouse | WMS 派生 | UserObjects/Warehouse（Origin=HBW3D WMS） |
| Source / TruckArrivals | Factory51 | Source | MaterialFlow/Source（标准库） |
| StoreEntry / StoreExit | Factory51 | Buffer | MaterialFlow/Buffer（标准库） |
| StorageArea | Factory51 | StorageArea | CranesAndMore/StorageArea |
| MultiPortalCrane / SmallCrane | Factory51 | MultiPortalCrane | CranesAndMore/MultiPortalCrane |
| 各 Line/Converter/AngularConverter | 各处 | Line/Converter/AngularConverter | UserObjects/Line 或标准库 |
| Milling1..3 / Inspection1..3 | P1/P2 | Milling / Station | UserObjects/Milling 或 MaterialFlow/Station |

### 3.3 逐类说明（继承/引用/属性绑定）

- **Production（自定义 Frame 类）**：`InternalClassType: Frame`，无 Origin（直接从标准 Frame 派生）。内部 `Init` Method 根据 `NumAGVs` 变量在 `Track` 上创建 AGV。它是 P1、P2 的模板，P1/P2 通过 `Origin=3e014d4c…`（Production 的 UUID）继承其结构，实现"一条线定义、两条线实例化"的组件化建模。
- **Painting / PolishingCell / PostProcess / Drying（自定义 Frame 类）**：均为工序单元模板。子类（如 ClearPaint、Painting1、Polishing1、PostProcess1）通过 `Origin` 指向这些父类，再被 P1/P2 下的具体 Frame 实例化。PaintColor 变量类（`Origin=68fe277b`，即标准 Variable）用于喷漆颜色参数。
- **RackLane / WMS（HBW3D 库类）**：来自外部 ApplicationObjects 库 `HBW3D`。UserObjects/Warehouse/RackLane1..5 与 WMS 分别以 `Origin` 指向 `ApplicationObjects/HBW3D/RackLane`、`ApplicationObjects/HBW3D/WMS`，实现"巷道类 + 仓库管理类"的复用。
- **CranesAndMore 库类**：`MultiPortalCrane`（Track 类）、`StorageArea`（Store 类）等，由主 Frame 的 MultiPortalCrane/SmallCrane/StorageArea 实例引用（Origin 指向库内对象）。
- **MU 类族**：`Box`（Container）、`Pallet/PalletSmall`（Container）、`Part`（Part）、`DummyPart`（Part 派生）、`AGV/Forklift/Truck`（Transporter）。这些是物料单元（MU）的自定义类，被 Source/TruckArrivals 的 OnEntrance 通过 `.UserObjects.MUs.X.create(...)` 动态创建。
- **标准库基础类引用**：MaterialFlow/InformationFlow/Resources/UserInterface 目录下的 `.yaml` 文件（如 `Converter.yaml`、`Method.yaml`、`Workplace.yaml`、`Display.yaml`、`Variable.yaml`）是标准库对象的"父类模板"，实例通过 `Origin` 指向它们。

### 3.4 类库来源与命名约定

- **标准类库（Basic Objects）**：位于模型根目录 `MaterialFlow/`、`Resources/`、`InformationFlow/`、`MUs/`、`UserInterface/`，对应 Siemens 标准对象库。
- **自定义类库（UserObjects）**：位于 `UserObjects/`，含 `MUs`、`Production`、`Warehouse`、`Painting`、`PolishingCell`、`PostProcess`、`Drying` 等子文件夹；命名上以"工序/实体语义"命名（如 Milling、Polishing、PostProcessStation、AGV、Box）。
- **外部应用对象库（ApplicationObjects）**：
  - `CranesAndMore`：起重机/堆垛机库（MultiPortalCrane、GantryLoader、JibCrane、CrossSlidingCar、SevenAxisRobot、Lift、VehicleLift、StorageArea 等）。
  - `HBW3D`：高架立体仓库（High-Bay Warehouse）3D 库（RackLane、WMS、RSU 及相关 Method/Variable）。
- **路径约定**：代码中通过 `.UserObjects.MUs.Box`、`.UserObjects.MUs.AGV` 等访问自定义类；根 Frame 内对象用 `.Models.Factory51.xxx` 引用。

---

## 四、物料流拓扑（物流路径）

> 基于各对象 `$Successors` / `$Predecessors`、`EntranceCtrl` / `ExitCtrl` 与 Method 源码归纳。

### 4.1 进货与入库（卡车 → 立体仓库）

```
TruckArrivals(Source)
  └─ OnEntrance：若 SupplyRoad.NumMU>1 则 TrucksMissed+1 并删除卡车（限流）
  └─ 否则创建 Truck，内装 Pallet→Box→Part
        │
        ▼
SupplyRoad(TwoLaneTrack) ──► 卡车到达
        │
        ▼
UnloadTruck(Method)：AGVPool.Cont 叉车按 [M_RoadTurn→M_Road→M_Truck] 路线卸货
        │
        ▼
StoreEntry(Buffer)
  └─ ExitCtrl = StorageArea.storing（触发入库）
        │
        ▼
StorageArea(Store) ◄── MultiPortalCrane / SmallCrane（堆垛机在轨道上存取）
        │
        ▼
StoreExit(Buffer) ──► PaletteLine / 生产线配送
```

### 4.2 生产线内部（P1/P2，以 P1 为例）

```
PartEntrance / BoxEntrance (Interface)  ← 来自仓库/主线
        │
        ▼
Line(Conveyor) → Converter → AngularConverter → Line1..31（传送网）
        │
        ├── Milling1..3（机加工 Station）
        ├── Polishing1..3（抛光，内部 Buffer/Polishing/Workplace）
        ├── ClearPaint / Painting1 / Painting2（喷漆工序）
        ├── Drying / Drying1 / Drying2（烘干）
        ├── PostProcess1..3（后处理，Step1..3）
        └── Inspection1..3（质检 Station）
        │
        ├── PickAndPlaceAubergine / PickAndPlaceStrawberry（按产品分流）
        ├── QualityControlDrain（不合格品出口）
        └── AGV_Exit（成品出线，AGV 接驳）
```

- **分流（FlowControl 逻辑）**：`Production/Line`（Conveyor）的 `ExitCtrl= self.OnExit` 中：
  ```
  PlatesInProduction += 1
  if Polishing1.Polishing.Empty
      @.move(2)   // 走抛光
  else
      @.move(1)   // 走其他分支
  end
  ```
  通过 `@.move(n)` 按目标站点空满状态动态选择后继，实现拉式（Pull）分流。
- **产品类型**：Source 的 OnEntrance 按 `statNumOut < Number/2` 生成两类零件——`Aubergine`（紫，`makeRGBValue(107,0,128)`）与 `Strawberry`（粉，`makeRGBValue(255,0,128)`），并在后续由对应 PickAndPlace 分流。

### 4.3 成品入库与出货

```
生产线 AGV_Exit ──► AGV（沿 Track）──► Warehouse/WMS
        │
        ▼
WMS（placeIntoStock / reserveBox / getFreePlace）
        │
        ▼
RackLane1..5（IN/MainEntrance → Line/Converter → RackLeft/RackRight 货架）
        │
        ▼
WMS（removeProduct / autoRemove）──► 出货
        │
        ▼
Shipment1..3 (Drain) / TruckDepartures (Drain)
```

- **循环/回流**：AGV 沿 `Track` 循环运行；叉车/AGV 通过 `setRoute` 在多标记点间往返（UnloadTruck 中多次 `setRoute` 往返实现卸货循环）。
- **并行**：P1、P2 两条生产线完全并行；生产线内部 Polishing1..3、PostProcess1..3 为同构并行工序。

---

## 五、控制与数据流关系

### 5.1 控制挂载（Entrance/Exit/Trigger/Init 等）

| 对象 | 控制类型 | 挂载方法 | 说明 |
| --- | --- | --- | --- |
| Source | EntranceCtrl | `self.OnEntrance` | 生成 1 托盘→4 箱→4 零件/箱，设置颜色与材质 |
| TruckArrivals | EntranceCtrl | `self.OnEntrance` | 限流 + 生成卡车载荷（Pallet→Box→Part） |
| TruckArrivals | InitCtrl | `self.~.Path.create(self.~)` | 初始化时创建卡车 |
| StoreEntry | ExitCtrl | `StorageArea.storing` | 出站时触发入库 |
| StoreExit | ExitCtrl | `self.OnExit` | 出站时触发配送逻辑 |
| PaletteLine | ExitCtrl | `self.OnExit` | 出站分流 |
| Track/Track1 | ExitCtrl | `self.OnExit` | 出站控制 |
| Production/Line | ExitCtrl | `self.OnExit` | `PlatesInProduction+=1` + 按 Polishing 空满分流 |

### 5.2 Method 被调用关系（调用方 → 被调 Method）

| 调用方 | 被调 Method | 调用时机 |
| --- | --- | --- |
| Source（EntranceCtrl） | `self.OnEntrance`（内置属性方法） | 每次生成 MU 时 |
| TruckArrivals（EntranceCtrl） | `self.OnEntrance` | 每次生成卡车时 |
| TruckArrivals（InitCtrl） | `self.~.Path.create` | 初始化 |
| StoreEntry（ExitCtrl） | `StorageArea.storing` | MU 离开 StoreEntry 时 |
| StoreExit（ExitCtrl） | `self.OnExit` | MU 离开 StoreExit 时 |
| Production/Init | （内联）创建 AGV | Frame 初始化 |
| UnloadTruck（Method） | 调用 `AGVPool.Cont`、`forklift.setRoute/moveFork/move` | 卡车到达时触发 |
| WMS/RackLane 内部 | WMS_Init、InitRackLane、placeIntoStock、reserveBox、getFreePlace、removeProduct、autoRemove 等 | 出入库事件 |

### 5.3 数据表/变量与对象的读写关系

| 变量/数据表 | 读写方 | 关系 |
| --- | --- | --- |
| TrucksArrived / TrucksMissed | UnloadTruck / TruckArrivals.OnEntrance | 统计卡车到达/错过数量 |
| PlatesInProduction | Production/Line.OnExit | 生产中板件计数（`+=1`） |
| NumAGVs | Production/Init | 决定创建 AGV 数量 |
| ChargeCount1/2 | ChargeTrack1/2 | 充电计数 |
| PalDeliveryInterval | 主 Frame | 托盘配送间隔参数 |
| TPH | 生产线 | 每小时产出统计 |
| WMS/RackLane 系列变量（NumberOfRows/Columns、OccupancyLeft/Right、RackLanes、Inventory、ProductRanges、PredefinedRacks） | WMS/RackLane 各 Method | 仓库库存、巷道占用、产品范围等数据读写 |
| StorageArea.Content / Layout | StorageArea（Store） | 存储区内容与布局数据表 |

---

## 附注：文件证据来源说明

- Frame 层级与对象清单：来自 `Models/Factory51/**/$.yaml`、各对象 `.yaml` 的 `InternalClassType`、`Name`、`Origin`、`UUID` 字段。
- 类结构与继承：来自 `UserObjects/**`、`ApplicationObjects/**` 中 `$.yaml` 与类定义 `.yaml` 的 `Origin`/`InternalClassType`/`Name` 对照。
- 物料流拓扑：来自各对象 `$Successors`/`$Predecessors`、`EntranceCtrl`/`ExitCtrl` 字段与 `$.jt`/Method 的 `Program` 源码。
- 控制与数据流：来自 `UnloadTruck.yaml`、`TruckArrivals.yaml`、`Source.yaml`、`Production/Init.yaml`、`Production/Converter.yaml`、`Production/Line.yaml` 等文件的 `Program` 与 `$CustomAttributes`。

> 对象类型均对照 Siemens Plant Simulation 标准对象库命名；未能在文件中直接确认的连接关系已用"推测/示意"措辞说明，未编造。
