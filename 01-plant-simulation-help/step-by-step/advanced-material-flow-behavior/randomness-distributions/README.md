# Randomness Distributions（随机分布）

> 本目录整理了 Plant Simulation 帮助文档中关于**随机过程建模**的内容，来源为 *Plant Simulation Help — Modeling Random Processes*（第 10-304 至 10-308 页）。

## 目录说明

- `randomness-distributions.md` — 本主题的整理版总结（Markdown）。
- `randomness-distributions.txtx` — 帮助文档原文的文本提取（含页眉页码与版权信息）。

## 内容概览

### 1. 随机过程建模（Model Random Processes）

许多计算机程序使用随机数生成器产生位于 `(0, 1)` 区间内的随机数流。从给定的**种子值（seed values）**出发，程序需要生成大量统计独立的随机数。

随机数在计算机程序中的典型应用：

- **游戏程序**：让游戏运行序列更加多样。
- **数据库程序**：批量录入数据以测试数据库功能。
- **仿真程序**（如 Plant Simulation）：表示机器的故障间隔等。

### 2. 随机数及其统计分布（Random Numbers and Their Statistical Distribution）

过程分为两类：

- **确定性过程（deterministic process）**：结果可预测（如借助自然规律）。
- **随机过程（random process）**：当影响过程的因素不完全已知时，结果为随机。

在生产仿真中，**停顿/暂停的发生是确定性过程**；**机器故障或产生的废品是随机过程**。

随机过程产生**随机数**，该过程的重复（复制）产生随机数的**实现（realization）**。例如掷骰子是随机过程，所得点数即为相应的随机数。

#### 离散 vs. 连续随机数

- **离散（discrete）**：取值是有限或无限个独立、分开的数值（如长期内的废品数、一天内的订单数）。描述时给出各数值的概率，所有概率之和必须为 1。
- **连续（continuous）**：可取某区间内的所有值（如机器的平均故障间隔 MTBF、平均修复时间 MTTR）。无法指定单个数值的概率，只能指定随机数落在两个给定值之间（某区间）的概率。

#### 概率密度函数（Probability Density Function）

概率密度函数描述随机数的分布：

- 连续随机数的密度函数取值 ≥ 0，且可连续绘制而不中断。
- 两点 `a`、`b` 之间的曲线下方面积，即为随机数落在 `[a, b]` 的概率。
- 密度函数在 `x` 处的取值描述“接近 `x` 的值”出现的频率。
- 整条曲线下方的总面积为 1（每次实现总会产生某个值）。

**示例（Gamma 分布，Alpha = 3，Beta = 5.5）**：

- 大多数随机数出现在密度函数顶点附近（`x = 11`），该值称为**众数/模态值（modal value / mode）**。
- 多次实现的**均值**明显大于众数，约为 16.5。
- 该分布产生 24 到 26 之间随机数的概率为 0.04（对应曲线下方的灰色面积）。

### 3. 伪随机数的使用（Use Pseudo Random Numbers）

计算机按固定计算规则运算，无法产生真正随机的序列，因此其生成的序列只能近似具备随机数特性，故称为**伪随机数（pseudo random numbers）**。

- 计算机生成的数字序列称为**随机数流（random number stream）**。
- 算法从**种子值**开始，可生成任意数量的值。
- 使用不同种子值可建模多个彼此独立的随机过程。

创建随机数时，通常只需生成区间 `(0,1)` 内**均匀分布**的随机数。均匀分布是指某区间的概率仅取决于区间长度，而与它在数轴上的位置无关。借助均匀分布随机数，计算机可算法化地生成具有给定均值与标准差的正态分布随机数等。

均匀分布的伪随机数需满足以下要求：

- 随机数的排列无明显特征（相邻随机数的代数符号无典型模式）。
- 算法必须呈周期性（因计算机状态有限），故**周期长度应尽可能大**。
- 从给定种子值出发，需为仿真提供大量统计独立的随机数。
- 仿真的随机过程必须**可复现**，以便使用方差缩减等统计方法。

### 4. 概率分布的使用（Use Probability Distributions）

通常，关于随机过程（如机器两次故障的间隔）可获得的观测数据非常少。

为在仿真模型中复现这些随机过程，Plant Simulation 提供了多种概率分布，参见 **Probability Distributions**、**Empirical Distributions** 和 **User-defined Distributions**。

- **Step 3: Decide Which Distribution to Use** 借助 **DataFit** 对象帮助选择合适的分布。
- 从列表中选择分布后，Plant Simulation 会在选项卡上边框显示该分布所需的参数。
- 根据观测数据（来自客户）计算相应参数值并填入文本框。
- **下界（lower bound）**与**上界（upper bound）**为可选项——可以指定，也可以不指定。

## 关键术语

| 英文 | 中文 |
| --- | --- |
| random number | 随机数 |
| seed value | 种子值 |
| pseudo random number | 伪随机数 |
| random number stream | 随机数流 |
| deterministic process | 确定性过程 |
| random process | 随机过程 |
| discrete / continuous | 离散 / 连续 |
| probability density function | 概率密度函数 |
| modal value (mode) | 众数 / 模态值 |
| mean value | 均值 |
| uniform distribution | 均匀分布 |
| MTBF / MTTR | 平均故障间隔 / 平均修复时间 |
