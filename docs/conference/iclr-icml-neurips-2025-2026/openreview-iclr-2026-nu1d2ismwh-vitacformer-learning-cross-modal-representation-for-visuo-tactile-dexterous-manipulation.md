---
title: "ViTacFormer: Learning Cross-Modal Representation for Visuo-Tactile Dexterous Manipulation"
title_zh: "ViTacFormer: 学习视觉-触觉跨模态表征用于灵巧操作"
authors: "Liang Heng, Haoran Geng, Kaifeng Zhang, Pieter Abbeel, Jitendra Malik"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=Nu1D2IsmWH"
tags: ["query:robot"]
score: 10.0
evidence: 融合视觉和触觉的跨模态表征学习用于灵巧操作
tldr: 针对灵巧操作中视觉被遮挡或环境非结构化的问题，提出ViTacFormer，通过跨注意力融合高分辨率视觉与触觉，并预测未来触觉信号，结合由易到难训练课程，提升视觉触觉表征的准确性和鲁棒性。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 纯视觉方法在遮挡或非结构化环境中不足，触觉对精细控制至关重要。
method: 跨注意力编码器融合视觉触觉，自回归预测未来触觉信号，配合课程学习。
result: 跨模态表征在灵巧操作任务中准确性和鲁棒性显著提升。
conclusion: 视觉-触觉跨模态学习有效增强灵巧操作性能。
---

## Abstract
Dexterous manipulation is a cornerstone capability for robotic systems aiming to interact with the physical world in a human-like manner. Although vision-based methods have advanced rapidly, tactile sensing remains crucial for fine-grained control—particularly in unstructured or visually occluded settings. We present ViTacFormer, a representation-learning approach that couples a cross-attention encoder to fuse high-resolution vision and touch with an autoregressive tactile-prediction head that anticipates future contact signals. Building on this architecture, we devise an easy-to-challenging curriculum that steadily refines the visual-tactile latent space, boosting both accuracy and robustness. The learned cross-modal representation drives imitation learning for multi-fingered hands, enabling precise and adaptive manipulation. Across a suite of challenging real-world benchmarks, our method achieves approximately 50% higher success rates than prior state-of-the-art systems. To our knowledge, it is also the first to autonomously complete long-horizon dexterous manipulation tasks that demand highly precise control with an anthropomorphic hand—successfully executing up to 11 sequential stages and sustaining continuous operation for 2.5 minutes.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
融合视觉和触觉的跨模态表征学习用于灵巧操作。

### 2. 核心内容
针对灵巧操作中视觉被遮挡或环境非结构化的问题，提出ViTacFormer，通过跨注意力融合高分辨率视觉与触觉，并预测未来触觉信号，结合由易到难训练课程，提升视觉触觉表征的准确性和鲁棒性。

### 3. 对应检索需求
visual-tactile cross-modal representation learning for manipulation。

### 4. 来源与原文
- Source：ICLR-2026-Public
- OpenReview：[https://openreview.net/forum?id=Nu1D2IsmWH](https://openreview.net/forum?id=Nu1D2IsmWH)
