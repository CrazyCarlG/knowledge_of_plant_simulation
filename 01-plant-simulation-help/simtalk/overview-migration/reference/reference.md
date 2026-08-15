# SimTalk Reference

## Overview

SimTalk is the programming language integrated in Plant Simulation. It lets you implement custom behavior and logic in your simulation model that is not covered by the built-in functionality of the simulation objects.

## Remarks

- SimTalk contains an **Interpreter** that directly executes the instructions you write in objects of type **Method** when Plant Simulation runs the simulation.
- SimTalk is tightly integrated with the simulation objects. You can access all **attributes**, **read-only attributes**, and **methods** of the built-in objects.

## Notes

- The **Copilot** accesses the Plant Simulation Help and can assist you in writing source code in a Method.
- The **Copilot (local)** provides a better knowledge base and the ability to hook up your own LLM to solve programming tasks.
- You can create your own reusable objects in an object of type **Dialog** with behavior for your specific needs, implemented in SimTalk. Together with the integrated **Method Debugger**, SimTalk is an easy-to-use programming environment.
- Instead of programming in SimTalk, you can also program code in **Python**.

## Python vs. SimTalk

- Python code is **not intended to replace SimTalk code**.
- Since SimTalk code accesses compiled built-in functions, it is generally quite a bit **faster** than Python code.
- Because many university graduates are exposed to Python, the **PythonModule** makes programming in Plant Simulation easier and faster.

## SimTalk 2.0

- SimTalk 2.0 was introduced in Plant Simulation 12.1, simplifying the syntax and adding features to make writing code easier.
- The Plant Simulation Help only describes SimTalk 2.0. The topic **SimTalk 2.0 and SimTalk 1.0 Compared** describes the major differences.
- SimTalk 1.0 still works in the current and previous versions of Plant Simulation, and you can continue using it in old and new models.
- The command **Find Outdated Functions** on the Debugger ribbon tab finds outdated methods, attributes, read-only attributes, and functions in the source code of all Methods in your simulation model.

## Description Structure

The description of SimTalk is divided into:

- **General Access to SimTalk**
- **SimTalk Access to 3D Functions**

## Language Support

- SimTalk supports **English and German** for programming the source code of your methods.
- For this reason, the German Help shows the English name of the attribute, read-only attribute, or method next to the German name, separated by a forward slash. Example:

```simtalk
EnergieAktiv [SimTalk] / EnergyActive
```

- This facilitates programming methods when working with the German version of Plant Simulation while creating an English-language model that colleagues in other countries can use.
- See also: **Creating a German Model with English Identifiers**.

## See Also

- What's New
- SimTalk Reference
- Introducing Plant Simulation
- Update Arbitrary Old Models
- The User Interface Components
- The Step-by-Step Help
- Outdated SimTalk Names
- The Quick Reference Card
- The Add-Ins Reference Help
- The Libraries Reference
