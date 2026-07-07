---
title: "GraphMimic: Graph-to-Graphs Generative Modeling from Videos for Policy Learning"
title_zh: GraphMimic：基于图到图生成建模的视频策略学习
authors: "Chen, Guangyan, Cui, Te, Wang, Meiling, Yang, Chengcai, Hu, Mengxiao, Lu, Haoyang, Mu, Yao, Peng, Zicai, Zhou, Tianxing, Jiang, Xinran, Yang, Yi, Yue, Yufeng"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_GraphMimic_Graph-to-Graphs_Generative_Modeling_from_Videos_for_Policy_Learning_CVPR_2025_paper.pdf"
tags: ["query:data"]
score: 7.0
evidence: 利用视频数据的图生成建模预训练策略，用于从人类视频中学习机器人操作
tldr: GraphMimic将视频帧抽象为物体和视觉动作图，通过图生成模型预测未来图状态，从而从无动作标签的视频数据中预训练策略模型。该方法有效利用了大规模视频数据中的物理和行为知识，为机器人从人类视频中学习操作技能提供了可扩展的途径。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-chen-graphmimic-graph-to-graphs-generative-modeling-from-videos-for-policy-learning-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 875, \"height\": 815, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-chen-graphmimic-graph-to-graphs-generative-modeling-from-videos-for-policy-learning-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1636, \"height\": 714, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-chen-graphmimic-graph-to-graphs-generative-modeling-from-videos-for-policy-learning-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 867, \"height\": 541, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-chen-graphmimic-graph-to-graphs-generative-modeling-from-videos-for-policy-learning-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1788, \"height\": 358, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-chen-graphmimic-graph-to-graphs-generative-modeling-from-videos-for-policy-learning-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1775, \"height\": 897, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-chen-graphmimic-graph-to-graphs-generative-modeling-from-videos-for-policy-learning-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1789, \"height\": 307, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-chen-graphmimic-graph-to-graphs-generative-modeling-from-videos-for-policy-learning-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1773, \"height\": 802, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-chen-graphmimic-graph-to-graphs-generative-modeling-from-videos-for-policy-learning-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 883, \"height\": 455, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-chen-graphmimic-graph-to-graphs-generative-modeling-from-videos-for-policy-learning-cvpr-2025-paper/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 861, \"height\": 209, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-chen-graphmimic-graph-to-graphs-generative-modeling-from-videos-for-policy-learning-cvpr-2025-paper/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 884, \"height\": 455, \"label\": \"Table\"}]"
motivation: 标注动作的机器人演示数据昂贵，视频数据丰富但难以直接用于策略学习。
method: 将视频抽象为图表示，用图到图生成模型预测未来图，预训练策略网络。
result: 在多种操作任务上，用视频预训练的模型表现优于从头训练。
conclusion: GraphMimic展示了利用无标注视频预训练提升机器人策略学习的有效性。
---

## Abstract
Learning from demonstration is a powerful method for robotic skill acquisition. However, the significant expense of collecting such action-labeled robot data presents a major bottleneck. Video data, a rich data source encompassing diverse behavioral and physical knowledge, emerges as a promising alternative. In this paper, we present GraphMimic, a novel paradigm that leverages video data via graph-to-graphs generative modeling, which pre-trains models to generate future graphs conditioned on the graph within a video frame. Specifically, GraphMimic abstracts video frames into object and visual action vertices, and constructs graphs for state representations. The graph generative modeling network then effectively models internal structures and spatial relationships within the constructed graphs, aiming to generate future graphs. The generated graphs serve as conditions for the control policy, mapping to robot actions. Our concise approach captures important spatial relations and enhances future graph generation accuracy, enabling the acquisition of robust policies from limited action-labeled data. Furthermore, the transferable graph representations facilitate the effective learning of manipulation skills from cross-embodiment videos. Our experiments exhibit that GraphMimic achieves superior performance using merely 20% action-labeled data. Moreover, our method outperforms the state-of-the-art method by over 17% and 23% in simulation and real-world experiments, and delivers improvements of over 33% in cross-embodiment transfer experiments.

---

## 论文详细总结（自动生成）

### 论文核心问题与整体含义  
- **研究动机**：演示学习是机器人技能获取的有效范式，但标注动作的机器人数据收集成本高昂，成为主要瓶颈。  
- **背景问题**：视频数据（如人类操作视频）蕴含丰富的行为与物理知识，却因缺乏动作标签而难以直接用于策略学习；现有视频预测方法多基于像素空间建模，忽略了物体内部结构、空间关系以及物体与效应器之间的相互作用。  
- **整体含义**：本文提出 GraphMimic，将视频预训练形式化为“图到图的生成建模”，通过构建并预测视频帧中的图表示，将无标签视频的知识迁移到机器人策略学习中，从而大幅减少对标注动作数据的依赖，并支持跨具身（cross-embodiment）迁移。  

### 方法论  
GraphMimic 的核心思想是利用视频帧构造“动作感知的可迁移图”，并通过层级化图生成网络预测未来图序列，为下游策略提供精准的引导信息。

- **动作感知的可迁移图 (Action-informed Transferable Graph)**  
  - 从视频帧中提取顶点：  
    - **物体顶点**：用 VLMs 识别任务相关物体，通过分割模型获取物体掩码并均匀采样顶点。  
    - **视觉动作顶点**：将具身本体抽象为关键交互点（如人手指尖），避免模态特异性，增强跨具身迁移能力。  
  - 边构建：基于空间距离阈值连接相邻顶点对，形成图结构 \(G_t = (V_t, E_t)\)，其中顶点集包含物体和动作顶点。  

- **属性感知的图生成建模 (Property-aware Graph Generative Modeling)**  
  - **物体属性估计**：利用历史图序列提取物体中心图（仅含该物体顶点和边），通过 GNN 池化得到物体图特征，再输入 LSTM 建模长期依赖，隐式推断如刚度等物理属性，得到属性特征 \(\phi_t^\Omega\)。  
  - **层级化图建模**：  
    - 对动作和物体顶点集分别用 K-means 聚类，每簇添加一个全局顶点（根），位置为簇内顶点均值。  
    - 构建三种边：叶子到根 (\(E_{t}^{L2R}\))、根到叶子 (\(E_{t}^{R2L}\))、根到根全连接 (\(E_{t}^{R2R}\))，与原始边一起形成层级图 \(G_t^h\)。  
    - 顶点嵌入融合历史位置、类别和估计属性，经 GNN 得到图特征。  
  - **图生成**：将图特征、图像嵌入（ResNet）和语言指令嵌入（BERT）送入 Transformer 生成器，输出未来 \(F_G\) 步的顶点位置，根据距离阈值重建未来图序列 \(\hat{G}_{t:t+F_G}\)。训练使用预测顶点位置与真值的 MSE 损失。  

- **图引导的策略学习 (Graph Guided Policy)**  
  - 策略网络接收生成的未来图、当前观测和机器人本体感知。  
  - 状态编码器用 Transformer 融合多模态 token 得到 CLS token；动作头将 CLS token 与图 token 拼接，通过 MLP 预测未来 \(F_a\) 步动作。  
  - 策略训练使用少量标注动作数据的 MSE 损失。  

### 实验设计  
- **数据集 / 场景**  
  - **仿真**：LIBERO 基准（130 个语言引导操控任务），细分为 LIBERO-Spatial、Object、Goal、Long、LIBERO-90 等五个套件。  
  - **真实世界**：12 项日常操作任务（如开抽屉、堆积木、折布、倒水等），每任务收集 50 个无动作视频和 10 个动作标注轨迹。  
- **对比基线**  
  - BC（纯行为克隆，不含图条件）  
  - R3M（预训练视觉表示，Ego4D 权重微调后初始化策略视觉编码器）  
  - UniPi（文本条件视频扩散生成 + 反向动力学）  
  - ATM（轨迹跟踪生成 + 轨迹引导策略）  
  - 同样比较了仅用 20% 标注数据的 BC 完整训练集。  
- **跨具身迁移实验**  
  - 机器人到机器人：Franka 臂视频预训练 + UR 臂标注动作（仿真）  
  - 人类到机器人：真实人类视频 + Franka 臂标注动作  

### 资源与算力  
- 文中未明确说明所使用的 GPU 型号、数量、训练时长等具体算力信息。  
- 仅提及使用预训练模型（如 Ego4D、ResNet、BERT）进行特征编码，但未给出训练 GraphMimic 模型的硬件开销。  

### 实验数量与充分性  
- **总体规模**：超过 140 项任务（仿真 130 项 + 真实 12 项），覆盖多类操控场景。  
- **对比实验**：在 5 个仿真套件和 12 个真实任务上，与 4 种主流基线相比，均采用相同数据量和训练配置。  
- **消融研究**：  
  - 状态表示（网格顶点 vs. 点云 vs. 相关顶点图）  
  - 视觉动作表示（无动作、末端执行器、交互点）  
  - 物体表示（仅被操纵物、全部物体、任务相关物体）  
  - 层级建模（局部连接、全局连接、层级架构）  
  - 物体属性估计（无估计、无 LSTM、图+LSTM）  
  - 分析涵盖机器人-机器人迁移与真实世界场景，确保结论可靠。  
- **公平性**：所有方法在相同数据量、相同随机种子下评估，成功率为人工评估或多次运行平均，对比客观。  

### 主要结论与发现  
- 仅使用 20% 的动作标注数据（如每任务 2 条轨迹），GraphMimic 在仿真和真实世界均显著优于使用五倍标注数据的 ATM 和 UniPi。  
- 在相同 10 条标注轨迹下，相比 ATM，仿真任务平均成功率提升超过 17%，真实世界提升超过 23%。  
- 跨具身迁移（机器人到机器人、人类到机器人）中，性能提升超过 33%，表明图表示具备良好的模态无关性。  
- 消融实验证实：基于任务相关物体和交互点的图结构、层级化消息传递、以及属性估计模块对性能提升至关重要。  

### 优点  
- **创新表示**：将视频帧抽象为物体-动作图，显式编码空间关系与物理交互，有效提取任务相关结构信息。  
- **高效预训练**：图到图生成模型直接预训练，无需构建奖励函数或复杂仿真环境，易于扩展。  
- **强样本效率**：大幅降低对昂贵动作标注的依赖，仅需少量演示即可获得高性能。  
- **跨具身泛化**：交互点抽象使知识能够在不同形态的机器人或人之间迁移，扩宽数据来源。  

### 不足与局限  
- **跟踪质量依赖**：现有 SOTA 点跟踪模型在低纹理或大运动物体上易失效，影响训练图序列的精度，可能制约最终性能。  
- **算力透明度**：未提供训练所需 GPU 资源、时间等信息，难以评估实际部署成本。  
- **图构建手工性**：物体顶点选择依赖 VLMs 和分割模型，动作顶点需预定义关键点（如指尖），对非手指类末端可能需重新设计。  
- **真实任务范围有限**：真实实验仅涵盖 12 个桌面操作任务，尚未在更多样化、长周期、接触密集型任务上验证。  

（完）
