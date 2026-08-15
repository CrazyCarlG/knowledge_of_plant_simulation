# Attributes of the Object Cycle

The object `Cycle` provides:

- The attributes listed in the table of contents.
- The **Attributes of All Objects**.
- The **Attributes of the Material Flow Objects**.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

- Select **Show Attributes and Methods** on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class.
- Press **F8** or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show them for the selected Instance.

You can set and get an attribute value with check boxes, text boxes, drop-down lists, or by assigning values to the respective attributes.

```simtalk
MyCycleObject.Active := true
```

```simtalk
print MyCycleObject.EmptyCycleAllowed
posit := MyStation.Cont.XPos
```

---

## GetLastStation [SimTalk]

Returns the last station of the balanced line which the `Cycle` designated by `<Path>` synchronizes.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.GetLastStation -> object`
- **Return Value:** The return value has the data type `object`.

```simtalk
print MyCycleObject.GetLastStation
```

**See also:** Last Station, Attributes of the Object Cycle

---

## Active [SimTalk] - Cycle

Activates line balancing with the `Cycle` designated by `<Path>` (`true`) or deactivates it (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>.Active:boolean`
- **Assignment Value:** You can assign a value of data type `boolean`.

```simtalk
MyCycleObject.Active := true
```

**See also:** Active [check box] - Cycle

---

## EmptyCycleAllowed [SimTalk]

Sets if parts within the `Cycle` designated by `<Path>` can be moved on, although no part is ready to move on from the predecessor of the synchronized stations (`true`) or not (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>.EmptyCycleAllowed:boolean`
- **Assignment Value:** You can assign a value of data type `boolean`.

```simtalk
MyCycleObject.EmptyCycleAllowed := true
```

**See also:** Empty Cycle Allowed [check box]

---

## EntranceOnlyOnCycle [SimTalk]

Sets if parts are allowed to enter the `Cycle` designated by `<Path>` only when the cycle moves all MUs by one station on (`true`).

- **Remarks:** Specify `false` to allow parts to enter the Cycle at any time.
- **Type:** Attribute
- **Syntax:** `<Path>.EmptyCycleAllowed:boolean`
- **Assignment Value:** You can assign a value of data type `boolean`.

```simtalk
MyCycleObject.EmptyCycleAllowed := true
```

**See also:** Part Can Only Enter on Cycle [check box]

---

## Related

- **Fluid Objects:** Plant Simulation provides fluid objects to simulate free-flowing materials (liquid, gaseous, or pourable form). They are especially suited for the food and beverages processing industries and for the pharmaceutical industries.
