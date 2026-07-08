---
title: Robotic Manipulation by Imitating Generated Videos Without Physical Demonstrations
title_zh: 通过模仿生成视频实现机器人操作，无需物理演示
authors: "Shivansh Patel, Shraddhaa Mohan, Hanlin Mai, Unnat Jain, Svetlana Lazebnik, Yunzhu Li"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=tv0Sz8A9Tc"
tags: ["query:data"]
score: 7.0
evidence: 通过模仿AI生成视频实现操作，无需物理演示，从视频提取轨迹并重定向到机器人
tldr: 针对物理机器人演示数据获取昂贵的问题，RIGVid提出通过模仿AI生成的视频来执行操作任务，利用视频扩散模型生成演示视频，VLM过滤无效结果，6D位姿跟踪器提取物体轨迹并重定向到机器人。真实世界实验表明过滤后的生成视频与真实演示一样有效，为机器人学习提供了低成本的数据来源。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 物理机器人演示数据收集成本高昂，制约了机器人操作的扩展性。
method: 使用视频扩散模型生成操作演示，VLM过滤，6D位姿跟踪提取轨迹并重定向到机器人。
result: 过滤后的生成视频在真实世界操作任务中与真实演示效果相当。
conclusion: RIGVid为机器人操作提供了一种无需物理演示的数据生成引擎，降低了数据门槛。
---

## Abstract
This work introduces Robots Imitating Generated Videos (RIGVid), a system that enables robots to perform complex manipulation tasks—such as pouring, wiping, and mixing—purely by imitating AI-generated videos, without requiring any physical demonstrations or robot-specific training. Given a language command and an initial scene image, a video diffusion model generates potential demonstration videos, and a vision-language model (VLM) automatically filters out results that do not follow the command. A 6D pose tracker then extracts object trajectories from the video, and the trajectories are retargeted to the robot in an embodiment-agnostic fashion. Through extensive realworld evaluations, we show that filtered generated videos are as effective as real demonstrations, and that performance improves with generation quality. We also show that relying on generated videos outperforms more compact alternatives such as keypoint prediction using VLMs, and that strong 6D pose tracking outperforms other ways to extract trajectories, such as dense feature point tracking. These findings suggest that videos produced by a state-of-the-art off-the-shelf model can offer an effective source of supervision for robotic manipulation.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
通过模仿AI生成视频实现操作，无需物理演示，从视频提取轨迹并重定向到机器人。

### 2. 核心内容
针对物理机器人演示数据获取昂贵的问题，RIGVid提出通过模仿AI生成的视频来执行操作任务，利用视频扩散模型生成演示视频，VLM过滤无效结果，6D位姿跟踪器提取物体轨迹并重定向到机器人。真实世界实验表明过滤后的生成视频与真实演示一样有效，为机器人学习提供了低成本的数据来源。

### 3. 对应检索需求
Papers central to scale data for robot learning, especially work that connects or combines: r; robot manipulation data engine; scalable manipulation dataset; web-scale robot learning data; robot learning from human videos; transferring human skills to robots; methods for converting human video demonstrations into robot executable action data; reconstructing hand object interactions from human videos for robot manipulation learning; aligning human body motion with different robot morphologies for robot learning from human demonstrations; scaling laws for robot learning from large scale internet video data.

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=tv0Sz8A9Tc](https://openreview.net/forum?id=tv0Sz8A9Tc)
