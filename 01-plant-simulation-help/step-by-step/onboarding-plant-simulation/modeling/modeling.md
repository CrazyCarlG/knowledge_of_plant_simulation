# Modeling

> Source: `modeling.txtx` — "Getting to Know Plant Simulation" help section (Plant Simulation Help, © 2026 Siemens).

## Overview

This document introduces the basic concepts on which simulation is based and the basics of working with Plant Simulation. It covers the theoretical background of simulation and modeling concepts, and what to keep in mind before starting to model.

The section structure is:

- Simulation and Modeling Concepts
- What is Simulation?
- Time-Oriented Simulation and Event-Controlled Simulation
- Why Use Simulation?
- Implement a Simulation Project

Related topics (see also):

- Modeling the Material Flow
- Visualizing the Material Flow
- Working with Classes in the Class Library
- Using Inheritance
- Model Hierarchically (general)

---

## Simulation and Modeling Concepts

Simulation concepts and modeling concepts introduce the theoretical background of simulation and show what to keep in mind before modeling.

Operations research processes are intended to help make the right decisions, qualitatively and quantitatively. They formulate optimization models containing all relevant factors (target function, conditions, target description). These processes require increasing processing power the more detailed the model is; their results and acceptance are often not satisfactory.

Alongside linear optimization models, simulation is increasingly used for making the right decisions. Simulation offers good solutions for complex problems but does **not** automatically produce the actual optimum — justified by the comparatively low mathematical expenditure required to obtain that result.

As processes become more complicated and complex, and more factors must be included, simulation — with its analysis of real processes — becomes more important. Such processes cannot be covered by mathematical or optimization solution processes, or only with a large amount of resources.

The aim of simulation is to arrive at objective decisions by dynamic analysis, allowing managers to plan safely and ultimately reduce costs. When real systems and plants are too expensive for experiments and trial time is too limited/expensive, modeling, simulation, and animation are excellent tools for analyzing and optimizing time-dynamic processes.

---

## What is Simulation?

VDI Technical Rule 3633 defines simulation as **the emulation of a system, including its dynamic processes, in a model one can experiment with**. It aims to achieve results that can be transferred to a real-world plant. Simulation also defines the preparation, execution, and evaluation of carefully directed experiments within a simulation model.

### A typical simulation study follows these steps

1. **Check the real-world plant** — inspect the plant to be modeled and collect the data needed to create the simulation model.
2. **Abstract and model** — abstract the real plant and create the simulation model according to the aims of the study.
3. **Run experiments** — execute simulation runs to produce results, e.g., how often machines fail, how often they are blocked, which set-up times accrue per station type, and machine utilization.
4. **Interpret the data** — interpret the results produced by the simulation runs.
5. **Make decisions** — management uses the results as a base for decisions about optimizing the real plant.

### Model development is cyclical and evolutionary

Start with a first draft, then refine and modify it using the intermediary results of simulation runs. After several cycles, you arrive at the final model.

### Key questions a simulation expert must never lose sight of

- What do you want to accomplish with the simulation study?
- What are you examining?
- Which conclusions do you draw from the results of the simulation study?
- How do you transfer the results of the simulation study to the real-world plant?

---

## Time-Oriented Simulation and Event-Controlled Simulation

Plant Simulation is a **discrete, event-controlled** simulation program: it only inspects the points in time at which events take place within the model.

In reality, time elapses continually (e.g., a part moving along a conveyor shows no jumps in time — the distance-over-time curve is a continuous straight line). A discrete, event-controlled program, however, only considers points in time (events) that matter to the further course of the simulation. Examples of events:

- A part entering a station.
- A part leaving a station.
- A part moving on to another machine.

Movements in between are of little interest — only the **entrance** and **exit (Out)** events must be displayed correctly. When a part enters a material flow object, Plant Simulation computes the time until it exits that object and inserts an exit event into the list of scheduled events of the **EventController** for that point in time.

As a result, the simulation time displayed by the EventController jumps from event to event, as soon as an event is processed. The **List** shows all events that trigger an action (click the button to open it).

---

## Why Use Simulation?

Simulation is used for **planning a new plant** or **optimizing an existing plant**.

### Planning a new plant

Simulation helps to:

- Detect and eliminate problems that would otherwise require cost- and time-consuming correction during production ramp-up.
- Determine and optimize times (processing, failure, recovery, etc.) and plant throughput.
- Determine buffer sizes and the number of machines required for the intended throughput (knowing whether you need one or more machines of a type matters when a single machine costs hundreds of thousands of dollars).
- Determine the performance limits of machines and of the plant as a whole.
- Investigate how failures affect throughput and machine utilization.
- Determine how many workers/staff are required for the intended throughput.
- Gain knowledge about the behavior of the plant.
- Determine suitable control strategies for the machines and how they interact.
- Evaluate different alternatives by running multiple simulation experiments.
- Minimize investment cost for production lines without jeopardizing required output.

### Optimizing an existing plant

Simulation helps to:

- Optimize performance of existing production systems by implementing measures verified in a simulation environment first.
- Optimize devised control strategies.
- Optimize the sequence of orders to minimize tool changes.
- Test daily proceedings to ensure everything works smoothly.

### Putting the plan into practice

Simulation helps to:

- Develop a template for creating control strategies.
- Test different scenarios during the warm-up phase of the plant.
- Train machine operators in the different states machines and the plant can be in.

### General benefits

- Enhance productivity of existing production facilities.
- Reduce investment in planning new production facilities.
- Cut inventory and throughput time.
- Optimize system dimensions, including buffer sizes.
- Reduce investment risks by early proof of concept.
- Maximize use of manufacturing resources.
- Improve line design and schedule.

---

## Implement a Simulation Project

Developing a simulation model is a **cyclical and evolutionary** process: start with a first draft, then refine and modify it using intermediary results; after several cycles you arrive at the final model.

### Workflow before/during implementation

- **Describe the project**
  Determine the goals so the purpose becomes clear. Why examine a problem? Which questions need answers? Put the project definition in writing and consult it repeatedly — the purpose determines the effort to be made.

- **Plan the project**
  Create a concept of the model: initial values, model items, variables, logic of proceeding, and a preliminary description of the simulation experiments. Determine which parameters to change, which data to collect, and how to interpret it. List all functional units of the installation, group identical/similar functionality, and derive a list of application objects to create. Consider re-using existing objects; specify and plan remaining objects on paper. Define and describe interfaces for material and information flow. Outline reset and init methods.

- **Find out about the data you need and how to acquire it**
  Ensure early on that the data needed to run experiments will be available — acquiring data often involves a lot of time and effort. Have the name of a person responsible for acquiring the data from the client.

- **Build the simulation model**
  Build a first version in its simplest, most basic form. Build and test application objects one by one, then assemble the overall model. Document clearly — months later you may not remember how or why you solved a problem a certain way.

- **Verify the simulation model and check its validity**
  Verify that the modeled components perform the tasks they were programmed to do. Test every object individually, in combination, then in the overall model; ensure all parameters are correct. Then check validity: confirm functionality matches the planned/real plant and results are plausible and credible. Estimate the most important results and compare with the simulation. Introduce the model to a production or planning expert and discuss results, proceedings, and modeling approach.

- **Execute simulation experiments and collect the results**
  (Section continues; see the full help for experiment execution and result collection.)

---

## Notes

- No code examples are present in this source file — the content is conceptual prose describing simulation theory, the Plant Simulation event model, and project methodology.
