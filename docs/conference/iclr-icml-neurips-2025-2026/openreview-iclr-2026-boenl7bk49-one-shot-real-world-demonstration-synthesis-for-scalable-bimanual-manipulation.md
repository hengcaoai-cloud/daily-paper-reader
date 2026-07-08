---
title: One-Shot Real-World Demonstration Synthesis for Scalable Bimanual Manipulation
title_zh: 从单个真实世界示例合成可扩展的双臂操作演示
authors: "Huayi Zhou, Kui Jia"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=BOENl7Bk49"
tags: ["query:data"]
score: 9.0
evidence: BiDemoSyn 从单个真实示例合成多样双手机器人演示，实现灵巧操作数据的可扩展生成。
tldr: 学习双手机灵巧操作策略高度依赖大规模高质量演示，但遥操作耗力，仿真又存在 sim-to-real 差距。本文提出 BiDemoSyn，通过任务分解为不变协调块和可变物体依赖调整，利用视觉引导对齐和轻量轨迹优化，从单个真实世界示例合成数千个物理可行的双臂演示。该方法在保持物理合理性的同时大幅扩展数据规模，为双臂灵巧操作的数据高效学习提供了新途径。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 双臂灵巧操作需要大规模演示数据，但遥操作昂贵且仿真有 sim-to-real 差距。
method: BiDemoSyn 将任务分解为不变协调块和可变调整，利用视觉对齐和轨迹优化从单个示例合成多样化双臂演示。
result: 可合成数千个物理可行的双臂演示，数据多样性增加，且保持任务成功率。
conclusion: 该方法显著降低了获取双臂操作演示的成本，为灵巧操作的数据驱动学习提供了高效数据引擎。
---

## Abstract
Learning dexterous bimanual manipulation policies critically depends on large-scale, high-quality demonstrations, yet current paradigms face inherent trade-offs: teleoperation provides physically grounded data but is prohibitively labor-intensive, while simulation-based synthesis scales efficiently but suffers from sim-to-real gaps. We present BiDemoSyn, a framework that synthesizes contact-rich, physically feasible bimanual demonstrations from a single real-world example. The key idea is to decompose tasks into invariant coordination blocks and variable, object-dependent adjustments, then adapt them through vision-guided alignment and lightweight trajectory optimization. This enables the generation of thousands of diverse and feasible demonstrations within several hour, without repeated teleoperation or reliance on imperfect simulation. Across six dual-arm tasks, we show that policies trained on BiDemoSyn data generalize robustly to novel object poses and shapes, significantly outperforming recent baselines. By bridging the gap between efficiency and real-world fidelity, BiDemoSyn provides a scalable path toward practical imitation learning for complex bimanual manipulation without compromising physical grounding.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
BiDemoSyn 从单个真实示例合成多样双手机器人演示，实现灵巧操作数据的可扩展生成。

### 2. 核心内容
学习双手机灵巧操作策略高度依赖大规模高质量演示，但遥操作耗力，仿真又存在 sim-to-real 差距。本文提出 BiDemoSyn，通过任务分解为不变协调块和可变物体依赖调整，利用视觉引导对齐和轻量轨迹优化，从单个真实世界示例合成数千个物理可行的双臂演示。该方法在保持物理合理性的同时大幅扩展数据规模，为双臂灵巧操作的数据高效学习提供了新途径。

### 3. 对应检索需求
Papers central to scale data for robot learning, especially work that connects or combines: r; robot manipulation data engine; scalable manipulation dataset; web-scale robot learning data; robot learning from human videos; transferring human skills to robots; methods for converting human video demonstrations into robot executable action data; reconstructing hand object interactions from human videos for robot manipulation learning; aligning human body motion with different robot morphologies for robot learning from human demonstrations; scaling laws for robot learning from large scale internet video data.

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=BOENl7Bk49](https://openreview.net/forum?id=BOENl7Bk49)
