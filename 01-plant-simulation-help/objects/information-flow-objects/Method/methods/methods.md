# Methods of the Method

## Debugger Editing Commands

- **Copy** — Copies the selected text to the clipboard.
- **Paste** — Pastes the clipboard contents at the cursor position.
- **Delete** — Deletes the selected text.

## Overview

Accessing a Method automatically executes its source code. To access built-in methods, read-only attributes, or attributes, use the reference operator `&`.

The object **Method** provides the methods listed below plus the *Methods of All Objects*.

> **Note:** You can only access the methods of the Method object (which refer to the object itself) via the reference operator `&`. Without `&`, the method is applied to the *contents* of the Method.

To view all methods, read-only attributes, and attributes, open **Show Attributes and Methods** (press `F8` or use the context menu of the Class Library).

### Syntax conventions

Example signature:

```
&Method.execute([Argument1:any, ...[, @:object:=@, ?:object:=self]])
```

- The signature consists of the anonymous identifier `&`, the method name, and parameter data types in parentheses.
- `(Parameter:string)` designates a parameter of data type `string`. A variable of the required type or a method returning the required type may be used instead of a constant.
- Optional parameters are listed in brackets, e.g. `[,Parameter:boolean]`.
- Default values appear after the parameter in the signature.
- If the method has a return value, its data type appears after the arrow `->`.

---

## checkArguments [SimTalk]

Checks if the parameters passed to the Method (designated by `&`) have compatible data types.

**Remarks:** Use `checkArguments` to make sure values entered into a dialog may be passed to Methods.

- **Type:** Method
- **Syntax:** `<&>Method.checkArguments([Argument1:any, ...])`
- **Parameter:** Optional `Argument` of data type `any` — the arguments to check.

```java
&MyMethod.checkArguments(42,void)
```

---

## decrypt [SimTalk]

Decrypts the Method designated by `&` which was previously encrypted.

- **Type:** Method
- **Syntax:** `<&>Method.decrypt(Key:string) → boolean`
- **Parameter:** `Key` (string) — the password.
- **Return Value:** `boolean`

```java
&MyMethod.decrypt("zTrqYa8%e")
```

**See also:** Encrypt Method

---

## deleteMethCall [SimTalk]

Deletes all scheduled calls of the Method designated by `&` in the EventController.

**Remarks:** Use `deleteMethCall` to delete calls you no longer need.

- **Type:** Method
- **Syntax:** `<&>Method.deleteMethCall`

```java
&MyMethod.deleteMethCall // deletes all scheduled method calls
```

**See also:** executeIn

---

## encrypt [SimTalk]

Encrypts the source code of the Method designated by `&`.

- **Type:** Method
- **Syntax:** `<&>Method.encrypt(Key:string) → boolean`
- **Parameter:** `Key` (string) — the password.
- **Return Value:** `boolean`

```java
&MyMethod.encrypt("zTrqYa8%e")
```

**See also:** Decrypt Method

---

## execute [SimTalk] — Method

Runs the Method designated by `&` as a subroutine.

**Remarks:**
- Execution of the calling Method is interrupted until the called Method finishes.
- Especially handy when the path to a Method is stored in a variable of data type `object`.

- **Type:** Method
- **Syntax:** `<&>Method.execute([Argument1:any, ... ][, @:object=@, ?:object=self])`
- **Parameters:** Optional `Argument` (any) — the arguments to be executed. If two additional optional parameters of type `object` are given, `@` is assigned to the anonymous identifier `@` and `?` is assigned `self`.

```java
Variable := &MyMethod1      // variable is of data type object
Variable.execute            // executes MyMethod1
&MyMethod2.execute("abc")   // executes myMethod2
                            // that expects 1 parameter
                            // of data type string
self.execute(n+1)           // calls a method recursively
```

> **Note:** From Python, `execute` runs like a formula. Therefore you cannot move or delete MUs in the Method, and you cannot use `wait`, `waituntil`, or `stopuntil` instructions. Also, Plant Simulation does not show the Expressions tab of the Method Debugger.

```python
# call myMethod from Python
res = current.myMethod.execute()
print(res)
```

**See also:** Run [button] — Method, Tab Expressions [Watch window]

---

## executeIn [SimTalk]

Calls the Method (or a user-defined attribute of data type `method`) designated by `&` after the specified number of seconds of simulation time has elapsed.

**Remarks:**
- Plant Simulation enters a `MethCall` event into the EventController's list of scheduled events at the current simulation time plus `CallAt`.
- `CallAt` must be `>= 0`. If events are already scheduled at this time, the `MethCall` is appended at the end of existing simultaneous events.
- In the called Method, `?` references the caller; `@` references the EventController.

- **Type:** Method
- **Syntax:**
  - `<&>Method.executeIn(CallAt:time[, Argument1:any, ...])`
  - `<&>Method.executeIn(CallAt:dateTime[, Argument1:any, ...])`
- **Parameters:** `CallAt` (time in seconds, or a `dateTime` value) designates when the Method is called. Optional `Argument1, ...` are passed to the Method when called.

```java
&MyMethod1.executeIn(23.5)
// throttle the engine in 5 seconds to 85 percent
&ThrottleEngine.executeIn(5, 0.85)
// New year's day 2025 midnight, year-month-day notation
&MyMethod2.executeIn(str_to_date("2025/12/31"))
// New year's day 2025 midnight, day-month-year notation
&MyMethod2.executeIn(str_to_date("31.12.2025"))
// call the method with a local variable reference, passing two parameters
var obj: object := &MyMethod3
obj.executeIn(4, "my string", true)
```

**See also:** deleteMethCall, executeNewCallChain, List of Events

---

## executeNewCallChain [SimTalk]

Runs the Method designated by `&` after Plant Simulation has processed all active call chains.

**Remarks:**
- Similar to `&Method.executeIn(0)`, but differs: `executeIn` requires an EventController and a method scheduled with `executeIn(0)` runs only after already-scheduled simultaneous events.
- If a method scheduled with `executeNewCallChain` triggers controls, the interrupted method continues only after those controls finish; the new method runs after the controls but before the interrupted method resumes.
- In the called method, `?` references the caller (or the location of a user-defined attribute of type `method`).

- **Type:** Method
- **Syntax:** `<&>Method.executeNewCallChain([Argument1:any, ...][,@:object:=@, ?:object:=self])`
- **Parameter:** Optional `Argument1` (any) and following — the arguments to execute. If two additional optional parameters of type `object` are entered, `@` is assigned to `@` and `?` is assigned `self`.

```java
var o : object := .Models.Model.&MyMethodWithoutParameters
o.executeNewCallChain
```

**See also:** `&` (reference operator), executeIn

---

## hasSyntaxError [SimTalk]

Returns whether the source code of the Method designated by `&` has syntax errors.

**Remarks:** Also applies to user-defined attributes of type `method`.

- **Type:** Method
- **Syntax:** `<&>Method.HasSyntaxError([byref ErrorMessage:string, byref Line:integer]) → boolean`
- **Parameters:**
  - Optional `ErrorMessage` (string) — a local variable receiving an error message (empty string if no error).
  - Optional `Line` (integer) — a local variable receiving the line where the error is located.
- **Return Value:** `boolean`

```java
var NewSourceCode: string := prompt  -- user input
&MyMethod.Program := NewSourceCode   -- assign new source code
if &MyMethod.HasSyntaxError
   print "syntax error"
else
   MyMethod   -- call the Method and execute the new source code
end
```

---

## load [SimTalk] — source code

Loads the contents of an ASCII text file as source code into the Method designated by `&`.

- **Type:** Method
- **Syntax:** `<&>Method.load(FileName:string) → boolean`
- **Parameter:** `FileName` (string) — the name of the text file.
- **Return Value:** `boolean`

```java
&MyMethod.load("C:\Users\Ralf\sourcecode.txt")
```

**See also:** Import from File

---

## Read-Only Attributes of the Method

The Method provides the read-only attributes listed in the table of contents plus the *Read-Only Attributes of All Objects*.

> **Note:** Read-only attributes of the Method object (which refer to the object itself) can only be accessed via the reference operator `&`. You can query their values but cannot set them — Plant Simulation computes the value at the point in time you query it.

To view all attributes, open **Show Attributes and Methods** (`F8`).

Example query:

```java
print &Method.Encrypted
```
