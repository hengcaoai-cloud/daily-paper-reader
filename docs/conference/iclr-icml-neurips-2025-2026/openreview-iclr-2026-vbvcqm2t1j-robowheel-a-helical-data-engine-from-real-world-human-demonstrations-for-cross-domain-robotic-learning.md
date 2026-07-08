---
title: "ROBOWHEEL: A HELICAL DATA ENGINE FROM REAL-WORLD HUMAN DEMONSTRATIONS FOR CROSS-DOMAIN ROBOTIC LEARNING"
title_zh: RoboWheel：一个从真实世界人类示范生成跨领域机器人学习数据的螺旋式数据引擎
authors: "Yuhong Zhang, Zihan Gao, Shengpeng Li, Ling-Hao Chen, Kaisheng Liu, Runqing Cheng, Xiao Lin, Junjia Liu, Zhuoheng Li, Jingyi Feng, Ziyan He, Jintian Lin, Zheyan Huang, Zhifang Liu, Haoqian Wang"
date: 2025-09-02
pdf: "https://openreview.net/pdf?id=VBVCqm2t1J"
tags: ["query:data"]
score: 10.0
evidence: 将野外人类手物交互视频转换为跨形态机器人监督数据，可扩展数据引擎
tldr: 机器人学习缺乏大规模、高质量的操作数据。RoboWheel 提出一个螺旋式数据引擎，从野外人类手物交互视频中高精度重建动作并重定向到多种机器人形态，包括机械臂、灵巧手和人形机器人。结合仿真数据增强和域随机化，该引擎可生成大规模可执行训练数据，助力跨形态机器人泛化。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 从人类视频中获取机器人操作数据极具挑战，现有方法缺乏物理合理性且难以跨形态迁移。
method: 通过高精度手物交互重建与强化学习优化器确保物理约束，并重定向到不同机器人本体。
result: 成功将人类视频转化为跨形态机器人的可执行操作轨迹，并在仿真中实现多样化任务。
conclusion: 提供了一种可扩展的从人类示范到机器人学习的数据生成范式，显著降低数据采集门槛。
---

## Abstract
We introduce robowheel, a helical data engine that converts in-the-wild human hand–object interaction (HOI) videos into training-ready supervision for cross-morphology robotic learning. From monocular RGB/RGB-D inputs, we perform high-precision HOI reconstruction and enforce physical plausibility via a reinforcement learning optimizer that refines hand–object relative poses under contact and penetration constraints. The reconstructed, contact-rich trajectories are then retargetted to cross-domain embodiments, robot arms with simple end-effectors, dexterous hands, and humanoids, yielding executable actions and rollouts. To scale coverage, we build a simulation-augmented framework on Isaac Sim with diverse domain randomization (body variants, trajectories, object replacement, background changes, hand motion mirroring), which expands observations and labels while preserving contact semantics. This process forms an end-to-end pipeline from video → reconstruction → retargeting → augmentation → data acquisition, closing the loop for iterative policy improvement. Across vision-language-action and imitation-learning settings, \nbname-generated data provides reliable supervision and consistently improves task performance over baselines, enabling direct use of Internet HOI videos (hand-only or upper-body) as labels for scenario-specific training. We further assemble a large-scale multimodal dataset combining multi-camera captures, monocular videos, and public HOI corpora, and demonstrate transfer on dexterous-hand and humanoid platforms.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
将野外人类手物交互视频转换为跨形态机器人监督数据，可扩展数据引擎。

### 2. 核心内容
机器人学习缺乏大规模、高质量的操作数据。RoboWheel 提出一个螺旋式数据引擎，从野外人类手物交互视频中高精度重建动作并重定向到多种机器人形态，包括机械臂、灵巧手和人形机器人。结合仿真数据增强和域随机化，该引擎可生成大规模可执行训练数据，助力跨形态机器人泛化。

### 3. 对应检索需求
Papers central to scale data for robot learning, especially work that connects or combines: r; robot manipulation data engine; scalable manipulation dataset; web-scale robot learning data; robot learning from human videos; transferring human skills to robots; methods for converting human video demonstrations into robot executable action data; reconstructing hand object interactions from human videos for robot manipulation learning; aligning human body motion with different robot morphologies for robot learning from human demonstrations; scaling laws for robot learning from large scale internet video data.

### 4. 来源与原文
- Source：ICLR-2026-Public
- OpenReview：[https://openreview.net/forum?id=VBVCqm2t1J](https://openreview.net/forum?id=VBVCqm2t1J)
