# Store 的方法与只读属性（Methods & Read-Only Attributes）

本目录记录了 **Store（仓库）** 对象中 **PE（Production Element，即 Store 内的存储位置/货位）** 以及 Store 本身提供的方法与只读属性。

> 目录内当前仅包含 `methods.md`（以及对应的原始文本 `methods.txtx` 与 PDF 源文件），没有子文件夹。以下为全部内容的总结。

---

## 总览

| 名称 | 类型 | 返回类型 | 作用 |
| --- | --- | --- | --- |
| `Cont` | 只读属性 | `object` | 返回指定存储位置最顶部的 MU |
| `exitBlockList` | 方法 | `void` / `object[]` | 返回即将离开 Store 并等待 Worker 接取的 MU |
| `getStackHeight` | 只读属性 | `length` | 返回指定存储位置上堆栈的物理高度（米） |
| `mu` | 方法 | `object` | 返回指定存储位置上堆叠的所有 MU |
| `NumMU` | 只读属性 | `integer` | 返回指定 PE（生产元素）上的 MU 数量 |

---

## 详细说明

### 1. Cont（只读属性）— `pe`, `Store`

返回 `<Path>` 指定的 Store 中、指定存储位置（生产元素）最顶部的 MU。

- **语法：**
  ```simtalk
  <Path>.pe(X:integer, Y:integer).Cont → object
  <Path>[X:integer, Y:integer].Cont → object
  ```
- **参数：**
  - `X`（integer）：存储位置在 X 维度上的位置。
  - `Y`（integer）：存储位置在 Y 维度上的位置。
- **返回值：** `object`
- **示例：**
  ```simtalk
  MyStore.pe(1,1).Cont.move(Station)
  MyStore[1,1].Cont.move(Station)
  ```

---

### 2. exitBlockList（方法）— `Store`

返回一个数组，包含即将离开 Store 并等待 Worker 接取的 MU。

- **语法：**
  ```simtalk
  <Path>.exitBlockList([ExitBlockingList:table]) -> void/object[]
  ```
- **参数：**
  - `ExitBlockingList`（table，可选）：用于写入退出阻塞列表内容的表（DataTable 或局部变量）。
    - 若指定该表，Plant Simulation 自动生成两列格式：
      - 第 1 列（`object`）：未能成功离开对象的 MU。
      - 第 2 列：这些 MU 尝试离开对象的仿真时间。
    - 对 Store 而言，退出阻塞列表还包含该部件所对应的存储位置信息，因此若需要该信息，须指定 table 而不是 array。
  - 若不指定该参数，则返回一维数组（仅含阻塞列表中的对象）；如需阻塞的开始时间，可通过 `BlockingStarttime` 属性查询。
- **返回值：** `object` 数组
- **示例：**
  ```simtalk
  var musToExit := Store.exitBlockList   // 返回即将离开的 MU 数组
  var t:table
  Store.exitBlockList(t)                 // 将即将离开的 MU 写入表 t
  ```

---

### 3. getStackHeight（只读属性）— `Store`

返回 `<Path>` 指定的 Store 中、指定存储位置上的堆栈高度（单位：米）。

- **说明：**
  - 也适用于托盘/容器（pallets/Containers）上的位置，以及装载空间为 Store 类型的运输工具（Transporter）。
  - 这里的“堆栈高度”指物理高度，而非堆栈上的部件数量。
  - 用 `print` 输出时，单位为 `Preferences/Model Settings > Unit > Length` 中设定的长度单位。
- **语法：**
  ```simtalk
  <Path>.pe(X:integer, Y:integer).getStackHeight → length
  <Path>[X:integer, Y:integer].getStackHeight → length
  ```
- **参数：**
  - `X`（integer）：存储位置在 X 维度上的位置。
  - `Y`（integer）：存储位置在 Y 维度上的位置。
- **返回值：** `length`
- **示例：**
  ```simtalk
  print MyStore.pe(2,1).getStackHeight
  print MyStore[2,1].getStackHeight
  ```

---

### 4. mu（方法）— `PE`, `Store`

返回 `<Path>` 指定的 Store 中、指定存储位置（生产元素）上所有堆叠的 MU。

- **说明：**
  - 仅当 Z 维度大于 1 时，`mu` 才能访问堆栈上的 MU。
  - 索引不代表进入（堆叠）的顺序。
  - 可通过只读属性 `NumMU` 查询最大索引。
  - 最后一个 MU 始终是位于最底层存储位置的 MU（通常是最先移入该对象的 MU）。
- **语法：**
  ```simtalk
  <Path>.pe(X:integer, Y:integer).mu(MU:integer) → object
  <Path>[X:integer, Y:integer].mu(MU:integer) → object
  ```
- **参数：**
  - `X`（integer）：存储位置在 X 维度上的位置。
  - `Y`（integer）：存储位置在 Y 维度上的位置。
  - `mu`（integer）：存储位置在 Z 维度上的位置；指定 `-1` 返回堆栈底部的 MU；若对象为空则返回 `VOID`。
- **参数默认值：** 参数 `Number` 的默认值为 `1`。
- **返回值：** `object`
- **示例：**
  ```simtalk
  print MyStore.pe(5,5).mu(1) // 返回堆栈最顶部的 MU
                              // 等同于 print MyStore.pe(5,5).cont
  print MyStore[5,5].mu(2)    // 返回堆栈上从顶部数第二个 MU
  print MyStore[5,5].mu(3)    // 返回有 3 个部件的堆栈底部的 MU
  print MyStore[1,1].MU(1)   // 返回堆栈最顶部的 MU
  print MyStore[1,1].MU(-1)  // 返回堆栈底部的 MU
  ```

---

### 5. NumMU（只读属性）— `PE`, `Store`

返回 `<Path>` 指定的 Store 中、指定 PE（生产元素）上的 MU 数量。

- **语法：**
  ```simtalk
  <Path>.pe(X:integer, Y:integer).NumMU → integer
  <Path>[X:integer, Y:integer].NumMU → integer
  ```
- **参数：**
  - `X`（integer）：存储位置在 X 维度上的位置。
  - `Y`（integer）：存储位置在 Y 维度上的位置。
- **返回值：** `integer`
- **示例：**
  ```simtalk
  print MyStore.pe(1,1).NumMU
  print MyStore[1,1].NumMU
  ```

---

## Store 的只读属性（Read-Only Attributes of the Store）

Store 提供：

- 目录（table of contents）中列出的只读属性。
- 所有对象的只读属性（Read-Only Attributes of All Objects）。
- 物料流对象的只读属性（Read-Only Attributes of the Material Flow Objects）。

**注意：** 只读属性的值只能查询、不能设置，因为 Plant Simulation 会在查询的时刻实时计算其值。大多数只读属性对应对象某个选项卡（如 Statistics 选项卡）上不可编辑的对话框项。

**查看所有方法、只读属性与属性：** 打开 **Show Attributes and Methods** 窗口：

- 在类库（Class Library）的上下文菜单中选择 **Show Attributes and Methods**，可查看所选类的方法、只读属性与属性。
- 按 F8 键，或在插入实例的 Frame 的 Home 功能区选项卡上点击 **Show Attributes and Methods**，可查看所选实例的方法、只读属性与属性。

**查询只读属性示例：**
```simtalk
print Store.Capacity
```

---

## 相关主题（See also）

- X-Dimension [Store]、Y-Dimension [Store]、Z-Dimension [Store]
- Stack Parts in the Store（在 Store 中堆叠部件）
- Exit Blocking List（退出阻塞列表）
- `BlockingStarttime` [SimTalk]、`ZDim` [SimTalk] - Store
- Length [preferences]（长度单位偏好设置）
