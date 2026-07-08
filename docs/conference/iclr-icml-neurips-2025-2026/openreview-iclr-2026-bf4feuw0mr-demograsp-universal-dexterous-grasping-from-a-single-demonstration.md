---
title: "DemoGrasp: Universal Dexterous Grasping from a Single Demonstration"
title_zh: "DemoGrasp: 从单一演示实现通用灵巧抓取"
authors: "Haoqi Yuan, Ziye Huang, Ye Wang, Chuan Mao, Chaoyi Xu, Zongqing Lu"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=Bf4FeuW0Mr"
tags: ["query:robot"]
score: 10.0
evidence: 从单一演示实现通用灵巧抓取，通过编辑腕部位姿和手部关节角度适应新物体
tldr: DemoGrasp 针对多指灵巧手通用抓取中强化学习探索困难的问题，提出从单一抓取演示出发，通过编辑动作中的腕部位姿和手部关节角度来适应新物体和姿态，无需复杂奖励设计。在多样化物体上验证了有效的通用抓取能力。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 多指灵巧手通用抓取因高维、长时域探索而需要复杂奖励和课程设计，易导致次优解。
method: 从单一成功抓取演示轨迹出发，通过改变腕部位姿决定抓取位置，改变手部关节角度调整抓取姿态，进行动作编辑。
result: 在多种物体和姿态下实现了通用灵巧抓取，性能优于需要复杂设计的强化学习方法。
conclusion: 基于演示的动作编辑是一种简单有效的通用灵巧抓取学习范式。
---

## Abstract
Universal grasping with multi-fingered dexterous hands is a fundamental challenge in robotic manipulation. While recent approaches successfully learn closed-loop grasping policies using reinforcement learning (RL), the inherent difficulty of high-dimensional, long-horizon exploration necessitates complex reward and curriculum design, often resulting in suboptimal solutions across diverse objects. We propose DemoGrasp, a simple yet effective method for learning universal dexterous grasping. We start from a single successful demonstration trajectory of grasping a specific object and adapt to novel objects and poses by editing the robot actions in this trajectory: changing the wrist pose determines where to grasp, and changing the hand joint angles determines how to grasp. We formulate this trajectory editing as a single-step Markov Decision Process (MDP) and use RL to optimize a universal policy across hundreds of objects in parallel in simulation, with a simple reward consisting of a binary success term and a robot–table collision penalty. In simulation, DemoGrasp achieves a 95% success rate on DexGraspNet objects using the Shadow Hand, outperforming previous state-of-the-art methods. It also shows strong transferability, achieving an average success rate of 84.6% across diverse dexterous hand embodiments on six unseen object datasets, while being trained on only 175 objects. Through vision-based imitation learning, our policy successfully grasps 110 unseen real-world objects, including small, thin items. It generalizes to spatial, background, and lighting changes, supports both RGB and depth inputs, and extends to language-guided grasping in cluttered scenes.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义
- **研究背景**：多指灵巧手（如 Shadow Hand）在机器人操作中实现通用抓取是一个根本性挑战。抓取任务的高维动作空间与长时程特性，使强化学习（RL）探索极为困难。
- **现有方法痛点**：主流 RL 方法不得不依赖复杂的奖励设计和课程学习来引导探索，这不仅增加了工程负担，还容易收敛到对不同物体适应性差的次优解。
- **论文含义**：提出 DemoGrasp 方法，试图用极简范式替代复杂设计——**仅从一条成功的抓取演示轨迹出发**，通过编辑动作中的腕部位姿和手指关节角度，即能以较高的成功率泛化到大量新物体，避免了繁琐的奖励工程，展现出“简单而有效”的通用灵巧抓取新思路。

## 2. 论文提出的方法论
- **核心思想**
  - 利用**单一抓取演示轨迹**（对某个特定物体的成功抓取），将该轨迹中的机器人动作视为可编辑的原型。
  - **动作编辑双要素**：修改腕部位姿（决定“在哪儿抓”）和修改手部关节角度（决定“怎么抓”），使原轨迹适应新物体的几何形状与位姿。
- **问题形式化**
  - 将轨迹编辑过程建模为**单步马尔可夫决策过程（MDP）**，即策略仅基于当前观测（如物体点云或状态）输出一次编辑动作，而非逐步交互。
  - 使用强化学习在仿真中并行训练一个通用策略，优化编辑动作。
- **奖励设计**
  - 采用极简的二值奖励结构：抓取成功项 + 机器人与桌面碰撞惩罚。
  - 无需分阶段课程或密集引导奖励。
- **策略学习与迁移**
  - 在数百个物体上并行仿真训练通用策略。
  - 仿真策略可直接部署，也可通过视觉模仿学习（如行为克隆）扩展到真实世界，支持 RGB/深度输入及语言引导。

## 3. 实验设计
- **仿真基准与物体集**
  - 主实验使用 **Shadow Hand** 在 **DexGraspNet** 物体集上测试，训练物体约 175 个。
  - **跨形态泛化**：在 6 个未见物体数据集上、多种不同灵巧手构型上评估迁移能力。
- **对比方法**
  - 与先前的 SOTA 方法对比（摘要中提及 outperforming previous state-of-the-art methods，未列出具体名称），这些方法通常依赖复杂的奖励和课程设计。
- **真实世界实验**
  - 通过视觉模仿学习，策略成功抓取 **110 个未见过的真实物体**，包括小型、薄壁物体。
  - 验证了在空间位置、背景和光照变化下的鲁棒性。
  - 支持 RGB 与深度两种视觉模态。
  - 扩展到语言引导的杂乱场景抓取。

## 4. 资源与算力
- 论文提供的摘要及元数据中**未明确说明训练所使用的 GPU 型号、数量及训练时长**。这一部分信息在公开材料中缺失，无法给出具体算力估计。

## 5. 实验数量与充分性
- **实验覆盖**
  - 多组仿真评估：标准基准成功率、跨 6 个数据集泛化、多灵巧手构型。
  - 真实世界系统验证：110 个未见物体、环境泛化、视觉模态、语言引导。
  - 整体实验层次从仿真到现实、从单一手到多手、从视觉到语言，较为丰富。
- **充分性、客观性与公平性**
  - 对比对象是先前需要复杂设计的 SOTA 方法，使用同一物体集或公开基准（如 DexGraspNet），具备可比性。
  - 未见物体的仿真和真实测试数量较大，能较好反映泛化能力。
  - 消融研究细节虽未在摘要中展开，但方法本身组件明确（单演示 vs. 无演示、简单奖励 vs. 复杂奖励），留有验证空间；从已披露实验看，设计较为充分。

## 6. 论文的主要结论与发现
- **方法有效性**：DemoGrasp 仅依赖单一抓取演示，在 Shadow Hand + DexGraspNet 上取得 **95% 成功率**，超越以往需复杂奖励设计的 SOTA。
- **泛化能力**：在 6 个未见数据集及多种灵巧手形态上平均成功率 **84.6%**，展示出良好的跨物体、跨手型迁移。
- **真实世界可行性**：通过模仿学习成功抓取 110 个未见物体，且能适应环境变化、输入模态和语言指令，具备实用潜力。
- **范式总结**：基于演示的动作编辑是一种简单有效的通用灵巧抓取学习范式，避免了繁琐的奖励和课程工程。

## 7. 优点
- **方法简洁**：摈弃复杂奖励与课程，仅用单一演示和简单二值奖励，显著降低设计门槛。
- **通用性强**：一次训练可泛化到大量新物体、新灵巧手形态，并迁移到真实世界。
- **真实实验充分**：涵盖多种物体（含薄小件）、环境变化、视觉模态和语言引导，验证全面且贴近实际部署需求。
- **思想明确**：将轨迹编辑看作单步决策，问题建模清晰，易于复现和扩展。

## 8. 不足与局限
- **算力信息缺失**：摘要及元数据未提供训练所用 GPU 数、时间等，无法评估计算开销。
- **对演示依赖**：方法基于单一成功演示，若该演示质量较差或无法覆盖关键接触模式，可能影响策略上界。
- **训练物体规模有限**：仿真训练仅使用 175 个物体，虽泛化效果良好，但面对极端或全新类别物体时是否依然鲁棒未经验证。
- **真实世界需额外学习**：仿真策略无法零样本迁移，还需借助视觉模仿学习环节，引入额外的数据采集与训练成本。
- **单步 MDP 假设**：轨迹编辑被简化为单步决策，可能忽略抓取过程中的序贯动态调整，对于需要动态适应或交互复杂场景可能不够精细。

（完）
