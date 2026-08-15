# return

本目录介绍 SimTalk 中的 `return` 关键字，以及 Method 中的错误处理（Error Handling）机制。

## 内容概要

### 1. 使用 `return` 退出方法

- `return` 关键字用于终止当前正在执行的 Method，并返回到调用它的 Method。
- 语法：`return`
- 示例：当某条件不满足时立即返回。

  ```simtalk
  if ParallelStation.failed   -- 无法处理？
     return                   -- 立即返回
  else
     ...
  end
  ```

- 对于需要返回结果的方法，可用 `return <expression>` 结束，其效果等同于 `result := expression` 后再 `return`。

  ```simtalk
  param n: integer -> integer -- 计算 n 的阶乘
  if n = 0
     return 1
  end
  return n * self.execute(n-1)
  ```

- 相关关键字：`return`、`result`。

### 2. 错误处理（Error Handling）

错误处理（也称异常处理）用于在 Method 执行源码时对运行时错误做出反应，例如在模拟必须继续运行并记录错误，或需要对预期错误采取相应措施时。

- **实现方式**
  - 对于 Method 对象：创建一个数据类型为 `method` 或 `object` 的用户自定义属性，命名为 `ErrorHandler`。该属性可建在 Method 自身，或建在插入 Method 的 Frame 中。
  - 对于数据类型为 `method` 的用户自定义属性：在该对象中再创建一个数据类型为 `method` 或 `object` 的用户自定义属性，命名为 `ErrorHandler`。

- **示例 ErrorHandler 源码**

  ```simtalk
  param byref error: string,
        method_path: string,
        line_number: integer -> any
  if error = "Division by zero."
     error := ""  -- 捕获该错误
     return 1e300 -- 向调用方法返回值
  end
  -- 将错误消息传递给调用方法
  error := "error in " + method_path + ": " + error
  ```

- **调用链机制**
  - 当 Method 发生运行时错误时，Plant Simulation 会取消执行该 Method，并调用其 `ErrorHandler`。
  - 若该 Method 没有 `ErrorHandler`，Plant Simulation 会在调用链中向上查找；若调用链中没有任何 Method 拥有 `ErrorHandler`，则采用标准错误处理流程（打开 Method Debugger）。

- **参数**
  - 向 `ErrorHandler` 传递三个参数：错误消息、出错 Method 的路径、出错代码所在行号。

- **处理行为**
  - 若将空字符串 `""` 赋给错误消息变量，Plant Simulation 认为错误已被妥善处理；此时不会继续执行出错 Method，而是跳回调用该 Method 的 Method。
  - 若拥有 `ErrorHandler` 的 Method 会返回值，则 `ErrorHandler` 也应返回一个值。
  - 若无法恰当处理（如遇到未预期的错误），不应删除错误消息，但可修改其内容。若未删除错误消息，Plant Simulation 会认为错误未被处理，并将（可能已修改的）错误消息传递给调用 Method；若调用链中还有带 `ErrorHandler` 的 Method，则用修改后的错误消息调用该 `ErrorHandler`；否则采用标准错误处理流程（打开 Method Debugger）。

- **注意**：若在错误处理过程中再次发生运行时错误，Plant Simulation 不会重复执行错误处理 Method。

- 相关关键字：`setErrorHandler`、`getCallStack`、`throwRuntimeError`。

## 目录文件

- `return.md` — `return` 关键字与错误处理机制的详细说明（本 README 的源内容）。
- `return.txtx` — 与 `return.md` 对应的纯文本版本。
