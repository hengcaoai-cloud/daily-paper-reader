---
title: "VidBot: Learning Generalizable 3D Actions from In-the-Wild 2D Human Videos for Zero-Shot Robotic Manipulation"
title_zh: VidBot：从野生2D人类视频学习可泛化的3D动作用于零样本机器人操作
authors: "Chen, Hanzhi, Sun, Boyang, Zhang, Anran, Pollefeys, Marc, Leutenegger, Stefan"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_VidBot_Learning_Generalizable_3D_Actions_from_In-the-Wild_2D_Human_Videos_CVPR_2025_paper.pdf"
tags: ["query:data"]
score: 10.0
evidence: 从野生人类视频提取3D手部轨迹，实现零样本机器人操作
tldr: VidBot提出一种从大规模互联网人类视频中提取3D手部轨迹的框架，用于零样本机器人操作学习。它结合深度估计和手部姿态重建，将人类视频转化为可供机器人执行的3D动作。实验表明，该方法在多种操作任务上实现了零样本泛化，无需真实机器人数据。这为利用互联网人类视频规模化地训练操作技能开辟了新路径。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-chen-vidbot-learning-generalizable-3d-actions-from-in-the-wild-2d-human-videos-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1798, \"height\": 655, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-chen-vidbot-learning-generalizable-3d-actions-from-in-the-wild-2d-human-videos-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 776, \"height\": 456, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-chen-vidbot-learning-generalizable-3d-actions-from-in-the-wild-2d-human-videos-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1802, \"height\": 595, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-chen-vidbot-learning-generalizable-3d-actions-from-in-the-wild-2d-human-videos-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 832, \"height\": 335, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-chen-vidbot-learning-generalizable-3d-actions-from-in-the-wild-2d-human-videos-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1705, \"height\": 671, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-chen-vidbot-learning-generalizable-3d-actions-from-in-the-wild-2d-human-videos-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 827, \"height\": 442, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-chen-vidbot-learning-generalizable-3d-actions-from-in-the-wild-2d-human-videos-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1782, \"height\": 283, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-chen-vidbot-learning-generalizable-3d-actions-from-in-the-wild-2d-human-videos-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 860, \"height\": 252, \"label\": \"Table\"}]"
motivation: 物理机器人学习无法规模化，互联网人类视频提供了丰富的数据源但存在具身鸿沟。
method: 通过从单目RGB人类视频中提取3D手部轨迹，构建3D可供性，并学习零样本操作策略。
result: 在多个操作任务上，VidBot实现了零样本泛化，成功率显著。
conclusion: VidBot展示了利用野生人类视频进行通用机器人操作学习的潜力。
---

## Abstract
Future robots are envisioned as versatile systems capable of performing a variety of household tasks. The big question remains, how can we bridge the embodiment gap while minimizing physical robot learning, which fundamentally does not scale well. We argue that learning from in-the-wild human videos offers a promising solution for robotic manipulation tasks, as vast amounts of relevant data already exist on the internet. In this work, we present VidBot, a framework enabling zero-shot robotic manipulation using learned 3D affordance from in-the-wild monocular RGB-only human videos. VidBot leverages a pipeline to extract explicit representations from them, namely 3D hand trajectories from videos, combining a depth foundation model with structure-from-motion techniques to reconstruct temporally consistent, metric-scale 3D affordance representations agnostic to embodiments. We introduce a coarse-to-fine affordance learning model that first identifies coarse actions from the pixel space and then generates fine-grained interaction trajectories with a diffusion model, conditioned on coarse actions and guided by test-time constraints for context-aware interaction planning, enabling substantial generalization to novel scenes and embodiments. Extensive experiments demonstrate the efficacy of VidBot, which significantly outperforms counterparts across 13 manipulation tasks in zero-shot settings and can be seamlessly deployed across robot systems in real-world environments. VidBot paves the way for leveraging everyday human videos to make robot learning more scalable.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义
- **核心问题**：如何弥合机器人操作中人类视频（2D）与真实机器人执行（3D）之间的“具身鸿沟”，使机器人能够从互联网上大量易得的野生人类视频中直接习得可泛化的操作技能，而无需针对每种新环境和新型机器人反复收集昂贵的遥操作演示数据。
- **研究动机**：传统机器人技能学习依赖大量专家遥操作演示，成本高、难以规模化。互联网上已有海量人类日常活动视频，若能从中提取与环境、视角无关的 3D 动作表示（即 3D 可供性），则可大幅降低机器人学习门槛，实现零样本泛化。
- **整体含义**：VidBot 框架旨在将野生 2D 人类视频转化为 3D 动作知识，使机器人能够“看视频学操作”，并在全新的场景和机器人形态上零样本执行日常任务，从而推动机器人学习走向规模化。

### 2. 方法论
- **核心思想**：从单目 RGB 视频中提取具有时空一致性的度量级 3D 手部轨迹，将其作为与具身无关的 3D 可供性表示，随后通过由粗到细的可供性学习模型，在测试时结合场景约束生成可泛化的交互轨迹。
- **3D 可供性提取管道**：
    - 对视频使用 SfM（Structure-from-Motion）估计相机内参、无尺度位姿及稀疏地标。
    - 利用度量深度基础模型预测逐帧稠密深度。
    - 引入梯度优化方法联合优化全局尺度和相机位姿，使深度与 SfM 结果对齐，得到时域一致的度量级重建。
    - 从对齐后的 3D 数据中提取手部中心点轨迹，下采样得到接触点（contact points）和目标点（goal points），作为训练监督信号。
- **由粗到细的可供性学习模型**：
    - **粗阶段**：输入 RGB-D 图像和语言指令，预测目标点热图及其深度、接触点热图，通过 RoI 池化、视觉编码器及 Perceiver 模块融合全局与局部信息，得到 3D 目标点和接触点。
    - **细阶段**：以扩散模型为基础，条件于接触点、目标点、TSDF 体素特征和语言特征，生成完整的 3D 交互轨迹；使用 1D U-Net 直接预测去噪后的轨迹。
- **测试时代价引导**：在去噪过程中引入可微分代价函数，包括多目标点到达、场景碰撞避免和接触法向一致性，通过梯度扰动轨迹样本，使其适应新场景和新形态，并利用最终代价选择最优交互计划。
- **训练损失**：粗阶段使用二元交叉熵、目标点深度回归和辅助向量场损失；细阶段使用扩散模型的标准 L2 重建损失。

### 3. 实验设计
- **数据集**：训练数据来源于 EpicKitchens-100 等野生人类视频。测试环境使用 IsaacGym 模拟器，选取 FrankaKitchen、PartManip、ManiSkill 三个基准中的 13 项日常任务（开/关柜门、拉/推抽屉、抓取物体等）。
- **评估协议**：每个任务在三种不同视角下各生成 5 条轨迹（共15次试验），以成功率（对象自由度超过阈值且无碰撞）作为指标。
- **对比方法**：
    - 基于模拟器交互训练的 GAPartNet、Where2Act；
    - 预训练于大规模遥操作数据并微调的 Octo；
    - 同样使用人类视频但输出 2D 可供性的 VRB（经 3D 提升）；
    - 使用光流但依赖真值深度的 GFlow。
- **真实机器人实验**：在 Hello Robot Stretch 3 和 Boston Dynamics Spot 两个平台上测试了推抽屉、开柜门、取纸巾等任务，共进行 55 次试验。
- **下游应用**：视觉目标到达和探索任务，验证所提可供性作为先验的泛化能力。

### 4. 资源与算力
- 论文**未明确提及**训练所用的 GPU 型号、数量及具体训练时长，无法给出确切算力信息。

### 5. 实验数量与充分性
- **实验组成**：
    - 主实验：13 个任务 × 5 种方法（约195组测试）；
    - 消融实验：6 个任务 × 5 个变体（V1-V5）；
    - 真实机器人实验：55 次试验；
    - 下游任务实验：视觉目标到达和探索各一组。
- **充分性与公平性**：实验覆盖了多种操作原语、物体类别和视角变化；对比方法包含了模拟器学习、遥操作预训练、人类视频学习等不同范式；消融实验系统评估了粗阶段预测与各代价指引项的作用；基准中统一了接触配置的推断方式以公平比较轨迹质量。总体设计较为全面、客观。

### 6. 主要结论与发现
- VidBot 在零样本设定下，13 项任务的平均成功率达 **88.2%** ，比次优方法（Octo）高出约 **19%**。
- 粗阶段预测（目标/接触点）对性能至关重要，移除后成功率大幅下降（85.6% → 57.8%）。
- 测试时多目标点指引对性能提升最显著（+12.3%），碰撞避免指引在抓取任务中效果突出（+26.7%）。
- 真实机器人实验成功率达 **80.0%**，验证了方法的具身无关性和零样本迁移能力。
- 在下游视觉目标到达和探索任务中，VidBot 收敛更快、最终性能更优，展现了作为强先验的通用性。

### 7. 优点
- **规模化潜力**：利用互联网已有视频，无需遥操作标注，极大降低数据获取成本。
- **3D 可供性表示**：提取的度量级、时域一致的 3D 轨迹具有具身无关性，易于迁移。
- **由粗到细+代价引导**：分层设计结合可微分代价函数，在保持动作多样性的同时自适应新场景约束。
- **全面验证**：涵盖多种仿真任务、真实机器人、下游应用，多角度证实方法的有效性。
- **开源友好**：仅依赖 RGB 视频和开源基础模型，不要求特殊硬件（如动捕、深度传感器）。

### 8. 不足与局限
- **数据质量依赖基础模型**：3D 轨迹提取受限于深度基础模型和 SfM 的精度，可能产生噪声标签。
- **任务范围有限**：当前主要处理刚体操作（推、拉、抓），尚未展示轮式拧瓶盖等精细灵巧操作。
- **未报告计算开销**：缺乏训练时长、GPU 资源等量化信息，难以评估实际部署成本。
- **真实实验规模较小**：仅两个平台、三个环境、55 次试验，环境多样性有限。
- **动态与遮挡处理**：管道对快速手部运动或严重遮挡的鲁棒性未深入讨论。

（完）
