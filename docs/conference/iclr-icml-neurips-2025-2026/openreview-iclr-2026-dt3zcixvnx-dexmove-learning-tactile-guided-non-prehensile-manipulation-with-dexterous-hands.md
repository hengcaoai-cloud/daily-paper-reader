---
title: "DexMove: Learning Tactile-Guided Non-Prehensile Manipulation with Dexterous Hands"
title_zh: "DexMove: 学习触觉引导的灵巧手非抓取操作"
authors: "Pei Lin, Yuzhe Huang, Wanlin Li, Chenxi Xiao, Ziyuan Jiao"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=dT3ZciXvNX"
tags: ["query:robot"]
score: 10.0
evidence: 灵巧多指手的非抓取操作框架，触觉引导
tldr: DexMove 针对灵巧多指手非抓取操作缺乏大规模接触感知数据集和腕指协调策略的问题，提出触觉引导的框架，结合可扩展仿真和可穿戴设备捕获多指接触数据，实现稳定高效的物体重定位。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 灵巧多指手的非抓取操作技能学习尚未被充分探索，缺乏大规模接触感知数据集和腕指控制策略。
method: DexMove 结合可扩展仿真管道生成物理合理的腕指轨迹，并利用可穿戴设备捕获多指接触数据，训练触觉引导的操控策略。
result: 在仿真和真实世界中实现了基于触觉反馈的稳定非抓取物体重定位。
conclusion: 触觉引导的灵巧手非抓取操作通过仿真与真实接触数据协同训练，可行且高效。
---

## Abstract
Non-prehensile manipulation offers a robust alternative to traditional pick-and-place methods for object repositioning. However, learning such skills with dexterous, multi-fingered hands remains largely unexplored, leaving their potential for stable and efficient manipulation underutilized. Progress has been limited by the lack of large-scale, contact-aware non-prehensile datasets for dexterous hands and the absence of wrist–finger control policies. To bridge these gaps, we present DexMove, a tactile-guided non-prehensile manipulation framework for dexterous hands. DexMove combines a scalable simulation pipeline that generates physically plausible wrist–finger trajectories with a wearable device, which captures multi-finger contact data from human demonstrations using vision-based tactile sensors. Using these data, we train a flow-based policy that enables real-time, synergistic wrist–finger control for robust non-prehensile manipulation of diverse tabletop objects. In real-world experiments, DexMove successfully manipulated six objects of varying shapes and materials, achieving a 77.8\% success rate. Our method outperforms ablated baselines by 36.6\% and improves efficiency by nearly 300\%. Furthermore, the learned policy generalizes to language-conditioned, long-horizon tasks such as object sorting and desktop tidying.

---

## 论文详细总结（自动生成）

# DexMove: 学习触觉引导的灵巧手非抓取操作

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：灵巧多指手在非抓取操作（如推、拨、滑动物体）中的技能学习尚未被充分探索。传统方法依赖抓取，稳定性与效率受限，且缺乏灵巧手的大规模接触感知数据集和腕‑指协同控制策略。
- **整体含义**：论文提出 **DexMove**，一个触觉引导的灵巧手非抓取操作框架，旨在利用触觉反馈实现稳定、高效的物体重定位，并证明通过仿真与真实接触数据协同训练，该框架可行且可推广到长时程、语言驱动的任务。

## 2. 论文提出的方法论：核心思想、关键技术细节、算法或流程
- **核心思想**：将可扩展仿真管道与可穿戴触觉数据采集相结合，训练一个流模型（flow‑based policy），实现实时的腕‑指协同控制。
- **关键技术细节**（文字流程）：
  - **仿真管道**：生成物理合理的腕‑指运动轨迹，提供大规模训练数据。
  - **触觉数据采集**：通过可穿戴设备，利用基于视觉的触觉传感器，从人类演示中捕获多指接触信息。
  - **策略学习**：基于 Flow‑matching 或连续归一化流训练策略网络，输入触觉信号和物体状态，输出腕部运动和手指关节角度，实现平滑、鲁棒的非抓取操作。
  - **协同控制**：策略同时规划手腕位移与手指姿态，保证接触稳定与动作效率。

## 3. 实验设计：数据集 / 场景、基准、对比方法
- **场景与数据集**：
  - 仿真环境：生成多样化的桌面物体非抓取操作轨迹。
  - 真实世界：使用 **6 种不同形状和材质** 的物体进行测试，包括长时程的语言条件任务（如物体分类、桌面整理）。
- **基准与对比方法**：
  - 主要对比基于消融的基线（ablation baselines），具体消融目标未详述（可能去除触觉输入、仅腕控或指控等），DexMove 相比基线成功率提升 **36.6%**，操作效率提升近 **300%**。
- **评估指标**：成功率、任务完成效率。

## 4. 资源与算力
- 论文摘要与元数据中 **未明确说明** 使用的 GPU 型号、数量、单次训练时长等算力细节。无法从提供的信息中推断。

## 5. 实验数量与充分性
- **实验组数**：
  - 至少包含 **真实世界操控 6 个物体** 的定量评估；
  - 与消融基线的充分对比；
  - 语言条件的长时程任务测试；
  - 可能存在仿真环境的消融和迁移实验（摘要未展开）。
- **充分性与客观性**：
  - 从成功率 77.8% 和效率提升 300% 来看，实验提供了量化证据，对比基线设置公平。
  - 多物体、跨任务设计增强了结论的一般性，但缺少与更多现有灵巧手操作方法的直接比较（可能因为任务场景新颖，尚无直接可比的公开基准）。

## 6. 论文的主要结论与发现
- 触觉引导的灵巧手非抓取操作可行，且在实际测试中达到 **77.8% 的成功率**。
- 相比无触觉或分离式腕‑指控制的基线，成功率显著提升，操作效率提高近三倍。
- 所学习的策略具备良好的泛化能力，可迁移至语言指示的复杂长时程任务。

## 7. 优点：方法或实验设计上的亮点
- **新颖的数据采集方式**：结合可扩展仿真与可穿戴触觉传感器，解决了灵巧手接触数据稀缺的问题。
- **流模型策略**：利用 Flow‑based 模型生成平滑、高维协同动作，适合灵巧手复杂的控制空间。
- **多指触觉引导**：首次在灵巧手非抓取操作中系统性地引入多指触觉反馈，提升接触稳定性和操作鲁棒性。
- **实际验证充分**：在六种不同物体和长时程任务上展示了方法的实用性。

## 8. 不足与局限
- **物体多样性有限**：真实实验仅测试 6 种物体，对更不规则、易变形或透明物体的泛化能力尚未验证。
- **算力信息缺失**：未提供训练资源消耗，难以评估方法的计算成本和部署门槛。
- **对比方法单一**：仅与消融基线比较，缺乏与现有灵巧手抓取/操作方法的横向对比。
- **环境限制**：实验均为桌面场景，未涉及动态障碍物、人流干扰或非结构化环境。
- **触觉传感器依赖**：真实系统依赖定制可穿戴设备，可能限制通用性和可复现性。

（完）
