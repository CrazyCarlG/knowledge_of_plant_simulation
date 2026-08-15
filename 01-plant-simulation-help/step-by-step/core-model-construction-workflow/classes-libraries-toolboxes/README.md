# Classes, Libraries & Toolboxes — 目录说明

本目录汇总了 Plant Simulation Help 中关于**类（Classes）、库（Libraries）与工具箱（Toolbox）**的内容，主题涵盖仿真模型的创建、类/子类/实例、继承、类库的配置与使用、用户自定义类、对象与库的保存/加载，以及工具箱的操作。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `classes-libraries-toolboxes.md` | 本主题的整理版总结（17 个章节） |
| `classes-libraries-toolboxes.txtx` | 原始帮助文档文本（源材料） |

> 注：本目录下没有子文件夹，因此不存在子文件夹中的 README.md。

---

## 内容总结

### 1. 创建仿真模型（Creating a Simulation Model）
通过从**类库（Class Library）**将内置对象和用户自定义（应用）对象拖入 **Models 文件夹下的 Frame `Model`** 来搭建模型。最常用的内置对象包括：

- **Frame** — 在其中创建模型的容器对象。
- **EventController** — 启动、停止、重置仿真运行。
- **主动物料流对象** — 运输并/或主动加工移动对象（MU）。
- **被动物料流对象** — 存储零件并作为零件移动的轨道。
- **移动对象（MU）** — 表示被创建、存储、运输、加工、移除的零件。
- **流体对象** — 模拟自由流动的物料（液态/气态/可倾倒），适用于食品饮料、制药行业。
- **资源对象** — 建模 Worker 如何从 WorkerPool 移动到工作站。
- **Method 对象** — 用 **SimTalk** 编程实现动作，并提供 **Method Debugger**。
- **列表与表格** — 实现对象间信息的任意交换。
- **Chart 与 Report** — 图形化显示仿真运行中收集的统计值。
- **Dialog** — 创建自定义对话框作为简单用户界面。
- **BottleneckAnalyzer / SankeyDiagram** — 分析评估仿真结果；**ExperimentManager** 定义实验执行方式。

关键建模概念：**嵌套层级**（Frame 套 Frame）、**继承**（派生/复制，子对象保留与父对象模板的可控链接，可逐项关闭继承）、**接口**（仿真运行期间与其他程序交换数据）。

两种建模策略：**自顶向下（Top-down）** 与 **自底向上（Bottom-up）**。

> **建议**：不要修改内置对象的默认设置（合并模型或更新类库时会被丢弃）。如需自定义，应在类库中**派生**对象，派生对象默认放入 `UserObjects` 文件夹。

### 2. 创建带英文标识的德文模型（Creating a German Model with English Identifiers）
SimTalk 解释器可同时处理德文与英文命令名。在打开模型前，通过 **Datei/File > Voreinstellungen/Preferences** 选择 **English** 作为模型语言，即可让文件夹与对象名显示为英文，而菜单与对话框仍为德文。可选启用下拉列表按模型语言显示，便于查看属性/方法返回值（如 `Einzelstation.Bearbeitungszeit.Typ` 返回 `Konst`，英文模型返回 `Const`）。

### 3. 类的引入（Introducing Classes）
通过一个"为生产车间寻找最优仓库类型"的示例，对比传统系统（复制基本模型，逐份修改）与 Plant Simulation（**继承**基本模型得到子模型，父模型改动自动传播到子模型）。

### 4. 类、子类与实例（Classes, Subclasses, and Instances）
- **Class（类）** — 插入 Frame 的实例的模板。类把所有属性传给实例；只把继承仍激活的属性传给子类。
- **Subclass（子类）** — 继承父类**部分**属性的类库对象，通过关闭特定对话框项的继承来定义子类专属属性。
- **Instance（实例）** — 从类库/工具箱把类对象拖入 Frame 得到的对象。

快捷操作：**Derive（派生）** = 右键 `Derive` 或 **Ctrl+Shift** 拖拽；**Duplicate（复制）** = 右键 `Duplicate` 或 **Ctrl** 拖拽。

继承关系：对象从**类对象（class object）**继承基本属性，从**源对象（origin object）**继承未被本地修改的设置。

> 继承只能从类到子类/实例单向进行，反之不行。

### 5. 用拖放替换与合并对象（Replacing and Merging Objects with Drag-and-Drop）
- **用类替换实例**：按住 **Alt** 把类对象拖到实例上（如把 `Station` 换成 `AssemblyStation`）。保留已连接的 Connector，但删除对象上的所有 MU；可选择性复制原实例的属性值；保留原名称。
- **合并类**：按住 **Alt + 左键**，把替换对象拖到被替换的类上。

### 6. 使用继承（Using Inheritance）
继承让类/对象可融入另一类/对象的数据或行为，用于**特化（Specialization）**、**扩展（Extension）**、**代码复用（Code re-use）**。每个对话框项右侧的复选框控制继承开关：开启时使用源对象的值，关闭时仅对当前对象生效（橙色按钮中的减号辅助视障用户识别）。

### 7. 在类库中显示继承关系（Show Inheritance Relations in the Class Library）
右键类库对象 → **Show Inheritance**，打开 **Inheritance** 对话框，显示所有派生自该对象的路径。

### 8. 在类库中显示对象的源（Show the Origin of an Object in the Class Library）
右键类库对象 → **Show Origin**，选中它被实例化/派生自的对象；可重复操作向上追溯直至最初的源。

### 9. 在类库中处理类（Working with Classes in the Class Library）
类库以分层文件夹结构显示内置对象，默认包含 **MaterialFlow、Fluid、Resource、InformationFlow、MUs、UserInterface、UserObjects、Models、Tools** 等文件夹。加附加组件（add-in）会出现在 **Basis**（表示类库自身）之下。

### 10. 配置类库（Configure the Class Library）
可为新模型与现有模型配置类库，获得精简的类库与整洁的工具箱：
- 增删基础对象；**Clean up class library** 删除未使用的类；增删库与工具；添加自定义库；更新库。

含四个子流程：**增删基础对象**、**增删库/工具**、**添加自研库**（在 `File > Preferences > Libraries Directories` 设置路径）、**更新库**（库管理器发现新版本时提示，用 **Merge Report** 查看增删对象，或用 **Update All Libraries** 批量更新）。

### 11. 为仿真模型创建文件夹结构（Create a Folder Structure for Your Simulation Model）
建模前规划类库结构。安装库默认位于 `C:\Program Files\Siemens\Tecnomatix Plant Simulation XX\Libraries`。建议新建文件夹存放对象（而非内置文件夹），推荐使用 `UserObjects`，并创建 `BasicObjects` 子文件夹使库独立于模型语言与命名约定。

### 12. 为仿真模型设置根文件夹（Set the Root Folder for Your Simulation Model）
用匿名标识符 `RootFolder` 避免长路径。将某文件夹的属性 `RootFolder` 设为 `true`（`.ApplicationObjects.Transport.RootFolder := true` 或右键设置），即可用 `RootFolder.MyComponent.openComponent` 直接调用共享 Method。

### 13. 创建用户自定义类（Creating User-defined Classes）
- **共享全部特性的类**：右键 `Derive`（或 **Ctrl+Shift** 拖拽）后重命名；也可把 Frame 中多个对象拖到类库文件夹。
- **共享部分特性的子类**：先关闭要修改特性的继承，再 `Derive`。
- **无继承关系的类**：右键 `Duplicate`（或 **Ctrl** 拖拽），切断所有继承关系。

派生/复制对象放入 `UserObjects`，可像内置类一样编辑、插入，并拖到工具栏 **UserObjects**。

### 14. 在类库中处理文件夹、Frame 与对象（Work with Folders, Frames, Objects in the Class Library）
- 移动文件夹：点击拖到目标位置上方；移动到另一文件夹用 **Shift** 拖拽；复制到另一文件夹用 **Ctrl** 拖拽。
- 合并文件夹/对象：**Alt** 拖拽替换对象到被替换对象上。
- 排序、向工具栏添加图标、重命名（双击 / F2 / 右键 Rename / 打开对象按 F4）。

### 15. 在类库中显示 Frame 内容（Show the Contents of a Frame in the Class Library）
类库只显示对象的**类**而非**实例**。要查看 Frame 内部的层级结构，右键 Frame → **Show Structure**。

### 16. 保存文件夹/对象并加载到另一模型（Saving a Folder or an Object and Loading it into Another Model）
**库（`.pslib`）** 是带版本号、可维护与共享的对象集合。子主题：
- **将文件夹保存为库**：右键 `Make Library` → 填写 Name/Version/Description；用 `Save Library As` 存为文件；可编辑库信息与设置**替代路径**（`$German$` 等语言前缀）。
- **将对象/文件夹保存为对象（`.psobj`）**：`Save Object As` / `Save Folder As`。
- **将对象/文件夹加载到模型**：右键任意文件夹 → `Load Object`；名称冲突时用 **Replace or Rename Class** 对话框处理（替换/全部替换/重命名保留）。
- **加载到另一文件夹**：`Load Object into Folder`。
- **更新类库**：保存为 `.psobj` 后右键 → `Save/Load > Update Class Library`。

### 17. 在工具箱中处理对象（Working with Objects in the Toolbox）
**工具箱（Toolbox）** 是容纳类库对象工具栏的容器，默认显示 **Material Flow、Fluids、Resources、Information Flow、User Interface、Mobile Units、Tools** 等工具栏。可添加自定义工具栏（右键文件夹 → `New > Toolbar`）、向工具栏增删对象、调整图标顺序、复制对象到另一工具栏、右键 → `Show Class` 打开对象类。

---

## 核心要点速览

1. **始终派生而非修改内置对象** —— 修改内置对象设置会在合并/更新类库时丢失。
2. **类 → 子类/实例的单向继承** —— 父类改动自动传播，子类本地修改会覆盖继承值。
3. **派生（Derive）/复制（Duplicate）的区别** —— 派生保留继承链接（Ctrl+Shift 拖拽），复制切断继承（Ctrl 拖拽）。
4. **拖放快捷键** —— Alt 拖拽 = 替换/合并。
5. **`RootFolder`** —— 匿名标识符，用于从类库直接调用共享 Method，避免长路径。
6. **库（`.pslib`）vs 对象文件（`.psobj`）** —— 库带版本号、可维护共享；对象文件用于保存/加载单个对象或文件夹。
