---
title: "DexNDM: Closing the Reality Gap for Dexterous In-Hand Rotation via Joint-Wise Neural Dynamics Model"
title_zh: "DexNDM: 通过关节级神经动力学模型弥合灵巧手中旋转的现实鸿沟"
authors: "Xueyi Liu, He Wang, Li Yi"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=80vjyj5o7l"
tags: ["query:robot"]
score: 9.0
evidence: 关节级动力学模型实现灵巧手中旋转的仿真到现实迁移
tldr: 针对灵巧手中旋转因接触丰富导致仿真到现实差距大的问题，提出关节级神经动力学模型，通过学习修正动力学差异，使仿真训练的策略能泛化到真实世界中多种物体和条件。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 灵巧手中旋转的接触丰富动力学导致仿真到现实差距大。
method: 提出关节级动力学模型来弥合仿真与现实之间的差距。
result: 单一策略在真实世界中泛化到各种物体和条件。
conclusion: 关节级动力学建模有效解决灵巧操作的现实鸿沟。
---

## Abstract
Achieving generalized in-hand object rotation remains a significant challenge in robotics, largely due to the difficulty of transferring policies from simulation to the real world. The complex, contact-rich dynamics of dexterous manipulation create a "reality gap" that has limited prior work to constrained scenarios involving simple geometries, limited object sizes and aspect ratios, constrained wrist poses, or customized hands. We address this sim-to-real challenge with a novel framework that enables a single policy, trained in simulation, to generalize to a wide variety of objects and conditions in the real world. The core of our method is a joint-wise dynamics model that learns to bridge the reality gap by effectively fitting limited amount of real-world collected data and then adapting the sim policy’s actions accordingly.  The model is highly data‑efficient and generalizable across different whole‑hand interaction distributions by factorizing dynamics across joints, compressing system-wide influences into low‑dimensional variables, and learning each joint’s evolution from its own dynamic profile, implicitly capturing these net effects. We pair this with a fully autonomous data collection strategy that gathers diverse, real-world interaction data with minimal human intervention. Our complete pipeline demonstrates unprecedented generality: a single policy successfully rotates challenging objects with complex shapes (*e.g.*, animals), high aspect ratios (up to 5.33), and small sizes, all while handling diverse wrist orientations and rotation axes. Comprehensive real-world evaluations and a teleoperation application for complex tasks validate the effectiveness and robustness of our approach. Website: [DexNDM](https://meowuu7.github.io/DexNDM/).

---

## 论文详细总结（自动生成）

### 1. 检索相关性
关节级动力学模型实现灵巧手中旋转的仿真到现实迁移。

### 2. 核心内容
针对灵巧手中旋转因接触丰富导致仿真到现实差距大的问题，提出关节级神经动力学模型，通过学习修正动力学差异，使仿真训练的策略能泛化到真实世界中多种物体和条件。

### 3. 对应检索需求
robot dexterous manipulation with multi-fingered hands。

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=80vjyj5o7l](https://openreview.net/forum?id=80vjyj5o7l)
