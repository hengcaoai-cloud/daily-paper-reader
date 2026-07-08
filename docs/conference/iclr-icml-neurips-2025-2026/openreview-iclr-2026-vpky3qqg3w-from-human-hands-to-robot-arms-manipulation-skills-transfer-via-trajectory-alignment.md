---
title: "From Human Hands to Robot Arms: Manipulation Skills Transfer via Trajectory Alignment"
title_zh: 从人手到机械臂：基于轨迹对齐的操作技能迁移
authors: "Han Zhou, Jinjin Cao, Liyuan Ma, Xueji Fang, Guo-Jun Qi"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=vPKy3qQG3W"
tags: ["query:robot"]
score: 8.0
evidence: 通过3D轨迹对齐将人类视频中的操作技能迁移到机器人
tldr: 为解决真实机器人演示数据稀缺的问题，提出Traj2Action框架，利用操作端点的3D轨迹作为统一中间表示，将人类视频中的操作知识转移到机器人动作空间，无需配对数据即可实现跨形态技能迁移，在多个操作任务上验证了有效性。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 真实机器人遥操作演示成本高且难以扩展，而人类视频与机器人间存在显著形态差异。
method: 提出Traj2Action，以操作端点3D轨迹为中间表示，学习生成粗轨迹并转换为机器人动作。
result: 在多种操作任务上成功将人类技能迁移至机器人，无需配对数据。
conclusion: 3D轨迹对齐是弥合人机形态差异进行技能迁移的有效方式。
---

## Abstract
Learning diverse manipulation skills for real-world robots is severely bottlenecked by the reliance on costly and hard-to-scale teleoperated demonstrations. While human videos offer a scalable alternative, effectively transferring manipulation knowledge is fundamentally hindered by the significant morphological gap between human and robotic embodiments. 
To address this challenge and facilitate skill transfer from human to robot, we introduce Traj2Action,a novel framework that bridges this embodiment gap by using the 3D trajectory of the operational endpoint as a unified intermediate representation, and then transfers the manipulation knowledge embedded in this trajectory to the robot's actions.
Our policy first learns to generate a coarse trajectory, which forms an high-level motion plan by leveraging both human and robot data. 
This plan then conditions the synthesis of precise, robot-specific actions (e.g., orientation and gripper state) within a co-denoising framework. Extensive real-world experiments on a Franka robot demonstrate that Traj2Action boosts the performance by up to 27% and 22.25% over $\pi_0$ baseline on short- and long-horizon real-world tasks, and achieves significant gains as human data scales in robot policy learning.Our project website, featuring code and video demonstrations, is available at https://anonymous.4open.science/w/Traj2Action-4A45/.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
通过3D轨迹对齐将人类视频中的操作技能迁移到机器人。

### 2. 核心内容
为解决真实机器人演示数据稀缺的问题，提出Traj2Action框架，利用操作端点的3D轨迹作为统一中间表示，将人类视频中的操作知识转移到机器人动作空间，无需配对数据即可实现跨形态技能迁移，在多个操作任务上验证了有效性。

### 3. 对应检索需求
robot learning from human demonstrations for dexterous tasks。

### 4. 来源与原文
- Source：ICLR-2026-Public
- OpenReview：[https://openreview.net/forum?id=vPKy3qQG3W](https://openreview.net/forum?id=vPKy3qQG3W)
