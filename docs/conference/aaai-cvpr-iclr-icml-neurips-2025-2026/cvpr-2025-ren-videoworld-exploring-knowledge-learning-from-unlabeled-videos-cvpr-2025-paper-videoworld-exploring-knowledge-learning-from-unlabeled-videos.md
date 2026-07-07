---
title: "VideoWorld: Exploring Knowledge Learning from Unlabeled Videos"
title_zh: VideoWorld：探索从未标记视频中学习知识
authors: "Ren, Zhongwei, Wei, Yunchao, Guo, Xun, Zhao, Yao, Kang, Bingyi, Feng, Jiashi, Jin, Xiaojie"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Ren_VideoWorld_Exploring_Knowledge_Learning_from_Unlabeled_Videos_CVPR_2025_paper.pdf"
tags: ["query:data"]
score: 7.0
evidence: 使用从未标记视频训练的视频生成模型，学习用于机器人控制的知识
tldr: 探索仅从视觉输入学习复杂知识的可能性，开发了自回归视频生成模型VideoWorld，实验表明仅靠未标记视频训练即可获得围棋和机器人控制所需的规则、推理和规划能力，关键在于视觉变化表示。该工作表明大规模未标记视频数据是机器人学习的丰富知识源，视觉变化表示至关重要。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-ren-videoworld-exploring-knowledge-learning-from-unlabeled-videos-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 854, \"height\": 402, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-ren-videoworld-exploring-knowledge-learning-from-unlabeled-videos-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 774, \"height\": 566, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-ren-videoworld-exploring-knowledge-learning-from-unlabeled-videos-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 866, \"height\": 880, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-ren-videoworld-exploring-knowledge-learning-from-unlabeled-videos-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 709, \"height\": 814, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-ren-videoworld-exploring-knowledge-learning-from-unlabeled-videos-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1797, \"height\": 843, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-ren-videoworld-exploring-knowledge-learning-from-unlabeled-videos-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 855, \"height\": 770, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ren-videoworld-exploring-knowledge-learning-from-unlabeled-videos-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 867, \"height\": 388, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ren-videoworld-exploring-knowledge-learning-from-unlabeled-videos-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1814, \"height\": 446, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ren-videoworld-exploring-knowledge-learning-from-unlabeled-videos-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 860, \"height\": 207, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ren-videoworld-exploring-knowledge-learning-from-unlabeled-videos-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 505, \"height\": 234, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ren-videoworld-exploring-knowledge-learning-from-unlabeled-videos-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1645, \"height\": 238, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ren-videoworld-exploring-knowledge-learning-from-unlabeled-videos-cvpr-2025-paper/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 649, \"height\": 235, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ren-videoworld-exploring-knowledge-learning-from-unlabeled-videos-cvpr-2025-paper/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 416, \"height\": 265, \"label\": \"Table\"}]"
motivation: 当前模型主要依赖文本，但视觉信息是否足以学习复杂知识尚待探索。
method: 提出VideoWorld，基于自回归视频生成，引入潜在动力学模型（LDM）以高效编码视觉变化。
result: 在视频围棋和机器人控制任务中，VideoWorld成功学习到规则和规划能力，验证了纯视觉学习的可行性。
conclusion: 该工作表明大规模未标记视频数据是机器人学习的丰富知识源，视觉变化表示至关重要。
---

## Abstract
This work explores whether a deep generative model can learn complex knowledge solely from visual input, in contrast to the prevalent focus on text-based models like large language models (LLMs). We develop VideoWorld, an auto-regressive video generation model trained on unlabeled video data, and test its knowledge acquisition abilities in video-based Go and robotic control tasks. Our experiments reveal two key findings: (1) video-only training provides sufficient information for learning knowledge, including rules, reasoning and planning capabilities, and (2) the representation of visual change is crucial for knowledge acquisition. To improve both the efficiency and efficacy of this process, we introduce the Latent Dynamics Model (LDM) as a key component of VideoWorld. Remarkably, VideoWorld reaches a 5-dan professional level in the Video-GoBench with just a 300-million-parameter model, without relying on search algorithms or reward mechanisms typical in reinforcement learning. In robotic tasks, VideoWorld effectively learns diverse control operations and generalizes across environments, approaching the performance of oracle models in CALVIN and RLBench. This study opens new avenues for knowledge acquisition from visual data, with all code, data, and models open-sourced for further research.

---

## 论文详细总结（自动生成）

# VideoWorld：探索从未标记视频中学习知识

## 1. 核心问题与研究背景
- **核心问题**：当前主流模型（如大语言模型）通过大规模文本学习知识与推理能力，但自然界生物（如灵长类动物）主要通过视觉观察而非语言获取生存技能。本文探索一个根本性问题：**深度生成模型能否仅从原始视觉输入中习得复杂的规则、推理与规划能力**，而不依赖文本标注、奖励信号或搜索算法。
- **研究背景**：视频生成模型近年快速发展，但多数仍需语言或动作标签进行策略学习。部分工作已利用视频进行策略学习，但普遍局限于简单控制且依赖语言指令，尚未涉及需长程推理的任务。本文将视频学习拓展至围棋（需复杂策略）和机器人操作，检验纯视觉信号的潜力。

## 2. 方法论

### 基础框架
- 采用基于 VQ‑VAE + 自回归 Transformer 的视频生成模型，将每一帧离散化为 token，并通过下一帧预测范式训练。
- 推理阶段，生成下一帧后，利用一个**逆向动力学模型（IDM）** 将相邻帧映射为具体动作（如围棋落子位置或机器人末端位移），从而在不使用动作标签的前提下完成策略学习。

### 关键洞察
- 实验发现，基础框架能从原始视频中学会围棋规则和基础机器人操作，但学习效率显著低于直接利用状态序列（如棋盘坐标）的模型。原因在于**视觉变化的表示不够紧凑**，原始视频需大量 token 描述动作相关变化，削弱了学习信号。

### 核心贡献：潜在动力学模型（LDM）
- **动机**：压缩多步视觉变化，提供紧凑、富含时序信息的表示。
- **结构**：
  - 使用一个因果编解码器（causal codec），对当前帧及后续 H 帧进行编码，但不做量化以保留细节。
  - 引入一组可学习的查询向量 \( q_h \)，通过交叉注意力机制逐步提取从 \( t \) 到 \( t+h \) 的视觉变化，经 FSQ 离散量化得到潜码 \( z_h^t \)。
  - 解码器根据当前特征图 \( f_t \) 和所有潜码，因果地重建未来帧 \( x_{t+1} \) 到 \( x_{t+H} \)，以 ℓ2 重构损失训练。
- **集成至自回归 Transformer**：LDM 提取的潜码与离散化的视频 token 拼接，作为 Transformer 的预测目标。词表合并了视频 token 和 LDM 码本，使模型同时生成视觉帧和潜码。
- **动作映射**：IDM 扩展为利用当前帧、预测帧及对应 LDM 潜码，输出动作决策。

## 3. 实验设计与基准
### 数据集与环境
- **Video‑GoBench**（自建）：1000 万盘 9×9 围棋对局，来源包括 KataGO 自对弈（320 万局）和人类对弈（780 万局）并经 KataGO 重新标注，共约 4 亿个状态图像。测试集 1000 局，剔除开局以检验新局面的泛化。
- **CALVIN**：语言条件化的长程机器人操控基准，评估 Push Blocks、Open/Close Drawer、Turn On/Off Light 三个任务。额外生成了 30k 轨迹用于数据增强实验。
- **RLBench**：增加 Close Microwave、Close Fridge 两个视觉差异较大的任务，与 CALVIN 联合训练以验证跨环境泛化。

### 评价指标
- 围棋：合法率、Elo 等级分（与 KataGO‑1d/5d/9d 的人类水平对比）、最佳动作命中率、动作价值比（与 KataGO‑9d 的一致程度）。
- 机器人：各任务的成功率。

### 对比方法
- 围棋：RL 驱动的不同 KataGO 水平版本；基于状态训练的 Transformer；基础视频 Transformer；以及 VideoWorld （50M、150M、300M 参数）。
- 机器人：MCIL、HULC、SPIL、LCD 等动作监督方法，Oracle Transformer（带动作标签），以及基础视频 Transformer 和 VideoWorld（不同数据量）。

## 4. 资源与算力
- 论文中**未明确说明**所使用的 GPU 型号、数量及训练耗时。仅提及模型规模（最大 300M 参数）和训练数据量，算力开销信息缺失。

## 5. 实验数量与充分性
- 整体设计充分，涵盖**多组对照**：
  - **主实验表**：围棋（Table 1）和 CALVIN（Table 2）上多种基线及 VideoWorld 不同规模/数据量的对比。
  - **跨环境泛化**：CALVIN 与 RLBench 联合训练（Table 3）。
  - **分析实验**：压缩长度 H 的影响（Table 4a, 4b）、潜码干预（Table 4c）、码书尺寸（Table 4d）、数据来源与质量（Table 4e）。
  - **可视化分析**：潜码 UMAP 投影展示所学模式，前向规划示例。
- 评估指标全面，比较公平，消融充分揭示了 LDM 的设计选择对性能的影响。

## 6. 主要结论与发现
1. 从未标注视频中进行下一帧预测，**足以习得复杂的规则、推理与规划能力**，包括围棋基本规则与中高级策略、机器人操控技能。
2. **紧凑的视觉变化表示对知识获取至关重要**。原始视频 token 存在冗余，经由 LDM 压缩的多步变化潜码显著提升了学习效率与最终性能。
3. VideoWorld 仅凭 300M 参数即达到**业余 5 段**的人类围棋水平，无需搜索或奖励信号，并在 CALVIN 及 RLBench 上接近使用真实动作标签的 **Oracle 模型**，且展现出跨环境的泛化能力。
4. 模型表现出**数据缩放特性**，增加训练数据或模型容量可进一步提升性能。

## 7. 优点
- **开创性探索**：首次系统性地证明纯视频生成模型可习得高水平推理和规划，打破对文本标签或强化学习的依赖。
- **方法简洁有效**：LDM 设计精巧，通过压缩视觉变化提升学习效率，可即插即用地集成到自回归生成框架中。
- **基准建设**：公开了 Video‑GoBench 数据集，为后续研究奠定基础。
- **通用性**：同一框架在围棋和多种机器人操控任务上均取得优异结果，显示了统一视觉策略学习的潜力。
- **充分开源**：代码、数据、模型全部开放，可复现性强。

## 8. 不足与局限
- **大规模探索有限**：模型最大 300M 参数，训练数据量相对较小，尚未验证在更大规模预训练下的能力上限。
- **真实世界应用缺失**：实验在简化视觉的围棋环境和仿真机器人中进行，未处理复杂纹理、光照变化，距真实部署仍有差距。
- **仍需少量标签**：逆动力学模型需少量动作标签进行训练，并非完全无监督的策略提取。
- **计算资源不透明**：未报告训练用的具体硬件和耗时，无法评估所需算力门槛。
- **任务范围较窄**：目前局限于两款基准，且围棋已脱离低层视觉细节，对更复杂的开放世界视觉任务泛化性未知。

（完）
