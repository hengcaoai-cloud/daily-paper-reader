---
title: "Real-IKEA : Simulating What Robots Will Really See and Touch"
title_zh: Real-IKEA：模拟机器人将真实看见和触碰的对象
authors: "Kunqi Xu, Zhenhao Huang, Siyuan Luo, Ziqiu ZENG, Fan Shi"
date: 2025-09-03
pdf: "https://openreview.net/pdf?id=eQ4kdm5iYj"
tags: ["query:robot"]
score: 9.0
evidence: Real-IKEA 提供具有高保真视觉和触觉真实感的数据集和仿真框架，用于接触丰富操作。
tldr: 机器人操作虽得益于仿真数据，但接触丰富任务中策略常因对象资产、物理真实感和视觉保真度不足而难以迁移。本文提出 Real-IKEA 数据集和仿真框架，以真实 IKEA 家具为基础，提供 1079 种精确网格、校准摩擦和铰链阻力的关节体配置，并引入双向表面偏差度量确保接触几何精度，致力于从视觉和触觉角度高保真模拟真实操作环境。该工作为接触丰富操作提供了一个可靠、可扩展的仿真基准。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 仿真到现实的差距源于对象资产、物理真实感和视觉保真度不足，限制接触丰富操作策略迁移。
method: 构建 Real-IKEA 数据集和仿真框架，结合真实 IKEA 家具、精确网格、校准物理参数和逼真视觉渲染。
result: 提供 1079 种关节体配置，在接触几何和视觉上高度逼近真实，缩小了 sim-to-real 差距。
conclusion: 高保真仿真数据集是桥接接触丰富操作 sim-to-real 差距的关键，Real-IKEA 为相关研究提供了坚实基础。
---

## Abstract
Robotic manipulation has greatly benefited from simulated data, yet in contact-rich tasks policies often fail to transfer. We trace this sim-to-real gap to three sources: object assets, physical realism and visual fidelity. We emphasize accuracy along all three axes—precise meshes and collisions, calibrated friction and hinge resistance, and visually realistic observations—and present Real-IKEA, a dataset and simulation framework designed with accuracy as a first-class goal. At scale, Real-IKEA provides 1,079 articulated asset configurations, created by combining real IKEA furniture bases with a curated library of 83 authentic IKEA handles and knobs. For contact-geometry accuracy, we introduce a bidirectional surface-deviation metric ($E_{Q\to P}$, $E_{P\to Q}$) that quantifies collision meshes against the visual mesh. For dynamics accuracy, we establish resistance-calibrated benchmarks that vary damping and friction. To narrow the vision gap, we pair real-time teleoperation with offline high-fidelity re-rendering and quantify alignment via FID/EMD across multiple encoders. Extensive comparisons show that Real-IKEA yields more realistic asset structure, more accurate physical interactions, and visuals more closely aligned with real data, enabling policies to exploit geometry and torque rather than rely on friction-only pulling. This accuracy-centric design, coupled with large scale, enables the scalable collection of reliable manipulation data and more robust sim-to-real transfer.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
Real-IKEA 提供具有高保真视觉和触觉真实感的数据集和仿真框架，用于接触丰富操作。

### 2. 核心内容
机器人操作虽得益于仿真数据，但接触丰富任务中策略常因对象资产、物理真实感和视觉保真度不足而难以迁移。本文提出 Real-IKEA 数据集和仿真框架，以真实 IKEA 家具为基础，提供 1079 种精确网格、校准摩擦和铰链阻力的关节体配置，并引入双向表面偏差度量确保接触几何精度，致力于从视觉和触觉角度高保真模拟真实操作环境。该工作为接触丰富操作提供了一个可靠、可扩展的仿真基准。

### 3. 对应检索需求
datasets for robot dexterous manipulation and grasping。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=eQ4kdm5iYj](https://openreview.net/forum?id=eQ4kdm5iYj)
