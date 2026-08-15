# Methods of the Tank

The Tank provides the following groups of methods:

- The General Methods of the Tank.
- The Methods of the Sensors of the Tank.
- The Methods of the Fluid Objects.
- The Methods of All Objects.

To view all methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**:

- Select **Show Attributes and Methods** on the context menu of the Class Library to show them for the selected Class.
- Press the **F8** key or click **Show Attributes and Methods** on the Home ribbon tab of the Frame into which you inserted an instance to show them for the selected Instance.

## Syntax Line Example

An example of the syntax line of an individual method might look like this:

```
<Path>.openDialog([CallOpenControl:boolean:=false]) → boolean
```

- `<Path>` designates the path of the object to which the method applies.
- The signature of the method, consisting of the identifier and the data type of each parameter, is listed in parentheses. `(Parameter:string)`, for example, designates a parameter of data type string. Instead of a constant value, you can also use a variable of the required type or a method that returns the required data type.
- Optional parameters are listed within brackets: `[,Parameter:boolean]` means you can, but do not have to, enter the boolean parameter.
- If a parameter has a default value, the signature shows the default value after the parameter, e.g. `:= false`.
- If the method has a return value, the signature shows its data type after the arrow `→`, e.g. `→ boolean`.

> **Note:** Make sure to enter the parentheses for expressions within parentheses `(…)`. Not entering them may lead to unexpected results and open the Debugger.

---

## General Methods of the Tank

The Tank provides the general method `setCurrentContent`.

### setCurrentContent

Sets the Current Amount of the material in the Tank designated by `<Path>`.

**Remarks:** The new content replaces the previous content.

**Note:** Typically, you set the initial state of the object with the method `setCurrentContent`.

- **Type:** Method
- **Syntax:**

```
<Path>.setCurrentContent(Amount:real[, Material:string, MaterialsTable:path])
```

**Parameters:**

- `Amount` (real) — designates the amount of the material.
- `Material` (string, optional) — designates the material as such.
- `MaterialsTable` (path, optional) — designates the path to the MaterialsTable.

**Note:** If the Tank already contains a material, you can just enter the new `Amount` as a single parameter. Otherwise, you also have to specify the `Material` and the `MaterialsTable`.

**Examples:**

```simtalk
Tank1.setCurrentContent(3, "MyProduct", .Fluids.MaterialsTable)
MyTank.setCurrentContent(5) -- MyTank already contains a material
```

**See also:** MaterialsTable

---

## Methods of the Sensors of the Tank

The Tank provides the following methods for sensors:

- `createSensor`
- `deleteSensor`
- `existsSensorID`
- `sensorID`
- `sensorNo`
- `sensors.ID`

### createSensor

Creates a new sensor for the Tank designated by `<Path>`.

- **Type:** Method
- **Syntax:**

```
<Path>.createSensor([Position:real, Control:method, Exceeded:boolean, Underrun:boolean, PositionType:string]) → integer
```

**Parameters (define the sensor):**

- `Position` (real, optional) — sets the relative position.
- `Control` (method, optional) — designates the name of the Method object that the sensor triggers. You can specify the name as a string, i.e., `"myMethod"`, or as `&myMethod`.
- `Exceeded` (boolean, optional) — sets whether the sensor is triggered when the amount of material in the Tank has exceeded (located above the sensor position) `true` or not `false`.
- `Underrun` (boolean, optional) — sets whether the sensor is triggered once the amount of material in the Tank has underrun (located below the sensor position) `true` or not `false`.
- `PositionType` (string, optional) — designates the position type of the sensor: `Relative` or `Absolute`.

**Return Value:** `integer` — the unique number of the sensor. You can use this number to access the sensor.

**Example:**

```simtalk
var ID1,ID2: integer
ID1 := MyTank.createSensor(0.5,"SensorCtrl",true,false)
ID2 := MyTank.createSensor(0.7,&myMethod,false,true)
ID3 := MyTank.createSensor(3,"SensorCtrl",true,false,"absolute")
```

**See also:** Sensors [Tank], _Attributes of the Sensors of the Tank

### deleteSensor

Deletes the specified sensor from the Tank designated by `<Path>`.

- **Type:** Method
- **Syntax:**

```
<Path>.deleteSensor(SensorID:integer)
```

**Parameter:** `SensorID` (integer) — designates the SensorID.

**Example:**

```simtalk
MyTank.deleteSensor(2)
```

**See also:** Sensors [Tank], Delete [sensor]

### existsSensorID

Returns whether the specified sensor exists (`true`) or does not exist (`false`) in the Tank designated by `<Path>`.

- **Type:** Method
- **Syntax:**

```
<Path>.existsSensorID(SensorID:integer) → boolean
```

**Parameter:** `SensorID` (integer) — designates the SensorID.

**Return Value:** `boolean`.

**Example:**

```simtalk
print MyTank.existsSensorID(2)
```

**See also:** Sensors [Tank]

### sensorID

Returns the designated sensor of the Tank designated by `<Path>`.

**Remarks:** The methods `sensorNo(SensorID:integer)` and `sensorID(SensorID:integer)` may reference different sensors.

- **Type:** Method
- **Syntax:**

```
<Path>.sensorID(SensorID:integer) → any
```

**Parameter:** `SensorID` (integer) — designates the unique Sensor-ID which Plant Simulation assigns when you create the sensor.

**Return Value:** `any`.

**Example:**

```simtalk
MyTank.SensorID(3).Exceeded := true
if MyTank.SensorID(3).Exceeded = true then
   ?.EntranceLocked := true
end
```

**See also:** Sensors [Tank]

### sensorNo

Returns a sensor of the Tank designated by `<Path>` whose unique identifier you do not know.

**Remarks:** The methods `sensorNo(SensorNumber:integer)` and `sensorID(SensorID:integer)` may reference different sensors.

- **Type:** Method
- **Syntax:**

```
<Path>.sensorNo(SensorNumber:integer) → object
```

**Parameter:** `SensorNumber` (integer) — may be a value between 1 and the number of sensors. Which sensor Plant Simulation returns may change during the simulation (i.e., if existing sensors are deleted). Thus only use the method `sensorNo` if a method call iterates through all sensors of the object.

**Return Value:** `object`.

**Example:**

```simtalk
MyTank.sensorNo(1).Underrun := true
```

**See also:** Sensors [Tank]

### sensors.ID

Returns the specified sensor of the Tank designated by `<Path>`.

- **Type:** Method
- **Syntax:**

```
<Path>.sensors.ID(<Number>) → any
```

**Return Value:** `any`. The number after the ID designates the unique identifier which Plant Simulation assigns when you create the sensor.

**Examples:**

```simtalk
MyTank.sensors.ID3.Front := true
var sensor := MyTank.sensors.ID2
sensor.Front := true
```

**See also:** Sensors [Tank], New [sensor]

---

## Read-Only Attributes of the Tank

The Tank provides read-only attributes (including `sensors.ID`).
