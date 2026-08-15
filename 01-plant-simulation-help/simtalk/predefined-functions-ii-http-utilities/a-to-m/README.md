# Miscellaneous Global Functions (A–M) — 摘要

本目录汇总了 Plant Simulation SimTalk 中 **A–M** 开头的全局函数（Miscellaneous Global Functions），共 **56 个函数**。这些函数覆盖了应用程序/系统控制、模型与文件管理、窗口与交互、仿真运行时、数学与几何计算、对象存在性检查、哈希与安全、颜色等多个应用领域。

> 数据来源：`a-to-m.md`（Plant Simulation Help，Miscellaneous Global Functions, A–M）。

---

## 函数总览（按类别分组）

### 1. 应用程序 / 系统

| 函数 | 语法 | 说明 |
|------|------|------|
| `applicationHome` | `applicationHome → string` | 返回 Plant Simulation 安装目录 |
| `applicationVersion` | `applicationVersion → integer` | 返回版本号（`VVMMMPPP` 编码） |
| `exitApplication` | `exitApplication` | 结束仿真运行并退出 Plant Simulation（不保存） |
| `language` | `language → integer` | 返回模型语言（0 德语 / 1 英语 / 2 日语 / 3 中文 / 8 匈牙利语） |
| `licenseName` | `licenseName → string` | 返回当前激活的许可证名称（如 `EMPLANT_PRO`） |
| `checkForLicense` | `checkForLicense(Feature, Version, PasswordHash) → integer` | 检查用户自定义许可证是否可用（返回 0–7 状态码） |
| `createLicenseFile` | `createLicenseFile(...) → string` | 生成用户自定义许可证并写入注册表文件，返回密码的 SHA-1 哈希 |
| `getCommandLineArg` | `getCommandLineArg(Arg, byref Value) → boolean` | 查询启动 Plant Simulation 时传入的命令行参数 |
| `hideBBL` | `hideBBL(Minimize[, Hide]) → boolean` | 将 Plant Simulation 最小化到任务栏状态区 |
| `keepWindowsAlwaysOnTop` | `keepWindowsAlwaysOnTop(boolean)` | 设置窗口是否总在最前 |
| `enableFullScreenMode` | `enableFullScreenMode(Activate)` | 激活/取消全屏模式 |
| `isComputerAccessPermitted` | `isComputerAccessPermitted → boolean` | 检查当前 Method 是否被允许访问计算机 |

### 2. 模型与文件管理

| 函数 | 语法 | 说明 |
|------|------|------|
| `loadModel` | `loadModel(ModelName[, Password]) → boolean` | 加载指定仿真模型（需先关闭当前模型） |
| `closeModel` | `closeModel → boolean` | 关闭当前模型（不保存；可配合 `onCloseModel` 清理） |
| `modelFile` | `modelFile → string` | 返回当前模型文件的路径 |
| `existsFile` | `existsFile(Name) → boolean` | 判断文件或文件夹是否存在 |
| `deleteFile` | `deleteFile(FileName) → integer` | 永久删除指定文件（返回错误码） |
| `getFileModificationDateTime` | `getFileModificationDateTime(FilePath) → dateTime` | 返回文件最后写入的日期时间 |
| `makePathRelative` | `makePathRelative(Path[, StartObject]) → string` | 将绝对路径转换为相对路径 |
| `getLogFile` | `getLogFile → string` | 获取写入控制台消息的日志文件 |
| `clearLogFile` | `clearLogFile → boolean` | 清空日志文件内容（不删除文件本身） |
| `getLibrariesDirectories` | `getLibrariesDirectories → string[]` | 返回首选项中设置的库目录 |
| `getLibraryFiles` | `getLibraryFiles(FolderPath) → string[]` | 返回 `.pslib` 文件路径及版本（交替排列） |
| `getLibraryVersionFromFile` | `getLibraryVersionFromFile(FilePath) → string` | 返回指定库文件的版本 |

### 3. 窗口与交互

| 函数 | 语法 | 说明 |
|------|------|------|
| `clearConsole` | `clearConsole` | 清空控制台窗口内容 |
| `closeConsole` | `closeConsole → boolean` | 关闭控制台窗口 |
| `closeAllWindows` | `closeAllWindows([Unused])` | 关闭所有打开的对象窗口（含 3D 窗口） |
| `closeHTMLWindow` | `closeHTMLWindow(Title) → boolean` | 按标题关闭之前打开的浏览器窗口 |
| `messageBox` | `messageBox(Text[, Buttons[, Icons]]) → integer` | 显示系统消息框，返回按钮结果码 |

### 4. 仿真运行时

| 函数 | 语法 | 说明 |
|------|------|------|
| `animation` | `animation([Activate]) → boolean` | 激活/取消 MU 与状态的动画显示 |
| `currentEventCtl` | `currentEventCtl → object` | 返回控制当前仿真运行的 EventController |
| `callEvery` | `callEvery(Frame, Method[, Parameters])` | 深度优先调用指定 Frame 及子 Frame 中所有同名 Method |
| `execute` | `execute(SourceCode[, Parameters])` | 将字符串当作 Method 源码解释执行（出错打开调试器） |
| `executeSilent` | `executeSilent(SourceCode[, Parameters])` | 静默执行源码（出错不打开调试器） |
| `getExecuteSilentError` | `getExecuteSilentError → string` | 返回 `executeSilent` 或公式计算后的错误消息 |
| `executePythonFile` | `executePythonFile(File) → boolean` | 执行指定 Python 文件的源码 |
| `getCallStack` | `getCallStack → list` | 返回当前调用堆栈并写入表格 |
| `getHighResolutionClock` | `getHighResolutionClock → real` | 返回自打开模型以来经过的秒数（高精度计时） |
| `getSeedTable` | `getSeedTable → table` | 返回当前随机数种子表 |
| `getEpsilon` | `getEpsilon → real` | 返回数值视为“约相等”的阈值 |
| `connectAutomatically` | `<Path>.connectAutomatically → boolean` | 自动连接附近入口/出口相邻的对象 |
| `getProfileCallCycles` | `getProfileCallCycles([Max]) → json` | 返回 Profiler 收集的调用周期（JSON） |

### 5. 数学与几何

| 函数 | 语法 | 说明 |
|------|------|------|
| `calcBrakingDistance` | `calcBrakingDistance(Speed, Deceleration) → length` | 计算制动距离（`s = ½·v²/a`） |
| `calcDroppedPerpendicularFootPoint` | `calcDroppedPerpendicularFootPoint(A1, A2, P) → length[3]` | 计算点到直线垂足坐标 |
| `deg2rad` | `deg2rad(AngleInDegrees) → real` | 角度转弧度 |
| `createCombinations` | `createCombinations(Elements[], Length) → integer[]` | 生成指定长度的所有组合 |
| `createPermutations` | `createPermutations(Elements[], Length) → integer[]` | 生成指定长度的所有排列 |

### 6. 对象 / 名称存在性检查

| 函数 | 语法 | 说明 |
|------|------|------|
| `checkID` | `checkID(Expression) → boolean` | 检查表达式能否用作对象名称 |
| `existsMethod` | `existsMethod(Name) → boolean` | 判断路径是否指向 Method 或 method 类型属性 |
| `existsObject` | `existsObject(Name) → boolean` | 判断仿真对象路径是否有效 |
| `isSet` | `<Path>.isSet(Value) → boolean` | 判断内置属性值是否被设置（与模型语言无关） |

### 7. 哈希与安全

| 函数 | 语法 | 说明 |
|------|------|------|
| `computeSHA1Hash` | `computeSHA1Hash(Text) → string` | 返回文本的 40 位 SHA-1 哈希 |
| `computeSHA3Hash` | `computeSHA3Hash(Text) → string` | 返回文本的 SHA3-256 哈希 |

### 8. 颜色

| 函数 | 语法 | 说明 |
|------|------|------|
| `getStandardColor` | `getStandardColor(Index) → integer` | 返回标准调色板（30 色）中的颜色值 |
| `makeRGBValue` | `<Path>.makeRGBValue(R, G, B) → integer` | 由 RGB 分量生成颜色值 |

### 9. 其他

| 函数 | 语法 | 说明 |
|------|------|------|
| `deleteAllDebugExpressions` | `deleteAllDebugExpressions` | 删除所有 Method 中的调试表达式 |

---

## 重点函数说明

### 许可证相关（`checkForLicense` / `createLicenseFile` / `licenseName`）

- `checkForLicense` 返回 0–7 的状态码：`0` 有效、`1` 未注册、`2` 注册表格式错误、`3` SHA-1 哈希错误、`4` Host-ID 错误、`5` 版本过旧、`6` 已过期、`7` 与许可证类型不兼容。
- `createLicenseFile` 支持通过 MAC 地址、`COMPOSITE=...`、`SOLDTO=...` 或 `ECA=...` 指定 Host-ID，返回密码 SHA-1 哈希供 `checkForLicense` 校验。

### 动态执行（`execute` / `executeSilent` / `executePythonFile`）

- `execute` 遇到运行时错误会打开调试器（当“忽略公式错误”关闭时），否则行为等同 `executeSilent`。
- `executeSilent` 出错时不打开调试器，并返回对应类型的默认值。
- 两者都支持匿名标识符 `?`（调用方 Method）与 `@`（调用方接收）。

### 模型生命周期（`loadModel` / `closeModel` / `exitApplication` / `modelFile`）

- `loadModel` 仅在无已加载模型时有效，通常配合 `closeModel` 或外部接口（COM）使用；加密模型可传入密码。
- `closeModel` 与 `exitApplication` 均可通过定义 `onCloseModel` Method（含布尔参数 `onExitApplication`）执行清理任务。

### 模型语言（`language`）

- 返回整数编码：`0` 德语、`1` 英语、`2` 日语、`3` 中文、`8` 匈牙利语。

---

*Source: Plant Simulation Help（Miscellaneous Global Functions, A–M），详见同目录 `a-to-m.md`。*
