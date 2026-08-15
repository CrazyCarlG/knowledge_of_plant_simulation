# Attributes of the PlaceBuffer

## Overview

This document summarizes the attributes of the **PlaceBuffer** object. Attributes are listed in:

- The table of contents (left panel).
- The *Attributes of All Objects*.
- The *Attributes of the Material Flow Objects*.

To view all methods, read-only attributes, and attributes of an object, open the **Show Attributes and Methods** window:

- Select **Show Attributes and Methods** on the context menu of the **Class Library** to show them for a selected **Class**.
- Press **F8** or click **Show Attributes and Methods** on the **Home** ribbon tab of the **Frame** into which you inserted an instance, to show them for a selected **Instance**.

You can set and get the value of an attribute using the check boxes, text boxes, and drop-down lists in the dialog windows, or by assigning values to the respective attributes.

**To set the value of an attribute:**

```simtalk
MyPlaceBuffer.Accumulating := true
```

**To get the value of an attribute:**

```simtalk
print MyPlaceBuffer.Accumulating
posit := MyStation.Cont.XPos
```

---

## Accumulating [SimTalk] - PlaceBuffer

Sets whether the following MUs may move up (`true`) or have to wait (`false`) when the preceding MU cannot exit the PlaceBuffer designated by `<Path>`.

**Remarks:** If the preceding part cannot exit and `Accumulating` is `false`, no further MU can enter the PlaceBuffer.

- **Type:** Attribute
- **Syntax:** `<Path>.Accumulating:boolean`
- **Watchable:** The attribute is watchable.
- **Assignment Value:** You can assign a value of data type `boolean`.

**Example:**

```simtalk
MyPlaceBuffer.Accumulating := true
```

**See also:** Accumulating [check box] - PlaceBuffer

---

## Capacity [SimTalk] - PlaceBuffer

Sets the Capacity, i.e., the number of stations of the PlaceBuffer designated by `<Path>`.

**Remarks:**
- The value `-1` designates an infinite capacity if `SequentiallyIndexing` is set to `false`.
- You can access the individual locations by their index.
- You can only reduce the Capacity when enough places are free.
- If parts are located in the PlaceBuffer you cannot change its Capacity; you can only change it when it is empty.

- **Type:** Attribute
- **Syntax:** `<Path>.Capacity:integer`
- **Watchable:** The attribute is watchable.
- **Assignment Value:** You can assign a value of data type `integer`.

**Example:**

```simtalk
MyPlaceBuffer.Capacity := 12
```

**See also:** SequentiallyIndexing [SimTalk], Sequentially Indexing [check box]

---

## SequentiallyIndexing [SimTalk]

Sets whether the Processing Time on a place of the PlaceBuffer designated by `<Path>` only starts when the succeeding place is free (`true`) or not (`false`).

**Remarks:**
- In Sequentially Indexing mode, the Processing Time does not represent the time a part is processed on a place, but the time used for moving the part from its current place to the succeeding place.
- If the Capacity is four, the Processing Time passes three times before the part can leave the PlaceBuffer, because three move processes have to take place.
- The total time can get longer because of waiting times. For this reason no time is used on the last place, and the part can exit the PlaceBuffer immediately once it reaches the last place, provided the successor can accept the part.

- **Type:** Attribute
- **Syntax:** `<Path>.SequentiallyIndexing:boolean`
- **Assignment Value:** You can assign a value of data type `boolean`.

**Example:**

```simtalk
MyPlaceBuffer.SequentiallyIndexing := true
```

**See also:** Sequentially Indexing [check box]

---

## Buffer [object]

Use the object **Buffer** for temporarily holding a large number of parts and then passing them on to their successor.

### Description

Insert a Buffer between two components of your plant:

- **To temporarily hold parts**, if one of the components following it in the sequence of stations fails, preventing the preceding machines from stopping production.
- **To move parts on**, if the preceding components stop working, preventing the production process from grinding to a halt.

Dimensioning a Buffer with a large enough capacity for covering all failures leads to a complete decoupling of the respective components of your plant. The Buffer not only tides over failure times but also serves as a compensating station for fluctuating transport and operating times, which lead to queues forming in front of a machine or component. However, even then it cannot always prevent the material flow from being interrupted or grinding to a halt.

As the Buffer does not have individual places, it does not have to divide the processing time (the time during which the part remains in it) into small individual steps. Instead, you can select the sequence in which the parts exit the Buffer.

**Buffer Type [drop-down list]:**

- **Queue** — parts exit the Buffer in the same order in which they entered it (First In First Out).
- **Stack** — the part that entered last leaves the Buffer first (Last In First Out).

**Note:** Each MU remains in the Buffer for at least the time entered as the **Dwell Time [Buffer]**. For the Buffer Type > Stack, a MU can only exit the Buffer when all parts that entered after the current part have already exited, i.e., when the MU is located at the very top of the stack.

To show a tooltip with information about the Buffer, hover the mouse over it.

---

*Source: Plant Simulation Help — Unpublished work. © 2026 Siemens*
