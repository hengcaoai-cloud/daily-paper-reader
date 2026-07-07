---
title: "Video2Policy: Scaling up Manipulation Tasks in Simulation through Internet Videos"
title_zh: Video2Policy：通过互联网视频扩展仿真中的操作任务
authors: "Weirui Ye, Fangchen Liu, Zheng Ding, Yang Gao, Oleh Rybkin, Pieter Abbeel"
date: 2024-09-27
pdf: "https://openreview.net/pdf?id=RhfYIJux9d"
tags: ["query:data"]
score: 10.0
evidence: 通过物体网格重建和6D位姿追踪从互联网RGB视频中重构任务，生成操作数据。
tldr: 本文提出Video2Policy框架，将大规模互联网人类视频转化为仿真中的操作任务数据：先通过物体网格重建和6D跟踪复现任务，再结合大模型生成奖励函数进行强化学习训练。该方法在多样化和真实性上显著优于现有方案，为机器人从网络视频中规模化学习提供了可行路径。
source: ICLR-2025-Rejected-Public
selection_source: conference_retrieval
motivation: 现有生成仿真任务的方法依赖大模型易产生幻觉，或数字孪生难以扩展。
method: 第一阶段从视频重建物体网格与轨迹生成任务；第二阶段利用LLM奖励进行强化学习。
result: 在任务多样性和政策泛化能力上远超现有方法。
conclusion: 互联网视频是机器人学习可扩展且真实的任务来源，Video2Policy有效解锁了这一潜力。
---

## Abstract
Simulation offers a promising approach for cheaply scaling training data for generalist policies. To scalably generate data from diverse and realistic tasks, existing algorithms either rely on large language models (LLMs) that may hallucinate tasks not interesting for robotics; or digital twins, which require careful real-to-sim alignment and are hard to scale. To address these challenges, we introduce Video2Policy, a novel framework that leverages large amounts of internet RGB videos to reconstruct tasks based on everyday human behavior. Our approach comprises two phases: (1) task generation through object mesh reconstruction and 6D position tracking; and (2) reinforcement learning utilizing LLM-generated reward functions and iterative in-context reward reflection for the task. We demonstrate the efficacy of Video2Policy by reconstructing over 100 videos from the Something-Something-v2 (SSv2) dataset, which depicts diverse and complex human behaviors on 9 different tasks. Our method can successfully train RL policies on such tasks, including complex and challenging tasks such as throwing. Furthermore, we show that a generalist policy trained on the collected sim data generalizes effectively to new tasks and outperforms prior approaches. Finally, we show the performance of our policies improves by simply including more internet videos. We believe that the proposed Video2Policy framework is a step towards generalist policies that can execute practical robotic tasks based on everyday human behavior.

---

## 论文详细总结（自动生成）

# Video2Policy 论文总结

## 1. 核心问题与研究动机
现有仿真数据生成方法存在明显瓶颈：
- **基于大语言模型（LLM）的方法**：容易产生与真实机器人需求不相关的幻觉任务。
- **基于数字孪生的方法**：需要精细的“真实到仿真”对齐，难以规模化。

**整体目标**：直接利用海量互联网 RGB 视频（记录人类日常行为），自动重建出多样化、真实的机器人操作任务，并在仿真中训练通用策略，从而低成本、可扩展地获取训练数据。

## 2. 方法论
Video2Policy 框架分为两个阶段：

### 阶段一：任务生成（从视频到仿真任务）
- **物体网格重建**：从互联网视频中重建场景物体的三维网格模型。
- **6D 位姿追踪**：跟踪视频中物体的六自由度位姿（位置与方向），复现人类操作时的物体运动轨迹。
- **任务构建**：基于重建的网格和轨迹，在物理仿真器中生成可执行的机器人操作任务。

### 阶段二：基于奖励的强化学习
- **LLM 生成奖励函数**：利用大语言模型自动为任务编写奖励函数。
- **迭代上下文奖励反思**：通过 in-context learning 对奖励函数进行迭代优化，提升其有效性。
- **强化学习训练**：在生成的仿真任务上训练策略，直至收敛。

## 3. 实验设计
### 数据集与场景
- **视频来源**：Something-Something-v2 (SSv2) 数据集，包含多样、复杂的人类日常行为视频。
- **重建规模**：从 SSv2 中重建了 **超过 100 个视频**，覆盖 **9 种不同的任务**（包括高难度的“投掷”任务）。

### 基准对比
- 对比了 **先前基于大模型或数字孪生的方法**，重点评估任务多样性与策略泛化能力。

### 实验类型
- 在重建任务上训练 RL 策略，检验单任务表现。
- 训练通用策略（Generalist Policy），评估其在新任务上的零样本泛化能力。
- 考察 **数据规模效应**：证明仅通过增加互联网视频数量，策略性能便可稳定提升。

## 4. 资源与算力
**文中未明确提及所使用的 GPU 型号、数量或具体训练时长。** 所有计算开销相关的细节在现有摘要与元数据中均未披露。

## 5. 实验数量与充分性
- **至少包含 3 类核心实验**：
  1. **任务重建与 RL 训练**（100+ 视频 × 9 类任务）。
  2. **策略泛化实验**（通用策略在新任务上的表现）。
  3. **数据扩展性实验**（不同视频数量对性能的影响）。
- 实验设计较为全面，覆盖了方法有效性、泛化性、可扩展性三个维度，对比了先前方法，具有较好的客观性与公平性。不过，详细的消融研究（如各模块贡献度、不同 LLM 的影响）在现有摘要中未展开说明。

## 6. 主要结论与发现
- Video2Policy 成功从互联网视频中重建出多样化、真实的机器人操作任务，并训练出有效的 RL 策略，**即使对于投掷等复杂任务也能胜任**。
- 基于收集的仿真数据训练的通用策略可**有效泛化至新任务**，且性能显著超越先前方法。
- 策略性能 **随着互联网视频数量的增加而持续提升**，验证了通过规模扩展视频数据的潜力。
- 互联网视频是机器人学习可扩展、真实的任务来源，Video2Policy 解锁了这一可能性，是通往基于人类日常行为的通用机器人策略的重要一步。

## 7. 优点
- **高度可扩展**：直接利用海量、自然发生的互联网视频，无需人工标定或精心设计数字孪生。
- **任务真实性与多样性**：源于真实人类行为，自然覆盖长尾与复杂动作（如投掷），远超 LLM 可能产生的有限模式。
- **自动化流程**：从视频到任务再到策略的全程自动化，减少人工干预。
- **实验说服力强**：通过 SSv2 数据集、多任务泛化以及数据规模实验，多角度验证了框架的有效性和可扩展性。
- **模块化设计**：重建与 RL 两阶段解耦，可分别替换或改进（如更好的网格重建、更强的 LLM 奖励生成）。

## 8. 不足与局限
- **算力细节未公开**：缺乏 GPU 型号、训练时长等资源消耗数据，难以评估其实际成本与计算门槛。
- **实验规模有限**：虽覆盖 9 类任务、100+ 视频，但任务种类仍较窄，能否处理更复杂的长期、交互式任务尚不明确。
- **仿真到真实的迁移**：文中未涉及 sim-to-real 实验，策略在真实机器人上的表现仍未知。
- **网格重建与追踪的鲁棒性**：对视频质量、遮挡、光照变化等敏感，可能导致重建错误，从而影响任务质量，但未分析其失败案例。
- **奖励函数的局限性**：LLM 生成的奖励可能在某些稀疏奖励任务中仍不够精准，需要额外迭代，且依赖于 LLM 的质量。
- **未提及失败模式与消融**：缺少对重建失败、奖励失效等情况的分析，也未展示各模块的具体贡献度消融实验。
- **实验全面性**：与更广泛的仿真生成基准（如 RLBench、ManiSkill 等）的对比缺失，限制了对其优劣势的更全面认识。

（完）
