# Miscellaneous Global Functions (N–Z) — 摘要

本目录汇总了 Plant Simulation SimTalk 中 **N–Z** 开头的全局函数（Miscellaneous Global Functions），共 **32 个函数**。这些函数覆盖了对象计数、对话框与选择框、控制台、HTML 浏览器、性能分析（Profiler）、时间测量、文件读写、随机数、模型保存、邮件发送、MU 追踪、Python 环境、统计报告、哈希、错误处理以及界面语言等多个应用领域。

> 数据来源：`n-to-z.md`（Plant Simulation Help，Miscellaneous Global Functions, N–Z）。

---

## 函数总览（按类别分组）

### 1. 对象计数

| 函数 | 语法 | 说明 |
|------|------|------|
| `numOfLimitedObjects` | `numOfLimitedObjects → integer` | 统计整个模型中所有内置对象的数量（用于 Standard License 4000 对象限制） |

### 2. 对话框与选择框

| 函数 | 语法 | 说明 |
|------|------|------|
| `openColorSelectBox` | `openColorSelectBox(Color:integer) → integer` | 打开 Windows 颜色选择对话框，返回用户选择的 RGB 颜色值 |
| `openDateSelectBox` | `openDateSelectBox(TitleText:string[, InitialDate:date]) → date` | 打开日期选择对话框，返回用户选择的日期 |
| `openObjectSelectBox` | `openObjectSelectBox(Filter:string, FrameOrFolder:object) → string` | 打开“选择对象”对话框，可按类型过滤对象 |

### 3. 控制台

| 函数 | 语法 | 说明 |
|------|------|------|
| `openConsole` | `openConsole → boolean` | 打开控制台窗口 |
| `setConsoleFilter` | `setConsoleFilter(Filter:string, Activate:boolean) → boolean` | 设置是否激活指定的控制台过滤器（`Info`/`Message`/`Print`/`Debug`） |

### 4. HTML 浏览器 / 窗口

| 函数 | 语法 | 说明 |
|------|------|------|
| `openHTMLBrowser` | `openHTMLBrowser(WWWAddress:string) → string` | 启动 HTML 浏览器并打开指定地址 |
| `openHTMLWindow` | `openHTMLWindow(Address:string, WindowTitle:string, X:integer, Y:integer, Width:integer, Height:integer) → boolean` | 打开无常规浏览器属性的浏览器窗口（可显示 PDF） |

### 5. 时间与性能（Profiler）

| 函数 | 语法 | 说明 |
|------|------|------|
| `processTime` | `processTime → real` | 返回 Plant Simulation 已使用的 CPU 时间（秒，毫秒级分辨率） |
| `profiler` | `profiler(Activate:boolean)` | 激活/停用 Profiler，持续收集方法调用频率与运行时间 |
| `resetProfile` | `resetProfile` | 删除 Profiler 收集的所有数据 |
| `saveProfile` | `saveProfile(FileName:string[, IncludeTop50CallCycles:boolean]) → boolean` | 将 Profiler 数据保存到文件（覆盖已有内容） |
| `updateGUI` | `updateGUI([forceUpdateNow:boolean:=false]) → integer` | 刷新图形界面，防止长方法执行时程序看似无响应 |
| `setInfiniteLoopDetectionTimeout` | `setInfiniteLoopDetectionTimeout(Timeout:integer) → integer` | 设置方法执行多久后弹出可停止执行（Shift+Alt+Ctrl）的提示 |

### 6. 属性值

| 函数 | 语法 | 说明 |
|------|------|------|
| `putValuesIntoTable` | `putValuesIntoTable(TargetTable:table)` | 将字符串属性（仅能取预定义值）的所有取值写入表格 |

### 7. 数学

| 函数 | 语法 | 说明 |
|------|------|------|
| `rad2deg` | `rad2deg(AngleInRadians:real) → real` | 将弧度转换为角度 |
| `setEpsilon` | `setEpsilon(Value:real) → real` | 设置数值被视为“约相等”的阈值（配合 `~=` 比较） |

### 8. 文件读写

| 函数 | 语法 | 说明 |
|------|------|------|
| `readStringFromFile` | `readStringFromFile(FileName:string) → string` | 读取整个文件内容并作为字符串返回（自动处理 BOM） |
| `writeStringToFile` | `writeStringToFile(Text:string, FileName:string[, Append:boolean, Encoding:string:="UTF-8"])` | 将文本写入文件（支持追加与编码选择） |

### 9. 随机数

| 函数 | 语法 | 说明 |
|------|------|------|
| `resetRandomNumberStream` | `resetRandomNumberStream(Stream:integer)` | 重置分布函数（如 `z_uniform`、`z_normal`）的随机数流 |
| `setAntitheticRandomNumbers` | `setAntitheticRandomNumbers(AntitheticRandomNumbers:boolean) → boolean` | 设置是否使用对偶随机数 |
| `setRandomSeedCounter` | `setRandomSeedCounter(CounterValue:integer) → integer` | 影响随机数种子值的自动分配（`0` 仅查询当前计数器） |
| `setSeedTable` | `setSeedTable(SeedTable:table)` | 设置随机数种子表以创建随机数流 |

### 10. 模型保存

| 函数 | 语法 | 说明 |
|------|------|------|
| `saveFolderModel` | `saveFolderModel(FileName:string[, CompactFormat:boolean:=false, UseGit:boolean:=false])` | 以文件夹/文件结构保存模型，便于使用 Git 等版本控制 |
| `saveModel` | `saveModel(ModelName:string[, StopMethodExecution:boolean[, UseNewName:boolean[, SaveCallChains:boolean]]]) → boolean` | 以指定文件名保存当前模型 |

### 11. 邮件

| 函数 | 语法 | 说明 |
|------|------|------|
| `sendSMTPMail` | `sendSMTPMail(Mail-Server:string, Receiver:string, Subject:string, MessageText:string)` | 通过指定邮件服务器发送电子邮件 |

### 12. MU 追踪

| 函数 | 语法 | 说明 |
|------|------|------|
| `setMUTraceRouteMethod` | `setMUTraceRouteMethod(&Method:object) → object` / `setMUTraceRouteMethod([array_of_Methods:any]) → object` | 指定 MU 每次移动到另一对象时调用的 Method（或其数组） |

### 13. Python 环境

| 函数 | 语法 | 说明 |
|------|------|------|
| `setPythonDLLPath` | `setPythonDLLPath(dllpath:string)` | 指定要使用的 Python 安装路径（支持 3.12 / 3.13 / 3.14） |

### 14. 统计报告

| 函数 | 语法 | 说明 |
|------|------|------|
| `showStatisticsReport` | `showStatisticsReport(List:list[, FileName:string])` | 显示列表中对象的统计报告（可写入文件） |

### 15. 哈希

| 函数 | 语法 | 说明 |
|------|------|------|
| `strHash` | `strHash(string) → integer` | 计算传入字符串的哈希值（0 至 2147483647，区分大小写） |

### 16. 错误处理

| 函数 | 语法 | 说明 |
|------|------|------|
| `throwRuntimeError` | `throwRuntimeError(ErrorMessage:string)` | 向调用 Method 返回错误消息并触发调试器或错误处理 |

### 17. 界面语言

| 函数 | 语法 | 说明 |
|------|------|------|
| `userInterfaceLanguage` | `userInterfaceLanguage → integer` | 返回用户界面语言（`0` 德语 / `1` 英语 / `2` 日语 / `3` 中文 / `8` 匈牙利语） |

---

## 重点函数说明

### 模型保存（`saveFolderModel` / `saveModel`）

- `saveFolderModel` 以文件夹/文件结构保存模型，便于版本控制：
  - `CompactFormat`（默认 `false`）：为 `true` 时将 Frame 内有原点的对象保存为独立 `.yaml` 文件；为 `false` 时全部对象保存进 Frame 的 `$.yaml`（文件更少，大模型性能更好）。
  - `UseGit`（默认 `false`）：为 `true` 时首次保存自动创建 Git 仓库并提交初始版本，同时生成 `.gitignore`（需已安装 Git）。
  - 注册表键 `FolderModelCommitCommand` 可设置在保存时调用的提交命令（默认启动 TortoiseGit；设为空字符串 `""` 则不打开提交对话框）。
- `saveModel` 支持可选参数：`StopMethodExecution`（加载后停止方法执行并打开调试器）、`UseNewName`（是否采用新文件名，默认 `true`）、`SaveCallChains`（是否保存调用链，默认 `true`）。

### 随机数（`resetRandomNumberStream` / `setAntitheticRandomNumbers` / `setRandomSeedCounter` / `setSeedTable`）

- 这些函数作用于分布函数（如 `z_uniform`、`z_normal`）使用的随机数流；每个物流对象自身的随机数流由属性 `RandomSeed` 设置，不通过 `resetRandomNumberStream` 访问。
- `setSeedTable` 接受一列（种子值）或两列（种子值 + 注释）的表格，行号对应随机数流编号，并立即重置所有随机数流。
- `setRandomSeedCounter(0)` 仅查询当前计数器；非零值设置计数器，常用于自动创建模型时保持种子值一致。

### 哈希（`strHash`）

- 哈希值位于 `0` 至 `2147483647`（含边界），区分大小写（可用 `strToLower` 先转小写）。
- 非双射（不可唯一逆推）；定位后仍需比较原字符串。构建哈希表时通常使用 `strHash(...) mod N + 1` 将值映射到较小范围。

### 错误处理（`throwRuntimeError`）

- 通常在库方法中对非法参数值报错；也可在库外使用。
- 触发后打开调用 Method 的调试器（加密方法则弹出消息框）；若调用链中存在 `ErrorHandler`，则优先调用错误处理方法（由内向外查找，最终回退到全局错误处理器）。

### HTML 浏览器安全（`openHTMLBrowser` / `openHTMLWindow`）

- 受“禁止访问计算机”安全设置影响：仅允许 `http`、`https`、`file`、UNC 路径及普通文件系统路径；不许可可执行文件（扩展名列于 `PATH_EXT`）；文件路径仅限模型文件夹及其子文件夹。
- `openHTMLWindow` 在装有 Microsoft Edge WebView2 Runtime 时可直接显示 PDF 文档。

---

*Source: Plant Simulation Help（Miscellaneous Global Functions, N–Z），详见同目录 `n-to-z.md`。*
