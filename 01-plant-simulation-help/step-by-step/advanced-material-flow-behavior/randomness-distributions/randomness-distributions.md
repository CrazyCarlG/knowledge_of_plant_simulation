# Randomness Distributions

> Source: Plant Simulation Help — Modeling Random Processes (pp. 10-304 to 10-308)

## Model Random Processes

Many computer programs use random number generators to create a stream of random numbers generally located in the interval between 0 and 1. Starting from given start values — the so-called **seed values** — a large number of stochastically independent random numbers has to be available.

Examples of random number usage in computer programs:

- **Gaming programs** use random numbers to allow greater diversity of the operating sequence of the game.
- **Database programs** use random numbers to enter a large number of data sets and thus test the functionality of the database.
- **Simulation programs** (such as Plant Simulation) use random numbers to represent, among others, the interval between failures of machines.

## Random Numbers and Their Statistical Distribution

There are **deterministic processes** and **random processes**:

- For a **deterministic process**, the result can be predicted, for example by knowing a law of nature.
- If all factors that characterize a process are not known, its result is **random**.

When simulating production processes:

- The occurrence of pauses is a deterministic process.
- Failures of machines or the rejects produced are random processes.

A random process results in a **random number**. The replication of the process results in the **realization** of the random number. For example, throwing dice is a random process; the resulting number of points is the associated random number.

### Discrete vs. Continuous Random Numbers

**Discrete** random numbers have individual, separate values (limited or unlimited in count), such as the number of rejects over a long period of time or the number of orders during a day. A limited number may result from throwing dice; an unlimited number can be a countable amount. These values can be simplified to 0, 1, 2, etc. To describe the random number, specify the probability for the individual numbers; the sum of all probabilities must be 1 (as one of the numbers will always be thrown).

**Continuous** random numbers can take all values within a limited or unlimited interval. Examples are the **mean time between failures (MTBF)** and the **mean time to repair (MTTR)** of a machine. For a continuous random number, you cannot specify the probability for an individual number; instead you specify the probability that the random number lies between two given values (an interval).

### Probability Density Function

The **probability density function** describes the distribution of a random number:

- The density function of a continuous random number only has values greater than or equal to 0, and can be drawn continuously without interruption.
- The area underneath the function between two values `a` and `b` is the probability that the random number lies between `a` and `b`.
- The value of the density function at position `x` describes how often a value approximating `x` will occur.
- The entire area below the curve has the value 1 (each realization always produces some value).

#### Example: Gamma Distribution

For the gamma distribution with parameters **Alpha = 3** and **Beta = 5.5**:

- Most random numbers occur near the apex of the density function (`x = 11`), called the **modal value** (mode).
- The **mean value** of many realizations is substantially greater than the mode — around 16.5.
- The distribution creates random numbers between 24 and 26 with a probability of 0.04 (equal to the gray area under the curve).

## Use Pseudo Random Numbers

It seems impossible to simulate random processes with a computer, because a computer computes numbers according to fixed stipulated calculation rules. A computer cannot create a truly random sequence of numbers — such a sequence can only approximately have the properties of random numbers, which is why they are called **pseudo random numbers**.

- The sequence of numbers a computer creates is called a **random number stream**.
- The computer computes the following number starting from a random number. The algorithm starts with **seed values** and can generate any number of values from them.
- Using different seed values lets you model several random processes that are independent of each other.

To create a random number, it often suffices to create a **uniformly distributed** random number in the interval `(0,1)`. A random number is uniformly distributed when the probability for an interval depends only on its length, not on its position on the number line. From a uniformly distributed random number, the computer can algorithmically create, for example, a normally distributed random number with a given mean value and standard deviation.

A uniformly distributed pseudo random number must meet these requirements:

- The arrangement of the random numbers shows no typical characteristics (the algebraic signs of consecutive random numbers display no typical patterns).
- The algorithm has to become periodic (the computer has only a finite number of states), so the period length has to be as large as possible.
- Starting from the given seed values, a large number of stochastically independent random numbers has to be available for the simulation.
- The random processes of a simulation have to be reproducible to allow certain statistical methods, such as variance reduction.

## Use Probability Distributions

As a rule, only very few observed data about a random process (such as the interval between two failures of a machine) are available.

To reproduce these random processes in a simulation model, Plant Simulation provides a number of probability distributions — see **Probability Distributions**, **Empirical Distributions**, and **User-defined Distributions**.

**Step 3: Decide Which Distribution to Use** assists in picking the right distribution using the object **DataFit**.

When you select a distribution from the list, Plant Simulation shows the parameters the distribution requires along the upper border of the tab. Calculate the respective values from the observed data (received from the customer) and type them into the text box. The **lower bound** and **upper bound** are optional — you can, but do not have to, specify them.
