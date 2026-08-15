# Preparing Data for the Simulation with DataFit

> Back to Model a Battery-powered Transporter, Extended

One purpose of a simulation study is to optimize the availability of resources (machines, laborers, vehicles, etc.) for an existing or planned production plant. This means reducing the number of failures and down-times of machines. When a machine fails, it has to be repaired, which delays production and costs money.

The Mean Time Between Failures (MTBF) and the Mean Time To Repair (MTTR) are often stochastically distributed. The type of distribution is known from the qualitative properties of the system; the parameters of the distribution are what must be determined.

Availability is defined as:

```
Availability = MTBF / (MTBF + MTTR) × 100%
```

When two of the three values (AV/availability, MTTR, MTBF) are known, the third can be computed. The **DataFit Wizard** computes the distribution parameters for MTTR and MTBF to arrive at the availability you want to achieve.

> **Note:** The DataFit objects were modeled in Frames and with the object Dialog, so they use the Windows design rather than the Siemens PLM standard design.

**See also:** Compare Statistics Tools

---

## Step 1: Define the Task and the Objectives

Start by defining the task and objective of the simulation study, being careful not to predefine any one solution you might expect or want to be true.

Questions you want answers for:

- What throughput and output can we expect?
- What is the optimal number of resources (machines, workers, tools)?
- Where in the plant are buffers necessary? What is the optimal buffer size?
- What is the optimal number of work piece carriers?
- Which control strategies are best suited for the task?
- How do some or all of the above factors interact and produce different results?

Then decide the scope of the simulation:

- Do you only need to simulate the production plant?
- Or do you also have to simulate other areas, such as receiving parts delivered by suppliers, warehousing, shipping, etc.?

---

## Step 2: Collect and Prepare Data

Collecting and preparing data is one of the most important tasks. It takes up about **35%** of the project time:

- Creating the model: 25%
- Validating and correcting: 15%
- Running experiments: 10%
- Analyzing and evaluating: 15%

### Data types used

**Static data:**

- Data extracted from the production program (collected by watching machines or received from shop-floor experts).
- Data extracted from the structure of the plant.
- Data from a shift model.

**Stochastic data:**

- The failure behavior.
- The processing and set-up times.
- The amount of rejects.

### Data needed for material flow of interlinked production/assembly facilities

**1. Data covering the entire production system (model data):**

- The production program (produced products, lot sizes, etc.).
- The layout of the plant, its structure, controls, and the points where parts are introduced into or discharged from the system.
- Reworking (reworking times, the station that produces rejects, and the frequency of rejects).

**2. Data covering the staff (object data):**

- The number of workers and their qualifications.
- The shifts worked.
- The distances covered and the required times.

**3. Data covering machines, transport systems and work stations (object data):**

- Failures, including MTBF, MTTR, reference time, distribution, and variance.
- Cycle times, capacities and cycle variance.
- Set-up times.
- Supply with materials.

---

## Step 3: Decide Which Distribution to Use

Once data is collected, decide:

- Which distributions to select for the Processing Time, Set-up Time, Recovery Time, Cycle Time, and Failure Times.
- Which parameters to enter for the selected distribution.

For this, Statistics Wizards are provided. You can:

- Practice Distribution-Fitting with DataFit.
- Use Distributions with Bounds.

**See also:** Compare Model Random Processes

---

## Distribution-Fitting with DataFit

Use the object **DataFit** for distributions without bounds.

Proceed as follows:

- Enter a sample of observations of a random number and a **Level of significance**.
- The Wizard then finds the parameters of the selected distribution.

The Wizard estimates the parameters of the selected distribution(s) and performs a **goodness-of-fit** test with the filtered data on the **Fit** tab.

> **Note:** The Level of significance is the probability with which a distribution with estimated parameters will be rejected by the goodness-of-fit test, although it is suitable for the sample.

**Compare sample models:** Click the Window ribbon tab, click Start Page > Getting Started > Example Models > Small Examples. Then select the respective Category, Topic, and Example in the dialog Examples Collection, and click Open Model.

**See also:** Compare Statistics Tools

---

## Input Data in DataFit

> **Note:** DataFit only computes distribution parameters for a sample with **more than 10 values**.

You can only proceed to the next tab after selecting the required settings and typing the data on the active tab. DataFit then activates buttons and/or text boxes on the next tab. Most buttons are toggle buttons that turn a feature on or off.

### Import data to be fitted (tab Input)

- Import the data (sample data observed on the shop floor, or results of a previous simulation run) into a column of a Plant Simulation table file. Then drag this table over the object DataFit in the Frame and drop it there.
- Select a column that contains the data in the dialog that opens and click **Load**.

Or:

- Click **Read** to import data from the file whose name you type into the **Data file** text box.
- When importing from other programs (e.g., Excel), select the same **Decimal separator** in Plant Simulation that you used in the other application. You might also paste the sample data into the table via the Windows clipboard (click **Open** to open the input table).

### Select the data type

- **Discrete numbers** — any integer number greater than or equal to 0 (0, 1, 2, 3, etc.).
- **Continuous numbers** — includes negative numbers and floating point numbers (e.g., -10, 1.4, 5, ...).

When all required data is entered or settings selected, proceed to the **Filter** tab.

---

## Filter Data in DataFit

Filter the data on the **Filter** tab. Filtering serves three purposes:

1. It cuts off data that is atypical.
2. It eliminates outliers (removes these values from the sample).
3. It transforms data to a certain range (translates or zooms data).

To filter data:

- You can (but do not have to) enter a value for the **Lower bound** and a value for the **Upper bound**.
- Click **Start** to start filtering the data.
- This activates the buttons **Show descriptive statistics** and **Open filtered data**.
  - Clicking **Show** opens a table with descriptive statistics of the characteristics of the sample data.
  - Clicking **Open filtered data** opens a table with the sorted data to be used for data fitting (i.e., after eliminating unwanted values).

Once done, proceed to the **Fit** tab.

---

## Fit Data in DataFit

DataFit estimates the parameters of the selected distribution(s) and performs a goodness-of-fit test with the filtered data on the **Fit** tab.

- Click **Select** and select one, several, or all distributions in the dialog that opens.
- Enter a **Level of significance** (a number between 0 and 1; in most cases between 0 and 0.2).
- Click **Fit** to estimate the parameters for the selected distribution(s) using the sample.
- For a large sample, use the **Chi-Square Test** as the Goodness-of-Fit Test, entering the **Number of classes**. The Goodness-of-Fit Test describes how well the distribution with its parameters fits the given sample.
- Click **Show** to display a histogram of the sample in a chart.

Once done, proceed to the **Evaluation** tab.

---

## Evaluate Data in DataFit

Perform an analysis of the filtered data on the **Evaluation** tab.

Select how DataFit sorts the fitting tests:

- **Chi-Square test** — suits all purposes. It splits the sampled data into classes. The sample must have more than **40 values**.
- **Kolmogorov-Smirnov** and **Anderson-Darling** tests — only suited for continuous distributions with **10 to 2000 values**.

Open the results table that shows which parameters of which distribution to enter in Plant Simulation:

- The columns **Result Chi**, **Result KS**, **Result AD** tell whether the distributions are applicable to the sampled values. This is the case when the respective value statistic is less than the respective value. Naturally, the evaluation takes the Level of significance into account.
- The columns **Parameter 1**, **Parameter 2**, and **Parameter 3** show the exact numbers and the names of the rounded parameters as you enter them into the dialogs of the Plant Simulation objects.
- Click **Show** to show a Report of the parameters and the goodness-of-fit test.
- Click **Delete** to reduce the size of the model, which might have been bloated by the Report.
- When none of the selected distributions adequately represent the sample, use an **empirical distribution** to model the data in Plant Simulation. Click **Open** to open the Frequency table.

---

## Use Distributions with Bounds

The distributions used in a simulation may have realizations that are arbitrarily large or small. Use distributions with upper and lower bounds to cut off values you do not want to consider.

> **Be aware:** Using a distribution with bounds changes the mean value and the standard deviation.

When using the normal distribution for modeling a random time, the lower bound automatically is 0.

Example: when you type in the parameters **µ = 2.0** and **σ = 1** for the normal distribution, a real mean value of the distribution with the lower bound 0 and the upper bound 3 will be **1.77**.

Use the object **TruncDistribution** for distributions with bounds:

- Select a distribution and both bounds.
