# Read-Only Attributes of the AGVPool

本目录包含 AGVPool（AGV 池）对象的只读属性文档，来源于 Plant Simulation Help（11-3457 至 11-3460）。

## 内容概览

AGVPool 提供以下只读属性和方法。只读属性的值由 Plant Simulation 在查询的时间点计算，可以查询但不能设置。大多数只读属性对应对象标签页（如 Statistics 标签）上不可用的对话框项。

| 名称 | 类型 | 语法 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `getIdleAGV` | 方法 | `<Path>.getIdleAGV → object` | `object`（无空闲 AGV 时返回 `VOID`） | 返回 `IsIdle` 为 `true` 的 AGV，并将其 `IsIdle` 设为 `false` |
| `NumIdleAGVs` | 只读属性（可监视） | `<Path>.NumIdleAGVs → integer` | `integer` | 返回 `IsIdle` 为 `true` 的 AGV 数量 |
| `StatAverageTraveledDistance` | 只读属性 | `<Path>.StatAverageTraveledDistance → length` | `length` | 返回 AGVPool 中 AGV 行驶的平均距离（米） |

## 成员详解

### getIdleAGV [SimTalk]

返回 AGVPool 中属性 `IsIdle` 为 `true` 的一个 AGV。

- **备注**：该方法会将返回 AGV 的 `IsIdle` 设为 `false`。若要让该 AGV 再次可用，需要自行将 `IsIdle` 重新设为 `true`（通常是在 AGV 到达路线终点时）。
- **示例**：
  ```simtalk
  waituntil AGVPool.NumIdleAGVs > 0
  var AGV := AGVPool.getIdleAGV
  ```

### NumIdleAGVs [SimTalk]

返回 AGVPool 中属性 `IsIdle` 为 `true` 的 AGV 数量。

- **可监视**：该只读属性是可监视的（watchable）。
- **示例**：
  ```simtalk
  waituntil AGVPool.NumIdleAGVs > 0
  var AGV := AGVPool.getIdleAGV
  ```

### StatAverageTraveledDistance [SimTalk] - AGVPool

返回 AGVPool 中 AGV 行驶的平均距离（单位：米）。

- **示例**：
  ```simtalk
  print AGVPool.StatAverageTraveledDistance
  ```

## 使用说明

- 查询只读属性的值，例如：
  ```simtalk
  print MyAGVPool.StatAverageTraveledDistance
  ```
- 查看对象的所有方法、只读属性和属性，可打开 **Show Attributes and Methods** 窗口：
  - 在 Class Library 的上下文菜单中选择 **Show Attributes and Methods**，查看所选类的相关项。
  - 在插入实例的 Frame 中按 **F8** 键，或点击 Home 功能区标签上的 **Show Attributes and Methods**，查看所选实例的相关项。

## 参见

- `IsIdle` [SimTalk] - Transporter
- Fine-position an AGV
- Attributes of the AGVPool
- Read-Only Attributes of All Objects
- 相关视频：https://youtu.be/PYXYutlaGOs?si=G_5eRYYGFXUoUrSv&t=36

---

*Source: Plant Simulation Help (11-3457 to 11-3460), © 2026 Siemens*
