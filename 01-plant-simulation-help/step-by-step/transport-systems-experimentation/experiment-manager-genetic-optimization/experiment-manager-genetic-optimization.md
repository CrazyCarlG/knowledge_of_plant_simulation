# Experiment Manager & Genetic Optimization

## Overview

This document covers two related Plant Simulation capabilities:

1. **Running Simulation Experiments** with the `ExperimentManager` — validating a model and studying how input parameters affect output values.
2. **Optimizing Models with Genetic Algorithms** using the `GAWizard` — finding good parameterizations when many solution variants exist.

---

## Running Simulation Experiments

After creating a model, you validate it (ensure it shows intended properties/behavior). A simulation study examines how **input values** (model parameters) influence **output values** (result values).

Use the `ExperimentManager` to:

### 1. Arrive at statistically safe results

- Compare shop-floor data with simulation results when re-creating an existing plant.
- Assign different seed values to random components of the random number streams.
- The `ExperimentManager` changes seeds for each set of input values, producing a set of observations.
- For each output value (with fixed input values), it produces a **confidence interval** and a **min-max interval** (combined in a **box plot**) at a chosen confidence level.
- Conclusions about systems with random components can only be stated with a defined **confidence level (level of significance)**.

### 2. Optimize the results

Use **Genetic Algorithms** to determine parameters that lead to desired results or to optimize results.

> **Note:** The `ExperimentManager` dialog uses the Windows design (not the Siemens PLM standard design) because it is modeled with the `Dialog` object.

---

## Licenses

The `ExperimentManager` behavior depends on your license:

- **Runtime** — execute experiments; modify parameters in tables; cannot change the structure of the ExperimentManager model; cannot control distributed simulations.
- **Application** — also change the structure of the model.
- **Professional / Standard / Foundation** — additionally define experiments in a Method.
- **Student** — cannot control distributed simulations.

With the setting **Highest Available** for the remote license, different license types can be used as simulation machines (the controlling computer can also serve as a simulation machine).

> **Note:** A simulation study contains several experiments. Each experiment executes several simulation runs, each leading to an observation.

---

## Running a Simple Simulation Study

Three quick steps:

- **Step 1:** Define input and output values of the experiments.
- **Step 2:** Run the experiments with the defined settings.
- **Step 3:** Evaluate the results.

### Step 1: Define input and output values

- Each simulation study needs at least **one output value**.
- **Output values:** Click `Define Output Values` on the `Definition` tab. An output value can be a method or an attribute of an object. You can add a description for easier understanding. Drag an object onto the ExperimentManager to see all numerical attributes and methods usable as output values.
- **Results table:** If results are in a Plant Simulation table, drag the table onto the ExperimentManager to use it as the output value.
- **Input values:** Click `Define Input Variables` on the `Definition` tab. An input value can be an attribute of an object or an entry in a table. Before an experiment runs, the ExperimentManager sets input values; they are not changed during the runs.
- Hold **Shift** and drag an object onto the ExperimentManager to show all attributes in a dialog; hold **Ctrl** and click to select one or more attributes.
- Input values can also be **parameters of probability distributions**. The ExperimentManager recognizes: `Uniform`, `Triangle`, `Normal`, `Lognorm`, `Erlang`, `Negexp`, `Geom`, `Hypgeo`, `Weibull`, `Binomial`, `Poisson`, and `Beta`.
- To set the input values for experiments, click `Define Experiments` on the `Definition` tab.
- A simulation run must end. If using the `stop` method of the `EventController`, call `endSim` of the ExperimentManager at the appropriate place — or set an **End time** / `End` attribute on the EventController.

### Step 2: Run the experiments

1. Click **Reset** to reset the ExperimentManager.
2. Click **Start** to start the experiment run.

At the end, the ExperimentManager opens a report. Long runs can be executed overnight.

### Step 3: Evaluate the results

You can:
- View the results as a **table**.
- View the results in a **chart**.
- View the results in a **HtmlReport**.

#### View results as a table

- Click `Open Results` on the `Evaluation` tab to show an overview of all experiments (all input values and all mean values of the output values). Select a cell and press **F2** to show a results table in a subtable.
- Click `Detailed Results` to show values for all output values. Each experiment's observations form a sample from which these are computed:
  - Mean value
  - Standard deviation
  - Minimum
  - Maximum
  - Left bound of the confidence interval
  - Right bound of the confidence interval
- If a table is the output value, `DetailedResults` provides subtables with mean value, standard deviation, minimum, maximum.
- The `Observations` column provides results of all simulation runs for all output values.

#### View results in a chart

- Show **min-max intervals** or **confidence intervals** for output values.
- Optionally show 25%, 50%, and 75% **quartiles** for min-max intervals (under `Tools > Advanced Settings > Settings`).
- This display is a **box plot** showing the distribution of observations of an output value of an experiment.

#### View results in a HtmlReport

- Click `Report` to show results as a HtmlReport.
- Configure content under `Tools > Advanced Settings > Report` (auto-show report, save report, save `Results` table to an Excel file).
- Click `Folder` to select a target folder for the report/Excel file.
- Drag a Chart from the model over the ExperimentManager icon to add it to the report.

---

## Refining the Settings

Beyond the basic study, you can:

- **Set Static Parameters** — specific values for each experiment/parameter. You can also **Modify Settings in the Configuration Method** (under `Tools > Advanced Settings > Settings`) using a SimTalk method. The parameter (data type `integer`) designates the experiment number; the source code modifies the experiment's settings.
- **Set Dynamic Parameters** — under `Tools > Advanced Settings > Rules`, results of previous experiments produce the input values of the current experiment. A rule is a logic expression with a **condition** and an **action**.

### Dynamic parameter procedure

1. Select **use rules**.
2. Select a built-in rule from **Select rule**, or **Create a Rule of Your Own**.
3. Select **Rule is active** to execute the rule before the experiment.
4. Optionally enter the experiment number(s) for which the rule applies.
5. Enter a **Priority** (higher number = higher priority; priority 10 runs before priority 1).
6. Select **Use for first simulation run** to use the rule from the first experiment; otherwise it is used from the second experiment onward.

### Create a rule of your own

1. Click **Create New Rule** and enter a name.
2. Click **Table Condition** and enter values:
   - **Opening Parenthesis** level (inner parentheses evaluated first).
   - **Object** name whose attribute value to compare.
   - **Attribute** of that object.
   - **Operator**: `<`, `>`, `=`, `~=` (about equal), or `/=` (unequal).
   - **Value** or the name of the object/attribute to compare against.
   - **Closing Parenthesis** level.
   - **Boolean Operation**: `AND` or `OR` connecting the logical expressions.
3. Optionally test a condition in a Method (**Method Condition**).
4. Click **Table Action** and enter:
   - Object name whose attribute value to manipulate.
   - Attribute name.
   - Operator that manipulates the value.
   - Value that the operator adds, subtracts, or equates to the attribute.
5. Optionally program a Method (**Method Action**) that executes an action.

---

## Optimizing Models with Genetic Algorithms

Use **Genetic Algorithms** when the optimization task has a large number of solution variants. The **GAWizard** integrates genetic algorithms into a simulation model — for optimizations evaluated by simulation runs or by calculations in Methods.

### Key concepts

- Genetic algorithms are **stochastic** and usually produce only an approximate solution (sufficient for most practical applications).
- Solution proposals are called **individuals** (managed in a **generation**). Quality is measured by a **fitness value**.
- Solutions are passed to the simulation model; one or more simulation runs are started per solution; the resulting fitness value is passed back to the GAWizard.
- For models with **random components**, run several simulation runs per individual — each fitness value is an **observation**, and the algorithm uses the mean of observations. Set the number of observations on the `Define` tab.
- For **deterministic** simulations, use a single observation per individual.
- If a duplicate individual is created, the GAWizard reuses the already-evaluated fitness value (no wasted time).

> **License note:** Your Plant Simulation license determines how you can use the GAWizard.

### Configure the GAWizard

1. Insert the GAWizard from the **Tools** toolbar; double-click to open its dialog.
   - **Drag-and-Drop:** Hold **Shift** and drag tables (or objects to optimize attributes of) onto the GAWizard; change value ranges in the `ProblemDefinition` table (click `Open` next to "Definition of the optimization parameter" on the `Define` tab). Drag the object whose attributes/methods evaluate solutions onto the GAWizard; weight values via `Open` next to "Fitness calculation by table".
   - **Built-in GA objects:** Define a configuration method on the `Define` tab, then hold **Shift** and drag GA objects (`GASelection`, `GASequence`, `GARangeAllocation`, `GASetAllocation`) onto the Wizard and click **Apply**. The attribute `individual` designates the table of the individual to evaluate; transmit chromosome properties to the model in the configuration method. The method returns `true` when the parameterization is executable; otherwise the individual gets a **penalty value** (`penaltyValue` attribute, changeable via the F8 key).
2. Select optimization direction (**Minimum** or **Maximum**), **Size of generation**, and **Number of generations** on the `Define` tab.
3. Determine the fitness value:
   - **By table (`Fitness`):** Select "Fitness calculation by table" and click `Open`; enter target value names in the `Target value` column and weightings in the `Weighting` column.
   - **By method:** Select the radio button, insert a Method, click **Apply**. The return value is the fitness value and must have a numeric data type (`real`, `time`, etc.).
4. Click **Reset** and **Start** on the `Run` tab to start optimization.

You can stop after the active generation is fully evaluated, modify settings, then continue (the button shows **Wait** while evaluating, then **Start** again).

### After optimization

- A dialog shows the time taken. The wizard transfers the input values of the **best solution** into the simulation model.
- Start additional runs with **Reset** + **Start**, or right-click the GAWizard icon and choose **Reset** / **Start** / **Stop**.

### Number of simulation runs

The number of required simulation runs can become large. The GAWizard executes:

```
Number of simulation runs = observations per individual * (generation size + 2 * generation size * (number of generations - 1))
```

Example: 3 observations per individual, 10 generations, generation size 30:

```
3 * (30 + 2 * 30 * 9) = 1710 simulation runs
```

> In the first generation, the number evaluated equals the generation size; in each following generation it evaluates twice as many individuals.

If the number of individuals to generate is ≤ 50,000, the GAWizard recognizes already-evaluated individuals and applies their fitness values (same ID in the `Statistics of Fitness Values` table on the `Evaluate` tab). The attribute `lastGeneration4DuplicatesCheck` describes the last generation up to which duplicates are checked; the default `-1` checks all generations.

### Analyze the results of the optimization

- On the `Run` tab, the currently best fitness value is shown.
- Click **Show Evolution** on the `Evaluate` tab to open a diagram of the best, average, and worst fitness values per generation.
- Click **Show** (HTML Report group, `Evaluate` tab) to show results and the optimization course in a Report. Clear "Show detailed HTML report" when many individuals exist.
- For stochastic simulations, the chart shows **Min-Max intervals** of an individual's fitness values. If values fluctuate greatly, check whether optimizing the model makes sense.
- Click the buttons to analyze the statistics table of fitness values; **column 7** shows if individuals were created multiple times but evaluated only once.
- Click **Show** next to "Data of the report" for results and optimization history.

> **Note:** Use the attribute `DecimalSeparator` (data type `string`) to set `"."` or `","` as the decimal separator in results tables.

---

## For the Advanced User

To start several optimizations one after the other with a BATCH file, compare **Specifying Start Options**. Plant Simulation may not open any modal dialogs that require user actions.
