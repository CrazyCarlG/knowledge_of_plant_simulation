# 文件夹模型（Folder Model）总结

本目录包含 `folder-model.md`，说明 Plant Simulation 的**文件夹模型（Folder Model）**保存格式——即把模型保存为「文件夹 + 多文件」的目录结构，便于用 Git 等版本控制系统管理。以下为要点总结。

## 1. 是什么

文件夹模型（`.psfm`）本质是一个**目录**，内部是多个文本文件，而非单个二进制文件。设计目的是让模型能被 Git 逐文件 diff / commit。

## 2. 内部结构

| 文件 | 作用 |
| --- | --- |
| `$.spp` | 根部模型主文件，`loadModel` 的入口 |
| `$.yaml` | 每 Frame 一个，含该 Frame 全部对象（默认） |
| 独立 `.yaml` | `CompactFormat=true` 时，有原点的对象各自成文件 |
| `.py` | PythonModule 代码 |
| `.UserSettings.yaml` | 用户设置，被 `.gitignore` 忽略 |

## 3. 关键函数

- `saveFolderModel(FileName, CompactFormat:=false, UseGit:=false)` —— 以文件夹结构保存；`CompactFormat=true` 拆独立 `.yaml`，`UseGit=true` 自动建 Git 仓库。
- `loadModel("...\MyFolderModel.psfm\$.spp")` —— 加载，入口是文件夹里的 `$.spp`。

## 4. 说明

- 本篇为**汇编条目**：官方第 9 章 *What is a Folder Model?*（p.264–273）尚未转录入本知识库，本篇由 `saveFolderModel` / `loadModel` / PythonModule / Method.RandomSeed 等已有条目汇编而成，非第 9 章原文。

*来源：Plant Simulation Help — saveFolderModel / loadModel / PythonModule / Method.RandomSeed。Unpublished work. © 2026 Siemens.*
