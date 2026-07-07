---
title: Cross-Embodiment Dexterous Grasping with Reinforcement Learning
title_zh: 跨形态灵巧抓取与强化学习
authors: "Haoqi Yuan, Bohan Zhou, Yuhui Fu, Zongqing Lu"
date: 2025-01-22
pdf: "https://openreview.net/pdf?id=twIPSx9qHn"
tags: ["query:data"]
score: 9.0
evidence: 提出基于人手本征抓取的通用动作空间，实现跨形态灵巧抓取。
tldr: 为实现不同灵巧手的通用抓取策略，本文受人类遥操作启发，提出基于人手本征抓取的通用动作空间，策略输出本征抓取动作后通过重定向映射转换为各机器人手的关节动作。该方法显著简化跨形态学习，实验验证了其在多种灵巧手上的一致高性能。
source: ICLR-2025-Accepted
selection_source: conference_retrieval
motivation: 现有灵巧抓取策略多针对特定机器人手，缺乏跨形态通用策略。
method: 定义基于人手本征抓取的通用动作空间，并通过重定向映射适配不同手。
result: 在多种灵巧手上实现了高性能的跨形态抓取，泛化性强。
conclusion: 利用人手启发的通用动作空间可实现高效跨形态灵巧操作策略学习。
---

## Abstract
Dexterous hands exhibit significant potential for complex real-world grasping tasks. While recent studies have primarily focused on learning policies for specific robotic hands, the development of a universal policy that controls diverse dexterous hands remains largely unexplored.
In this work, we study the learning of cross-embodiment dexterous grasping policies using reinforcement learning (RL). Inspired by the capability of human hands to control various dexterous hands through teleoperation, we propose a universal action space based on the human hand's eigengrasps. The policy outputs eigengrasp actions that are then converted into specific joint actions for each robot hand through a retargeting mapping. We simplify the robot hand's proprioception to include only the positions of fingertips and the palm, offering a unified observation space across different robot hands. Our approach demonstrates an 80\% success rate in grasping objects from the YCB dataset across four distinct embodiments using a single vision-based policy. Additionally, our policy exhibits zero-shot generalization to two previously unseen embodiments and significant improvement in efficient finetuning. For further details and videos, visit our project page (https://sites.google.com/view/crossdex).

---

## 论文详细总结（自动生成）

# Cross-Embodiment Dexterous Grasping with Reinforcement Learning 论文总结

## 1. 核心问题与研究动机
- **核心问题**：如何学习一个**跨形态（cross-embodiment）** 的通用灵巧抓取策略，使单一策略能够控制多种不同的机器人灵巧手。
- **背景与动机**：
  - 灵巧手在复杂真实世界抓取任务中潜力巨大，但现有研究大多针对**特定机器人手**设计策略，缺乏通用性。
  - 受人类能够通过遥操作控制不同灵巧手的启发，作者希望利用**人手本征抓取（eigengrasps）** 构建一个统一动作空间，实现策略的跨形态迁移。

## 2. 方法论
- **核心思想**：
  - 设计一个基于**人手本征抓取**的通用动作空间，策略输出本征抓取动作。
  - 通过**重定向映射（retargeting mapping）** 将本征抓取动作转换为每个具体机器人手的关节动作。
- **关键技术细节**：
  - **通用动作空间**：利用人手抓取的低维本征表示（eigengrasps，可能通过主成分分析等方法得到），作为策略的输出动作。
  - **重定向映射**：为每种机器人手预先定义或学习一个映射函数，将本征抓取参数映射为相应手的关节角度。
  - **统一观测空间**：将机器人手的本体感知简化为**指尖和手掌的位置**，从而在不同手之间提供一致的观测表示。
  - 使用**强化学习（RL）** 训练基于视觉的策略（视觉观测 + 统一本体感知），输出本征抓取动作。
- **算法流程**（推断）：
  1. 环境提供视觉观测（如深度图/RGB）和指尖、手掌位置。
  2. 策略网络输出本征抓取动作向量。
  3. 根据当前机器人手类型，通过重定向映射将本征抓取动作转为关节指令。
  4. 执行动作，获得奖励，更新策略。

## 3. 实验设计
- **数据集/场景**：
  - 使用 **YCB 数据集** 中的物体进行抓取测试。
- **Benchmark 与对比方法**：
  - 在**四种不同的灵巧手形态**上评估单一策略的成功率。
  - 对比方法/设置可能包括：针对特定手单独训练的策略、直接迁移等方法（具体对比内容需从完整论文确认，摘要未详列）。
- **评估指标**：
  - 抓取成功率（80%）。

## 4. 资源与算力
- 摘要中**未明确说明**所用 GPU 型号、数量及训练时长。需要查阅完整论文获取相关细节。

## 5. 实验数量与充分性
- **实验数量**（从摘要推断）：
  - 至少包含在**四种已知形态**上的训练与评估实验。
  - **零样本泛化实验**：对两种未见过的形态进行测试。
  - **高效微调实验**：验证微调后的性能提升。
  - 可能还包括消融实验（如动作空间、观测空间的影响等），但摘要未提及。
- **充分性与公平性**：
  - 实验覆盖了多个不同形态，并验证了零样本泛化，显示了一定的通用性。
  - 与单独训练策略对比（未明确但常见）可体现跨形态学习的效果。
  - 若缺乏更多形态、更多物体集以及与其他跨形态方法的对比，可能限制结论的稳健性。摘要信息有限，难以全面判断。

## 6. 主要结论与发现
- 提出的方法在 YCB 物体抓取任务中，**单一视觉策略在四种不同形态手上达到 80% 成功率**。
- 策略展现出对**两种全新形态手的零样本泛化能力**。
- 跨形态预训练策略在微调时能显著提升效率。

## 7. 优点
- **通用性强**：首次实现单一视觉强化学习策略控制多种迥异的灵巧手，极具实用性。
- **思路巧妙**：利用人手本征抓取构建通用动作空间，受遥操作启发，具有良好的生物学合理性。
- **观测简化**：仅用指尖和手掌位置作为本体感知，降低了形态差异带来的观测复杂度。
- **泛化能力**：展示了零样本迁移和快速微调，证明了方法的可扩展性。

## 8. 不足与局限
- **实验覆盖**：摘要仅提及 YCB 数据集，是否覆盖不同场景（如杂乱场景、动态环境）未知。
- **形态多样性**：测试了四种已知和两种未知手，但相对于真实世界灵巧手的多样性仍有限。
- **重定向映射**：重定向映射的构建方法和质量对效果影响大，文中可能未充分探讨不同映射方式的影响。
- **观测依赖**：仅依赖指尖和手掌位置可能丢失某些手的关键信息（如关节力矩、触觉等），限制精细操作。
- **对比缺失**：摘要未提及与其他跨形态方法的直接对比，可能缺乏性能基准。
- **真实世界验证**：摘要未说明是否在真实机器人上实验，目前可能仅限于仿真。

（完）
