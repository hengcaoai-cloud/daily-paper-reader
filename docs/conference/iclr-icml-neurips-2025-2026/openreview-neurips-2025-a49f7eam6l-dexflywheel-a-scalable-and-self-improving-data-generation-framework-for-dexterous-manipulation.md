---
title: "DexFlyWheel: A Scalable and Self-improving Data Generation Framework for Dexterous Manipulation"
title_zh: "DexFlyWheel: 面向灵巧操作的可扩展自改进数据生成框架"
authors: "Kefei Zhu, Fengshuo Bai, YuanHao Xiang, Yishuai Cai, Xinglin Chen, Ruochong Li, Xingtao Wang, Hao Dong, Yaodong Yang, Xiaopeng Fan, Yuanpei Chen"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=a49F7EAm6l"
tags: ["query:robot"]
score: 10.0
evidence: 通过自我改进的IL-RL循环进行可扩展灵巧操作数据生成
tldr: 针对灵巧操作数据集多样性不足、难以扩展的问题，提出DexFlyWheel框架，从少量种子演示出发，通过模仿学习与残差强化学习的闭环迭代实现数据自我改进与丰富，大幅提升数据多样性和质量，为灵巧操作学习提供可扩展数据引擎。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 灵巧操作高质量数据集稀缺，现有数据收集方法多样性有限，难以扩展。
method: 提出DexFlyWheel，从种子演示预热，通过IL与残差RL闭环迭代持续丰富数据多样性。
result: 生成的数据集在多样性上显著优于基线，支撑更鲁棒的策略学习。
conclusion: 自改进闭环为灵巧操作数据生成提供了一种可扩展解决方案。
---

## Abstract
Dexterous manipulation is critical for advancing robot capabilities in real-world applications, yet diverse and high-quality datasets remain scarce. Existing data collection methods either rely on human teleoperation or require significant human engineering, or generate data with limited diversity, which restricts their scalability and generalization. In this paper, we introduce DexFlyWheel, a scalable data generation framework that employs a self-improving cycle to continuously enrich data diversity. Starting from efficient seed demonstrations warmup, DexFlyWheel expands the dataset through iterative cycles. Each cycle follows a closed-loop pipeline that integrates Imitation Learning (IL), residual Reinforcement Learning (RL), rollout trajectory collection, and data augmentation. Specifically, IL extracts human-like behaviors from demonstrations, and residual RL enhances policy generalization. The learned policy is then used to generate trajectories in simulation, which are further augmented across diverse environments and spatial configurations before being fed back into the next cycle. Over successive iterations, a self-improving data flywheel effect emerges, producing datasets that cover diverse scenarios and thereby scaling policy performance. Experimental results demonstrate that DexFlyWheel generates over 2,000 diverse demonstrations across four challenging tasks. Policies trained on our dataset achieve an average success rate of 81.9\% on the challenge test sets and successfully transfer to the real world through digital twin, achieving a 78.3\% success rate on dual-arm lift tasks.

---

## 论文详细总结（自动生成）

# DexFlyWheel 论文深度总结

## 1. 论文的核心问题与整体含义

- **研究背景**：灵巧操作（Dexterous Manipulation）是提升机器人在真实世界应用能力的关键技术，然而目前高质量、多样化的灵巧操作数据集仍然十分稀缺。
- **核心问题**：现有数据采集方法存在两大瓶颈：
  - **人工依赖**：要么靠人类遥操作，要么需要大量人工工程参与，成本高、扩展性差。
  - **多样性不足**：生成的数据场景单一，难以覆盖丰富的任务变化，限制了策略的泛化能力和数据集的规模化扩展。
- **整体含义**：论文旨在从少量初始演示出发，构建一个能 **自我改进、持续扩展数据多样性** 的自动数据生成框架，从而突破灵巧操作学习中“数据饥渴”和“场景单一”的困境。

## 2. 论文提出的方法论

### 2.1 核心思想：自我改进的数据飞轮

- **DexFlyWheel** 框架模仿“数据飞轮”效应，以 **少量种子演示为起点**，通过 **模仿学习（IL）与残差强化学习（RL）的闭环迭代**，逐步生成越来越多样化的轨迹数据，每一轮生成的数据反馈回下一轮训练，形成正向循环。

### 2.2 关键技术流程（每次迭代的闭环步骤）

1. **种子演示预热（Seed Demonstration Warmup）**
   - 收集有限的一组人类或脚本生成的演示，作为初始训练数据。
2. **模仿学习（IL）提取类人行为**
   - 从当前数据集中学习一个模仿策略，使机器人能够复刻演示中的基本操作技能。
3. **残差强化学习（Residual RL）增强泛化**
   - 在 IL 策略基础上，叠加一个可学习的残差策略，通过 RL 在仿真环境中探索更优的动作修正，提升策略对未见过情景的泛化能力。
4. **轨迹生成与收集**
   - 使用训练好的（IL + Residual RL）策略在仿真器中执行任务，采集大量不同环境下的完整操作轨迹。
5. **数据增强与反馈**
   - 对采集到的轨迹进行跨环境、跨空间配置的增强（如改变物体位姿、光照、物理参数等），扩充为新训练样本，将其合并到数据集中，供下一轮 IL 和 RL 使用。

- **迭代堆积**：上述闭环反复执行，每轮都可以产生比上一轮更加多样化的数据，策略性能也随之不断提升，最终实现“数据自我改进”的飞轮效应。

### 2.3 公式与算法文字说明

- 无具体公式原文，但流程可概括为：
  1. 给定数据集 $D_0$（种子演示），训练 IL 策略 $\pi_{\mathrm{IL}}$；
  2. 训练残差策略 $\pi_{\mathrm{res}}$，使最终策略 $\pi = \pi_{\mathrm{IL}} + \pi_{\mathrm{res}}$，通过 RL 最大化奖励；
  3. 用 $\pi$ 在随机化环境中生成新轨迹集 $T$；
  4. 应用数据增强函数 $Aug(T)$ 得到 $T'$；
  5. 更新数据集 $D_{k+1} = D_k \cup T'$，重复 1–4。

## 3. 实验设计

### 3.1 使用场景与任务

- **四个挑战性任务**（文中未列出具体任务名称，但涵盖了灵巧操控的典型场景），包括双臂提升（dual-arm lift）等复杂作业。
- 生成的数据集规模：**超过 2,000 条多样化演示**。

### 3.2 Benchmark 与对比方法

- 元数据未提供详细对比的 baselines。但从摘要可推断，其主要对比对象可能是：
  - 单纯依靠遥操作或静态数据集的方法；
  - 未引入自改进循环的固定多样性数据收集方法。
- 主要评价指标：**任务成功率**。

### 3.3 仿真与真实世界测试

- **仿真挑战测试集**：策略平均成功率达到 **81.9%**。
- **真实世界迁移**：通过数字孪生（digital twin）将策略部署到真实机器人，在 **双臂提升任务上成功率达 78.3%**，证明生成的多样化数据有助于缩小仿真到现实的差距。

## 4. 资源与算力

- 论文元数据及摘要中**未明确提及**所用的 GPU 型号、数量、训练时长等算力细节。若需精确信息，必须查阅论文全文。

## 5. 实验数量与充分性

- **实验组数**：至少涉及 4 个任务，每个任务生成数千条演示，并进行了仿真和真机双验证。
- **充分性评价**：
  - 实验覆盖了从仿真到现实的完整验证链，体现了数据多样性的提升效果。
  - 然而，因信息有限，无法获知是否包含彻底消融研究（如去掉残差 RL、去掉数据增强、不同迭代轮数的影响）或与其他 SOTA 数据生成方法的定量对比。
  - 若全文中有相应对比实验，则实验设计较为公平客观；若无，则说服力略减。

## 6. 论文的主要结论与发现

- **可扩展数据引擎**：DexFlyWheel 成功证明了通过 IL-RL 闭环迭代，可从少量种子数据自动生成覆盖广泛场景的大规模、多样化演示数据集。
- **策略性能显著提升**：随着迭代进行，生成的策略在挑战性测试集上的成功率持续上升，最终达到 81.9%。
- **仿真到现实高效迁移**：凭借数据多样性，策略无需昂贵微调即可迁移到真实双臂系统，成功率高达 78.3%，验证了框架的现实可行性。
- **“飞轮”效应成立**：自我改进循环能稳定增强数据多样性和策略鲁棒性，为灵巧操作学习提供了一种全新的数据生成范式。

## 7. 优点（方法或实验设计亮点）

- **自改进闭环设计**：将 IL 的行为先验和 RL 的探索能力巧妙融合，并在迭代中不断自我强化，无需持续的人工干预。
- **数据多样性显式驱动**：不仅仅是生成数据，更通过环境随机化和空间增强主动追求多样性，直接解决数据集“单调”的痛点。
- **端到端验证**：同时提供仿真性能和真实世界双臂任务结果，验证了方法的实用价值和迁移能力。
- **可扩展性强**：理论上可适应不同灵巧操作任务，只需更换种子演示和仿真环境。

## 8. 不足与局限

- **算力信息缺失**：摘要未提及资源开销，大规模迭代 IL+RL 可能耗费可观的计算资源，限制了低资源用户的复现。
- **对比基线不详**：无法确认其相对于最新数据生成方案（如直接强化学习、域随机化、其他自生成方法）的优越性，可能存在选择性报告。
- **任务描述模糊**：摘要未具体说明四个任务的具体内容和难度，难以评估其在更广泛灵巧操作场景中的代表性和泛化边界。
- **真实世界验证场景有限**：仅展示了一个双臂提升任务，其他任务的真机表现未知，可能不足以证明全部迁移能力。
- **依赖高质量种子演示**：若初始种子行为差或覆盖不足，飞轮可能难以“转动”到高多样性区域，存在冷启动风险。
- **仿真偏差**：所有增强都在仿真内完成，若仿真器与真实物理差异过大，生成数据的有效性会打折扣。

（完）
