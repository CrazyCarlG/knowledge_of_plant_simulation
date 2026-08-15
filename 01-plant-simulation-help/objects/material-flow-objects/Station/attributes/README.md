# Station — Attributes（属性）总结

本目录存放 **Station（工位）** 对象的属性（Attributes）相关文档，内容来源于 Siemens Plant Simulation Help（11-1719 / 11-1720）。本 README 是对 `attributes.md`（`attributes.txtx` 为其原始提取文本，两者内容一致）的总结。

## 内容来源

目录内包含以下文件：

- `attributes.md` — 属性页面的 Markdown 版总结（本 README 的依据）。
- `attributes.txtx` — 从 Plant Simulation 帮助 PDF 提取的原始文本。
- `Plant-Simulation-Help2606_4649-4650.pdf` — 帮助文档原文（第 11-1719 至 11-1720 页）。

## 1. 查看属性与方法

打开 **Show Attributes and Methods（显示属性与方法）** 窗口即可查看对象的所有方法、只读属性和属性：

- 在 **类库（Class Library）** 的上下文菜单中选择 **Show Attributes and Methods**，可显示所选 **类（Class）** 的方法、只读属性与属性。
- 在插入了实例的 Frame 中，按 **F8** 键或点击 **Home** 功能区选项卡上的 **Show Attributes and Methods**，可显示所选 **实例（Instance）** 的方法、只读属性与属性。

## 2. 查询只读属性

只读属性的值只能在查询时刻获取。查询示例：

```simtalk
print MyStation.UUID
```

## 3. Station 提供的属性

Station 提供：

- **所有对象的属性（The Attributes of All Objects）**
- **物料流对象的属性（The Attributes of the Material Flow Objects）**

要查看对象的所有方法、只读属性与属性，请打开 **Show Attributes and Methods** 窗口。

## 4. 设置与获取属性值

既可以通过对话框窗口中的复选框、文本框和下拉列表，也可以通过对相应属性赋值来设置或获取属性值。

- **设置属性值**，例如：

```simtalk
MyStation.Pause := true
```

- **获取属性值**，例如：

```simtalk
print MyStation.Pause
posit := MyStation.Cont.XPos
```

## 5. ParallelStation（并行工位）

使用 **ParallelStation** 对象为同时并行加工多个工件的机器建模。

- ParallelStation 的内置属性与 Station 相同。
- ParallelStation 拥有**多个加工位置**，而 Station 只有**单个加工位置**。
- 若某个 MU 的名称与其之前加工的工件（即前驱）不同，则始终会应用**设置时间（set-up time）**。
- Plant Simulation 总是将 MU **作为一个整体**移动（而非连续移动）——一旦 MU 的前端位于 ParallelStation 上，整个 MU 即位于其上。
- 在 **MU Animation** 选项卡上，可设置工件在 ParallelStation 动画区域上的分布方式。
- 将鼠标悬停在 ParallelStation 上，可显示包含其信息的工具提示。

## 目录说明

- `attributes.md`：Station 对象属性说明的 Markdown 版本（本总结的源文件）。
- `attributes.txtx`：相同内容的文本提取版本。
- `Plant-Simulation-Help2606_4649-4650.pdf`：对应帮助文档的 PDF 片段。
- 本目录无子文件夹，故无子文件夹 README.md。

---

*来源：Plant Simulation Help。未发表作品。© 2026 Siemens*
