# 文件夹模型（Folder Model）

> 说明：本篇为**汇编条目**。官方帮助第 9 章 *Plant Simulation User Interface* 中的 *What is a Folder Model?*（原书 p.264–273，含 Save As > Folder Model / Compact format / Git support 三个子节）尚未转录入本知识库。以下内容由知识库中已有的权威条目（`saveFolderModel`、`loadModel`、PythonModule、Method.RandomSeed）汇编而成，非第 9 章原文。

## 一、什么是文件夹模型

**文件夹模型（Folder Model）** 是 Plant Simulation 的一种模型保存格式：它不是把整个模型存成一个二进制文件，而是把模型保存为一个**「文件夹 + 多文件」的目录结构**。这一设计的目标是让模型能被版本控制系统（如 Git）管理——因为里面的内容都是文本文件，可以逐行 diff、逐文件提交。

官方英文表述（`saveFolderModel` 条目）：

> Saves the simulation model in a folder/file structure, which facilitates storing the model in a version control system such as Git.

## 二、与单文件模型（`.spp`）的区别

| | 文件夹模型 `.psfm` | 单文件模型 `.spp` |
| --- | --- | --- |
| 存储形态 | 一个目录（文件夹） | 单个文件 |
| 内部内容 | 多个文本文件（`$.spp` / `$.yaml` / `.py`） | 可能为二进制或文本 |
| 版本控制 | 天然适合 Git（逐文件 diff / commit） | 不易 diff |
| 加载入口 | `loadModel("...\MyFolderModel.psfm\$.spp")` | `loadModel("...\myModel.spp")` |

## 三、文件夹内部结构

- **`$.spp`** —— 位于 `.psfm` 文件夹根部的模型主文件，也是 `loadModel` 的加载入口。
- **`$.yaml`** —— 每个 Frame 一个，包含该 Frame 内的全部对象（当 `CompactFormat=false`，即默认时）。
- **独立 `.yaml`** —— 当 `CompactFormat=true` 时，Frame 内有原点的对象各自存成独立 `.yaml` 文件。
- **`.py`** —— PythonModule 中的 Python 代码单独存为 `.py` 文件。
- **`.UserSettings.yaml`** —— 用户设置文件；启用 Git 时会被自动生成的 `.gitignore` 排除，不纳入版本控制。

## 四、保存：`saveFolderModel`

**类型**：Function（SimTalk）

**语法**

```
saveFolderModel(FileName:string[, CompactFormat:boolean:=false, UseGit:boolean:=false])
```

**参数**

- `FileName`（string）：模型的路径与名称。
- `CompactFormat`（boolean，默认 `false`）：
  - `true`：Frame 内有原点的对象保存为独立 `.yaml` 文件；
  - `false`：所有对象保存进该 Frame 的 `$.yaml` 文件（文件数更少，大模型性能更好）。
- `UseGit`（boolean，默认 `false`）：为 `true` 时，首次保存文件夹模型会自动创建 Git 仓库、自动提交初始版本，并生成 `.gitignore`（忽略 `.UserSettings.yaml`）。仅在已安装 Git 时可用。

**示例**

```
saveFolderModel("D:\MyModels\MyDeportioner.psfm", true, true)
```

## 五、加载：`loadModel`

**类型**：Function

**语法**

```
loadModel(ModelName:string[, Password:string]) → boolean
```

**说明**：仅在当前没有已加载模型时有效（通常在 `closeModel` 之后，或从 COM 等外部接口调用）。

**示例**

```
closeModel
loadModel("D:\MyModels\MyFolderModel.psfm\$.spp")
```

注意：文件夹模型的加载入口是 `.psfm` 文件夹内的 `$.spp` 主文件。

## 六、Compact format（紧凑格式）

`CompactFormat` 参数控制「对象拆成独立 `.yaml`」还是「并入 Frame 的 `$.yaml`」：

- `false`（默认）：全部对象并入 Frame 的 `$.yaml`，减少文件系统里的文件数量，超大模型下性能更好。
- `true`：Frame 内有原点的对象拆成独立 `.yaml` 文件，便于更细粒度的 diff 与版本管理。

## 七、Git 支持

- 通过 `saveFolderModel` 的 `UseGit=true` 启用：首次保存自动建仓库、自动提交初始版本、生成 `.gitignore`（忽略 `.UserSettings.yaml`）。
- 提交命令：可通过注册表键 `FolderModelCommitCommand`（String 类型）设置保存模型时调用的命令。注册表位置：`HKEY_CURRENT_USER\Software\Siemens\Tecnomatix Plant Simulation 2606` 或 `HKEY_LOCAL_MACHINE\...`。
  - 若键存在，启动 TortoiseGit；
  - 键值为空字符串 `""` 时，保存时不再弹出 Commit 对话框；
  - 使用其它版本控制系统时，把其路径作为 Value data。

## 八、特殊说明

- **PythonModule**：文件夹模型中 Python 代码保存在单独的 `.py` 文件；Python 变量 `__file__` 包含该 `.py` 文件路径。若模型不是文件夹模型，`__file__` 未定义。
- **Method.RandomSeed**：当某对象的 `RandomSeed` 属性值为 0 时，该属性不会显示在 *Show Attributes and Methods* 窗口中，也不会被写入文件夹模型。

## 九、来源

本篇汇编自知识库以下条目：

- `simtalk/predefined-functions-ii-http-utilities/n-to-z/` — `saveFolderModel`
- `simtalk/predefined-functions-ii-http-utilities/a-to-m/` — `loadModel`
- `objects/information-flow-objects/PythonModule/general/` — Python 代码保存说明
- `objects/information-flow-objects/Method/attributes/` — RandomSeed 说明

*来源：Plant Simulation Help — saveFolderModel / loadModel / PythonModule / Method.RandomSeed。Unpublished work. © 2026 Siemens.*
