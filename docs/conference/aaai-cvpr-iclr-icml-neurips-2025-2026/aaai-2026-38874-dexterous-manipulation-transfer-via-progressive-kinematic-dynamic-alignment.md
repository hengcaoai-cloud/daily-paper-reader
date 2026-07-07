---
title: Dexterous Manipulation Transfer via Progressive Kinematic-Dynamic Alignment
title_zh: 通过渐进式运动学-动力学对齐实现灵巧操作迁移
authors: "Wenbin Bai, Qiyu Chen, Xiangbo Lin, Jw L, Quancheng Li, Hejiang Pan, Yi Sun"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38874/42836"
tags: ["query:data"]
score: 10.0
evidence: 将人手操作视频转换为灵巧机器人轨迹，采用渐进式运动学-动力学对齐
tldr: 针对多指机器人操作数据稀缺问题，提出一种与手部无关的操作迁移系统，通过渐进式运动学-动力学对齐框架，高效地将人手演示视频转换为高质量灵巧操作轨迹，无需大量训练数据。实验验证了该方法能从少量人类视频中生成高质量轨迹，支持策略学习。该系统为解决灵巧操作数据稀缺提供了实用方案，促进了从人类演示到机器人技能的迁移。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38874/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 875, \"height\": 311, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38874/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1826, \"height\": 782, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38874/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 856, \"height\": 392, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38874/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 858, \"height\": 435, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38874/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 823, \"height\": 459, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38874/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 873, \"height\": 333, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38874/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 877, \"height\": 275, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38874/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 872, \"height\": 238, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38874/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 866, \"height\": 145, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38874/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 782, \"height\": 187, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38874/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 598, \"height\": 115, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38874/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 856, \"height\": 188, \"label\": \"Table\"}]"
motivation: 多指机器人硬件平台采集操作数据困难且可扩展性差，导致数据驱动的灵巧操作策略学习受限。
method: 设计了渐进式迁移框架：首先建立人手与灵巧手之间的运动学对应，然后优化动力学一致性，以生成协调的高自由度控制轨迹。
result: 实验验证该方法能从小量人类视频中生成高质量的灵巧操作轨迹，支持策略学习。
conclusion: 该系统为解决灵巧操作数据稀缺提供了实用方案，促进了从人类演示到机器人技能的迁移。
---

## Abstract
The inherent difficulty and limited scalability of collecting manipulation data using multi-fingered robot hand hardware platforms have resulted in severe data scarcity, impeding research on data-driven dexterous manipulation policy learning. To address this challenge, we present a hand-agnostic manipulation transfer system. It efficiently converts human hand manipulation sequences from demonstration videos into high-quality dexterous manipulation trajectories without requirements of massive training data. To tackle the multi-dimensional disparities between human hands and dexterous hands, as well as the challenges posed by high-degree-of-freedom coordinated control of dexterous hands, we design a progressive transfer framework: first, we establish primary control signals for dexterous hands based on kinematic matching; subsequently, we train residual policies with action space rescaling and thumb-guided initialization to dynamically optimize contact interactions under unified rewards; finally, we compute wrist control trajectories with the objective of preserving operational semantics. Using only human hand manipulation videos, our system automatically configures system parameters for different tasks, balancing kinematic matching and dynamic optimization across dexterous hands, object categories, and tasks. Extensive experimental results demonstrate that our framework can automatically generate smooth and semantically correct dexterous hand manipulation that faithfully reproduces human intentions, achieving high efficiency and strong generalizability with an average transfer success rate of 73%, providing an easily implementable and scalable method for collecting robot dexterous manipulation data. Refer to the arXiv version for the appendix.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义
- **核心问题**：多指灵巧机器人手硬件平台采集操作数据成本高、可扩展性差，造成严重的数据稀缺，阻碍了数据驱动的灵巧操作策略学习。
- **整体含义**：提出一种与手部构型无关（hand-agnostic）的操作迁移系统，仅需人类手部演示视频即可自动生成高质量的灵巧手操作轨迹，无需大规模训练数据，为灵巧操作数据的获取提供高效、可扩展的解决方案。

### 2. 方法论
论文提出 **渐进式运动学‑动力学对齐 (Progressive Kinematic‑Dynamic Alignment, PKDA)** 框架，包含四个模块：

- **交互感知器 (Interaction Perceptor)**：从原始人类演示视频中提取手部轨迹 H、物体轨迹 O、接触点 C 以及物体网格。对有已知物体模型的数据集（如 DexYCB）使用 HFL‑Net 估计手‑物姿态；对无模型视频则采用 HOLD 联合三维重建，并做凸分解以改善碰撞检测。
- **轨迹提议器 (Trajectory Proposer)**：通过非线性优化将人类指尖位置映射为灵巧手关节角序列，目标是最小化指尖位置误差，并辅以手掌朝向约束和时间平滑约束。从此获得主控制信号 A<sub>primary</sub>。
- **接触适应优化器 (ContactAdapt Optimizer)**：引入强化学习（RL）训练残差策略，动态优化接触交互。包含三项关键设计：
  - **RL‑配置器**：自动设置预抓取状态（选取拇指指尖最接近接触点且尚未碰撞的时刻）和目标状态（物体首次偏离初始位置 0.1m 时的姿态），实现跨任务统一配置。
  - **动作空间重缩放**：将手腕动作空间压缩到预抓取手腕位姿的邻域内，而保留手指关节完全运动范围，抑制无效探索。
  - **统一奖励函数**：分阶段设计接近奖励、抓取奖励（接触奖励+模仿奖励）和提升奖励，与任务无关。
- **手腕轨迹规划器 (Wrist Trajectory Planner)**：根据物体在操作阶段的位姿变化及稳定抓取时的手腕位姿，通过逆运算生成手腕轨迹，确保操作语义一致性。

整体流程：运动学匹配提供初级轨迹 → RL 优化手‑物接触动力学 → 物体轨迹引导生成手腕控制，实现完整的操作迁移。

### 3. 实验设计
- **测试场景**：
  - **全信息场景**：直接使用 GRAB 数据集提供的真值手‑物姿态，约 600 条单手柄操作轨迹。
  - **模型已知视觉场景**：从单目 RGB 视频估计手‑物姿态（假设物体 3D 模型已知），从 DexYCB 和 TACO 各选 10 个任务。
  - **模型未知视觉场景**：仅提供自摄 RGB 视频，包含 5 种日常物品操作任务。
- **对比基线**：
  - **Anyteleop**：纯运动学重定向。
  - **PGDM**：基于预抓取姿态和参考轨迹的 RL 方法。
  - **D‑Grasp**：基于单帧抓取姿态和特定奖励的动态抓取合成。
- **评价指标**：抓取成功率 (SR Grasp)、跟随成功率 (SR Follow)、物体平移误差 (Ep)、物体旋转误差 (Er)，以及意向级一致性指标：转移成功率 (TSR)。

### 4. 资源与算力
论文正文及提供的材料中**未明确提及所用 GPU 型号、数量、训练时长等算力相关细节**，无法给出具体计算资源估计。

### 5. 实验数量与充分性
- **主要实验组数**：
  - 比较实验（表1）：三个基线方法在 Adroit Hand 上的 40～600 条序列。
  - 鲁棒性实验（表2）：感知误差场景下的 2 种设置。
  - 跨灵巧手实验（表3）：Adroit、Allegro、Leap 三种手。
  - 消融实验（表4‑5）：重定向方法、预抓取策略（引导手指、触发距离）、动作空间重缩放。
  - 真实世界实验：UR10 臂 + Leap Hand 完成三个任务。
- **充分性与客观性**：实验覆盖多个数据集、不同感知条件、多种机器人手，消融设计严格，指标多维，对比公平，能较好支撑结论。

### 6. 主要结论与发现
- PKDA 仅从人类视频即可自动生成平滑、语义正确的灵巧操作轨迹，平均转移成功率达 **73%**。
- 相比纯运动学映射和 DRL 基线，PKDA 在成功率与学习效率上均表现更优，且无需任务特定参数调节。
- 对视觉感知误差具有鲁棒性，能够在模型已知和未知场景下保持 **70% 以上**的成功率。
- 拇指引导的预抓取和动作空间重缩放对 RL 探索效率至关重要，消融实验证实去除后成功率显著下降（从 77.5% 降至 37.5%）。

### 7. 优点
- **手部无关性**：能适应不同自由度和尺寸的灵巧手，只需指定手指对应关系，无需整体参数调整。
- **数据高效**：无需在线人类参与或大规模预训练，仅利用离线视频即可生成高质量迁移轨迹。
- **结构清晰的渐进式框架**：运动学提供探索导向，RL 在受限动作空间内优化动力学，兼顾效率与稳定性。
- **统一奖励与自动配置**：跨任务 RL 无需人工设计奖励，降低应用门槛。
- **完整的端到端迁移**：涵盖接近、抓取、操作全流程，而非只迁移部分动作片段。

### 8. 不足与局限
- **接触模式假设较强**：目前主要处理手‑物接触相对稳定的操作，对于接触点频繁变化的复杂灵巧操作尚无法有效应对（论文自身列为未来方向）。
- **仅验证开环执行**：真实世界实验采用开环控制，未涉及闭环反馈或扰动下的鲁棒性测试。
- **物体重建依赖**：在模型未知场景下依赖于物体三维重建及凸分解，重建缺陷可能影响效果，文中虽通过重心下移等方式缓解，但仍存在不确定性。
- **固定任务抽象**：将操作起始阶段统一抽象为“抓起”，可能不适用于特殊操作（如不抓取直接拨动）。
- **算力信息缺失**：未报告训练 RL 策略所需的 GPU 资源和时间，复现成本不透明。

（完）
