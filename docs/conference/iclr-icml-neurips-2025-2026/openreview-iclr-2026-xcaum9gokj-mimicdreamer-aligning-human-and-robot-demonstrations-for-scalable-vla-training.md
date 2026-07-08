---
title: "MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training"
title_zh: MimicDreamer：对齐人类与机器演示以实现可扩展VLA训练
authors: "Haoyun Li, Ivan Zhang, Runqi Ouyang, Xiaofeng Wang, Zheng Zhu, Zhiqin Yang, Zhentao Zhang, Boyuan Wang, Chaojun Ni, Wenkang Qin, Xinze Chen, Yun Ye, Guan Huang, Zhenbo Song, Xingang Wang"
date: 2025-09-03
pdf: "https://openreview.net/pdf?id=xCAum9gOkj"
tags: ["query:data"]
score: 9.0
evidence: 在视觉、视角和动作上对齐人类演示与机器人域，用于可扩展VLA训练
tldr: 针对人类视频与机器人执行视频之间存在显著域差距的问题，MimicDreamer提出联合对齐视觉、视角和动作的框架，将低成本人类演示转化为可用于VLA训练的监督信号。该方法有效缩小了跨实施例差异，使得大规模利用人类数据训练通用机器人模型成为可能。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 机器人交互数据昂贵，人类演示视频可扩展但存在视觉和运动域差距。
method: 联合对齐视觉、视角和动作，将人类视频演示转换为机器人可用的训练数据。
result: 成功将人类演示用于VLA训练，缩小了人机域差距。
conclusion: MimicDreamer为利用大规模人类数据训练通用机器人策略提供了有效途径。
---

## Abstract
Vision Language Action (VLA) models derive their generalization capability from diverse training data, yet collecting embodied robot interaction data remains prohibitively expensive. In contrast, human demonstration videos are far more scalable and cost-efficient to collect, and recent studies confirm their effectiveness in training VLA models. However, a significant domain gap persists between human videos and robot-executed videos, including unstable camera viewpoints, visual discrepancies between human hands and robotic arms, and differences in motion dynamics. To bridge this gap, we propose MimicDreamer, a framework that turns fast, low-cost human demonstrations into robot-usable supervision by jointly aligning vision, viewpoint, and actions to directly support policy training. For visual alignment, we propose H2R Aligner, a video diffusion model that generates high-fidelity robot demonstration videos by transferring motion from human manipulation footage. For viewpoint stabilization, EgoStabilizer is proposed, which canonicalizes egocentric videos via homography and inpaints occlusions and distortions caused by warping. For action alignment, we map human hand trajectories to the robot frame and apply a constrained inverse kinematics solver to produce feasible, low-jitter joint commands with accurate pose tracking. Empirically, VLA models trained purely on our synthesized human-to-robot videos achieve few-shot execution on real robots. Moreover, scaling training with human data significantly boosts performance compared to models trained solely on real robot data; our approach improves the average success rate by 14.7\% across six representative manipulation tasks.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
在视觉、视角和动作上对齐人类演示与机器人域，用于可扩展VLA训练。

### 2. 核心内容
针对人类视频与机器人执行视频之间存在显著域差距的问题，MimicDreamer提出联合对齐视觉、视角和动作的框架，将低成本人类演示转化为可用于VLA训练的监督信号。该方法有效缩小了跨实施例差异，使得大规模利用人类数据训练通用机器人模型成为可能。

### 3. 对应检索需求
Papers central to scale data for robot learning, especially work that connects or combines: r; robot manipulation data engine; scalable manipulation dataset; web-scale robot learning data; robot learning from human videos; transferring human skills to robots; methods for converting human video demonstrations into robot executable action data; reconstructing hand object interactions from human videos for robot manipulation learning; aligning human body motion with different robot morphologies for robot learning from human demonstrations; scaling laws for robot learning from large scale internet video data.

### 4. 来源与原文
- Source：ICLR-2026-Public
- OpenReview：[https://openreview.net/forum?id=xCAum9gOkj](https://openreview.net/forum?id=xCAum9gOkj)
