# Read-Only Attributes (DataStack)

本目录介绍了 `DataStack`（以及 `DataQueue`）对象的只读属性（read-only attributes）的查看与查询方法，并列出了这些对象提供的属性组。

## 目录内容

- `read-only-attributes.md` — 只读属性的说明页面（Markdown 格式）。
- `read-only-attributes.txtx` — 同一内容的纯文本导出版本。

## 内容总结

### 查看方法、只读属性与属性

要查看对象的所有方法、只读属性和属性，请打开 **Show Attributes and Methods**（显示属性和方法）窗口。以下两种方式可打开该窗口：

- 在 **Class Library**（类库）的上下文菜单中选择 **Show Attributes and Methods**，可查看所选 **Class**（类）的方法、只读属性和属性。
- 按 **F8** 键，或在插入了实例的 **Frame** 的 **Home** 功能区选项卡中点击 **Show Attributes and Methods**，可查看所选 **Instance**（实例）的方法、只读属性和属性。

### 查询只读属性

要查询某个只读属性的值，例如可以输入：

```python
print MyDataStack.Full
```

### DataQueue 与 DataStack 的属性

`DataStack` 和 `DataQueue` 提供：

- **列表和表格的属性（Attributes of Lists and Tables）**。
- **所有对象的属性（Attributes of All Objects）**。

---

*Plant Simulation Help 11-4243 — Unpublished work. © 2026 Siemens*
