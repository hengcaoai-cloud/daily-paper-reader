---
title: "EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos"
title_zh: "EgoVLA: 从第一人称人类视频学习视觉-语言-动作模型"
authors: "Ruihan Yang, Qinxi Yu, Yecheng Wu, Rui Yan, Borui li, An-Chieh Cheng, Xueyan Zou, Yunhao Fang, Xuxin Cheng, Ri-Zhao Qiu, Hongxu Yin, Sifei Liu, Song Han, Yao Lu, Xiaolong Wang"
date: 2025-09-08
pdf: "https://openreview.net/pdf?id=TLNT7JmNsf"
tags: ["query:robot"]
score: 9.0
evidence: 在第一人称人类视频上训练VLA模型，通过动作重定向实现机器人操作
tldr: 为突破真实机器人数据规模限制，探索用第一人称人类视频训练视觉-语言-动作（VLA）模型，通过预测人手动作并逆运动学重定向至机器人，微调少量机器人演示后得到通用操作策略，在仿真基准和真实任务上表明大规模人类视频可有效增强机器人学习。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 真实机器人数据收集受硬件限制，无法像人类视频那样大规模获取。
method: 在人类第一人称视频上训练VLA预测手腕/手部动作，经重定向与微调转为机器人策略。
result: 仿真和真实实验证明少量机器人数据微调的VLA可获得强操作策略。
conclusion: 利用大规模人类视频训练VLA是扩展机器人学习的可行路径。
---

## Abstract
Real robot data collection for imitation learning has led to significant advances in robotic manipulation. 
However, the requirement for robot hardware in the process fundamentally constrains the scale of the data.
In this paper, we explore training Vision-Language-Action (VLA) models using egocentric human videos. The benefit of using human videos is not only for their scale but more importantly for the richness of scenes and tasks. With a VLA trained on human video that predicts human wrist and hand actions, we can perform Inverse Kinematics and retargeting to convert the human actions to robot actions. We fine-tune the model using a few robot manipulation demonstrations to obtain the robot policy, namely EgoVLA. We propose a simulation benchmark called Ego Humanoid Manipulation Benchmark, where we design diverse bimanual manipulation tasks with demonstrations. We fine-tune and evaluate EgoVLA with \benchmarkName and show significant improvements over baselines and ablate the importance of human data

---

## 论文详细总结（自动生成）

### 1. 检索相关性
在第一人称人类视频上训练VLA模型，通过动作重定向实现机器人操作。

### 2. 核心内容
为突破真实机器人数据规模限制，探索用第一人称人类视频训练视觉-语言-动作（VLA）模型，通过预测人手动作并逆运动学重定向至机器人，微调少量机器人演示后得到通用操作策略，在仿真基准和真实任务上表明大规模人类视频可有效增强机器人学习。

### 3. 对应检索需求
how to use large scale first person human videos for robot dexterous manipulation。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=TLNT7JmNsf](https://openreview.net/forum?id=TLNT7JmNsf)
