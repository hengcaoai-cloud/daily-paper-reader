---
title: "VLBiMan: Vision-Language Anchored One-Shot Demonstration Enables Generalizable Bimanual Robotic Manipulation"
title_zh: VLBiMan：基于视觉-语言锚定的单次演示实现通用双臂机器人操作
authors: "Huayi Zhou, Kui Jia"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=he86smZzRk"
tags: ["query:robot"]
score: 9.0
evidence: 单次人类演示实现通用双臂灵巧操作
tldr: VLBiMan针对双臂灵巧操作中大量演示的需求，提出从单次人类示例中通过任务感知分解和视觉-语言锚定学习可泛化技能的方法。它将任务分解为不变的基元和可调组件，利用视觉-语言基础模型自适应场景变化，实现了动态环境下的高效操作。实验表明该方法在背景变化和物体重定位等场景下具有良好的泛化能力。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 双臂操作需要大量人类演示才能覆盖任务变化，现有方法在动态场景下缺乏灵活性。
method: 提出VLBiMan框架，从单个人类示例中通过任务感知分解提取可复用技能，并利用视觉-语言锚定动态调整。
result: 在具有背景变化、物体重定位等场景中展示了自适应能力和任务泛化性。
conclusion: 该方法提高了双臂机器人从人类演示中学习的效率，推动了灵巧操作的少样本学习。
---

## Abstract
Achieving generalizable bimanual manipulation requires systems that can learn efficiently from minimal human input while adapting to real-world uncertainties and diverse embodiments. Existing approaches face a dilemma: imitation policy learning demands extensive demonstrations to cover task variations, while modular methods often lack flexibility in dynamic scenes. We introduce VLBiMan, a framework that derives reusable skills from a single human example through task-aware decomposition, preserving invariant primitives as anchors while dynamically adapting adjustable components via vision-language grounding. This adaptation mechanism resolves scene ambiguities caused by background changes, object repositioning, or visual clutter without policy retraining, leveraging semantic parsing and geometric feasibility constraints. Moreover, the system inherits human-like hybrid control capabilities, enabling mixed synchronous and asynchronous use of both arms. Extensive experiments validate VLBiMan across tool-use and multi-object tasks, demonstrating: (1) a drastic reduction in demonstration requirements compared to imitation baselines, (2) compositional generalization through atomic skill splicing for long-horizon tasks, (3) robustness to novel but semantically similar objects and external disturbances, and (4) strong cross-embodiment transfer, showing that skills learned from human demonstrations can be instantiated on different robotic platforms without retraining. By bridging human priors with vision-language anchored adaptation, our work takes a step toward practical and versatile dual-arm manipulation in unstructured settings.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
单次人类演示实现通用双臂灵巧操作。

### 2. 核心内容
VLBiMan针对双臂灵巧操作中大量演示的需求，提出从单次人类示例中通过任务感知分解和视觉-语言锚定学习可泛化技能的方法。它将任务分解为不变的基元和可调组件，利用视觉-语言基础模型自适应场景变化，实现了动态环境下的高效操作。实验表明该方法在背景变化和物体重定位等场景下具有良好的泛化能力。

### 3. 对应检索需求
robot learning from human demonstrations for dexterous tasks。

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=he86smZzRk](https://openreview.net/forum?id=he86smZzRk)
