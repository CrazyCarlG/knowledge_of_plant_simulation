# Attributes of the Tank

The Tank provides:

- The General Attributes of the Tank.
- The Attributes of the Sensors of the Tank.
- The Attributes of the Fluid Objects.
- The Attributes of All Objects.

To view all of the methods, read-only attributes, and attributes of the object, open the window **Show Attributes and Methods**.

You can set the value of an attribute and you can get its value, either with the check boxes, the text boxes and drop-down lists in the dialog windows or by assigning values to the respective attributes.

- To set the value of an attribute, you might, for example, type:

```simtalk
MyTank.OutflowRate := 1
```

- To get the value of an attribute, you might, for example, type:

```simtalk
print MyTank.OutflowRate
posit := MyStation.Cont.XPos
```

## Origin [SimTalk] - Tank

Returns the origin of the sensor of the Tank designated by `<Path>`.

- **Type:** Read-only attribute
- **Syntax:** `<Path>.Sensor.Origin → integer`
- **Return Value:** The return value has the data type `integer`. If the sensor does not have an origin, it returns `VOID`.

Example:

```simtalk
print MyTank.Sensors.id1.Origin
```

See also: Sensors [Tank], Attributes of the Tank.

## OutflowRate [SimTalk] - Tank

Sets the Outflow Rate of the material, which the Tank designated by `<Path>` stores.

**Remarks**

The Outflow Rate is the amount of liters of the material that flows off in a second. The material then flows off through objects of type Pipe to the next object in the flow of materials.

**Note**

The current Outflow Rate depends on the number of attached Pipes. If you attached two Pipes, then the specified Outflow Rate flows through each one of these Pipes in case the Outflow Rate of the connected Pipes permits this. If you just want to let the specified amount flow out of the object, attach a single Pipe and split that up into several Pipes later on.

Plant Simulation outputs error messages if the Outflow Rate of an empty Tank is greater than the Inflow Rate or when the Inflow Rate of a full Tank is greater than the Outflow Rate. Do not ignore these error messages but create Sensors and program Methods which handle these situations. The Sensors have to prevent the Tank from becoming full or empty respectively by opening or closing the connected Pipes.

- **Type:** Attribute
- **Syntax:** `<Path>.OutflowRate:real`
- **Assignment Value:** You can assign a value of data type `real`.

Example:

```simtalk
MyTank.OutflowRate := 1
```

See also: Outflow Rate [Tank].

## Volume [SimTalk] - Tank

Sets the Volume, i.e., the amount of the ingredient, which the Tank designated by `<Path>` can hold.

- **Type:** Attribute
- **Syntax:** `<Path>.Volume:real`
- **Assignment Value:** You can assign a value of data type `real`.

Example:

```simtalk
MyTank.Volume := 10
```

See also: Volume [Tank].

## Attributes of the Sensors of the Tank

The Tank provides the attributes listed in the table of contents for sensors.

See also: Methods of the Sensors of the Tank.

### Control [SimTalk] - sensor, Tank

Designates a Method object of the object designated by `<Path>`.

**Remarks**

Plant Simulation runs the Control when the sensor of the Tank designated by `<Path>` is triggered. A value, which you assign, has to be the reference to a Method (object) or the name of the Method.

As soon as the sensor calls this Method, it passes the Sensor-ID as optional parameter. If the Method expects an integer parameter, the sensor passes the Sensor-ID to the Method. If you do not enter an integer parameter, the Method will be called without a parameter.

The optional parameter `Exceeded` of data type `boolean` shows the user if the sensor position is Exceeded or Underrun.

- **Type:** Attribute
- **Syntax:** `<Path>.Sensors.ID<Number>.Control:string`
- **Assignment Value:** You can assign a value of data type `string`.

Example:

```simtalk
MyTank.Sensors.ID2.Control := &mySensorCtrl
MyTank.Sensors.ID2.Control := "mySensorCtrl"
```

See also: Control [Tank], Sensor-ID.

### Exceeded [SimTalk]

Sets if the sensor is to be triggered if the amount of material in the Tank designated by `<Path>` has Exceeded, i.e., is located above the sensor position (`true`) or not (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>.Sensors.ID<Number>.Exceeded:boolean`
- **Assignment Value:** You can assign a value of data type `boolean`.

Example:

```simtalk
MyTank.Sensors.id1.Exceeded := true
if Exceeded = true then
   ?.EntranceLocked := true
end
```

See also: Exceeded [check box].

### Position [SimTalk] - Tank

Sets the Position of the sensor on the Tank designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.Sensors.ID<Number>.Position:real`
- **Assignment Value:** You can assign a value of data type `real`.

The values you can specify depend on the PositionType:

- For `relative` you can specify a value between 0 and 1, i.e., between 0 percent and 100 percent.
- For `absolute` you can specify a value between 0 and the Volume you specified.

Example:

```simtalk
MyTank.Sensors.id2.Position := 0.1
```

See also: Position [Tank], Volume [Tank].

### PositionType [SimTalk]

Sets the Position Type of the sensor on the Tank designated by `<Path>`.

- **Type:** Attribute
- **Syntax:** `<Path>.Sensors.ID<Number>.PositionType:string`
- **Assignment Value:** You can assign a value of data type `string`. You can specify `"absolute"` or `"relative"`.

Examples:

```simtalk
MyTank.Sensors.ID2.PositionType := "absolute"
MyTank.Sensors.ID1.PositionType := "relative"
```

See also: Position [Tank].

### Underrun [SimTalk]

Sets if the sensor is to be triggered if the amount of material in the Tank designated by `<Path>` has Underrun, i.e., is located below the sensor position (`true`) or not (`false`).

- **Type:** Attribute
- **Syntax:** `<Path>.Sensors.ID<Number>.Underrun:boolean`
- **Assignment Value:** You can assign a value of data type `boolean`.

Example:

```simtalk
MyTank.Sensors.id1.Underrun := true
```

See also: Underrun [check box].
