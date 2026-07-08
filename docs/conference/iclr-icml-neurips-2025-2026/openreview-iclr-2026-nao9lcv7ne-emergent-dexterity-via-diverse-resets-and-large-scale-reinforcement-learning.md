---
title: Emergent Dexterity Via Diverse Resets and Large-Scale Reinforcement Learning
title_zh: 通过多样化重置与大规模强化学习实现灵巧操作涌现
authors: "Patrick Yin, Tyler Westenbroek, Zhengyu Zhang, Ignacio Dagnino, Eeshani Shilamkar, Numfor Mbiziwo-Tiapo, Simran Bagaria, Xinlei Liu, Galen Mullins, Andrey Kolobov, Abhishek Gupta"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=nAO9LcV7nE"
tags: ["query:robot"]
score: 9.0
evidence: 可扩展强化学习框架通过多样化重置解决多指灵巧操作任务
tldr: 针对现有强化学习方法任务特定性强、难以扩展的问题，提出一种可扩展框架，通过多样化环境重置使on-policy RL无需复杂课程即可鲁棒解决各类长时域接触丰富的灵巧操作任务，性能随计算量增长，展示了从简单抓取到复杂手中操作的通用性。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有RL方法需大量任务工程，且在长时域接触丰富任务上易失败，性能不随计算量扩展。
method: 提出基于多样化重置的简单可扩展框架，使用单一奖励函数和固定超参数训练on-policy RL。
result: 在多个灵巧操作任务上实现鲁棒策略，性能随计算资源增加而提升。
conclusion: 为灵巧操作提供了一种通用、可扩展的RL解决方案。
---

## Abstract
Reinforcement learning in massively parallel physics simulations has driven major progress in sim-to-real robot learning.  However, current approaches remain brittle and task-specific, relying on extensive per-task engineering to design rewards, curricula, and demonstrations. Even with this engineering, they often fail on long-horizon, contact-rich manipulation tasks and do not meaningfully scale with compute, as performance quickly saturates when training revisits the same narrow regions of state space. We introduce \Method, a simple and scalable framework that enables on-policy reinforcement learning to robustly solve a broad class of dexterous manipulation tasks using a single reward function, fixed algorithm hyperparameters, no curricula, and no human demonstrations. Our key insight is that long-horizon exploration can be dramatically simplified by using simulator resets to systematically expose the RL algorithm to the diverse set of robot-object interactions which underlie dexterous manipulation. \Method\ programmatically generates such resets with minimal human input, converting additional compute directly into broader behavioral coverage and continued performance gains. We show that \Method\ gracefully scales to long-horizon dexterous manipulation tasks beyond the capabilities of existing approaches and is able to learn robust policies over significantly wider ranges of initial conditions than baselines. Finally, we distill \Method \ into visuomotor policies which display robust retrying behavior and substantially higher success rates than baselines when transferred to the real world zero-shot. Project webpage: https://omnireset.github.io

---

## 论文详细总结（自动生成）

### 1. 检索相关性
可扩展强化学习框架通过多样化重置解决多指灵巧操作任务。

### 2. 核心内容
针对现有强化学习方法任务特定性强、难以扩展的问题，提出一种可扩展框架，通过多样化环境重置使on-policy RL无需复杂课程即可鲁棒解决各类长时域接触丰富的灵巧操作任务，性能随计算量增长，展示了从简单抓取到复杂手中操作的通用性。

### 3. 对应检索需求
robot dexterous manipulation with multi-fingered hands。

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=nAO9LcV7nE](https://openreview.net/forum?id=nAO9LcV7nE)
