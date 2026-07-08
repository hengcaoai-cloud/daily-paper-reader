---
title: "AnyPos: Automated Task-Agnostic Actions for Bimanual Manipulation"
title_zh: AnyPos：面向双臂操作的任务无关动作自动化
authors: "Hengkai Tan, Yao Feng, Xinyi Mao, Shuhe Huang, Guodong Liu, Zhongkai Hao, Hang Su, Jun Zhu"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=BFiK4TVYeq"
tags: ["query:data"]
score: 7.0
evidence: 自动生成任务无关的动作数据，用于学习体现动力学
tldr: AnyPos针对机器人操作数据稀缺且与特定体现紧密耦合的问题，提出任务无关的体现建模方法，自动生成覆盖整个工作空间的动作数据。该方法通过学习体现动力学并将其与高层策略解耦，使得机器人能够利用独立图像-动作对数据进行训练，无需依赖序列化的任务数据，从而提升了策略在不同任务和平台间的迁移能力。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 机器人操作数据稀缺且与具体体现绑定，导致跨任务和跨平台迁移困难。
method: 提出任务无关的体现建模，直接从自动生成的动作数据中学习体现动力学。
result: 能生成覆盖整个工作空间的任务无关图像-动作对，解耦体现动力学与策略学习。
conclusion: 该方法通过数据驱动的方式促进了通用操作策略的学习和迁移。
---

## Abstract
Learning generalizable manipulation policies hinges on data, yet robot manipulation data is scarce and often entangled with specific embodiments, making both cross-task and cross-platform transfer difficult. 
We tackle this challenge with**task-agnostic embodiment modeling**, which learns embodiment dynamics directly from ***task-agnostic action*** data and decouples them from high-level policy learning. By focusing on exploring all feasible actions of the embodiment to capture what is physically feasible and consistent, task-agnostic data takes the form of independent image-action pairs with the potential to cover the entire embodiment workspace, unlike task-specific data, which is sequential and tied to concrete tasks. This data-driven perspective bypasses the limitations of traditional dynamics-based modeling and enables scalable reuse of action data across different tasks. 
Building on this principle, we introduce **AnyPos**, a unified pipeline that integrates large-scale automated task-agnostic exploration with robust embodiment modeling through inverse dynamics learning. AnyPos generates diverse yet safe trajectories at scale, then learns embodiment representations by *decoupling arm and end-effector motions* and employing a *direction-aware decoder* to stabilize predictions under distribution shift, which can be seamlessly coupled with diverse high-level policy models. 
In comparison to the standard baseline, AnyPos achieves a 51\% improvement in test accuracy. On manipulation tasks such as operating a microwave, toasting bread, folding clothes, watering plants, and scrubbing plates, AnyPos raises success rates by 30-40\% over strong baselines. These results highlight data-driven embodiment modeling as a practical route to overcoming data scarcity and achieving generalization across tasks and platforms in visuomotor control.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
自动生成任务无关的动作数据，用于学习体现动力学。

### 2. 核心内容
AnyPos针对机器人操作数据稀缺且与特定体现紧密耦合的问题，提出任务无关的体现建模方法，自动生成覆盖整个工作空间的动作数据。该方法通过学习体现动力学并将其与高层策略解耦，使得机器人能够利用独立图像-动作对数据进行训练，无需依赖序列化的任务数据，从而提升了策略在不同任务和平台间的迁移能力。

### 3. 对应检索需求
Papers central to scale data for robot learning, especially work that connects or combines: r; robot manipulation data engine; scalable manipulation dataset; web-scale robot learning data; robot learning from human videos; transferring human skills to robots; methods for converting human video demonstrations into robot executable action data; reconstructing hand object interactions from human videos for robot manipulation learning; aligning human body motion with different robot morphologies for robot learning from human demonstrations; scaling laws for robot learning from large scale internet video data.

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=BFiK4TVYeq](https://openreview.net/forum?id=BFiK4TVYeq)
