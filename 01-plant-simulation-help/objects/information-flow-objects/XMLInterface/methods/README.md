# XMLInterface 方法总结（Methods of the XML Interface）

本目录用于存放 **XMLInterface** 对象的方法文档。目录内的文档来源如下：

- `methods.md`：XMLInterface 方法的 Markdown 版本（主要文档）。
- `methods.txtx`：对应的原始导出文本，内容与 `methods.md` 基本一致。

> 说明：本目录下没有子文件夹，因此不存在子文件夹中的 `README.md`。

---

## 概述

XMLInterface 对象用于在 Plant Simulation 中读写 XML 文件。它提供了：

- 本目录文档所列出的方法（详见下文）。
- 所有对象通用的方法（Methods of All Objects）。

可通过 **Show Attributes and Methods** 窗口查看对象的所有方法、只读属性和属性（在 Class Library 的上下文菜单中选择，或在 Frame 的 Home 标签页按 **F8** / 点击 **Show Attributes and Methods**）。

### 语法行约定

示例：`<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean`

- `<Path>`：方法所作用对象的路径。
- 括号内为签名（参数标识符 + 数据类型），如 `(Parameter:string)`。
- 方括号 `[,Parameter:boolean]` 表示可选参数。
- `:= false` 表示参数的默认值。
- 箭头 `→ boolean` 表示返回值的数据类型。

---

## 访问模式

XMLInterface 的方法按数据访问方式可分为三类：

1. **顺序访问（Sequential access）**
   - 写：`openWrite` → `startElement` / `addAttribute` / `writeElement` / `endElement` → `close`
   - 读：`openRead`（会调用导入方法 Import Method）→ `close`

2. **随机访问（Random access，基于 XPath）**
   - `openDocument`、`newDocument`、`setContext`、`getNodes`、`selectNodes`、`getContainer`、`insertNodes`、`updateNodes`、`deleteNodes`

3. **随机遍历（Random traversal）**
   - `selectChildren`、`getNextNode`、`getNodeName`、`getNodeValue`、`getAttributeName`、`getAttributeValue`、`closeChildren`

---

## 方法速查表

| 方法 | 语法 | 返回值 | 访问方式 |
| --- | --- | --- | --- |
| `addAttribute` | `<Path>.addAttribute(Name:string, Value:string)` | boolean | 顺序访问 |
| `close` | `<Path>.close` | boolean | 通用 |
| `closeChildren` | `<Path>.closeChildren` | boolean | 随机遍历 |
| `deleteNodes` | `<Path>.deleteNodes(Instruction:string)` | boolean | 随机访问 |
| `endElement` | `<Path>.endElement` | boolean | 顺序访问 |
| `getAttributeName` | `<Path>.getAttributeName(Position:integer)` | string | 随机遍历 |
| `getAttributeValue` | `<Path>.getAttributeValue(Parameter:any)` | string | 随机遍历 |
| `getContainer` | `<Path>.getContainer(Depth:integer)` | table | 随机访问 |
| `getNextNode` | `<Path>.getNextNode` | boolean | 随机遍历 |
| `getNodeName` | `<Path>.getNodeName` | string | 随机遍历 |
| `getNodes` | `<Path>.getNodes(Instruction:string, NumberOfLevels:integer)` | table | 随机访问 |
| `getNodeValue` | `<Path>.getNodeValue` | string | 随机遍历 |
| `insertNodes` | `<Path>.insertNodes(NodesTable:list)` | boolean | 随机访问 |
| `newDocument` | `<Path>.newDocument(Name:string)` | boolean | 随机访问 |
| `openDocument` | `<Path>.openDocument` | boolean | 随机访问 |
| `openRead` | `<Path>.openRead` | boolean | 顺序访问（读） |
| `openWrite` | `<Path>.openWrite` | boolean | 顺序访问（写） |
| `remove` | `<Path>.remove` | boolean | 通用 |
| `selectChildren` | `<Path>.selectChildren` | boolean | 随机遍历 |
| `selectNodes` | `<Path>.selectNodes(Instruction:string)` | boolean | 随机遍历 |
| `setContext` | `<Path>.setContext(Node:string)` | boolean | 随机访问 |
| `startElement` | `<Path>.startElement(Element:string)` | boolean | 顺序访问 |
| `updateNodes` | `<Path>.updateNodes(NodesTable:list)` | boolean | 随机访问 |
| `write` | `<Path>.write` | boolean | 通用 |
| `writeElement` | `<Path>.writeElement(Name:string, Value:string)` | boolean | 顺序访问 |

---

## 方法说明摘要

### 顺序访问（Sequential access）

- **`openRead`**：打开 XML 文件进行顺序读取；会为文件中包含的所有对象调用导入方法（Import Method）。
- **`openWrite`**：打开 XML 文件进行顺序写入；以 UTF-8 编码写入（仅使用 ASCII 字符时可按 ASCII 文件处理）。
- **`startElement(Element:string)`**：标记指定元素的开始。
- **`addAttribute(Name:string, Value:string)`**：向 XML 文件添加新属性。
- **`writeElement(Name:string, Value:string)`**：写入元素并同时关闭它。
- **`endElement`**：终止由 `startElement` 开始的元素。
- **`close`**：关闭 XML 文件。

### 随机访问（Random access，基于 XPath）

- **`openDocument`**：打开 XML 文件，将数据读入 RAM，供随机访问使用。
- **`newDocument(Name:string)`**：在 RAM 中创建一个新的空 XML 文档。
- **`setContext(Node:string)`**：设置读取上下文节点，可限制要读取的数据范围，避免导入整个文件（节省时间与内存）。
- **`getNodes(Instruction:string, NumberOfLevels:integer)`**：返回 XPath 指令所选的所有节点（结果存入 table）。
- **`selectNodes(Instruction:string)`**：选择 XPath 指令所指定的节点。
- **`getContainer(Depth:integer)`**：返回一个预格式化的 table，作为要写入数据的容器。
- **`insertNodes(NodesTable:list)`**：将 table 中包含的节点插入 XMLInterface。
- **`updateNodes(NodesTable:list)`**：更新由 `getNodes` 选出的节点，并把它们写入 table（可修改 table 后再更新）。
- **`deleteNodes(Instruction:string)`**：删除通过 XPath 指令选中的所有节点。

### 随机遍历（Random traversal）

- **`selectChildren`**：选择活动节点的所有子节点。
- **`getNextNode`**：返回 `selectChildren` 之后位于活动层级上的下一个节点。
- **`getNodeName`**：返回活动层级上节点的名称。
- **`getNodeValue`**：返回活动层级上节点的值。
- **`getAttributeName(Position:integer)`**：返回指定位置的属性名称。
- **`getAttributeValue(Parameter:any)`**：返回指定属性的值。
- **`closeChildren`**：关闭当前子节点层级，返回结构中的上一级。

---

## 只读属性

- **`GetNumberAttributes`**：获取属性数量（只读，不可设置）。查询示例：`print MyXMLInterface.GetNumberAttributes`。

---

## 相关引用

- **Import Method [XML Interface]**：由 `openRead` 调用，用于顺序读取时导入 XML 文件中的对象。
- **Delete File [XML Interface]**：`remove` 方法的关联说明。
- **getNodes [SimTalk]**：`updateNodes` 的关联说明。
