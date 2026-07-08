---
title: "DexGarmentLab: Dexterous Garment Manipulation Environment with Generalizable Policy"
title_zh: DexGarmentLab：灵巧衣物操作环境与可泛化策略
authors: "Yuran Wang, Ruihai Wu, Yue Chen, Jiarui Wang, Jiaqi Liang, Ziyu Zhu, Haoran Geng, Jitendra Malik, Pieter Abbeel, Hao Dong"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=ZZ09oX2Xpo"
tags: ["query:robot"]
score: 9.0
evidence: 首个专为灵巧双手衣物操作设计的仿真环境，包含大规模3D资产和15个任务场景
tldr: 该工作针对灵巧衣物操作缺乏逼真仿真环境的问题，提出首个专门面向双手衣物操作的环境DexGarmentLab，提供15个任务场景的大规模高质量3D资产，并改进了衣物建模技术以缩小仿真与现实的差距。实验表明该环境可用于评估灵巧操作策略的泛化能力，为灵巧操作基准测试提供了重要平台。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 现有灵巧衣物操作研究受限于缺乏逼真仿真环境，难以评估策略泛化性。
method: 构建首个面向双手灵巧衣物操作的仿真环境，包含15个任务场景与高质量3D资产，优化衣物形变与接触建模。
result: 所提环境能有效缩小仿真与现实差距，支持灵巧操作策略的可靠评估。
conclusion: DexGarmentLab为灵巧衣物操作提供了首个基准测试平台，显著推进了该领域的研究。
---

## Abstract
Garment manipulation is a critical challenge due to the diversity in garment categories, geometries, and deformations. Despite this, humans can effortlessly handle garments, thanks to the dexterity of our hands. However, existing research in the field has struggled to replicate this level of dexterity, primarily hindered by the lack of realistic simulations of dexterous garment manipulation. Therefore, we propose DexGarmentLab, the first environment specifically designed for dexterous (especially bimanual) garment manipulation, which features large-scale high-quality 3D assets for 15 task scenarios, and refines simulation techniques tailored for garment modeling to reduce the sim-to-real gap. Previous data collection typically relies on teleoperation or training expert reinforcement learning (RL) policies, which are labor-intensive and inefficient. In this paper, we leverage garment structural correspondence to automatically generate a dataset with diverse trajectories using only a single expert demonstration, significantly reducing manual intervention. However, even extensive demonstrations cannot cover the infinite states of garments, which necessitates the exploration of new algorithms. To improve generalization across diverse garment shapes and deformations, we propose a Hierarchical gArment-manipuLation pOlicy (HALO). It first identifies transferable affordance points to accurately locate the manipulation area, then generates generalizable trajectories to complete the task. Through extensive experiments and detailed analysis of our method and baseline, we demonstrate that HALO consistently outperforms existing methods, successfully generalizing to previously unseen instances even with significant variations in shape and deformation where others fail. Our project page is available at: https://wayrise.github.io/DexGarmentLab/.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
首个专为灵巧双手衣物操作设计的仿真环境，包含大规模3D资产和15个任务场景。

### 2. 核心内容
该工作针对灵巧衣物操作缺乏逼真仿真环境的问题，提出首个专门面向双手衣物操作的环境DexGarmentLab，提供15个任务场景的大规模高质量3D资产，并改进了衣物建模技术以缩小仿真与现实的差距。实验表明该环境可用于评估灵巧操作策略的泛化能力，为灵巧操作基准测试提供了重要平台。

### 3. 对应检索需求
benchmarks for evaluating dexterous manipulation policies。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=ZZ09oX2Xpo](https://openreview.net/forum?id=ZZ09oX2Xpo)
