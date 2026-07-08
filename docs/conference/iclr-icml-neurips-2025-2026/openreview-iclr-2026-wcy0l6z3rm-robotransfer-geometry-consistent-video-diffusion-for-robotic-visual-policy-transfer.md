---
title: "RoboTransfer: Geometry-Consistent Video Diffusion for Robotic Visual Policy Transfer"
title_zh: RoboTransfer：面向机器人视觉策略迁移的几何一致性视频扩散
authors: "Liu.Liu, Xiaofeng Wang, Guosheng Zhao, Keyu Li, Wenkang Qin, Jiagang Zhu, Jiaxiong Qiu, Zheng Zhu, Guan Huang, Zhizhong Su"
date: 2025-09-16
pdf: "https://openreview.net/pdf?id=WCY0l6z3Rm"
tags: ["query:data"]
score: 7.0
evidence: 合成机器人视觉数据以克服数据收集瓶颈，实现可扩展的操纵数据集
tldr: RoboTransfer针对机器人模仿学习中数据收集昂贵且仿真与现实存在差距的问题，提出基于扩散模型的视频生成框架，通过交叉视角特征交互和3D几何一致性实现多视角几何对齐，并支持精细的场景元素控制如背景编辑和物体替换。该框架能够合成大规模且多样化的机器人操纵数据，缓解数据稀缺瓶颈，为可扩展的机器人学习数据引擎提供了有效方法。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 机器人模仿学习需要大量多样化演示，但真实数据收集昂贵，仿真数据合成存在现实差距。
method: 提出基于扩散的视频生成框架，利用跨视角特征和3D几何一致性合成多视角一致且可控的机器人操作视频。
result: （未提供具体结果，但声称能生成多视角几何一致并支持场景编辑的合成数据）。
conclusion: 该框架有助于从仿真向真实世界的策略迁移，为机器人学习提供可扩展的数据合成途径。
---

## Abstract
The goal of general-purpose robotics is to create agents that can seamlessly adapt to and operate in diverse, unstructured human environments. Imitation learning has become a key paradigm for robotic manipulation, yet collecting large-scale and diverse demonstrations is prohibitively expensive. Simulators provide a cost-effective alternative, but the sim-to-real gap remains a major obstacle to scalability. We present RoboTransfer, a diffusion-based video generation framework for synthesizing robotic data. By leveraging cross-view feature interactions and globally consistent 3D geometry, RoboTransfer achieves multi-view geometric consistency while enabling fine-grained control over scene elements, including background editing and object replacement. Experiments show that RoboTransfer generates videos with improved geometric consistency and visual fidelity, and that policies trained on this data generalize better to novel, unseen scenarios. The code and datasets will be released upon acceptance.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
合成机器人视觉数据以克服数据收集瓶颈，实现可扩展的操纵数据集。

### 2. 核心内容
RoboTransfer针对机器人模仿学习中数据收集昂贵且仿真与现实存在差距的问题，提出基于扩散模型的视频生成框架，通过交叉视角特征交互和3D几何一致性实现多视角几何对齐，并支持精细的场景元素控制如背景编辑和物体替换。该框架能够合成大规模且多样化的机器人操纵数据，缓解数据稀缺瓶颈，为可扩展的机器人学习数据引擎提供了有效方法。

### 3. 对应检索需求
Papers central to scale data for robot learning, especially work that connects or combines: r; robot manipulation data engine; scalable manipulation dataset; web-scale robot learning data; robot learning from human videos; transferring human skills to robots; methods for converting human video demonstrations into robot executable action data; reconstructing hand object interactions from human videos for robot manipulation learning; aligning human body motion with different robot morphologies for robot learning from human demonstrations; scaling laws for robot learning from large scale internet video data.

### 4. 来源与原文
- Source：ICLR-2026-Public
- OpenReview：[https://openreview.net/forum?id=WCY0l6z3Rm](https://openreview.net/forum?id=WCY0l6z3Rm)
