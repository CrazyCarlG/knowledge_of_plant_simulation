# Experiment Manager & Genetic Optimization — 目录说明

本目录收录 Plant Simulation 中两项相关能力的说明文档：

1. **使用 `ExperimentManager` 运行仿真实验（Running Simulation Experiments）** —— 验证模型、研究输入参数如何影响输出结果。
2. **使用 `GAWizard` 进行遗传算法优化（Optimizing Models with Genetic Algorithms）** —— 在解空间很大的情况下寻找合适的参数化方案。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `experiment-manager-genetic-optimization.md` | 格式化的 Markdown 文档，为本目录的主文档 |
| `experiment-manager-genetic-optimization.txtx` | 同一内容的纯文本原始导出（源自 Plant Simulation Help） |

> 注：本目录下没有子文件夹，因此没有子目录 README 需要汇总。

## 文档内容总结

### 一、运行仿真实验（ExperimentManager）

创建模型后需要先验证模型，随后通过仿真研究考察**输入值**（模型参数）对**输出值**（结果值）的影响。`ExperimentManager` 的两大用途：

1. **得到统计上可靠的结果**
   - 重建已有工厂时，将车间采集数据与仿真结果进行对比。
   - 为随机数流的各个随机分量分配不同种子值。
   - `ExperimentManager` 会为每组输入值更换种子，从而产生一组观测值（observations）。
   - 对每个输出值（固定输入值下）给出**置信区间**和**最小-最大区间**（二者合成为**箱线图**）。
   - 含随机分量的系统结论只能以某个**置信水平（显著性水平）**给出。

2. **优化结果**
   - 使用**遗传算法**确定能产生期望结果或优化结果的参数。

> 说明：`ExperimentManager` 对话框基于 `Dialog` 对象建模，因此使用 Windows 设计而非 Siemens PLM 标准设计。

### 二、许可证（Licenses）

`ExperimentManager` 的行为随许可证类型不同：

- **Runtime**：可执行实验、修改表格参数；不能更改 ExperimentManager 模型结构；不能控制分布式仿真。
- **Application**：还可更改模型结构。
- **Professional / Standard / Foundation**：还可在 Method 中定义实验。
- **Student**：不能控制分布式仿真。

远程许可证设置为 **Highest Available** 时，不同许可证类型的计算机可用作仿真机（控制计算机本身也可作为仿真机）。

> 说明：一个仿真研究包含若干实验，每个实验执行若干次仿真运行，每次运行产生一个观测值。

### 三、运行一个简单仿真研究（三个步骤）

- **Step 1 — 定义输入和输出值**：每个研究至少需要一个输出值；输出值可以是方法或对象属性，也可把 Plant Simulation 表格拖到 ExperimentManager 上作为输出值。输入值可以是对象属性、表格条目或概率分布参数（识别 `Uniform`、`Triangle`、`Normal`、`Lognorm`、`Erlang`、`Negexp`、`Geom`、`Hypgeo`、`Weibull`、`Binomial`、`Poisson`、`Beta`）。仿真运行必须结束：若使用 `EventController` 的 `stop` 方法，需在合适位置调用 `endSim`，或设置 `End time` / `End` 属性。
- **Step 2 — 运行实验**：先 **Reset** 再 **Start**，结束时自动打开报告，长运行可留待过夜执行。
- **Step 3 — 评估结果**：支持表格、图表和 HtmlReport 三种查看方式。
  - **表格**：`Open Results` 显示所有实验概览（F2 查看子表）；`Detailed Results` 显示均值、标准差、最小/最大值、置信区间左右边界；`Observations` 列给出所有仿真运行的结果。
  - **图表**：显示最小-最大区间或置信区间，可显示 25%/50%/75% 四分位数，即**箱线图**。
  - **HtmlReport**：`Report` 生成报告，可在 `Tools > Advanced Settings > Report` 配置，可保存报告 / 导出 Excel，可把 Chart 拖到 ExperimentManager 图标上加入报告。

### 四、细化设置（Refining the Settings）

- **静态参数（Static Parameters）**：为每个实验/参数设特定值；也可在 `Tools > Advanced Settings > Settings` 中用 SimTalk 方法（**Configuration Method**）修改设置，参数（`integer`）表示实验编号。
- **动态参数（Dynamic Parameters）**：在 `Tools > Advanced Settings > Rules` 中定义，由先前实验的结果产生当前实验的输入值。规则 = 条件（condition）+ 动作（action）。
  - 步骤：勾选 `use rules` → 选择内置规则或自建规则 → 勾选 `Rule is active` → 可指定适用实验编号 → 设置优先级（数值越大优先级越高）→ 勾选 `Use for first simulation run` 则从首个实验即生效，否则从第二个实验起生效。
  - **自建规则**：`Create New Rule` 命名 → `Table Condition` 填写括号层级、对象、属性、运算符（`<` `>` `=` `~=` `/=`）、比较值、布尔运算（`AND`/`OR`）；可另用 `Method Condition` 测试条件 → `Table Action` 填写对象、属性、操作符、操作值；可另用 `Method Action` 编程执行动作。

### 五、遗传算法优化（GAWizard）

当优化任务解空间很大时使用遗传算法。`GAWizard` 将遗传算法集成进仿真模型，可用于基于仿真运行或基于 Method 计算的优化。

**核心概念**
- 遗传算法是**随机**优化，通常只得到近似解（多数实际应用已足够）。
- 解方案称 **个体（individual）**，一代中的个体合为 **世代（generation）**，质量由**适应度值（fitness value）**衡量。
- 每个解传递给模型并执行一次或多次仿真运行，结果适应度值回传给 GAWizard。
- 含随机分量的模型需为每个个体执行多次运行（每次为一次**观测**，算法取观测均值）；确定性仿真每个个体用单次观测即可。
- 若生成重复个体，GAWizard 会复用已评估的适应度值，不浪费时间。

**配置步骤**
1. 从 **Tools** 工具栏插入 GAWizard 并双击打开对话框，可用两种方式定义优化问题：
   - **拖放**：Shift+拖表格/对象到 GAWizard，在 `ProblemDefinition` 表（`Define` 选项卡）修改取值范围；拖用于评估的对象并加权（`Fitness calculation by table`）。
   - **内置 GA 对象**：在 `Define` 选项卡定义配置方法，Shift+拖 `GASelection` / `GASequence` / `GARangeAllocation` / `GASetAllocation` 到向导并 **Apply**；属性 `individual` 表示待评估个体表格；配置方法把染色体属性传给模型；方法返回 `true` 表示可执行，否则该个体被赋**惩罚值**（`penaltyValue` 属性，F8 修改）。
2. 在 `Define` 选项卡选择优化方向（**Minimum**/`Maximum`）、**世代规模**、**世代数**。
3. 确定适应度值：
   - **按表（Fitness）**：选 "Fitness calculation by table" 并 `Open`，在 `Target value` 列填目标值名称、`Weighting` 列填权重。
   - **按方法**：选对应单选按钮，插入 Method 并 **Apply**，返回值为适应度值，需为数值类型（`real`、`time` 等）。
4. 在 `Run` 选项卡点 **Reset** 和 **Start** 开始优化。

评估完当前世代后可停止、修改设置后继续（评估期间按钮显示 **Wait**，完成后恢复 **Start**）。

**优化结束后**：对话框显示耗时，向导把**最优解**的输入值写入模型；可再次 Reset+Start 或右键图标 Reset/Start/Stop。

**仿真运行次数公式**：

```
运行次数 = 每个个体的观测次数 * (世代规模 + 2 * 世代规模 * (世代数 - 1))
```

示例（3 观测 × 10 代 × 世代规模 30）：`3 * (30 + 2 * 30 * 9) = 1710` 次运行。
> 第一代评估数量等于世代规模，之后每代评估两倍个体数。

若待生成个体数 ≤ 50,000，GAWizard 会识别已评估个体并复用适应度值（`Statistics of Fitness Values` 表中 ID 相同）；属性 `lastGeneration4DuplicatesCheck` 指定重复检查到第几代，默认 `-1` 表示检查所有世代。

**结果分析**
- `Run` 选项卡实时显示当前最优适应度值。
- `Show Evolution`（`Evaluate` 选项卡）显示每代最优/平均/最差适应度值曲线。
- `Show`（HTML Report 组）显示报告与优化过程；个体很多时建议清除 "Show detailed HTML report"。
- 随机仿真图表显示个体适应度值的 **Min-Max 区间**；若波动很大，应检查优化是否有意义。
- 统计表**第 7 列**显示个体是否被多次创建但仅评估一次。
- `DecimalSeparator`（`string`）属性可设置结果表的小数点为 `.` 或 `,`。

### 六、进阶用户（For the Advanced User）

如需用 BATCH 文件依次启动多个优化，参见 **Specifying Start Options**；Plant Simulation 不得打开任何需要用户操作的模态对话框。

---

## 备注

- 本 README 汇总自同目录 `experiment-manager-genetic-optimization.md`（与 `.txtx` 内容一致）。
- 完整操作细节与图例请参阅原文档。
