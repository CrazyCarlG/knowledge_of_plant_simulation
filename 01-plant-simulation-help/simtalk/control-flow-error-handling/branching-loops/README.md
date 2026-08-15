# Branching & Loops（SimTalk 控制流）

本目录收录 SimTalk 中「分支与循环」相关控制流语法的帮助文档。核心源文件为
`branching-loops.md`，其余同名 `.txtx` 文件为其原始文本版本，内容一致。

## 目录概览

| 文件 | 说明 |
|------|------|
| `branching-loops.md` | 分支与循环的完整说明（运算符优先级、if 系列、when-then-else、switch、循环） |
| `branching-loops.txtx` | 上述内容的原始文本导出（含页码与页眉） |

## 内容总结

SimTalk 的控制流并非总是线性执行，不同事件会影响执行路径。文档涵盖以下主题：

### 1. 运算符优先级（Precedence）

数学运算默认乘法优先于加法。SimTalk 可组合数学与关系运算符，借助优先级规则减少括号使用。优先级从高到低：

| 优先级 | 运算符 | 说明 |
|--------|--------|------|
| 最高 | `( )` | 括号 |
| | `–`, `NOT` | 正负号、逻辑非 |
| | `*`, `/`, `//`, `\` | 乘、除、整除、取模 |
| | `+`, `–` | 加、减 |
| | `<`, `<=`, `=`, `/=`, `>=`, `>` | 小于、小于等于、等于、不等于、大于等于、大于 |
| | `AND` | 逻辑与 |
| | `OR` | 逻辑或 |
| 最低 | `:=` | 赋值 |

括号内的表达式优先执行，嵌套括号由内向外解析。

### 2. 控制流语句（Control Flow Statements）

- 分支：`if-else-end`
- 多重分支：`if-elseif-end`
- 条件表达式：`when-then-else`
- 多值判断：`switch`
- 循环（Loops）
- 挂起方法：`waituntil`、`stopuntil`

### 3. 分支 `if-else-end`

根据条件决定执行路径，以关键字 `end` 结束。条件为真执行 `statement_list1`，否则执行
`else` 后的 `statement_list2`；省略 `else` 时直接跳转到分支后的第一条语句。语句列表可包含
赋值、方法调用、循环或嵌套分支，无嵌套层数限制。

```simtalk
if condition
   statement_list1
[else
   statement_list2]
end
```

### 4. 多重分支 `if-elseif-end`

当简单真假判断不够时，用 `elseif` 在多个可能中做选择。SimTalk 依次判断条件，命中第一个为真的
条件后执行对应语句；均不成立时执行可选的 `else` 分支，无 `else` 则继续执行 `end` 之后。

```simtalk
if condition1
   statement_list1
elseif condition2
   statement_list2
[...]
[else
   statement_list3]
end
```

### 5. 条件表达式 `when-then-else`

根据布尔表达式选择表达式：

```simtalk
when condition then expression1 else expression2
```

- `condition` 为真 → 选 `expression1`
- `condition` 为假 → 选 `expression2`

### 6. 多值判断 `switch`

用于替代冗长的 `if-elseif-end` 链。语法：

```simtalk
switch expression
   case constant_list statement_list
   [case constant_list statement_list ...]
   [else statement_list]
end
```

要点：

- 表达式数据类型可为 `integer`、`real` 或 `string`。
- 执行流程：表达式只求值一次并转换为常量对应类型；执行常量列表包含该结果的 `case` 分支；
  无匹配且存在 `else` 时执行 `else` 分支。
- `string` 值区分大小写。
- `real` 值不检查精确相等：忽略内部浮点显示的最后一位有效数字（`switch` 不支持 `~=` 容差比较，
  而 `if` 可用 `=`（精确）或 `~=`（约等）控制）。
- `case` 顺序及常量顺序不影响执行速度。

### 7. 循环（Loops）

提供 `while`、`repeat`、`for` 三种循环，可用 `exitLoop` 提前退出。

#### `while` 循环
先判断条件再执行；条件不满足时循环体可能一次都不执行。条件永假则死循环，可用
`Ctrl+Alt+Shift` 停止并打开 Method-Debugger。

```simtalk
while n > 1
   result := n * result
   n -= 1
end
```

#### `repeat` 循环
先执行一次再判断条件，至少执行一次；条件满足才退出。

```simtalk
repeat
   x := methodEnterLength
until x >= 0
```

#### `for` 循环
遍历起始值与结束值之间的范围，循环变量为 `integer`，每次迭代自动加 1；结束值小于起始值时
不执行。可用 `downto` 反向迭代（每次减 1）。循环变量仅在循环体内可见，循环结束后指向同名
对象（若存在）。为性能考虑，起始值与结束值只求值一次。

```simtalk
for var y := 1 to table.yDim
   print table[1,y]
next

for var y := table.yDim downto 1
   print table[1,y]
next
```

也可使用已声明的 `integer` 局部变量作为循环变量（省略 `var`/`local`），循环结束后变量仍可访问。

## 相关方法模板

文档中多次引用的方法模板（Method templates）包括：`if-else`、`if-else-end`、`if-elseif-end`、
`switch-case-end`、`switch-case-else-end`、`while-end`、`repeat-until`、`for-next`。
