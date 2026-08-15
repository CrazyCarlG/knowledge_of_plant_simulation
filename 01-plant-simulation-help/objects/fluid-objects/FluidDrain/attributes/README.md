# FluidDrain — Attributes（属性）

本目录包含 FluidDrain 对象的属性（Attributes）相关文档，总结如下。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `attributes.md` | FluidDrain 属性文档（Markdown 格式） |
| `attributes.txtx` | 与 `attributes.md` 内容基本一致，另附带部分无关内容（Tank 对象描述） |

> 注：本目录下没有子文件夹，因此没有子目录 README.md 需要汇总。

## 属性文档内容总结

### StatThroughputPerHour [SimTalk]

返回由 `<Path>` 指定的 FluidDrain 在**可用期间**每小时从工厂（plant）排出的物料量。

- **类型**：只读属性（Read-only attribute）
- **语法**：`<Path>.StatThroughputPerHour → real`
- **返回值**：数据类型为 `real`，吞吐量以**升（liters）**为单位
- **示例**：

```simtalk
print MyFluidDrain.StatThroughputPerHour
```

- **参见**：
  - Tab Statistics [FluidDrain]（统计选项卡）
  - Attributes of the FluidDrain（FluidDrain 的属性）

### Attributes of the FluidDrain（FluidDrain 的属性）

FluidDrain 提供以下属性：

- 流体对象（Fluid Objects）的 `_Attributes`
- 所有对象（All Objects）的 Attributes

### 查看属性与方法

要查看对象的所有方法（methods）、只读属性（read-only attributes）和属性（attributes），可打开 **Show Attributes and Methods**（显示属性与方法）窗口：

- 在类库（Class Library）的上下文菜单中选择 **Show Attributes and Methods**，可显示所选类的相关成员（一般说明）。
- 按 **F8** 键，或点击 Frame 的 Home 功能区（ribbon）选项卡中的 **Show Attributes and Methods**，可显示所选实例（Instance）的相关成员（一般说明）。

### 设置与获取属性值

属性值可通过对话框中的复选框、文本框和下拉列表设置/获取，也可通过为相应属性赋值来实现：

- **设置属性值**示例：

```simtalk
MyFluidDrain.Pause := true
```

- **获取属性值**示例：

```simtalk
print MyFluidDrain.Pause
posit := MyStation.Cont.XPos
```
