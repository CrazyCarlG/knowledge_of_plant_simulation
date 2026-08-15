# Operating System Functions（操作系统函数）

本目录汇总了 Plant Simulation 中 SimTalk 提供的一组**预定义操作系统函数**，用于在控制逻辑中访问操作系统的功能。

> 说明：本目录下的 `operating-system.md`（格式化版）与 `operating-system.txtx`（帮助原文）内容一致，均描述同一组共 **20 个函数**。以下为对其内容的总结。

## 概述

Plant Simulation 提供不依赖具体对象的通用预定义函数。SimTalk 通过下表所列函数访问操作系统（主要是 MS Windows）的能力，包括：

- 系统信息查询（内存、进程、目录、环境变量、注册表、系统文件夹）
- 文件/目录操作（复制文件、列出文件、选择文件对话框）
- 剪贴板操作（复制对象、复制文本、读取文本）
- 外部进程与系统命令（启动外部程序、执行系统命令）
- 运行控制（延时、代码页设置）

> **安全提示**：部分函数（`copyFile`、`setCurrentDirectory`、`setEnv`、`startExtProc`、`system`）受安全设置 *File > Model Settings > General > Prohibit Access to the Computer* 约束。启用该设置后，这些函数会被限制或禁止执行并报错。

---

## 函数索引

| # | 函数 | 语法 | 返回值 | 功能 |
|---|------|------|--------|------|
| 1 | `availableMemory` | `availableMemory → real` | real | 返回可用主内存总量（MB） |
| 2 | `browseForFolder` | `browseForFolder(Message:string) → string` | string | 打开文件夹选择/新建对话框 |
| 3 | `copyFile` | `copyFile(Source:string, Destination:string) → boolean` | boolean | 复制文件到指定位置 |
| 4 | `copyObjectsToClipboard` | `copyObjectsToClipboard(Objects:object/object[])` | — | 复制对象到内部剪贴板 |
| 5 | `copyTextToClipboard` | `copyTextToClipboard(TextToBeCopied:string)` | — | 复制文本到剪贴板 |
| 6 | `getApplicationProcessID` | `getApplicationProcessID → integer` | integer | 返回当前会话的进程标识（PID） |
| 7 | `getCurrentDirectory` | `getCurrentDirectory → string` | string | 返回当前工作文件夹 |
| 8 | `getEnv` | `getEnv(EnvironmentVariable:string) → string` | string | 返回指定的环境变量 |
| 9 | `getFilesOfFolder` | `getFilesOfFolder(SearchPattern:string) → list` | list | 列出匹配搜索模式的文件/文件夹 |
| 10 | `getRegistry` | `getRegistry(Key:string, Value:string)` | void/integer/string | 读取 Windows 注册表键值 |
| 11 | `getTextFromClipboard` | `getTextFromClipboard → string` | string | 从剪贴板读取文本 |
| 12 | `selectFileForOpen` | `selectFileForOpen([FileFilter:string[, PredefinedName:string]]) → string` | string | 打开"打开文件"对话框 |
| 13 | `selectFileForSave` | `selectFileForSave([FileFilter:string[, PredefinedName:string]]) → string` | string | 打开"另存为"对话框 |
| 14 | `setCodePage` | `setCodePage([CodePageName:integer])` | integer | 设置 ANSI 数据交换的代码页 |
| 15 | `setCurrentDirectory` | `setCurrentDirectory(WorkingFolder:string) → boolean` | boolean | 设置当前工作文件夹 |
| 16 | `setEnv` | `setEnv(EnvironmentVariable:string, Value:string) → boolean` | boolean | 设置环境变量 |
| 17 | `SHGetKnownFolderPath` | `SHGetKnownFolderPath(CLSID:string) → string` | string | 返回系统标准文件夹路径 |
| 18 | `sleep` | `sleep(Time:real[, SuspendProcess:boolean:=true])` | — | 按真实时间挂起 Method |
| 19 | `startExtProc` | `startExtProc(PathToProgram:string[, Visible:boolean, WaitUntilProcessTerminated:boolean]) → integer` | integer | 启动外部进程 |
| 20 | `system` | `system(Command:string) → integer` | integer | 执行系统命令（模拟运行期间） |

---

## 分组详解

### 1. 系统信息查询

- **`availableMemory`** — 返回主内存总量（MB），数据类型 `real`。
- **`getApplicationProcessID`** — 返回当前 Plant Simulation 会话的进程标识（PID），数据类型 `integer`。
- **`getCurrentDirectory`** — 返回当前工作文件夹，数据类型 `string`。
- **`getEnv(EnvironmentVariable)`** — 返回指定环境变量；变量不存在时返回空字符串 `""`。
- **`getRegistry(Key, Value)`** — 从 `HKEY_CLASSES_ROOT`、`HKEY_CURRENT_USER`、`HKEY_LOCAL_MACHINE` 读取注册表键值。返回值类型取决于键值类型：`void`（不存在）、`integer`（REG_DWORD）、`string`（其余类型）。
- **`SHGetKnownFolderPath(CLSID)`** — 返回系统标准文件夹路径（如桌面），CLSID 参考 KNOWNFOLDERID。

### 2. 文件与目录操作

- **`copyFile(Source, Destination)`** — 复制文件，成功返回 `true`，失败返回 `false`。受安全设置约束。
- **`getFilesOfFolder(SearchPattern)`** — 返回匹配模式的文件/文件夹列表；`*` 表示任意字符串，`?` 表示单个字符。
- **`selectFileForOpen`** — 打开"打开"对话框；返回所选文件路径字符串，点击取消返回 `""`。支持 Microsoft 风格的文件过滤器（`Comment1|Filter1|Comment2|Filter2||`）及可选的默认路径 `PredefinedName`。
- **`selectFileForSave`** — 打开"另存为"对话框；返回文件保存路径，点击取消返回 `""`。参数同 `selectFileForOpen`，`PredefinedName` 作为预填文件名。
- **`setCurrentDirectory(WorkingFolder)`** — 设置工作文件夹，成功返回 `true`。受安全设置约束。
- **`browseForFolder(Message)`** — 打开 Windows 文件夹选择/新建对话框，返回所选文件夹。

### 3. 剪贴板操作

- **`copyObjectsToClipboard(Objects)`** — 将单个或多个对象复制到 Plant Simulation 内部剪贴板；复制会清空剪贴板旧内容。连接器（Connector）需连同其前驱/后继对象一起复制才能成功。
- **`copyTextToClipboard(TextToBeCopied)`** — 复制文本到剪贴板；复制会清空旧内容。
- **`getTextFromClipboard`** — 从剪贴板读取文本并作为字符串返回。

### 4. 外部进程与系统命令

- **`startExtProc(PathToProgram[, Visible, WaitUntilProcessTerminated])`** — 启动外部进程（通常是带图形界面的程序），返回 PID，失败返回 `0`。路径分隔符用双反斜杠 `\\`。可控制窗口是否可见、是否等待进程结束。受安全设置约束。
- **`system(Command)`** — 执行系统命令（仅限 DOS 命令），执行期间 Plant Simulation 被阻塞；返回值为命令退出状态。带图形界面的程序应改用 `startExtProc`。受安全设置约束。

### 5. 运行控制与配置

- **`sleep(Time[, SuspendProcess:=true])`** — 按**真实时间**（而非仿真时间）挂起 Method。`SuspendProcess=true` 时挂起整个 Plant Simulation 进程以节省 CPU；`false` 时仅停止执行当前 Method（类似 `wait`，但 `wait` 用的是仿真时间）。
- **`setCodePage([CodePageName])`** — 设置 ANSI 数据交换的代码页（如 932 日文、936 中文、1250 匈牙利、1252 英/德、0 为操作系统代码页），返回设置前的旧代码页。
- **`setEnv(EnvironmentVariable, Value)`** — 设置环境变量，返回 `boolean`。受安全设置约束，启用时会被禁止并报错。

---

## 相关主题

- 安全设置：*File > Model Settings > General > Prohibit Access to the Computer*
- 相关函数：`pasteClipboard`（Frame）、`getTextFromClipboard` / `copyTextToClipboard`、`system` / `startExtProc` / `getApplicationProcessID`、`getCurrentDirectory` / `setCurrentDirectory`、`getEnv` / `setEnv`、`sleep` / `wait`
- 启动选项：`-cwd dir`、`/Codepage`
- 外部参考：KNOWNFOLDERID（https://docs.microsoft.com/en-us/windows/win32/shell/knownfolderid）
