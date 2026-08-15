# Mathematical Functions（数学函数）— 目录说明

本目录汇总了 Plant Simulation / SimTalk 中与数学运算、位操作相关的预定义函数。

> 目录内文件：
> - `mathematical-bit.md` —— 主要文档（本 README 的总结对象）
> - `mathematical-bit.txtx` —— 原始帮助文本（与 md 内容一致，含公式图占位）
> - 无子文件夹，因此没有子目录 README 可供汇总。

---

## 概述

Plant Simulation 提供了多种数学函数，调用时**无需输入路径**。这些函数分为以下几类：

1. 基础数学函数（Basic Mathematical Functions）
2. 数值处理函数（Functions for Numerical Values）
3. 三角函数（Trigonometric Functions）
4. 分布函数 / z_ 函数（Distribution Functions, z_ functions）
5. 位操作函数（Functions for Manipulating Individual Bits）
6. 字符串变量编辑函数（Functions for Editing Variables of Data Type String）

相关参考：算术运算符（Arithmetic Operators）、数学函数（Mathematical Functions）。

---

## 1. 基础数学函数

| 函数 | 形式 | 说明 |
|---|---|---|
| `abs` | `abs(x)` | x 的绝对值 |
| `beta` | `beta(x,y)` | Beta 函数，x, y > 0 |
| `betai` | `betai(x,y,z)` | 不完全 Beta 函数，x, y > 0 且 0 ≤ z ≤ 1 |
| `exp` | `exp(x)` | 指数函数 e^x |
| `gamma` | `gamma(x)` | Gamma 函数 Γ(x)，x > 0 |
| `log` | `log(x)` | 自然对数 |
| `log10` | `log10(x)` | 以 10 为底的对数 |
| `pow` | `pow(x,y)` | x^y |
| 幂运算符 | `x ** y` | 等价于 `pow(x,y)` |
| `sqrt` | `sqrt(x)` | 平方根（参数须 ≥ 0） |

**关于 `pow` 的约束：**
- 底数为 0 时，指数必须大于 0。
- 指数不是整数（如 -0.5）时，底数必须 ≥ 0。

**注意事项：**
- `sqrt` 只接受 ≥ 0 的参数。
- `sqrt` 与 `pow` 支持物理单位；`sqrt` 有限制：若被开方数带有平方单位，结果为不带平方的单位；其他幂运算返回无单位的 real。
- 使用 `exp`、`pow`、`gamma` 及算术运算符时，需确保结果在计算机可表示的数值范围内。
- 可用 `gamma` 计算阶乘：`n! = 1 · 2 · … · n = Γ(n+1)`。

**参数**：real、integer 或带物理单位的值。
**返回值**：real。

**示例**：
```simtalk
var area := 2m * 2m;
print area        // 输出 4m²
print sqrt(area)  // 输出 2m

var x: real := 2
var y: real := 3
var z: real := x ** y  // z = 8
```

---

## 2. 数值处理函数

| 函数 | 形式 | 说明 |
|---|---|---|
| `ceil` | `ceil(x)` | 大于等于 x 的最小整数 |
| `floor` | `floor(x)` | 小于等于 x 的最大整数 |
| `max` | `max(x,y[,z,...])` | 最大值 |
| `min` | `min(x,y[,z,...])` | 最小值 |
| `round` | `round(x)` | 四舍五入到相邻整数（`round(-1.5)` 得 -2） |
| `round` | `round(x:real, places:integer)` | 将 x 四舍五入到指定位数 |

**注意：**
- `max` / `min` 可接受多于两个参数。
- `max` / `min` 不能任意混用数据类型：所有参数必须同为数值类型、或同为 date/dateTime、或同为 string。

**参数**：real、integer 或带物理单位的值；`min`/`max` 还可接受 date、dateTime、string。
**返回值**：与所传参数相同的数据类型。

---

## 3. 三角函数

| 函数 | 形式 | 说明 |
|---|---|---|
| `acos` | `acos(x)` | 反余弦 |
| `asin` | `asin(x)` | 反正弦 |
| `atan` | `atan(x)` | 反正切 |
| `atan2` | `atan2(y,x)` | y 与 x 的反正切 |
| `cos` | `cos(x)` | 余弦 |
| `sin` | `sin(x)` | 正弦 |
| `tan` | `tan(x)` | 正切 |

**参数**：以弧度为单位（输入或返回均为弧度），类型为 real 或 integer。
**返回值**：real。

### `atan2(y, x)` 详细说明

返回平面正 x 轴与点 (x, y) 之间的弧度角（x、y 均不能为 0）。

- 语法：`atan2(y:real, x:real) → real`
- 参数：`y` 为 y 轴坐标，`x` 为 x 轴坐标。
- 返回值：real。逆时针方向（上半平面，y > 0）为正；顺时针方向（下半平面，y < 0）为负；当 x=0 且 y=0 时返回 0。

---

## 4. 分布函数（z_ 函数）

用于创建概率分布。可在对象的 Times / Failures 标签页对话框、`randtime` 类型变量以及 SimTalk 中生成随机数。

**分布函数一览：**

| 函数 | 分布 |
|---|---|
| `z_beta([Stream,]Alpha1,Alpha2) -> real` | Beta |
| `z_binomial([Stream,]n,p) -> real` | Binomial |
| `z_cauchy([Stream,]Mu,Theta[,LowerBound,UpperBound]) -> real` | Cauchy |
| `z_cemp([Stream,]Table) -> real` | cEmp（连续经验分布） |
| `z_demp([Stream,]Table) -> real` | dEmp（离散经验分布） |
| `z_emp([Stream,]Table,Column) -> integer` | Emp（原始经验分布） |
| `z_erlang([Stream,]Mu,Sigma[,LowerBound,UpperBound]) -> real` | Erlang |
| `z_frechet([Stream,]Mu,Theta[,LowerBound,UpperBound]) -> real` | Fréchet |
| `z_gamma([Stream,]Alpha,Beta[,LowerBound,UpperBound]) -> real` | Gamma |
| `z_geom([Stream,]p[,LowerBound,UpperBound]) -> real` | Geom |
| `z_gumbel([Stream,]Mu,Theta[,LowerBound,UpperBound]) -> real` | Gumbel |
| `z_hypgeom([Stream,]m,n,p) -> real` | Hypgeo |
| `z_laplace([Stream,]Mu,Theta[,LowerBound,UpperBound]) -> real` | Laplace |
| `z_logistic([Stream,]Mu,Theta[,LowerBound,UpperBound]) -> real` | Logistic |
| `z_loglogistic([Stream,]Mu,Theta[,LowerBound,UpperBound]) -> real` | Loglogistic |
| `z_lognorm([Stream,]Mu,Sigma[,LowerBound,UpperBound]) -> real` | Lognorm |
| `z_negexp([Stream,]Beta[,LowerBound,UpperBound]) -> real` | Negexp |
| `z_normal([Stream,]Mu,Sigma[,LowerBound,UpperBound]) -> real` | Normal |
| `z_paralogistic([Stream,]Mu,Theta[,LowerBound,UpperBound]) -> real` | Paralogistic |
| `z_pareto([Stream,]Mu,Theta[,LowerBound,UpperBound]) -> real` | Pareto |
| `z_poisson([Stream,]Lambda) -> real` | Poisson |
| `z_triangle([Stream,]c,a,b) -> real` | Triangle（三角分布） |
| `z_uniform([Stream,]LowerBound,UpperBound) -> real` | Uniform |
| `z_weibull([Stream,]Alpha,Beta) -> real` | Weibull |

**参数：**
- `Stream`（integer）：随机数流。在 Method 中调用时可省略；省略时使用 Method（或 method 类型用户属性）的随机数流。公式（formula）中必须显式指定，因为公式不使用所属对象的随机数流。
- 其余参数为各分布对应的参数（详见 Probability Distributions），类型为 real 或 integer。

**返回值**：real；其中 `z_emp` 返回 integer。

**相关参考**：`RandomSeed`、`resetRandomNumberStream`、Parameters of the Distributions、Probability Distributions、Methods of the Distributions。

### 单个分布函数说明

| 函数 | 别名 / 说明 | 参数要求 |
|---|---|---|
| `z_cauchy` | Cauchy 连续分布；用于大型系统开发中的故障发生建模 | µ 和 θ 均须 > 0；无法由参数直接算出均值与标准差 |
| `z_frechet` | 又称 Gumbel II 型 / 逆 Weibull；用于求多个随机数的最大值 | µ 和 θ 须为正 |
| `z_gumbel` | 又称 log-Weibull / Gumbel I 型 / 极值分布；用于样本最大值/最小值建模 | µ 和 θ 须为正；µ 决定均值；方差 σ² = π²·θ² / 6 |
| `z_laplace` | 又称双指数分布（连续分布） | µ 和 σ > 0；µ 决定均值，σ 决定标准差 |
| `z_logistic` | 连续分布；用于寿命分布建模 | µ 和 σ > 0；µ 决定均值，σ 决定标准差 |
| `z_loglogistic` | 又称 Fisk 分布；用于收入/寿命分布建模 | α > 0 且 β > 0 |
| `z_paralogistic` | Pareto 分布的变换形式 | α > 0 且 θ > 0 |
| `z_pareto` | 幂律概率分布 | α > 0 且 θ > 0 |

以上分布函数的语法形式统一为：

```
z_xxx([Stream:integer,]...参数...[,LowerBound:real,UpperBound:real]) → real
```

返回值均为 real（`z_emp` 例外，为 integer）。

---

## 5. 位操作函数

用于对整数值的单个位（bit）进行操作。

| 函数 | 语法 | 说明 |
|---|---|---|
| `BitAND` | `BitAND(Value1:integer, Value2:integer) → integer` | 对 Value1 和 Value2 执行按位与 |
| `BitClear` | `BitClear(OriginalValue:integer, BitPosition:integer) → integer` | 将 OriginalValue 中第 BitPosition 位置为 0 |
| `BitOR` | `BitOR(Value1:integer, Value2:integer) → integer` | 对 Value1 和 Value2 执行按位或 |
| `BitSet` | `BitSet(OriginalValue:integer, BitPosition:integer) → integer` | 将 OriginalValue 中第 BitPosition 位置为 1 |
| `BitShift` | `BitShift(Value:integer, NumberOfDigits:integer) → integer` | 将 Value 的位左移/右移 NumberOfDigits 位 |
| `BitTest` | `BitTest(Value:integer, BitPosition:integer) → boolean` | 检测 Value 中第 BitPosition 位是否为 1 |
| `BitXOR` | `BitXOR(Value1:integer, Value2:integer) → integer` | 对 Value1 和 Value2 执行按位异或 |

**要点：**
- `BitPosition` 取值范围为 0 到 63；最低有效位编号为 0，最高有效位编号为 63。
- `BitShift` 中 `NumberOfDigits` 大于 0 表示左移，小于 0 表示右移。
- `BitClear` 与 `BitSet` 互为参考；`BitTest` 返回 boolean，其余返回 integer。

**示例（BitTest）：**
```simtalk
var i : integer := 40 // 二进制：00101000
print bitTest(i, 3)   // 返回 true，因为第 3 位被置位
```

---

## 6. 字符串变量编辑函数

SimTalk 提供了用于编辑 string 类型变量的函数（详见左侧目录）。

**要点：**
- 这些函数**不会修改原字符串内容**，而是对字符串副本进行操作，将结果作为返回值返回。
- 这使得 Plant Simulation 可以在仿真运行期间将对象名称插入到消息文本中。

---

## 备注

- 本文档是对 `mathematical-bit.md`（及其原始文本 `mathematical-bit.txtx`）内容的总结，函数名与语法保持英文原样，便于与 Plant Simulation 帮助文档对应查阅。
