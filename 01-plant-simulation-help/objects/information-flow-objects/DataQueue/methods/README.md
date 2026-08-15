# DataQueue / DataStack 方法（Methods）总结

本目录汇总了 **DataQueue** 与 **DataStack** 对象的方法说明。完整内容见 `methods.md`（原始导出文本为 `methods.txtx`）。

## 概述

- 本页记录 DataQueue 和 DataStack 对象的方法。
- 其他方法可参考：
  - The Methods of Lists and Tables（列表与表格的方法）
  - The Methods of All Objects（所有对象的方法）
- 查看对象的全部方法、只读属性和属性：
  - 在 **Class Library** 的上下文菜单中选择 **Show Attributes and Methods** 查看所选类；
  - 按 **F8** 键，或点击 Frame 首页选项卡上的 **Show Attributes and Methods** 查看所选实例。

## 方法语法行阅读说明

示例：`<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean`

- `<Path>`：方法所作用的对象路径。
- 括号内为方法签名（参数标识符与数据类型），如 `(Parameter:string)`。
- 方括号 `[...]` 表示可选参数。
- 参数后若带默认值，则显示默认值。
- 箭头 `->` 后为返回值的数据类型。
- 注意：表达式内部的括号 `(…)` 必须输入，否则可能导致意外结果并打开调试器（Debugger）。

签名中使用的数据类型缩写：

| 参数数据类型 | 数据类型 | 取值范围 |
|---|---|---|
| integer | integer | 大于零的整数 |
| any | 所有数据类型 | 取决于数据类型 |
| listrange | — | 一个范围 |
| direction | string | "up"、"down"、" " |
| attributes | string | 属性名 |

## 方法列表

### createNestedList [SimTalk] - DataQueue
在 `<Path>` 指定的 DataStack 或 DataQueue 中创建一个嵌套列表。

- **类型**：方法
- **语法**：`<Path>.createNestedList([Name:string]) → list`
- **参数**：可选参数 `Name`（string）指定要创建的列表名称。
- **返回值**：`list` —— 创建的嵌套列表（DataList、DataQueue、DataStack 或 DataTable）。
- **备注**：DataStack/DataQueue 的数据类型必须为 `list`、`stack`、`queue` 或 `table`；已有条目向下移动一位；若指定索引大于最大有效索引，则放到首个可用位置以避免出现空隙。
- **示例**：`MyDataStack.createNestedList("My Sublist")`

### pop [SimTalk] - DataStack
从 `<Path>` 指定的单列列表中移除第一个单元格。

- **类型**：方法
- **语法**：`<Path>.pop`
- **返回值**：与 DataStack/DataQueue 数据类型一致。
- **备注**：DataStack 和 DataQueue 按各自内置属性删除条目。
- **示例**：
  ```
  value := MyDataStack.pop   -- 移除 MyDataStack 的第一个单元格
  value := MyDataQueue.pop   -- 移除 MyDataQueue 的最后一个单元格
  ```

### push [SimTalk] - Stack
在 `<Path>` 指定的单列列表的第一个位置添加指定单元格。

- **类型**：方法
- **语法**：`<Path>.push(Cell:any)`
- **参数**：`Cell`（any）指定单元格。
- **备注**：DataStack 和 DataQueue 按各自内置属性添加条目。
- **示例**：
  ```
  MyDataStack.push("bottles")  -- 将字符串 bottles 作为第一个单元格加入 DataStack
  MyDataQueue.push("cans")     -- 将字符串 cans 作为最后一个单元格加入 DataQueue
  ```
- **参见**：`pop [SimTalk] - DataStack`

### pushList [SimTalk]
将参数指定的列表放入 `<Path>` 指定的 DataStack 或 DataQueue。

- **类型**：方法
- **语法**：`<Path>.pushList(List:any)`
- **参数**：`List`（any）必须引用 `stack`、`queue`、`list` 或单列 `table` 类型的列表。
  - 只想放入列表的一部分时使用 `copy` 方法。
  - 插入数据的类型须与目标 DataStack/DataQueue 的数据类型一致。
- **示例**：
  ```
  // 将 DataList 的内容粘贴到 DataStack 中
  MyDataStack.pushList(MyDataList.copy)
  // 将从单元格 4 开始的指定范围粘贴到 DataQueue 中
  MyDataQueue.pushList(MyDataList.copy({4}..{*}))
  ```

### top [SimTalk]
读取单列列表中某个单元格的内容，但不删除它。

- **类型**：方法
- **语法**：`<Path>.top`
- **备注**：DataStack 和 DataQueue 根据各自内置属性决定单元格位置。
- **示例**：`print MyDataStack.top`

## 只读属性（Read-Only Attributes）

DataStack 和 DataQueue 提供：
- The _Read-Only Attributes of Lists and Tables（列表与表格的只读属性）
- The _Read-Only Attributes of All Objects（所有对象的只读属性）

只读属性的值只能查询，不能设置；Plant Simulation 在查询时计算其当前值。多数只读属性对应对象某个选项卡上不可用的对话框项，例如 **Statistics** 选项卡。
