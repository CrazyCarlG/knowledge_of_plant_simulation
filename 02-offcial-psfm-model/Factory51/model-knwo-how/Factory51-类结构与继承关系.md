# Factory51 类结构与继承关系

> 模型来源：`02-offcial-psfm-model/Factory51/Factory51.psfm`（Folder Model，PSFM 文本格式）
> 分析依据：`UserObjects/**`、`ApplicationObjects/**`、`MaterialFlow|Resources|InformationFlow|MUs|UserInterface/**` 中各 `.yaml` 的 `InternalClassType`、`Name`、`Origin`、`UUID` 字段，以及 `Models/Factory51/**` 中实例对象的 `Origin` 字段。

**判定规则（PSFM 格式）：**
- `Origin` 字段指向的 UUID 即该对象的"父类 / 派生来源"（Derived from）。`Origin` 为空表示该对象直接基于内置（Built-in）标准对象。
- 位于 `UserObjects/`、`ApplicationObjects/` 及标准库目录（`MaterialFlow/` 等）下的对象是**类定义（isClass）**；位于 `Models/` 下的对象是**实例（isInstance）**。
- `InternalClassType` 表示对象最终的内置对象类型。

---

## 一、类继承树（父类 → 子类）

> 三层层级：**内置对象（Built-in）→ 标准库基础类/自定义根类 → 派生类 → 实例**。

### 1.1 Frame 类继承树

```
Frame（内置 Built-in）
├── Production           (UserObjects/Production，自定义 Frame 类，isClass)
│    └── P1 / P2         (Models/Factory51，实例 isInstance)
├── Drying               (UserObjects/Drying，自定义 Frame 类)
│    ├── Drying1         (UserObjects/Production/Drying1，派生类)
│    ├── Drying2         (UserObjects/Production/Drying2，派生类)
│    └── (P1/Drying、Drying1、Drying2 为实例)
├── Painting             (UserObjects/Painting，自定义 Frame 类)
│    ├── ClearPaint      (UserObjects/Production/ClearPaint，派生类)
│    ├── Painting1       (UserObjects/Production/Painting1，派生类)
│    ├── Painting2       (UserObjects/Production/Painting2，派生类)
│    └── (P1/ClearPaint、Painting1、Painting2 为实例)
├── PolishingCell        (UserObjects/PolishingCell，自定义 Frame 类)
│    ├── Polishing1      (UserObjects/Production/Polishing1，派生类)
│    ├── Polishing2      (UserObjects/Production/Polishing2，派生类)
│    ├── Polishing3      (UserObjects/Production/Polishing3，派生类)
│    └── (P1/Polishing1..3 为实例)
├── PostProcess          (UserObjects/PostProcess，自定义 Frame 类)
│    ├── PostProcess1    (UserObjects/Production/PostProcess1，派生类)
│    ├── PostProcess2    (UserObjects/Production/PostProcess2，派生类)
│    ├── PostProcess3    (UserObjects/Production/PostProcess3，派生类)
│    └── (P1/PostProcess1..3 为实例)
├── Warehouse            (UserObjects/Warehouse，自定义 Frame 类)
│    └── Warehouse       (Models/Factory51/Warehouse，实例)
└── (外部库 HBW3D)
     ├── RackLane        (ApplicationObjects/HBW3D/RackLane，HBW3D 库 Frame 类)
     │    ├── RackLane1..5  (UserObjects/Warehouse/RackLane1..5，派生类)
     │    └── (Warehouse/RackLane1..5 为实例)
     └── WMS             (ApplicationObjects/HBW3D/WMS，HBW3D 库 Frame 类)
          └── WMS        (UserObjects/Warehouse/WMS，派生类)
               └── (Warehouse/WMS 为实例)
```

### 1.2 物料流 / 资源 / 信息流类继承树

```
Conveyor（内置）
├── Line                 (UserObjects/Line，自定义 Conveyor 类)
│    ├── Line1/Line2/Line3    (UserObjects/PostProcess/Line1..3，派生类)
│    └── Line1..Line231 等    (UserObjects/Production/*，派生类，Origin=Line)
└── CrossSlidingCar     (ApplicationObjects/CranesAndMore，库类)

Station（内置）
├── Milling              (UserObjects/Milling，自定义 Station 类)
│    └── Milling1..3     (UserObjects/Production/*，派生类)
├── Polishing            (UserObjects/Polishing，自定义 Station 类)
├── PostProcessStation   (UserObjects/PostProcessStation，自定义 Station 类)
│    └── Step1/Step2/Step3   (UserObjects/PostProcess/*，派生类)
├── Inspection1..3       (UserObjects/Production/*，派生类，Origin=标准 Station b6fe5447)
└── JibCrane / SevenAxisRobot / RSU  (CranesAndMore / HBW3D 库类)

Track（内置）
├── MultiPortalCrane     (ApplicationObjects/CranesAndMore/MultiPortalCrane，库类)
├── GantryLoader / VehicleLift  (CranesAndMore 库类)
└── (Track 实例直接引用标准 Track)

Store（内置）
└── StorageArea          (ApplicationObjects/CranesAndMore/StorageArea，库类)

Interface（内置）
└── AGV_Entrance / AGV_Exit / BoxEntrance / PartEntrance / Entry / Exit
                         (UserObjects 派生类，Origin=标准 Interface 2d7f401e)

Converter（内置）
└── Converter1..13       (UserObjects/Production/*，派生类，Origin=标准 Converter ae1814ce)

AngularConverter（内置）
└── AngularConverter1..9 (UserObjects/Production/*，派生类，Origin=标准 AngularConverter a0ac50ef)

PickAndPlace（内置）
└── PickAndPlaceAGV / PickAndPlaceAubergine / PickAndPlaceStrawberry
                         (UserObjects/Production/*，派生类，Origin=标准 PickAndPlace 39a9d6fe)

Drain（内置）
├── Shipment             (UserObjects/Shipment，自定义 Drain 类)
└── QualityControlDrain  (UserObjects/Production/*，派生类，Origin=标准 Drain e19f8c68)

Workplace（内置）
└── Workplace1..8 / Workplace51 / Workplace52 / (PostProcess)Workplace1..2
                         (UserObjects 派生类，Origin=标准 Workplace b1e894bf)

WorkerPool（内置）
└── ServiceTeam          (UserObjects/Production/ServiceTeam，派生类，Origin=标准 WorkerPool 961fe9c5)

Worker（内置）
└── Service              (UserObjects/Service，派生类，Origin=标准 Worker 9c2a965a)

Variable（内置）
├── PaintColor           (UserObjects/Painting/PaintColor，派生类)
├── NumAGVs / PlatesInProduction / TPH  (UserObjects/Production/*，派生类)
└── (Origin=标准 Variable 68fe277b)

Method（内置）
└── Init / INIT 等       (UserObjects 派生类，Origin=标准 Method 9f30bc1b 或 HBW3D Init 89275b5f)

Display（内置）
├── DisplayBuffer        (UserObjects/PolishingCell/DisplayBuffer，派生类)
└── Display1..5          (UserObjects/Production/*，派生类，Origin=标准 Display 3d49b650)

Comment（内置）
└── Comment1 / Comment11 (UserObjects/Production/*，派生类，Origin=标准 Comment e985ae5c)
```

### 1.3 MU 类（物料单元）继承树

```
Container（内置）
├── Box                  (UserObjects/MUs/Box，自定义 Container 类)
├── Pallet               (UserObjects/MUs/Pallet，自定义 Container 类)
└── PalletSmall          (UserObjects/MUs/PalletSmall，自定义 Container 类)

Part（内置）
├── Part                 (UserObjects/MUs/Part，自定义 Part 类)
└── DummyPart            (UserObjects/MUs/DummyPart，派生类，Origin=Part fe01ce2d)

Transporter（内置）
├── AGV                  (UserObjects/MUs/AGV，自定义 Transporter 类)
├── Forklift             (UserObjects/MUs/Forklift，自定义 Transporter 类)
└── Truck                (UserObjects/MUs/Truck，自定义 Transporter 类)
```

---

## 二、类与实例（对象）的实例化关系

> 区分两类实例：**自定义类实例**（`Origin` 指向 UserObjects/ApplicationObjects 自定义类）与**标准库对象实例**（`Origin` 指向标准库目录中的基础类文件）。

### 2.1 自定义类 → 实例映射

| 实例对象名 | 所属Frame | 对应类(Class) | 是否继承自父类 | 实例化位置 |
| --- | --- | --- | --- | --- |
| P1 | Factory51 | Production | 否（Production 为根类） | Models/Factory51/P1 |
| P2 | Factory51 | Production | 否 | Models/Factory51/P2 |
| P1/ClearPaint | P1 | ClearPaint | 是（Derived from Painting） | Models/Factory51/P1/ClearPaint |
| P1/Painting1、Painting2 | P1 | Painting1、Painting2 | 是（Derived from Painting） | Models/Factory51/P1/... |
| P1/Drying、Drying1、Drying2 | P1 | Drying 派生类 | 是（Derived from Drying） | Models/Factory51/P1/... |
| P1/Polishing1..3 | P1 | Polishing1..3 | 是（Derived from PolishingCell） | Models/Factory51/P1/... |
| P1/PostProcess1..3 | P1 | PostProcess1..3 | 是（Derived from PostProcess） | Models/Factory51/P1/... |
| P2/* | P2 | 同上（与 P1 同构） | 同上 | Models/Factory51/P2/* |
| Warehouse | Factory51 | Warehouse | 否（Warehouse 为根类） | Models/Factory51/Warehouse |
| Warehouse/RackLane1..5 | Warehouse | RackLane1..5 | 是（Derived from HBW3D RackLane） | Models/Factory51/Warehouse/... |
| Warehouse/WMS | Warehouse | WMS | 是（Derived from HBW3D WMS） | Models/Factory51/Warehouse/WMS |

### 2.2 标准库对象实例（直接引用标准基础类，`Origin` 指向标准库目录）

| 实例对象名 | 所属Frame | 对应基础类文件 | 内置类型 |
| --- | --- | --- | --- |
| Source | Factory51 | MaterialFlow/Source.yaml | Source |
| TruckArrivals | Factory51 | MaterialFlow/Source.yaml | Source |
| StoreEntry、StoreExit | Factory51 | MaterialFlow/Buffer.yaml | Buffer |
| StorageArea | Factory51 | ApplicationObjects/CranesAndMore/StorageArea.yaml | Store |
| EmptyPalletsStore | Factory51 | MaterialFlow/Store.yaml | Store |
| MultiPortalCrane、SmallCrane | Factory51 | ApplicationObjects/CranesAndMore/MultiPortalCrane.yaml | Track |
| Track、Track1..3、ChargeTrack1/2 | Factory51 | MaterialFlow/Track.yaml | Track |
| UpperStoreExit | Factory51 | MaterialFlow/Station.yaml | Station |
| Converter、Converter1..3 等 | Factory51 | MaterialFlow/Converter.yaml | Converter |
| PickAndPlace(1..5/Top/Bottom) | Factory51 | MaterialFlow/PickAndPlace.yaml | PickAndPlace |
| Line 系列 | Factory51 | UserObjects/Line.yaml（或标准 Conveyor） | Conveyor |
| Shipment1..3 | Factory51 | UserObjects/Shipment.yaml（Drain 类） | Drain |
| AGVPool | Factory51 | Resources/AGVPool.yaml | AGVPool |
| 各 Marker、Button、Display 等 | Factory51 | Resources/UserInterface 标准库 | 对应类型 |

### 2.3 类内对象（Containment：作为类模板内容的子对象）

> `UserObjects/Production/*.yaml`、`UserObjects/PostProcess/*.yaml` 等文件，是相应 Frame 类**内部包含**的子对象定义。当 P1/P2 实例化 Production 类时，这些子对象被复制到实例中。

| 父类 | 类内包含的子对象（Containment） |
| --- | --- |
| Production | AGV_Entrance/AGV_Exit/BoxEntrance/PartEntrance(Interface)、Line1..Line231(Conveyor)、Converter1..13、AngularConverter1..9、Milling1..3、Inspection1..3、PickAndPlaceAGV/Aubergine/Strawberry、QualityControlDrain、ServiceTeam(WorkerPool)、Workplace1..8/51/52、子Frame ClearPaint/Painting1/Painting2/Polishing1..3/PostProcess1..3/Drying1/Drying2、Init(Method)、NumAGVs/PlatesInProduction/TPH(Variable) 等 |
| PostProcess | Line1..3(Conveyor)、Step1..3(Station)、Workplace1..2、Display |
| PolishingCell | Polishing(Station)、Buffer、DisplayBuffer、Display、Workplace |
| Painting | Line(Conveyor)、Station、Workplace、LockoutZone、PaintColor(Variable)、Comment |
| Drying | Line(Conveyor) |
| Warehouse | Entry/Exit(Interface)、RackLane1..5、WMS |
| RackLane1..5（HBW3D 派生） | IN/OUT/MainEntrance/SideEntrance(Interface)、Line、Converter1/2、RackLeft/RackRight、RSU、INIT 及大量参数 Variable |
| WMS（HBW3D 派生） | WMS_Init/INIT/placeIntoStock/addProduct/removeProduct/reserveBox 等 Method、RackLanes/Inventory/ProductRanges/PredefinedRacks 等 DataTable/Variable |

---

## 三、类关系（继承 / 引用 / 委托 / 属性绑定）

### 3.1 继承（Inheritance）

- **Production → P1/P2**：P1、P2 以 `Origin=3e014d4c`（Production 的 UUID）继承 Production 类的全部结构与行为，实现"一条生产线定义、两条生产线实例化"。P2 与 P1 完全同构。
- **Painting → ClearPaint/Painting1/Painting2**：三个喷漆工序 Frame 均继承 Painting 类（`Origin=6714df70`），复用喷漆工位/传送带/锁定区结构。
- **PolishingCell → Polishing1..3**：三个抛光单元继承 PolishingCell 类（`Origin=58e37094`）。
- **PostProcess → PostProcess1..3**：三个后处理单元继承 PostProcess 类（`Origin=ab80fac3`）。
- **Drying → Drying1/Drying2**：烘干工序继承 Drying 类（`Origin=a28a86cf`）。
- **HBW3D RackLane → RackLane1..5**：五个巷道类继承外部库 HBW3D 的 RackLane 类（`Origin=d2ab5f41`）。
- **HBW3D WMS → WMS**：仓库管理系统继承外部库 HBW3D 的 WMS 类（`Origin=f2c13264`）。
- **Part → DummyPart**：DummyPart 继承自定义 Part 类（`Origin=fe01ce2d`），复用零件的三维图形组与属性。
- **Line → Line1/Line2/Line3 及 Production 内各 Line**：所有派生传送带继承自定义 Line 类（`Origin=b5918b15`），Line 类挂载了 `ExitCtrl=self.OnExit` 的分流逻辑，子类复用。
- **PostProcessStation → Step1..3**：后处理工序继承 PostProcessStation 类（`Origin=8534d217`）。

### 3.2 引用 / 挂载（Reference / Containment）

- **Production 类**内部挂载（包含）大量子对象（见 2.3 表），构成完整生产线：入口 Interface、传送网（Line/Converter/AngularConverter）、加工站（Milling/Inspection/子工序 Frame）、工人资源（Workplace/ServiceTeam/Broker）、分流机械手（PickAndPlace*）、质检出口（QualityControlDrain）。
- **Warehouse 类**内部挂载 `Entry`/`Exit` 接口、5 个 RackLane 巷道和 1 个 WMS。
- **RackLane 类**内部挂载货架（RackLeft/RackRight）、巷道堆垛机（RSU）、出入接口（IN/OUT/MainEntrance/SideEntrance）、传送带与转换器，以及大量参数 Variable 与控制 Method。
- **WMS 类**内部挂载库存管理 Method（placeIntoStock、reserveBox、getFreePlace、removeProduct 等）与数据表（Inventory、RackLanes、ProductRanges、PredefinedRacks）。

### 3.3 属性绑定 / 继承（Inherit from）

- 各派生类的 `Origin` 机制即属性继承来源。派生对象（如 Converter1..13、Workplace1..8、Display1..5、Inspection1..3）通过 `Origin` 指向标准基础类文件，继承其内置属性（如 `Length`、`Speed`、`$CustomAttributes`、`3D` 图形等），再在派生类中按需覆盖（override）坐标、参数等。
- 实例对象（如 `Models/Factory51/Source.yaml`）通过 `$CustomAttributes` 定义自定义属性方法（如 `OnEntrance`），并挂载 `EntranceCtrl="self.OnEntrance"`，实现属性→方法绑定。

### 3.4 委托 / 回调

- **Entrance/Exit Control 回调**：`Source.EntranceCtrl=self.OnEntrance`、`StoreEntry.ExitCtrl=StorageArea.storing`、`StoreExit.ExitCtrl=self.OnExit`、`PaletteLine.ExitCtrl=self.OnExit`、`Production/Line.ExitCtrl=self.OnExit` 等，均是将对象行为委托给自定义 Method（含跨对象调用，如 StoreEntry 委托给 StorageArea 的 `storing` 方法）。
- **跨 Frame 委托**：`TruckArrivals.Init` 委托 `self.~.Path.create(self.~)`；`UnloadTruck` 通过 `AGVPool.Cont` 获取叉车并调用 `forklift.setRoute/moveFork/move`。
- **HBW3D 委托**：`userSetTarget`（Method）由 HBW3D 库提供，供堆垛机目标设定；RackLane 的 `INIT` 方法继承自 HBW3D `RackLane/Init`。

---

## 四、类库来源与命名约定

### 4.1 使用的标准类库对象（Basic Objects）

| 大类 | 标准库目录 | 用到的内置对象类型 |
| --- | --- | --- |
| MaterialFlow | `MaterialFlow/` | Source, Station, Buffer, Store, Converter, Drain, Conveyor, Track, TwoLaneTrack, AngularConverter, PickAndPlace, Interface, Connector, EventController |
| Resource | `Resources/` | Worker, WorkerPool, Broker, FootPath, LockoutZone, Marker, Workplace, AGVPool |
| InformationFlow | `InformationFlow/` | Method, Variable, DataTable, DataList |
| Fluid | — | 未使用 |
| UserInterface | `UserInterface/` | Button, Chart, Checkbox, Comment, CostAnalyzer, Display, HtmlReport, Toolbar, SankeyDiagram |
| MU | `MUs/` | Container, Part, Transporter |

### 4.2 外部应用对象库（ApplicationObjects）

| 库名称 | 用途 | 关键类 |
| --- | --- | --- |
| `CranesAndMore` | 起重机/堆垛机/升降机/机器人库 | MultiPortalCrane(Track)、StorageArea(Store)、GantryLoader(Track)、CrossSlidingCar(Conveyor)、JibCrane(Station)、SevenAxisRobot(Station)、Lift(Conveyor)、VehicleLift(Track) |
| `HBW3D` | 高架立体仓库（High-Bay Warehouse）3D 库 | RackLane(Frame)、WMS(Frame)、RSU(Station)、userSetTarget(Method) 及配套 Method/Variable |

### 4.3 自定义类命名约定

- **路径前缀**：自定义类统一放在 `UserObjects/` 下；代码中通过 `.UserObjects.MUs.Box`、`.UserObjects.MUs.AGV` 等访问。
- **MU 类**：位于 `UserObjects/MUs/`，以实体语义命名（AGV、Box、Pallet、PalletSmall、Part、DummyPart、Forklift、Truck）。
- **工序单元 Frame 类**：以工序语义命名（Production、Drying、Painting、PolishingCell、PostProcess、Warehouse），派生类加数字后缀区分同构实例（Painting1/2、Polishing1..3、PostProcess1..3、Drying1/2、RackLane1..5）。
- **根 Frame 对象**：`Models/Factory51` 下实例对象直接以对象语义命名（Source、StoreEntry、MultiPortalCrane、PaletteLine、Shipment1 等）。
- **标准库路径**：模型根目录的 `MaterialFlow/`、`Resources/`、`InformationFlow/`、`MUs/`、`UserInterface/` 保存标准对象的基础类（作为派生来源）。

---

## 附注：无法从文件判定的关系

- 标准库目录（`MaterialFlow/` 等）中的 `.yaml` 文件是标准对象的"基础类模板"，其与 Siemens 内置对象（Built-in）的绑定由 `InternalClassType` 字段隐含表达；文件未显式给出内置对象的继承细节，故内置层在继承树中以"内置（Built-in）"概括。
- 派生类是否 override 了父类具体哪些属性，仅在部分文件（如 Line 的 `ExitCtrl`、Source 的 `$CustomAttributes`）中可见，其余派生类（如各 Converter、Workplace）仅体现 `Origin` 与坐标/参数差异，未逐一判定 override 项。
- P2 与 P1 同构的结论来自目录文件清单一致，具体实例差异（坐标等）未逐项比对。
