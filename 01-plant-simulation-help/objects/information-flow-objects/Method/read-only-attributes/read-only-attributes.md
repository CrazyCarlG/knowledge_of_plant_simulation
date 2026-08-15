# Read-Only Attributes of the Method

You can query the values of the read-only attributes, but you cannot set them: Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object (for example, on the **Statistics** tab).

To view all methods, read-only attributes, and attributes of the object, open the **Show Attributes and Methods** window:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance.

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print &Method.Encrypted
```

---

## Encrypted [SimTalk]

Returns whether the Method (or the user-defined attribute of data type `method` designated by the reference operator `<&>`) is encrypted (`true`) or not (`false`).

- **Type:** Read-only attribute
- **Syntax:** `<&>Method.Encrypted → boolean`
- **Return Value:** `boolean`

**Example**

```simtalk
print &MyMethod.Encrypted
```

---

## NumInExecution [SimTalk]

Returns how often the Method designated by the reference operator `<&>` is being executed at the moment.

- **Type:** Read-only attribute
- **Syntax:** `<&>Method.NumInExecution → integer`
- **Return Value:** `integer`

**Example**

```simtalk
print &MyMethod.NumInExecution
```

---

## Attributes of the Method

The object Method provides:

- The read-only attributes listed above.
- The Attributes of All Objects.

> **Note:** You can only access the attributes of the object Method that refer to the object itself via the reference operator `&`. Without the `&` operator the attribute is applied to the contents of the Method.
