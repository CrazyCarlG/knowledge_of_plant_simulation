# Read-Only Attributes of the Broker

The Broker provides:

- The read-only attributes listed in the table of contents to the left.
- The _Read-Only Attributes of All Objects.

You can query the values of the read-only attributes, but you cannot set them as Plant Simulation computes the value for the point-in-time at which you query it. In most cases a read-only attribute corresponds to an unavailable dialog item on one of the tabs of the object, for example on the tab Statistics.

To view all of the methods, read-only attributes, and attributes of the object, open the window Show Attributes and Methods. The figure below illustrates the information using the example of the object Station.

- Select Show Attributes and Methods on the context menu of the Class Library to show the methods, read-only attributes, and attributes of the selected Class [general description].
- Press the F8 key or click Show Attributes and Methods on the Home ribbon tab of the Frame into which you inserted an instance to show the methods, read-only attributes, and attributes of the selected Instance [general description].

To query the value of a read-only attribute, you might, for example, type:

```simtalk
print MyBroker.OpenCapacity
```

---

## AdministeredExporters [SimTalk]

Returns all Exporters/Workers which are registered with the Broker designated by `<Path>`.

**Remarks**

The array does not contain all Exporters/Workers that may be reached via the Broker-hierarchy, but only those that are registered directly with the Broker.

**Type**

Read-only attribute

**Syntax**

```
<Path>.AdministeredExporters → array
```

**Return Value**

The return value has the data type `array`.

**Examples**

```simtalk
print MyBroker.AdministeredExporters
var t :object[] := MyBroker.AdministeredExporters
```

**See also**

- Exporters [Broker]
- AdministeredExporters [SimTalk]

---

## MediatedCapacity [SimTalk] - Broker

Returns the capacity which the Broker designated by `<Path>` brokered.

**Type**

Read-only attribute

**Syntax**

```
<Path>.MediatedCapacity → integer
```

**Return Value**

The return value has the data type `integer`.

**Example**

```simtalk
print MyBroker.MediatedCapacity
```

**See also**

- Tab Statistics [Broker]
- MediatedCapacity [SimTalk] - Broker

---

## OpenCapacity [SimTalk]

Returns the total amount of open capacities which the Broker designated by `<Path>` could not fulfill.

**Type**

Read-only attribute

**Syntax**

```
<Path>.OpenCapacity → integer
```

**Return Value**

The return value has the data type `integer`.

**Example**

```simtalk
print MyBroker.OpenCapacity
```

**See also**

- Tab Statistics [Broker]
- OpenCapacity [SimTalk]

---

## OpenRequests [SimTalk]

Returns the actual number of open requests which the Broker designated by `<Path>` manages.

**Type**

Read-only attribute

**Syntax**

```
<Path>.OpenRequests → integer
```

**Return Value**

The return value has the data type `integer`.

**Example**

```simtalk
print MyBroker.OpenRequests
```

**See also**

- Tab Statistics [Broker]
- OpenRequests [SimTalk]

---

## SatisfiedRequests [SimTalk]

Returns the number of requests which the Broker designated by `<Path>` fulfilled.

**Type**

Read-only attribute

**Syntax**

```
<Path>.SatisfiedRequests → integer
```

**Return Value**

The return value has the data type `integer`.

**Example**

```simtalk
print MyBroker.SatisfiedRequests
```

**See also**

- Tab Statistics [Broker]
- SatisfiedRequests [SimTalk]

---

## StatMediatedCapacity [SimTalk]

Returns the total amount of brokered capacities which the Broker designated by `<Path>` manages.

**Type**

Read-only attribute

**Syntax**

```
<Path>.StatMediatedCapacity → integer
```

**Return Value**

The return value has the data type `integer`.

**Example**

```simtalk
print MyBroker.StatMediatedCapacity
```

**See also**

- Tab Statistics [Broker]
- Statistics report, Broker Statistics [described]
- StatMediatedCapacity [SimTalk]

---

## StatMediationTime [SimTalk]

Returns the sum of the times which the Broker designated by `<Path>` required to meet all satisfied requests.

**Remarks**

This is the time during which the importer/importers were waiting for the services.

**Type**

Read-only attribute

**Syntax**

```
<Path>.StatMediationTime → time
```

**Return Value**

The return value has the data type `time`.

**Example**

```simtalk
print MyBroker.StatMediationTime
```

**See also**

- Statistics report, Broker Statistics [described]
- StatMediationTime [SimTalk]

---

## StatMediationTimeDelta [SimTalk]

Returns the standard deviation of the medium procurement time which the Broker designated by `<Path>` required to meet all satisfied requests.

**Type**

Read-only attribute

**Syntax**

```
<Path>.StatMediationTimeDelta → time
```

**Return Value**

The return value has the data type `time`.

**Example**

```simtalk
print MyBroker.StatMediationTimeDelta
```

**See also**

- Statistics report, Broker Statistics [described]
- StatMediationTimeDelta [SimTalk]

---

## StatMediationTimeMu [SimTalk]

Returns the medium duration of the time which the Broker designated by `<Path>` required to meet a single request.

**Type**

Read-only attribute

**Syntax**

```
<Path>.StatMediationTimeMu → time
```

**Return Value**

The return value has the data type `time`.

**Example**

```simtalk
print MyBroker.StatMediationTimeMu
```

**See also**

- Statistics report, Broker Statistics [described]
- StatMediationTimeMu [SimTalk]

---

## StatOpenCapacity [SimTalk]

Returns the total amount of open capacities which the Broker designated by `<Path>` manages.

**Type**

Read-only attribute

**Syntax**

```
<Path>.StatOpenCapacity → integer
```

**Return Value**

The return value has the data type `integer`.

**Example**

```simtalk
print MyBroker.StatOpenCapacity
```

**See also**

- Tab Statistics [Broker]
- Statistics report, Broker Statistics [described]
- StatOpenCapacity [SimTalk]

---

## StatOpenRequests [SimTalk]

Returns the total number of open requests which the Broker designated by `<Path>` manages.

**Type**

Read-only attribute

**Syntax**

```
<Path>.StatOpenRequests → integer
```

**Return Value**

The return value has the data type `integer`.

**Example**

```simtalk
print MyBroker.StatOpenRequests
```

**See also**

- Tab Statistics [Broker]
- Statistics report, Broker Statistics [described]
- StatOpenRequests [SimTalk]

---

## StatSatisfiedRequests [SimTalk]

Returns the total number of requests which the Broker designated by `<Path>` satisfied.

**Type**

Read-only attribute

**Syntax**

```
<Path>.StatSatisfiedRequests → integer
```

**Return Value**

The return value has the data type `integer`.

**Example**

```simtalk
print MyBroker.StatSatisfiedRequests
```

**See also**

- Tab Statistics [Broker]
- Statistics report, Broker Statistics [described]
- StatSatisfiedRequests [SimTalk]

---

## StatStayTime [SimTalk]

Returns the sum of the times during which Exporters/Workers stayed at importers.

**Remarks**

These are the times during which the services managed by the Broker designated by `<Path>` were brokered.

**Type**

Read-only attribute

**Syntax**

```
<Path>.StatStayTime → time
```

**Return Value**

The return value has the data type `time`.

**Example**

```simtalk
print MyBroker.StatStayTime
```

**See also**

- Statistics report, Broker Statistics [described]
- StatStayTime [SimTalk]

---

## StatStayTimeDelta [SimTalk]

Returns the standard deviation of the time during which Exporters/Workers stayed at importers who are managed by the Broker designated by `<Path>`.

**Type**

Read-only attribute

**Syntax**

```
<Path>.StatStayTimeDelta → time
```

**Return Value**

The return value has the data type `time`.

**Example**

```simtalk
print MyBroker.StatStayTimeDelta
```

**See also**

- Statistics report, Broker Statistics [described]
- StatStayTimeDelta [SimTalk]

---

## StatStayTimeMu [SimTalk]

Returns the medium duration of the time during which Exporters/Workers stayed at a single importer who is managed by the Broker designated by `<Path>`.

**Type**

Read-only attribute

**Syntax**

```
<Path>.StatStayTimeMu → time
```

**Return Value**

The return value has the data type `time`.

**Example**

```simtalk
print MyBroker.StatStayTimeMu
```

**See also**

- Statistics report, Broker Statistics [described]
- StatStayTimeMu [SimTalk]
