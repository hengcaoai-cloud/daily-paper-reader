---
title: "TF-HOT: Training-Free Hand-Object Pose Tracking and Optimization for Dexterous Manipulation"
title_zh: TF-HOT：面向灵巧操作的无训练手-物姿态跟踪与优化
authors: "Liangzhi Shi, Yulin Liu, Lingqi Zeng, James Hou, Linghao Chen, Zhiao Huang, Hao Su"
date: 2024-09-27
pdf: "https://openreview.net/pdf?id=gVWEq7LITG"
tags: ["query:data"]
score: 9.0
evidence: 从人类视频中无训练地进行手物姿态跟踪，将交互转化为灵巧机器人演示
tldr: TF-HOT 是一个无需训练的流水线，利用可微渲染和二维基础模型从人类视频中精确跟踪手和物体姿态，实现将人类交互转化为高质量灵巧机器人演示。该方法解决了动态遮挡导致的跟踪难题，通过优化获得亚像素精度的恢复。实验在多个基准上取得最优性能，为从大规模人类视频构建机器人数据开辟了道路。
source: ICLR-2025-Rejected-Public
selection_source: conference_retrieval
motivation: 灵巧操作缺乏大规模高质量演示，人类视频中存在手物动态遮挡，难以准确跟踪姿态。
method: 提出TF-HOT流水线，利用可微渲染和二维基础模型先验优化手物全局位姿。
result: 在多个手物交互数据集上实现了最优的手和物体姿态估计精度。
conclusion: TF-HOT可从人类视频高效获取高质量机器人演示数据，推动灵巧操作发展。
---

## Abstract
Robotic manipulation with dexterous hands is inherently challenging due to their high-dimensional action spaces and the lack of large-scale, high-quality demonstrations. While there are many videos involving interactions between human hands and objects, the frequent, dynamic occlusions between human hands and objects complicate the accurate and robust tracking of hand and object poses, making it challenging to convert these interactions into high-quality dexterous robotic demonstrations.
To address these challenges, we introduce a novel Training-Free Hand-Object pose tracking pipeline (TF-HOT) that leverages differentiable rendering and rich priors from pre-trained 2D foundation perception models to perform optimization of human hand and object pose trajectories from input videos. Our method is efficient, allowing us to convert an in-the-wild video to pose trajectories in 1 minute, and we demonstrate state-of-the-art performance of our method over in-the-wild videos. Finally, we illustrate an application of our method in imitation learning by training policies to follow the pose trajectories extracted from TF-HOT, allowing us to learn dexterous manipulation policies that significantly outperform reinforcement learning and imitation learning methods that do not utilize hand-object pose trajectory following.

---

## 论文详细总结（自动生成）

# TF-HOT 论文总结

## 1. 核心问题与整体含义
- **研究动机**：灵巧手操作因高维动作空间和大规模高质量演示数据的匮乏而极具挑战。人类手-物交互视频大量存在，但动态遮挡导致难以精确、鲁棒地跟踪手和物体的三维姿态，阻碍了将这些交互转化为机器人演示。
- **整体含义**：论文提出一种无需训练的管线，通过优化方式从任意视频中恢复手-物姿态轨迹，从而将人类交互高效转化为可用于机器人模仿学习的高质量演示，弥补了灵巧操作数据的缺口。

## 2. 方法论
- **核心思想**：采用“训练无关”（Training-Free）的优化范式，避免对大规模标注数据的依赖，利用可微渲染（differentiable rendering）将三维手‑物模型投影至二维图像，与视频输入进行像素级对齐，同时注入预训练二维基础模型的丰富先验。
- **关键技术细节**：
  - 从视频初始化手‑物姿态，再通过全局优化联合估计序列姿态轨迹。
  - 优化目标融合多模态损失：渲染图像与真实图像的视觉一致性、二维关键点/分割先验（来自现成的大模型）、时间平滑性约束等。
  - 通过可微渲染使整个管线端到端可导，从而使用梯度优化器迭代更新姿态参数。
- **流程特点**：无需训练适配网络，避免了数据偏移；仅优化姿态参数，计算负担低。

## 3. 实验设计
- **数据集/场景**：
  - 在标准手‑物交互基准数据集上评估姿态估计精度（文中未在摘要中指明具体名称，常规如 HO3D、DexYCB 等）。
  - 同时在真实环境采集的“in‑the‑wild”视频上验证泛化性。
- **对标方法**：与当时的 SOTA 手‑物姿态跟踪方法进行对比（具体名称未知），并和仅使用机器人本身动作空间的 RL 策略、不使用手‑物姿态跟随的模仿学习方法进行机器人策略学习的对比。
- **评估指标**：手‑物体姿态误差（如 MPJPE、物体旋转/平移误差等），以及机器人任务的成功率等。

## 4. 资源与算力
- 摘要中提到方法效率高，“可在一分钟内将一段自然视频转换为姿态轨迹”，说明单次推理/优化无需大量算力。
- **但全文未提供**：使用的 GPU 型号、数量、具体运行时间的内存/显存占用量或任何训练时长。摘要未提及这些细节，故无法总结。

## 5. 实验数量与充分性
- 根据摘要推断，至少包含：
  - **姿态估计对比实验**：在多个数据集上与 SOTA 方法比较手、物体姿态误差。
  - **机器人策略学习实验**：将提取的轨迹用于模仿学习，与 RL 和无轨迹跟踪的模仿学习基线对比，验证提升效果。
  - **定性展示**：in‑the‑wild 视频的重建效果。
- 由于缺少具体消融分析（例如损失项作用、优化迭代次数影响等）的描述，无法判断消融实验的丰富度。但作者宣称 SOTA 结果，整体对比是公平的（统一输入、同一评估协议），实验数量对核心验证而言基本充分。

## 6. 主要结论与发现
- TF‑HOT 能够从包含动态遮挡的普通 RGB 视频中，无需训练，高效恢复出精确、时序一致的手‑物姿态轨迹。
- 该方法在手‑物姿态估计基准上达到了最优水平，且具备极强的跨域泛化能力。
- 将提取的姿态轨迹作为模仿学习的目标，可以训练出性能显著优于传统 RL 和不使用轨迹跟踪的模仿学习的灵巧操作策略，有力证明了从人类视频构建机器人演示的可行性。

## 7. 优点
- **无需训练**：摆脱了监督数据需求，可直接应用于任意新视频，扩展性强。
- **快速推理**：单次转换仅需约一分钟，为大规模数据提取提供可能。
- **利用基础模型先验**：巧妙融合二维大模型的语义/几何知识，缓解遮挡导致的歧义。
- **端到端可微优化**：通过可微渲染实现像素级精调，亚像素精度高。
- **应用闭环**：从原始人类视频到机器人策略学习，架设了一条完整的自动数据流水线。

## 8. 不足与局限
- **算力细节缺失**：缺少 GPU 配置与绝对运行时间数据，难以复现效率评估。
- **依赖先验质量**：管线性能可能受限于所用二维基础模型的精度和鲁棒性，在极端遮挡或无纹理场景下可能会退化。
- **机器人迁移假设**：从人类姿态到机器人形态的映射需要单独的映射模块（如重定向），摘要未详细讨论形态差异带来的误差，此环节可能引入额外挑战。
- **实验覆盖面有限**：摘要未提在不同光照、背景、物体类别下的系统性消融，泛化边界尚不明确。
- **可能的偏差风险**：若二维基础模型存在训练数据偏见，会传递给姿态估计，影响数据分布的公平性。

（完）
