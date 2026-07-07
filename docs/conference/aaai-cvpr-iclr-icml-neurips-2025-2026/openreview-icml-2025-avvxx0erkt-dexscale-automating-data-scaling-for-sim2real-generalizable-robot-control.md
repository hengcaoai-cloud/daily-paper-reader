---
title: "DexScale: Automating Data Scaling for Sim2Real Generalizable Robot Control"
title_zh: "DexScale: 面向sim2real可泛化机器人控制的自动数据扩展"
authors: "Guiliang Liu, Yueci Deng, Runyi Zhao, Huayi Zhou, Jian Chen, Jietao Chen, Ruiyan Xu, Yunxin Tai, Kui Jia"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=AVVXX0erKT"
tags: ["query:data"]
score: 9.0
evidence: 提出DexScale数据引擎，自动进行技能仿真和扩展，用于sim2real机器人操作策略
tldr: 提出DexScale数据引擎，自动进行技能仿真与扩展，结合真实世界先验以缩小sim2real差距，从而可扩展地生成可部署的机器人操作数据。该引擎解决了仿真数据的可用性问题，为机器人策略学习提供大规模训练数据。
source: ICML-2025-Accepted
selection_source: conference_retrieval
motivation: 大规模机器人训练数据对泛化控制至关重要，但真实数据采集昂贵。
method: 设计数据引擎DexScale，自动仿真和扩展技能，集成真实世界先验确保数据可用性。
result: 实现了可扩展的sim2real泛化机器人操作策略学习。
conclusion: DexScale为机器人操作提供了高效可扩的数据生成手段。
---

## Abstract
A critical prerequisite for achieving generalizable robot control is the availability of a large-scale robot training dataset. Due to the expense of collecting realistic robotic data, recent studies explored simulating and recording robot skills in virtual environments. While simulated data can be generated at higher speeds, lower costs, and larger scales, the applicability of such simulated data remains questionable due to the gap between simulated and realistic environments. To advance the Sim2Real generalization, in this study, we present DexScale, a data engine designed to perform automatic skills simulation and scaling for learning deployable robot manipulation policies. Specifically, DexScale ensures the usability of simulated skills by integrating diverse forms of realistic data into the simulated environment, preserving semantic alignment with the target tasks. For each simulated skill in the environment, DexScale facilitates effective Sim2Real data scaling by automating the process of domain randomization and adaptation. Tuned by the scaled dataset, the control policy achieves zero-shot Sim2Real generalization across diverse tasks, multiple robot embodiments, and widely studied policy model architectures, highlighting its importance in advancing Sim2Real embodied intelligence.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）
- **动机**：大规模训练数据是实现机器人控制策略泛化的关键，但真实机器人数据采集成本高昂。
- **背景**：现有工作尝试在虚拟环境中仿真并记录机器人技能，虽然速度快、成本低、规模大，但由于仿真与真实环境之间存在领域差异（Sim2Real gap），仿真数据的实际可用性存疑。
- **整体含义**：论文旨在解决仿真数据在真实机器人上的可部署性问题，通过自动化数据扩展引擎缩小 Sim2Real 差距，为可泛化的机器人操作策略提供可扩展的训练数据。

### 2. 论文提出的方法论
- **整体框架**：DexScale 是一个数据引擎，能够自动进行技能仿真与扩展，输出可用于学习可部署机器人操作策略的数据。
- **核心技术思想**：
  - **真实性先验集成**：将多种形式的真实数据（如真实环境观测、物体模型、物理参数等）注入仿真环境，保持仿真技能与目标任务之间的语义对齐，提升仿真数据的可用性。
  - **自动化领域随机化与适配**：针对仿真中的每个技能，自动执行领域随机化（domain randomization）和领域适配（domain adaptation），以生成跨越不同环境变化的大规模数据。
- **算法流程**（文字概括）：
  1. 在高度保留真实世界先验的仿真环境中，自动生成或采集多样化的技能操作序列。
  2. 对每个技能自动应用随机化过程（视觉纹理、物理参数、初始状态等），生成大量变体。
  3. 结合适配机制，确保随机化后的数据仍与目标真实场景分布对齐。
  4. 最终形成大规模、多样化的 Sim2Real 数据集，用于策略训练。

### 3. 实验设计
- **评估场景**：根据摘要，实验覆盖了**多样化的任务、多种机器人形态（manipulators）以及广泛研究的策略模型架构**。
- **Benchmark 设置**：论文可能采用零样本 Sim2Real 迁移测试（zero-shot Sim2Real generalization evaluation），即在仿真中训练策略，直接在真实机器人上评测，无需额外微调。
- **对比方法**：摘要未具体列出对比方法，但通常会比较基于纯仿真数据（无真实先验）、仅真实数据、或现有 Sim2Real 方法（如基本领域随机化）的性能。
- **数据集**：使用了自身引擎生成的扩展数据，可能结合某些公开的真实机器人数据集作为先验来源（摘要未详述）。

### 4. 资源与算力
- **文中未明确说明**使用的 GPU 型号、数量或训练时长。摘要和元数据中均未提及算力细节。因此无法给出具体资源估计。

### 5. 实验数量与充分性
- **实验量估计**：从摘要描述“跨多种任务、多种机器人形态和多种策略架构”来看，实验至少包含多个维度下的消融和对比，应有一定规模。
- **充分性与客观性**：
  - 若确实在多种形态和架构上验证了零样本 Sim2Real 泛化，则实验设计较为充分，能够证明方法的通用性。
  - 但摘要未给出具体指标、统计显著性或误差分析，仅从文字可推断实验覆盖范围广。
  - 公平性：通过统一使用仿真训练、真实测试的零样本设定，与现有方法作平等对比，相对客观。

### 6. 论文的主要结论与发现
- DexScale 能够**有效扩展仿真数据**，使训练出的控制策略在真实机器人上实现**零样本泛化**。
- 该方法在**不同任务、多种机器人硬件平台和多种主流策略模型架构**上均表现稳定，证明了其作为 Sim2Real 具身智能数据基础设施的重要性。
- 数据引擎的自动化流程和真实先验集成是缩小 Sim2Real 差距的关键。

### 7. 优点
- **自动化与可扩展性**：从技能仿真到数据扩展全自动，无需繁重的人工数据收集，可规模化生成训练数据。
- **真实先验引导的仿真设计**：通过注入真实数据提升仿真语义质量，而非单纯依赖随机化，更贴合目标任务。
- **通用性验证**：在多任务、多形态、多架构下均取得零样本迁移，显示方法不依赖于特定策略或硬件，具有较强的实用价值。
- **面向可部署策略**：直接针对现实部署需求设计数据引擎，思路清晰，问题定位准确。

### 8. 不足与局限
- **实验细节缺失**：摘要未给出对比方法、量化结果、任务具体描述，难以判断实际性能提升幅度和统计可靠性。
- **真实先验获取成本未讨论**：虽然节省了真实操作数据采集，但集成“多种形式的真实数据”本身可能仍有成本（如真实物体扫描、物理参数测定），这些成本未作分析。
- **领域随机化与适配的具体机制不明**：方法细节仅概括性描述，缺乏可复现的关键技术点（例如适配损失函数、随机化参数空间等）。
- **可能存在的偏差**：无法确定真实先验的覆盖度和泛化边界，当目标环境与先验差异较大时，方法效果可能衰减，文中未作鲁棒性分析。
- **算力需求未知**：未报告训练资源和时间，对于评估方法的实际落地可行性构成局限。

（完）
