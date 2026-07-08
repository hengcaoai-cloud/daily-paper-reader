---
title: "HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning"
title_zh: HumanoidGen：基于大语言模型推理的双臂灵巧操作数据生成
authors: "Zhi Jing, Siyuan Yang, Jicong Ao, Ting Xiao, Yu-Gang Jiang, Chenjia Bai"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=Mk9ykil8eP"
tags: ["query:robot"]
score: 9.0
evidence: 利用大语言模型推理自动生成双臂灵巧操作任务与示范数据
tldr: 现有机器人数据集多针对单臂平台，缺少面向人形机器人双臂灵巧手的操作任务与高质量示范。HumanoidGen提出一种自动化框架，结合原子灵巧操作空间标注与大语言模型推理，生成关系约束与多样任务。结果自动收集了大量高质量演示，弥补了人形机器人灵巧操作数据的空白，为相关研究提供了基础。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 人形机器人双臂灵巧操作数据极度缺乏，且手动收集代价高昂。
method: 利用原子操作与 LLM 推理，自动生成任务约束并收集高质量示范数据。
result: 自动生成了多样化仿真任务与高质量演示轨迹，覆盖多种灵巧操作场景。
conclusion: 为人形机器人灵巧操作研究提供了可扩展的数据生成方案和基准。
---

## Abstract
For robotic manipulation, existing robotics datasets and simulation benchmarks predominantly cater to robot-arm platforms. However, for humanoid robots equipped with dual arms and dexterous hands, simulation tasks and high-quality demonstrations are notably lacking. Bimanual dexterous manipulation is inherently more complex, as it requires coordinated arm movements and hand operations, making autonomous data collection challenging. This paper presents HumanoidGen, an automated task creation and demonstration collection framework that leverages atomic dexterous operations and LLM reasoning to generate relational constraints. Specifically, we provide spatial annotations for both assets and dexterous hands based on the atomic operations, and perform an LLM planner to generate a chain of actionable spatial constraints for arm movements based on object affordances and scenes. To further improve planning ability, we employ a variant of Monte Carlo tree search to enhance LLM reasoning for long-horizon tasks and insufficient annotation. In experiments, we create a novel benchmark with augmented scenarios to evaluate the quality of the collected data. The results show that the performance of the 2D and 3D diffusion policies can scale with the generated dataset. Project page is https://openhumanoidgen.github.io.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
利用大语言模型推理自动生成双臂灵巧操作任务与示范数据。

### 2. 核心内容
现有机器人数据集多针对单臂平台，缺少面向人形机器人双臂灵巧手的操作任务与高质量示范。HumanoidGen提出一种自动化框架，结合原子灵巧操作空间标注与大语言模型推理，生成关系约束与多样任务。结果自动收集了大量高质量演示，弥补了人形机器人灵巧操作数据的空白，为相关研究提供了基础。

### 3. 对应检索需求
datasets for robot dexterous manipulation and grasping。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=Mk9ykil8eP](https://openreview.net/forum?id=Mk9ykil8eP)
