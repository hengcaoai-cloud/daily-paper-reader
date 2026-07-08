---
title: Contact Map Transfer with Conditional Diffusion Model for Generalizable Dexterous Grasp Generation
title_zh: 基于接触图迁移和条件扩散模型的通用灵巧抓取生成
authors: "Yiyao Ma, Kai Chen, Kexin ZHENG, Qi Dou"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=ou9HeYvNhB"
tags: ["query:robot"]
score: 8.0
evidence: 提出基于扩散模型的灵巧抓取迁移框架，通过接触图生成抓取姿态
tldr: 针对灵巧抓取在未知物体上泛化性差的问题，本文提出基于条件扩散模型的抓取迁移框架，通过生成物体接触图将模板抓取迁移到同类新物体。实验表明该方法在多样物体上可实现稳定抓取，为数据高效的灵巧抓取生成提供了新思路。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 现有灵巧抓取生成方法在新物体和任务上泛化能力不足，受限于数据稀缺。
method: 利用条件扩散模型从形状模板迁移高质量抓取，通过接触图生成实现物体间抓取迁移。
result: 在多个物体类别上成功生成稳定灵巧抓取，显著提升了未知物体的抓取成功率。
conclusion: 该方法为灵巧抓取提供了一种数据高效、可泛化的解决方案，推动了灵巧操作的发展。
---

## Abstract
Dexterous grasp generation is a fundamental challenge in robotics, requiring both grasp stability and adaptability across diverse objects and tasks. Analytical methods ensure stable grasps but are inefficient and lack task adaptability, while generative approaches improve efficiency and task integration but generalize poorly to unseen objects and tasks due to data limitations. In this paper, we propose a transfer-based framework for dexterous grasp generation, leveraging a conditional diffusion model to transfer high-quality grasps from shape templates to novel objects within the same category. Specifically, we reformulate the grasp transfer problem as the generation of an object contact map, incorporating object shape similarity and task specifications into the diffusion process. To handle complex shape variations, we introduce a dual mapping mechanism, capturing intricate geometric relationship between shape templates and novel objects. Beyond the contact map, we derive two additional object-centric maps, the part map and direction map, to encode finer contact details for more stable grasps. We then develop a cascaded conditional diffusion model framework to jointly transfer these three maps, ensuring their intra-consistency. Finally, we introduce a robust grasp recovery mechanism, identifying reliable contact points and optimizing grasp configurations efficiently. Extensive experiments demonstrate the superiority of our proposed method. Our approach effectively balances grasp quality, generation efficiency, and generalization performance across various tasks. Project homepage: https://cmtdiffusion.github.io/

---

## 论文详细总结（自动生成）

### 1. 检索相关性
提出基于扩散模型的灵巧抓取迁移框架，通过接触图生成抓取姿态。

### 2. 核心内容
针对灵巧抓取在未知物体上泛化性差的问题，本文提出基于条件扩散模型的抓取迁移框架，通过生成物体接触图将模板抓取迁移到同类新物体。实验表明该方法在多样物体上可实现稳定抓取，为数据高效的灵巧抓取生成提供了新思路。

### 3. 对应检索需求
robot dexterous manipulation with multi-fingered hands。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=ou9HeYvNhB](https://openreview.net/forum?id=ou9HeYvNhB)
