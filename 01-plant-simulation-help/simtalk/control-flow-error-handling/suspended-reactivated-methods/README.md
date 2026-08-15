# Suspended and Reactivated Methods — 目录总结

本目录介绍 Plant Simulation / SimTalk 中**方法（Method）的中断、挂起与重新激活**机制，以及循环退出语句 `exitLoop`。

> 目录内只有一个 Markdown 文件 `suspended-reactivated-methods.md`，且无子文件夹，故本 README 汇总该文件的全部章节要点。

---

## 1. 用 `exitLoop` 退出循环

- 关键字 `exitLoop` 用于退出循环。
- 可选地传入一个整数来指定要退出的循环层数，例如 `exitLoop 2` 表示退出内层与外层两层循环。

---

## 2. 挂起方法（Suspending Methods）

方法在执行过程中可能因多种原因被中断（挂起）：

- 调用了另一个方法；
- 将 MU 移动到设置了入口控制（Entrance Control）的对象上，此时方法执行会中断，直到入口控制执行完毕；
- 通过条件挂起：`waituntil` 和 `stopuntil` 指令根据条件挂起方法，条件不满足时解释器保存整个调用链（含参数与局部变量），转而执行其他方法或继续仿真；条件满足时，解释器从挂起点继续执行被挂起的方法。

**示例**：解释器执行 MethodA 遇到 `waituntil`，条件不成立而挂起；随后执行 MethodB 改变了模型，使 MethodA 的条件成立；解释器立即中断 MethodB，重新激活并执行 MethodA，之后继续执行 MethodB。

### `waituntil` vs `stopuntil` 行为差异

- 用 `waituntil` 挂起的方法：每个被唤醒的方法处理完后，会重新评估其余待唤醒方法的条件与优先级。
- 用 `stopuntil` 挂起的方法：条件一旦满足一次，就会无条件唤醒，不再重新评估条件。

其他要点：

- 在 reset 阶段挂起自身的方法，reset 阶段结束时挂起会被删除。
- 被 `waituntil` / `stopuntil` / `wait` / `sleep` 挂起的方法，会在 Frame 窗口中显示 tooltip，包含：调用者、被挂起的指令、被挂起的方法数量。

---

## 3. `waituntil` 与 `stopuntil`

- 语法：

```simtalk
waituntil condition [prio number] [wait timespan:time]
stopuntil condition [prio number] [wait timespan:time]
```

- 组成：关键字、条件（布尔表达式）、可选的 `prio` 关键字 + 整数表达式（优先级）、可选的 `wait` 时间限制（配合 `waitExpired` 查询时间限制是否到期）。
- 条件满足时被挂起方法被立即唤醒；若此刻有其他方法正在执行，它们会被中断，待被唤醒方法执行完毕后再继续。
- 可观察只有路径最后一部分可监视的表达式，如 `Station.Origin.Name`。

### 重要注意事项

- 不要在对仿真有影响的方法中配合 `SimTime` 使用 `waituntil` / `stopuntil`——时间不是连续推进而是逐事件跳变。
- 不要在公式（formula）中使用这些语句，否则解释器会报错终止。
- reset 仿真模型时，会删除位于 EventController 同一 Frame（或其子 Frame）中方法（或调用者 `?` 位于该 Frame）的挂起。
- `waituntil` / `stopuntil` 不基于事件，无需 EventController；而 `wait` 语句需要 EventController。
- 语句后若以 `---` 或 `///` 开头的注释，Watch Window 与 Method Debugger 的 Suspended 选项卡只显示注释而不显示整个语句。
- 方法 `deleteSuspendedMethods` 删除所有方法的所有挂起。
- 被挂起的方法在图标顶部边框显示紫色矩形。

---

## 4. 条件（Condition）

- `waituntil` / `stopuntil` 中的条件决定了何时继续执行方法。
- 条件为真 → 继续执行下一条语句；条件为假 → 挂起方法并监视表达式各组件，某组件变化时重启方法重新分析条件。

**可用的运算符**：

- 基本运算符：`+`、`-`、`*`、`/`
- 比较运算符：`=`、`<=`、`>=`、`/=`
- 逻辑运算符：`AND`、`OR`、`NOT`
- 括号 `()`

**限制**：

- 不能使用方法调用、表访问、带参数的内置方法。
- 应避免有副作用的内置方法（如 `stack.pop`），因为条件可能被频繁分析。

**求值顺序**：逻辑运算从左到右，一旦表达式值确定即终止求值（短路求值），可避免运行时错误。

### 关于 `void` 属性

观察数据类型为 object 的用户定义属性时，其值变为 `void` 有两种原因：

1. 方法给该属性赋值 `void` → 条件会被重新评估，可能唤醒语句。
2. 该属性指向的对象被删除 → 条件不会被重新评估，语句不会唤醒。

---

## 5. 优先级（方法执行）

- 多个方法可能基于相同/相似条件被同时唤醒，解释器优先唤醒优先级最高的方法。
- 最高优先级方法执行完毕或再次遇到条件不满足的 `waituntil` 后，解释器重新分析剩余方法的条件，得到新的待唤醒子集，再重新分析优先级选择最高者。
- 评估优先级可使用方法、DataTable 或参数；避免副作用（删除 MU、改全局变量等），因为优先级表达式求值的频率与时机取决于解释器和模型状态。

---

## 6. 用 `wait` 中断方法执行

- 语法：

```simtalk
wait timespan:real
```

- `wait` 使调用链中断指定的仿真秒数，之后继续执行。仿真按调用链已结束的方式继续，EventController 会插入 `MethWakeup` 事件。
- **前提**：仿真模型必须包含 EventController。
- reset 阶段挂起自身的控制会被删除。
- 位于 Class Library 文件夹中的方法类（Method class），若被包含 EventController 的模型中的方法调用，也可用 `wait` 挂起。
- 被 `wait` 挂起的方法会在 Frame 窗口的 tooltip 中显示，并在图标顶部边框显示彩色矩形。

---

## 7. `waituntil` 与 `stopuntil` 的时间限制

- SimTalk 2.0 起可为 `waituntil` / `stopuntil` 指定时间限制。
- 挂起达到该时长后，即使条件未满足也会被重新激活。
- 关键字 `waitExpired` 在因时间限制被重新激活时设为 `true`；若因条件满足而结束挂起则为 `false`。

```simtalk
waituntil Station.Empty wait 60
   if waitExpired
       [Station]
   else
       @.delete
   end
```

---

## 8. 重新激活方法（唤醒方法）

- 条件的值可能因仿真事件或方法处理而改变。
- 有方法激活时，解释器会中断活动方法并保存其整个调用链。
- 之后重新分析被挂起方法的条件（不重复分析与变化无关的条件）：
  - 条件为假 → 立即挂起。
  - 条件为真 → 分析优先级并建立优先级列表，选择最高优先级方法恢复执行（重新激活），直至整个活动调用链执行完毕、出错、或再次遇到条件不满足的 `waituntil` 而被挂起。

---

## 9. 同时唤醒多个方法

- 多个方法可同时被激活时，优先重新激活优先级最高的方法。
- 唤醒某个方法可能影响其余方法的条件，使某些原本为真的条件变为假。
- `waituntil`：第一个方法执行完后重新分析条件，因此部分方法可能即使初始条件为真也保持挂起。
- `stopuntil`：不进行二次分析，条件一旦为真，其余方法都会被重新激活。
- 解释器按指定的优先级重新激活方法。

---

## 10. 用 `waituntil` 同时唤醒多个方法（示例）

- 场景：多辆 Transporter 从不同对象驶向同一 Station（Station 只有为空时才能接受 MU）。
- 前驱对象 Exit Control 源码：

```simtalk
waituntil Station.Empty prio @.Capacity
@.move(Station)
```

- 三个 Exit Control 被挂起；Station 变空时，Capacity 最大的 Transporter（优先级最高）驶向 Station；之后 `Station.Empty` 变假，其余两辆原地等待 Station 再次变空。

---

## 11. 用 `stopuntil` 同时唤醒多个方法（示例）

- 场景：用变量 `GateOpen` 建模 Store，`GateOpen` 为 `true` 时 MU 才能进入；MU 通过闸门后 `GateOpen` 又变 `false`。
- 前驱对象 Exit Control 源码：

```simtalk
stopuntil GateOpen prio 1
@.move(Store)
GateOpen := false
```

- `GateOpen` 为真时，解释器唤醒所有被挂起的方法，即使第一个方法调用后 `GateOpen`（挂起条件）已被设为 false。

---

## 12. 可监视值（Watchable Values）

- 可监视值是 Plant Simulation 在执行 SimTalk 代码时能够观察的值。
- `waituntil` / `stopuntil` 中的条件可被观察的前提是布尔表达式所有组件都可监视。
- 仅当某个可监视组件在仿真中发生变化时，SimTalk 才会重新评估条件。
- 无法监视的条件示例：用户自定义方法的返回值、持续变化的值（如站点利用率）。
- 若条件包含无法监视的组件，Method Debugger 会打开并显示错误 `Expression cannot be watched`。
- Show Attributes and Methods 窗口中的 Watchable 列显示了所有可监视的属性、方法与只读属性。

---

## 13. 创建与删除观察者（Observer）

- 相关视频（YouTube）：
  - https://youtu.be/5t-wLNmKpbU?si=iskEWwLFhy6WvVlb&t=1088
  - https://youtu.be/9g6Uou-8eMc?si=tMGvgn6iYeolw7V8&t=318
