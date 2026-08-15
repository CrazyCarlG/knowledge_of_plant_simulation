# README — Station Methods

本目录汇总了 **Station（工位）** 对象的方法（Methods）与只读属性（Read-Only Attributes）的帮助内容。

## 内容来源

目录内包含以下文件：

- `methods.md` — 方法页面的 Markdown 版总结（本 README 的依据）。
- `methods.txtx` — 从 Plant Simulation 帮助 PDF 提取的原始文本。
- `Plant-Simulation-Help2606_4647-4648.pdf` — 帮助文档原文（第 11-1717 至 11-1718 页）。

## 核心要点

### 方法（Methods）

Station 对象提供以下方法：

- **所有对象的方法（The Methods of All Objects）**
- **物流对象的方法（The Methods of the Material Flow Objects）**

查看全部方法、只读属性与属性：打开 **Show Attributes and Methods（显示属性与方法）** 窗口。

- 在 **类库（Class Library）** 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选 **类（Class）** 的方法、只读属性与属性。
- 在插入了实例的 Frame 中，按 **F8** 键或点击 **Home** 功能区选项卡上的 **Show Attributes and Methods**，可显示所选 **实例（Instance）** 的方法、只读属性与属性。

### 语法行（Syntax Line）约定

单个方法的语法行示例：

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>`：方法所作用的对象的路径。
- 括号内为方法签名（参数标识符 + 数据类型），如 `(Parameter:string)` 表示字符串类型参数；参数既可为常量，也可为所需类型的变量或返回该类型的方法。
- 方括号内为可选参数，如 `[,Parameter:boolean]` 表示布尔参数可省略。
- 参数默认值以 `:=` 标注，如 `:= false`。
- 返回值类型标注在箭头 `→` 之后，如 `→ boolean`。

> **注意**：表达式内部嵌套的括号 `(…)` 必须输入，否则可能导致意外结果并打开调试器（Debugger）。

### 只读属性（Read-Only Attributes）

Station 对象提供：

- **所有对象的只读属性（The Read-Only Attributes of All Objects）**
- **物流对象的只读属性（The Read-Only Attributes of the Material Flow Objects）**

只读属性的值由 Plant Simulation 在查询时刻计算，因此只能查询、不能设置。多数只读属性对应对象选项卡（例如 **Statistics** 选项卡）上不可编辑的对话框项。

---

*来源：Plant Simulation Help。未发表作品。© 2026 Siemens*
