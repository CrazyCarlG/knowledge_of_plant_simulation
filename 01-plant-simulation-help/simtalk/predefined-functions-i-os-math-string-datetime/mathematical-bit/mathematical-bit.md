# Mathematical Functions

Plant Simulation provides a number of mathematical functions. You do not have to enter a path for the mathematical functions.

- Basic Mathematical Functions
- Functions for Numerical Values
- Trigonometric Functions
- Distribution Functions, z_ functions
- Functions for Manipulating Individual Bits
- Functions for Editing Variables of Data Type String

See also: Arithmetic Operators, Mathematical Functions.

---

## Basic Mathematical Functions

Plant Simulation provides a number of basic mathematical functions.

| Function | Type | Results in |
|---|---|---|
| `abs` | `abs(x)` | the absolute value of \|x\| |
| `beta` | `beta(x,y)` | the beta function beta(x,y), x, y > 0 |
| `betai` | `betai(x,y,z)` | the incomplete beta function betai(x,y), x, y > 0 and 0 <= z <= 1 |
| `exp` | `exp(x)` | the exponential function e^x. The parameter is any number of data type real. |
| `gamma` | `gamma(x)` | the gamma function Γ(x), x > 0 |
| `log` | `log(x)` | the natural logarithm |
| `log10` | `log10(x)` | the logarithm to the base of 10 |
| `pow` | `pow(x,y)` | x^y |
| exponentiation operator | `x ** y` | the exponentiation operator. Is the same as `pow(x,y)`. |
| `sqrt` | `sqrt(x)` | the square root. The parameter of data type real has to be equal to or greater than 0. |

For `pow`:
- If the basis is 0, the exponent has to be greater than 0.
- If the exponent is not an integer, for example -0.5, the basis has to be greater than or equal to 0.

Notes:
- The square root function `sqrt` only accepts parameters greater than or equal to 0.
- The functions `sqrt` and `pow` also support the use of a physical unit. For `sqrt` this is limited though: if the radicand has a square unit, the result has the non-square unit. For other powers of units Plant Simulation returns a number of data type real without a unit.
- When using the functions `exp`, `pow`, `gamma` and the arithmetic operators in SimTalk, you have to make sure that the result is located within the range of numbers your computer can show. Use the gamma function to compute the factorial of a number n: n! = 1 · 2 · … · n = Γ(n+1).

### Parameter

The parameter for the basic mathematical functions has the data type real or integer, or it can be a value with a physical unit.

### Return Value

The return value has the data type real.

### Example

```simtalk
var area := 2m * 2m;
print area        // outputs 4m² in the Console
print sqrt(area)  // outputs 2m in the Console

-- exponentiation operator ** instead of pow
var x: real := 2
var y: real := 3
var z: real := x ** y  // z = 2*2*2 = 8
```

See also: Arithmetic Operators, Basic Mathematical Functions.

---

## Functions for Numerical Values

Plant Simulation provides a number of functions for numerical values.

| Function | Type | Results in |
|---|---|---|
| `ceil` | `ceil(x)` | the smallest integer number greater than or equal to x |
| `floor` | `floor(x)` | the greatest integer number smaller than or equal to x |
| `max` | `max(x,y[,z, ...])` | the maximum |
| `min` | `min(x,y[,z, ...])` | the minimum |
| `round` | `round(x)` | the next integer number. `print round(-1.5)` yields -2 |
| `round` | `round(x:real, places:integer)` | the rounding of the real number x to the number of specified places |

Note: You can specify more than two parameters for the functions `max` and `min`. For the functions `max` and `min` you cannot mix data types arbitrarily, i.e., all data types either have to be numerical, or all data types have to be of data type date and dateTime, or all have to be of data type string.

### Parameters

The parameter for the functions for numerical values can have the data type real, integer, or it can be a value with a physical unit. The parameter can also have the data type date, dateTime, or string for the functions `min` and `max`.

### Return Value

The return value has the same data type as the parameter that you specify.

See also: Arithmetic Operators, Functions for Numerical Values.

---

## Trigonometric Functions

Plant Simulation provides a number of trigonometric functions.

| Function | Type | Results in |
|---|---|---|
| `acos` | `acos(x)` | the arc cosine of x |
| `asin` | `asin(x)` | the arc sine of x |
| `atan` | `atan(x)` | the arc tangent of x |
| `atan2` | `atan2(y,x)` | the arc tangent of y and x |
| `cos` | `cos(x)` | the cosine of x |
| `sin` | `sin(x)` | the sine of x |
| `tan` | `tan(x)` | the tangent of x |

### Parameter

Trigonometric functions expect the parameter in radians or return the result in radians. You can specify parameters of data type real or integer.

### Return Value

The return value has the data type real.

### atan2

The function `atan2(y, x)` returns the angle in radians between the positive x-axis of a plane and the point given by the coordinates (x, y) on it for any real number arguments x and y, both of which are not equal to zero.

Type: Function.

#### Syntax

```
atan2(y:real, x:real) → real
```

#### Parameters

- The parameter `y` of data type real designates the coordinate on the y-axis.
- The parameter `x` of data type real designates the coordinate on the x-axis.

#### Return Value

The return value has the data type real. The angle is positive for counter-clockwise angles (upper half-plane, y > 0), and negative for clockwise angles (lower half-plane, y < 0). For x=0 and y=0 the function returns 0.

---

## Distribution Functions, z_ functions

Create probability distributions with the distribution functions (z_functions).

### Remarks

You can create random numbers for times in the dialogs of the objects on the Tab Times and on the Tab Failures, with a Variable of data type randtime, and in SimTalk with the functions described below.

Plant Simulation provides these distribution functions:

| Function | Results in this distribution |
|---|---|
| `z_beta([Stream:integer,]Alpha1:real,Alpha2:real) -> real` | Beta |
| `z_binomial([Stream:integer,]n:integer,p:real) -> real` | Binomial |
| `z_cauchy([Stream:integer,]Mu:time,Theta:real[,LowerBound:real,UpperBound:real]) -> real` | Cauchy |
| `z_cemp([Stream:integer,]Table:table) -> real` | cEmp (continuous empirical distribution) |
| `z_demp([Stream:integer,]Table:table) -> real` | dEmp (discrete empirical distribution) |
| `z_emp([Stream:integer,]Table:table,Column:integer) -> integer` | Emp (primitive empirical distribution) |
| `z_erlang([Stream:integer,]Mu:time,Sigma:time[,LowerBound:real,UpperBound:real]) -> real` | Erlang |
| `z_frechet([Stream:integer,]Mu:time,Theta:real[,LowerBound:real,UpperBound:real]) -> real` | Fréchet |
| `z_gamma([Stream:integer,]Alpha:real,Beta:time[,LowerBound:real,UpperBound:real]) -> real` | Gamma |
| `z_geom([Stream:integer,]p:real[,LowerBound:real,UpperBound:real]) -> real` | Geom |
| `z_gumbel([Stream:integer,]Mu:time,Theta:real[,LowerBound:real,UpperBound:real]) -> real` | Gumbel |
| `z_hypgeom([Stream:integer,]m:integer,n:integer,p:real) -> real` | Hypgeo |
| `z_laplace([Stream:integer,]Mu:time,Theta:real[,LowerBound:real,UpperBound:real]) -> real` | Laplace |
| `z_logistic([Stream:integer,]Mu:time,Theta:real[,LowerBound:real,UpperBound:real]) -> real` | Logistic |
| `z_loglogistic([Stream:integer,]Mu:time,Theta:real[,LowerBound:real,UpperBound:real]) -> real` | Loglogistic |
| `z_lognorm([Stream:integer,]Mu:time,Sigma:time[,LowerBound:real,UpperBound:real]) -> real` | Lognorm |
| `z_negexp([Stream:integer,]Beta:time[,LowerBound:real,UpperBound:real]) -> real` | Negexp |
| `z_normal([Stream:integer,]Mu:time,Sigma:time[,LowerBound:real,UpperBound:real]) -> real` | Normal |
| `z_paralogistic([Stream:integer,]Mu:time,Theta:real[,LowerBound:real,UpperBound:real]) -> real` | Paralogistic |
| `z_pareto([Stream:integer,]Mu:time,Theta:real[,LowerBound:real,UpperBound:real]) -> real` | Pareto |
| `z_poisson([Stream:integer,]Lambda:real) -> real` | Poisson |
| `z_triangle([Stream:integer,]c:real,a:real,b:real) -> real` | Triangle (triangular distribution) |
| `z_uniform([Stream:integer,]LowerBound:real,UpperBound:real) -> real` | Uniform |
| `z_weibull([Stream:integer,]Alpha:real,Beta:time) -> real` | Weibull |

### Parameters

- The parameter `Stream` of data type integer designates the random number stream (compare Random Number Seed Values).
  - If you call one of the distribution functions in a Method, the parameter `Stream` is optional. If you do not specify the stream, Plant Simulation uses the random number stream of the Method or of the user-defined attribute of data type method.
  - You can also call the distribution functions with the parameter `Stream`. For formulas this is required, as formulas never use the random number stream of the surrounding object.
- All other parameters are the parameters of the corresponding distribution function as described under Probability Distributions. They all either are of data type real or integer.

### Return Value

The return value has the data type real. The distribution function `z_emp` returns a value of data type integer.

### SimTalk / See also

- RandomSeed - Method/User-defined Attribute
- `resetRandomNumberStream`
- Parameters of the Distributions
- Probability Distributions
- Methods of the Distributions

---

## Individual Distribution Functions

### Cauchy — `z_cauchy`

The Cauchy distribution is a continuous probability distribution.

Remarks: Use the Cauchy distribution to represent the occurrence of failures while developing large systems.

Syntax:

```
z_cauchy([Stream:integer,]Mu:time,Theta:real[,LowerBound:real,UpperBound:real]) → real
```

Parameters: The parameters are µ and θ, both of which have to be greater than 0. The mean value and the standard deviation cannot be computed from the parameters.

Return Value: The return value has the data type real.

### Fréchet — `z_frechet`

The Fréchet distribution is also called the Gumbel type II distribution or the inverse Weibull distribution.

Remarks: Use the Fréchet distribution and the Gumbel distribution if you want to find out the maximum of several random numbers.

Syntax:

```
z_frechet([Stream:integer,]Mu:time,Theta:real[,LowerBound:real,UpperBound:real]) → real
```

Parameters: The parameters µ and θ have to be positive.

Return Value: The return value has the data type real.

### Gumbel — `z_gumbel`

The Gumbel distribution is also called the log-Weibull, the Gumbel type I distribution or the extreme value distribution.

Remarks: Use the Gumbel distribution to model the distribution of the maximum (or the minimum) of a number of samples of various distributions.

Syntax:

```
z_gumbel([Stream:integer,]Mu:time,Theta:real[,LowerBound:real,UpperBound:real]) → real
```

Parameters: The parameters µ and θ have to be positive. The parameter µ determines the mean value of the distribution. The variance is (where γ is the Euler-Mascheroni constant) σ² = π²·θ² / 6.

Return Value: The return value has the data type real.

### Laplace — `z_laplace`

The Laplace distribution is a continuous distribution. The Laplace distribution is also called the Double-exponential distribution.

Syntax:

```
z_laplace([Stream:integer,]Mu:time,Theta:real[,LowerBound:real,UpperBound:real]) → real
```

Parameters: The parameters are µ and σ > 0. The parameter µ sets the mean value of the distribution. The parameter σ > 0 sets the standard deviation of the distribution.

Return Value: The return value has the data type real.

### Logistic — `z_logistic`

The logistic distribution is a continuous probability distribution.

Remarks: Use the logistic distribution to model a lifetime distribution.

Syntax:

```
z_logistic([Stream:integer,]Mu:time,Theta:real[,LowerBound:real,UpperBound:real]) → real
```

Parameters: The parameters are µ and σ > 0. The parameter µ sets the mean value of the distribution. The parameter σ > 0 sets the standard deviation of the distribution.

Return Value: The return value has the data type real.

### Loglogistic — `z_loglogistic`

The loglogistic distribution is also called the Fisk distribution.

Remarks: Use the loglogistic distribution to model an income and lifetime distribution.

Syntax:

```
z_loglogistic([Stream:integer,]Mu:time,Theta:real[,LowerBound:real,UpperBound:real]) → real
```

Parameters: The parameters are α > 0 and β > 0.

Return Value: The return value has the data type real.

### Paralogistic — `z_paralogistic`

The paralogistic distribution is a transformed Pareto distribution.

Syntax:

```
z_paralogistic([Stream:integer,]Mu:time,Theta:real[,LowerBound:real,UpperBound:real]) → real
```

Parameters: The parameters are α > 0 and θ > 0.

Return Value: The return value has the data type real.

### Pareto — `z_pareto`

The Pareto distribution is a power-law probability distribution.

Syntax:

```
z_pareto([Stream:integer,]Mu:time,Theta:real[,LowerBound:real,UpperBound:real]) → real
```

Parameters: The parameters are α > 0 and θ > 0.

Return Value: The return value has the data type real.

---

## Functions for Manipulating Individual Bits

SimTalk provides the functions listed in the table of contents to the left for manipulating individual bits of an integer value.

### BitAND

Executes a bitwise AND of value 1 and value 2 and returns the result.

Type: Function.

Syntax:

```
BitAND(Value1:integer, Value2:integer) → integer
```

Parameters:
- `Value1` of data type integer designates value 1.
- `Value2` of data type integer designates value 2.

Return Value: The return value has the data type integer.

### BitClear

Changes the value of the parameter `OriginalValue` by setting the bit with the number designated by the parameter `BitPosition` to the bit value 0. The function returns the result of this computation.

Type: Function.

Syntax:

```
BitClear(OriginalValue:integer, BitPosition:integer) → integer
```

Parameters:
- `OriginalValue` of data type integer designates the original value of the computation.
- `BitPosition` of data type integer designates the bit position. The value range for the bit position is 0 to 63. The least significant bit has the number 0, the most significant bit has the number 63.

Return Value: The return value has the data type integer.

See also: BitSet.

### BitOR

Executes a bitwise OR of value 1 and value 2 and returns the result.

Type: Function.

Syntax:

```
BitOR(Value1:integer, Value2:integer) → integer
```

Parameters:
- `Value1` of data type integer designates value 1.
- `Value2` of data type integer designates value 2.

Return Value: The return value has the data type integer.

### BitSet

Changes the value of the parameter `OriginalValue` by setting the bit with the number designated by the parameter `BitPosition` to the bit value 1. The function returns the result of this computation.

Type: Function.

Syntax:

```
BitSet(OriginalValue:integer, BitPosition:integer) → integer
```

Parameters:
- `OriginalValue` of data type integer designates the original value of the computation.
- `BitPosition` of data type integer designates the bit position. The value range for the bit position is 0 to 63. The least significant bit has the number 0, the most significant bit has the number 63.

Return Value: The return value has the data type integer.

See also: BitClear.

### BitShift

Shifts the bits of the value designated by the parameter `Value` using the number of digits designated by `NumberOfDigits` and returns the result.

Type: Function.

Syntax:

```
BitShift(Value:integer, NumberOfDigits:integer) → integer
```

Parameters:
- `Value` of data type integer designates the value.
- `NumberOfDigits` of data type integer designates the number of digits. It moves them to the left, if you specified digits greater than 0. It moves them to the right, if you specified digits smaller than 0.

Return Value: The return value has the data type integer.

### BitTest

Returns if in the `Value` the bit at the position designated by `BitPosition` is set (true) or not (false).

Type: Function.

Syntax:

```
BitTest(Value:integer, BitPosition:integer) → boolean
```

Parameters:
- `Value` of data type integer designates the value.
- `BitPosition` of data type integer designates the bit position. The value range for the bit position is 0 to 63. The least significant bit has the number 0, the most significant bit has the number 63.

Return Value: The return value has the data type boolean.

Example:

```simtalk
var i : integer := 40 // binary representation: 00101000
print bitTest(i, 3)   // returns true because the bit 3 is set
```

### BitXOR

Executes a bitwise XOR of value 1 and value 2 and returns the result.

Type: Function.

Syntax:

```
BitXOR(Value1:integer, Value2:integer) → integer
```

Parameters:
- `Value1` of data type integer designates value 1.
- `Value2` of data type integer designates value 2.

Return Value: The return value has the data type integer.

---

## Functions for Editing Variables of Data Type String

SimTalk provides the functions listed in the table of contents to the left for editing variables of data type string.

These functions do not change the contents of the strings, but work with copies of the strings. The result of this operation is the return value. This enables Plant Simulation to enter names of objects into message texts during a simulation run.
