# Methods for Accessing Lists and Tables

本目录整理了列表和表格对象的访问方法（`accessing-lists-and-tables.md`）。这些方法用于读取和写入列表/表格的内容，读写权限取决于对象类。

适用于以下对象（除非另有说明）：`DataStack`、`DataQueue`、`DataList`、`DataTable`、`TimeSequence`。

可通过 **Show Attributes and Methods** 窗口查看对象的全部方法、只读属性和属性。

## 方法总览

| 方法 | 说明 | 返回值 |
| --- | --- | --- |
| `closeDialog` | 关闭列表对象的对话框 | `boolean` |
| `copy` | 复制整个列表/表格（可指定范围） | `list`/`table` |
| `countMatches` | 统计指定值在指定范围内出现的次数 | `integer` |
| `delete` | 删除列表对象的内容（可指定范围） | — |
| `insert` | 向单列列表对象插入条目 | — |
| `insertList` | 将列表内容插入到 DataTable 或 DataList | — |
| `intersection` | 返回两个范围/列表共有的交集值 | `list` |
| `openDialog` | 打开列表/表格的窗口 | `boolean` |
| `openDialogBox` | 以前置对话框形式打开列表对象 | `boolean` |
| `printList` | 打印列表内容（不含图标及来源/类信息） | `boolean` |
| `refillDialog` | 用当前值刷新已打开的对话框 | — |
| `showPrintDialog` | 打开默认打印机的打印对话框 | `boolean` |

## 方法详解

### closeDialog — 关闭对话框
关闭 `<Path>` 指定的列表对象对话框。

```simtalk
MyDataTable.closeDialog
MyDataList.closeDialog
```

### copy — 复制列表/表格
复制整个列表/表格并返回为 `list`/`table` 类型。`copy(Range)` 复制指定范围；未指定范围时复制整个列表。要连同列索引/行索引一起复制，可在范围中写入列 0 和/或行 0。复制结果可用于：赋值给同类型局部变量、插入表格某列、或作为独立的 DataList。

```simtalk
var MyDataList : list[integer]
MyDataList := MyDataList1.copy({1}..{5})
```

### countMatches — 统计出现次数
统计指定值在指定范围内出现的次数。可选的 `Range` 省略时搜索整个范围 `{1,1}..{*,*}`；`CaseSensitive` 默认 `false`（不区分大小写）。

```simtalk
print MyDataTable.countMatches("a1", {1,1}..{3,12})
```

### delete — 删除内容
删除列表对象内容，`delete(Range)` 删除指定范围（可多个范围）。未指定范围时删除所有单元格内容但不含列/行索引（等价于 `{1,1}..{*,*}`）。要删除 DataTable 的自定义行/列索引，须显式写入行 0 或列 0。也可删除继承内容的子表，继承关系会把引用传回源对象。

```simtalk
MyDataStack.delete
MyDataTable.delete({2,2}..{*,*})
MyDataTable.delete({0,1}..{0,*})
```

### insert — 插入条目
向单列列表对象添加条目。`Row` 为插入位置的单元格号，同号及之后的单元格下移一位；若大于最高位置则追加到末尾（不允许条目间有空隙）。`Entry` 的数据类型须与列表对象一致。

```simtalk
MyDataList.insert(2,12.24)
```

### insertList — 插入列表内容
将列表内容插入到 DataTable 或 DataList。在 DataTable 中会删除已有数据，在 DataList 中会移动数据到其他位置。大批量数据建议改用 `copyRangeTo`（对 DataTable 更快）。

```simtalk
var lst: list [string]
lst.create
lst.insert(1,"one")
MyDataList.insertList(3,lst)
DataTable.insertList(2,2,lst)
```

### intersection — 交集
返回两个范围/列表共有的值，两者数据类型须一致。返回单列列表，值可能重复出现。

```simtalk
destination.insertList(2,1,MyDataTable.intersection(DataList))
```

### openDialog — 打开窗口
打开 `<Path>` 指定列表/表格的窗口，也适用于子表及 `table` 类型的用户定义属性。可选 `CallOpenControl` 决定是否执行 Open Control。

```simtalk
MyDataTable.openDialog
MyDataStack.openDialog(true)
```

### openDialogBox — 前置对话框
将列表对象作为对话框显示在所有窗口之前。内容以统一标准字体显示；输入前需停用 `Inherit Contents`。标题栏的关闭按钮被禁用，须通过 OK 或 Cancel 关闭。可选 `AutoSizeColumns` 自动调整列宽（适用于 DataTable）。

```simtalk
MyDataTable.openDialogBox
MyDataList.openDialogBox
```

### printList — 打印
打印列表内容，不含图标及来源/类信息，与点击 List 选项卡的 Print 效果一致。

```simtalk
MyDataQueue.printList
MyTimeSequence.printList
```

### refillDialog — 刷新对话框
用当前值填充已打开的对话框，适合通过信息流修改值后更新对话框显示；若以常规列表窗口打开，则重计算公式。未应用的对话框修改会被丢弃。

```simtalk
MyDataTable.refillDialog
```

### showPrintDialog — 打印对话框
打开 Windows 默认打印机的打印对话框。

```simtalk
MyTimeSequence.showPrintDialog
```

## 相关方法

列表和表格还提供用于调整单元格顺序的方法（参见目录中 "Methods for the Order of Cells within Lists and Tables"）。
