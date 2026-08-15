# Sorter — Methods 与只读属性（README）

本目录汇总了 Sorter（此处内容实际为 Store 的 PE，即库位/生产元素）相关的方法与只读属性说明。以下内容基于目录内的 `methods.md`（及 `methods.txtx` 同源文本）整理。

> 说明：文档标题为 “Methods and Read-Only Attributes of the PE in the Store”，即 Store 中的 PE（production element，生产元素 / 库位）所提供的方法与只读属性。PE 通过 `<Path>.pe(X, Y)` 或 `<Path>[X, Y]` 定位。

---

## 总览

| 名称 | 类型 | 作用 |
| --- | --- | --- |
| `Cont` | 只读属性 | 返回指定库位最顶层的 MU |
| `exitBlockList` | 方法 | 返回即将离开 Store 并等待 Worker 接取的 MU 数组 |
| `getStackHeight` | 只读属性 | 返回指定库位的堆叠物理高度（米） |
| `mu` | 方法 | 返回指定库位堆叠中的 MU（可按 Z 方向索引） |
| `NumMU` | 只读属性 | 返回指定库位（PE）上的 MU 数量 |

---

## 1. Cont [SimTalk] — pe, Store

- **类型：** 只读属性（Read-only attribute）
- **作用：** 返回位于指定库位最顶层位置的 MU。
- **语法：**
  ```simtalk
  <Path>.pe(X:integer, Y:integer).Cont → object
  <Path>[X:integer, Y:integer].Cont → object
  ```
- **参数：**
  - `X`（integer）：库位在 X 维度的位置。
  - `Y`（integer）：库位在 Y 维度的位置。
- **返回值：** `object`
- **示例：**
  ```simtalk
  MyStore.pe(1,1).Cont.move(Station)
  MyStore[1,1].Cont.move(Station)
  ```
- **参见：** X-Dimension [Store]、Y-Dimension [Store]

---

## 2. exitBlockList [SimTalk] — Store

- **类型：** 方法（Method）
- **作用：** 返回一个数组，其中包含即将离开 Store、并等待 Worker 接取的 MU。
- **备注：**
  - 可选参数 `ExitBlockingList`（`table`）可将 Exit Blocking List 中的对象写入该表。
  - 对 Store 而言，Exit Blocking List 还包含“该零件所对应库位的位置”；如需该信息，应传入表而不是数组。
  - 不传可选参数时，返回的是一维数组，仅包含阻塞列表中的对象。
  - 查询阻塞开始时间可使用属性 `BlockingStarttime`。
- **语法：**
  ```simtalk
  <Path>.exitBlockList([ExitBlockingList:table]) -> void/object[]
  ```
- **参数：**
  - `ExitBlockingList`（table，可选）：用于写入结果的数据表名（DataTable 或局部变量）。Plant Simulation 会自动生成两列表格：
    - 第 1 列（`object`）：尝试离开对象但未成功的 MU。
    - 第 2 列：这些 MU 尝试进入对象时的仿真时间。
- **返回值：** `object[]`
- **示例：**
  ```simtalk
  var musToExit := Store.exitBlockList   // 返回即将离开的 MU 数组
  var t:table
  Store.exitBlockList(t)                 // 将即将离开的 MU 填入表
  ```
- **参见：** SimTalk、BlockingStarttime [SimTalk]、exitBlockList [SimTalk] - material flow objects、exitBlockList [SimTalk] - lane A or B、Exit Blocking List、Check the Contents List of the Stations

---

## 3. getStackHeight [SimTalk] — Store

- **类型：** 只读属性（Read-only attribute）
- **作用：** 返回指定库位上堆叠的物理高度（单位：米）。
- **备注：**
  - 也适用于托盘/Container 上的库位，以及装载空间为 Store 类型的 Transporter。
  - 堆叠高度指物理高度，而非堆叠零件数。
  - 使用 `print` 输出时，单位为 **Preferences / Model Settings > Unit > Length** 中所选单位。
- **语法：**
  ```simtalk
  <Path>.pe(X:integer, Y:integer).getStackHeight → length
  <Path>[X:integer, Y:integer].getStackHeight → length
  ```
- **参数：**
  - `X`（integer）：库位在 X 维度的位置。
  - `Y`（integer）：库位在 Y 维度的位置。
- **返回值：** `length`
- **示例：**
  ```simtalk
  print MyStore.pe(2,1).getStackHeight
  print MyStore[2,1].getStackHeight
  ```
- **参见：** SimTalk、ZDim [SimTalk] - Store、Stack Parts in the Store、Length [preferences]、X-Dimension [Store]、Y-Dimension [Store]

---

## 4. mu [SimTalk] — PE, Store

- **类型：** 方法（Method）
- **作用：** 返回指定库位（生产元素）上堆叠的所有 MU（可按 Z 方向索引访问）。
- **备注：**
  - 仅当 Z-Dimension 大于 1 时，`mu` 才访问堆叠中的 MU。
  - 索引不代表进入顺序。
  - 最大索引可通过只读属性 `NumMU` 查询。
- **语法：**
  ```simtalk
  <Path>.pe(X:integer, Y:integer).mu(MU:integer) → object
  <Path>[X:integer, Y:integer].mu(MU:integer) → object
  ```
- **参数：**
  - `X`（integer）：库位在 X 维度的位置。
  - `Y`（integer）：库位在 Y 维度的位置。
  - `mu`（integer）：库位在 Z 维度的位置。传入 `-1` 可返回堆叠底部的 MU；若对象为空则返回 VOID。
- **参数默认值：** 参数 `Number` 的默认值为 1。
- **备注：** 最后一个 MU 始终位于底部库位，通常是最先移动到该对象上的 MU。
- **返回值：** `object`
- **示例：**
  ```simtalk
  print MyStore.pe(5,5).mu(1) // 返回堆叠最顶层的 MU
                              // 等价于 print MyStore.pe(5,5).cont
  print MyStore[5,5].mu(2)    // 返回堆叠中自顶向下的第二个 MU
  print MyStore[5,5].mu(3)    // 返回含 3 个零件的堆叠底部的 MU
  print MyStore[1,1].MU(1)    // 返回堆叠最顶层的 MU
  print MyStore[1,1].MU(-1)   // 返回堆叠底部的 MU
  ```
- **参见：** SimTalk、NumMU [SimTalk] - PE, Store、X-Dimension [Store]、Y-Dimension [Store]、Z-Dimension [Store]

---

## 5. NumMU [SimTalk] — PE, Store

- **类型：** 只读属性（Read-only attribute）
- **作用：** 返回指定库位（PE）上的 MU 数量。
- **语法：**
  ```simtalk
  <Path>.pe(X:integer, Y:integer).NumMU → integer
  <Path>[X:integer, Y:integer].NumMU → integer
  ```
- **参数：**
  - `X`（integer）：库位在 X 维度的位置。
  - `Y`（integer）：库位在 Y 维度的位置。
- **返回值：** `integer`
- **示例：**
  ```simtalk
  print MyStore.pe(1,1).NumMU
  print MyStore[1,1].NumMU
  ```
- **参见：** X-Dimension [Store]、Y-Dimension [Store]

---

## Store 的只读属性（通用说明）

Store 提供：

- 左侧目录中列出的只读属性。
- 所有对象的只读属性（Read-Only Attributes of All Objects）。
- 物料流对象的只读属性（Read-Only Attributes of the Material Flow Objects）。

只读属性可以查询其值，但不能设置；Plant Simulation 会在你查询的时间点计算该值。多数情况下，只读属性对应对象某个选项卡（如 Statistics 选项卡）上不可编辑的对话框项。

查看对象的所有方法、只读属性与属性，可打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，查看所选 Class 的方法、只读属性与属性。
- 在插入实例的 Frame 的 Home 功能区选项卡上按 **F8** 或点击 **Show Attributes and Methods**，查看所选 Instance 的方法、只读属性与属性。

查询只读属性的示例：

```simtalk
print Store.Capacity
```
