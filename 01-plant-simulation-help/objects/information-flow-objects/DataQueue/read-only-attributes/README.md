# Read-Only Attributes（只读属性）— DataQueue 与 DataStack

本目录汇总了 **DataQueue** 与 **DataStack** 的只读属性（Read-Only Attributes）相关文档。目录内包含 `read-only-attributes.md` 与 `read-only-attributes.txtx`，两者内容一致；无子文件夹及子 README。

## 1. `top` [SimTalk]

**功能**：读取单列列表（list）中某个单元格的内容，但**不移除**该内容。

- **备注（Remarks）**：由 `<Path>` 指定的 DataStack 或 DataQueue 会根据其内建属性决定单元格的位置。
- **类型（Type）**：Method（方法）
- **语法（Syntax）**：
  ```
  <Path>.top
  ```
- **示例（Example）**：
  ```simtalk
  print MyDataStack.top
  ```

## 2. DataQueue 与 DataStack 的只读属性

DataStack 与 DataQueue 提供以下只读属性：

- 列表与表格（Lists and Tables）的只读属性
- 所有对象（All Objects）的只读属性

**说明**：
- 只读属性的值**只能查询，不能设置**，因为 Plant Simulation 会在查询的时间点计算该值。
- 大多数情况下，只读属性对应于对象某个选项卡上不可用的对话框项，例如 **Statistics（统计）** 选项卡。

**查看方法**：要查看对象的全部方法、只读属性与属性，打开 **Show Attributes and Methods** 窗口：

- 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选 Class 的方法、只读属性与属性。
- 在插入实例的 Frame 上按 **F8** 键，或点击 Home 功能区选项卡中的 **Show Attributes and Methods**，可显示所选 Instance 的方法、只读属性与属性。

**查询示例**：
```simtalk
print MyDataStack.Full
```

## 3. DataQueue 与 DataStack 的属性（Attributes）

DataStack 与 DataQueue 提供以下属性：

- 列表与表格（Lists and Tables）的属性
- 所有对象（All Objects）的属性

同样可通过 **Show Attributes and Methods** 窗口查看对象的所有方法、只读属性与属性。
