# Methods / Attributes of Cells

本目录介绍列表（Lists）与表格（Tables）中单元格（Cells）的只读属性（read-only attributes）与属性（attributes）。

## 目录内容

- [methodsAttributes of Cells.md](./methodsAttributes%20of%20Cells.md)：单元格的只读属性与属性说明。

## 内容总结

列表与表格中的单元格提供以下两个成员：

| 成员 | 类型 | 数据类型 | 说明 |
| --- | --- | --- | --- |
| `Name` | Attribute（属性） | `string` | 设置或返回指定单元格中所含子列表/子表格的名称 |
| `Void` | Read-only attribute（只读属性） | `boolean` | 返回指定单元格是否为空（`true` 为空，`false` 非空） |

### Name [SimTalk] - cells

设置由 `<Path>` 指定的列表/表格单元格中所含子列表或子表格的名称。

- **语法：**
  ```simtalk
  <Path-of-the-list[row]>.Name.string
  <Path-of-the-table[column,row]>.Name.string
  ```
- **返回值：** `string`
- **示例：**
  ```simtalk
  DataTable.createNestedList(1, 1, "abc")
  print DataTable[1,1].Name  // prints "abc"
  DataTable[1,1].Name := "XY"
  print DataTable[1,1].Name  // prints "XY"
  ```

### Void [SimTalk] - cells of lists/tables

返回由 `<Path>` 指定的列表/表格单元格是否为空。

- **语法：**
  ```simtalk
  <Path-of-the-list[row]>.void -> boolean
  <Path-of-the-table[column,row]>.void -> boolean
  ```
- **返回值：** `boolean`
- **示例：**
  ```simtalk
  if not DataTable[1,1].void
     DataTable[1,1] += 1
  end
  ```

## 其他说明

- 单元格的读写访问权限取决于对象类，详见各子章节。
- 列表与表格还提供用于返回其状态的只读属性。只读属性只能查询、不能设置，其值由 Plant Simulation 在查询时即时计算。多数只读属性对应对象某个选项卡（如 **Statistics**）上不可编辑的对话框项。
- 查看对象全部方法、只读属性与属性：打开 **Show Attributes and Methods** 窗口。可通过类库上下文菜单中的 **Show Attributes and Methods**（查看所选类），或在 Frame 的 Home 功能区中按 **F8** / 点击 **Show Attributes and Methods**（查看所选实例）打开。
