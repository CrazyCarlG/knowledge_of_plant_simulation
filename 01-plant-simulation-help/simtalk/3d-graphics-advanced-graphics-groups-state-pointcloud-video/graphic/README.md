# 图形组访问（Graphic Groups · SimTalk）

本目录汇总 SimTalk 中用于**访问图形组（Graphic Groups）**的方法、属性与只读属性。所有成员均可通过 Method Editor 的 **Auto Complete**（Edit 功能区）查看。

> 说明：本 README 是对同目录下 `graphic.md` / `graphic.txtx` 的内容摘要。当前目录下没有子文件夹，也没有其他 README.md，因此仅汇总这两个文档（两者内容一致）。

---

## 一、方法（Methods）

以 `_3D.` 前缀访问仿真对象（`<Path>`）的图形组级能力，或作用于 `getGraphic` 返回的 graphic / graphic group。

| 名称 | 类型 | 作用 |
|------|------|------|
| `ungroupGraphic` | 方法 | 取消指定图形的组（解组），作用于 `getGraphic` 返回的图形 |
| `_3D.addGraphicGroup(GraphicGroupName, Visible[, Internal:=false, Locked:=false])` | 方法 | 向对象添加指定图形组 |
| `_3D.deleteGraphicGroup(GraphicGroupName) → string` | 方法 | 从对象删除指定图形组，返回 string |
| `_3D.deleteGraphicGroupContent([GraphicGroupName])` | 方法 | 删除指定图形组中的图形（内容） |

要点：
- `ungroupGraphic` 不能用于自动生成的图形组，也不能用于位于自动生成图形组中的图形。
- `addGraphicGroup` 的 `Internal` 与 `Locked` 为可选参数，默认值均为 `false`；新写法可直接返回图形组，等价于旧的「先添加、再 `getGraphic`」写法。
- `deleteGraphicGroupContent` 不指定名称时删除默认图形组（`default`）的内容；尝试删除自动生成的默认图形组内容时会静默失败（不报错）。
- 上述方法赋值后都会**关闭图形继承（deactivates graphic inheritance）**。

---

## 二、对象级属性（`_3D`）

以 `_3D.` 前缀读写对象（`<Path>`）层面的图形组集合。

| 名称 | 类型 | 作用 |
|------|------|------|
| `_3D.ExternalGraphicGroups:string[]` | 属性 | 设置对象所有外部图形组列表 |
| `_3D.InternalGraphicGroups:string[]` | 属性 | 设置对象所有内部图形组列表 |
| `_3D.LockedGraphicGroups:string[]` | 属性 | 设置对象所有锁定图形组列表 |
| `_3D.VisibleGraphicGroups:string[]` | 属性 | 设置对象可见的图形组列表 |
| `_3D.GraphicGroupNames → string[]` | 只读属性 | 返回对象所有图形组名称列表 |

要点：
- `ExternalGraphicGroups` / `InternalGraphicGroups` / `LockedGraphicGroups` 赋值都会关闭对应 Frame 的图形继承；`VisibleGraphicGroups` 赋值会关闭所有图形组可见性设置的继承。
- 可见的外部图形组会显示在「打开了包含该 Frame 的父级」的 3D 窗口中；可见的内部图形组显示在「打开了该 Frame 本身」的 3D 窗口中。
- 锁定图形组可防止在 3D 窗口中被误选（例如厂房图形）。
- 不可见的图形组不会显示在任何 3D 窗口中，适用于同一对象在不同开发阶段的多种外观表示。

---

## 三、图形组属性（Graphic Group Properties）

作用于 `_3D.getGraphic(GraphicGroupName)` 返回的图形组（`<Path>`）。

| 名称 | 类型 | 作用 |
|------|------|------|
| `External:boolean` | 属性 | 设置图形组是否向外表示其所属 Frame（`true`/`false`） |
| `Internal:boolean` | 属性 | 设置图形组是否向内装饰其所属 Frame（`true`/`false`） |
| `Locked:boolean` | 属性 | 设置图形组是否锁定（`true`/`false`） |
| `Visible:boolean` | 属性 | 设置图形组是否可见（`true`/`false`） |
| `Generated:boolean` | 只读属性 | 返回图形组的图形是否为自动生成 |

要点：
- `External`：对外表示所属 Frame；需同时设置 `Visible` 才会在父级 3D 窗口中显示。
- `Internal`：向内装饰所属 Frame；需同时设置 `Visible` 才会在该 Frame 的 3D 窗口中显示。
- `Locked`：防止在 3D 窗口中被误选，典型场景是厂房等大图形。
- `Visible`：不可见的图形组不显示在任何 3D 窗口中，可用于同一对象不同开发阶段的多种外观。
- `Generated`：自动生成的图形组**不能增删图形**，但可编辑其可见性设置。
- `External` / `Internal` / `Locked` 赋值会关闭所属 Frame 的图形继承；`Visible` 赋值会关闭所属对象所有图形组可见性设置的继承。

---

## 四、完整成员速查表

| 名称 | 类型 | 用途 |
|------|------|------|
| `ungroupGraphic` | 方法 | 取消图形编组 |
| `_3D.addGraphicGroup` | 方法 | 添加图形组 |
| `_3D.deleteGraphicGroup` | 方法 | 删除图形组 |
| `_3D.deleteGraphicGroupContent` | 方法 | 删除图形组内容 |
| `_3D.ExternalGraphicGroups` | 属性 | 外部图形组列表 |
| `_3D.InternalGraphicGroups` | 属性 | 内部图形组列表 |
| `_3D.LockedGraphicGroups` | 属性 | 锁定图形组列表 |
| `_3D.VisibleGraphicGroups` | 属性 | 可见图形组列表 |
| `_3D.GraphicGroupNames` | 只读属性 | 所有图形组名称列表 |
| `External`（graphic group） | 属性 | 是否对外表示所属 Frame |
| `Internal`（graphic group） | 属性 | 是否向内装饰所属 Frame |
| `Locked`（graphic group） | 属性 | 是否锁定 |
| `Visible`（graphic group） | 属性 | 是否可见 |
| `Generated`（graphic group） | 只读属性 | 是否自动生成 |
