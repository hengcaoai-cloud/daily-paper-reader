---
title: Mitigating the Human-Robot Domain Discrepancy in Visual Pre-training for Robotic Manipulation
title_zh: 减轻机器人操作视觉预训练中的人机域差异
authors: "Zhou, Jiaming, Ma, Teli, Lin, Kun-Yu, Wang, Zifan, Qiu, Ronghe, Liang, Junwei"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Zhou_Mitigating_the_Human-Robot_Domain_Discrepancy_in_Visual_Pre-training_for_Robotic_CVPR_2025_paper.pdf"
tags: ["query:data"]
score: 9.0
evidence: 使用配对的人机视频数据减轻视觉预训练中的人机域差异，用于机器人操作
tldr: 针对人类活动数据预训练中存在的人机形态差异导致的域差异问题，提出一种利用配对的人机视频数据来桥接域差距的适应范式，从而提升下游机器人操作的视觉表征泛化能力。实验表明，该方法显著提高了基于人类数据预训练的模型在多种机器人操作任务上的性能。该范式使得大规模人类活动数据能够有效服务于机器人视觉预训练，缓解了数据稀缺问题。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhou-mitigating-the-human-robot-domain-discrepancy-in-visual-pre-training-for-robotic-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1723, \"height\": 712, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhou-mitigating-the-human-robot-domain-discrepancy-in-visual-pre-training-for-robotic-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1620, \"height\": 540, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhou-mitigating-the-human-robot-domain-discrepancy-in-visual-pre-training-for-robotic-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1799, \"height\": 626, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhou-mitigating-the-human-robot-domain-discrepancy-in-visual-pre-training-for-robotic-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 780, \"height\": 426, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhou-mitigating-the-human-robot-domain-discrepancy-in-visual-pre-training-for-robotic-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 689, \"height\": 263, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhou-mitigating-the-human-robot-domain-discrepancy-in-visual-pre-training-for-robotic-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1809, \"height\": 553, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhou-mitigating-the-human-robot-domain-discrepancy-in-visual-pre-training-for-robotic-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 860, \"height\": 224, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhou-mitigating-the-human-robot-domain-discrepancy-in-visual-pre-training-for-robotic-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 859, \"height\": 245, \"label\": \"Table\"}]"
motivation: 利用大规模人类数据预训练视觉表征时，显著的人机形态差异导致了域差异，阻碍模型泛化到机器人操作任务。
method: 设计了一种人机对比学习策略，利用容易获得的配对数据对齐人类和机器人视频的视觉表征。
result: 实验表明，该方法显著提高了基于人类数据预训练的模型在多种机器人操作任务上的性能。
conclusion: 该范式使得大规模人类活动数据能够有效服务于机器人视觉预训练，缓解了数据稀缺问题。
---

## Abstract
Learning generalizable visual representations across different embodied environments is essential for effective robotic manipulation in real-world scenarios. However, the limited scale and diversity of robot demonstration data pose a significant challenge. Recent research has explored leveraging large-scale human activity data for pre-training, but the substantial morphological differences between humans and robots introduce a significant human-robot domain discrepancy, hindering the generalization of these models to downstream manipulation tasks. To overcome this, we propose a novel adaptation paradigm that leverages readily available paired human-robot video data to bridge the domain gap. Our method employs a human-robot contrastive alignment loss to align the semantics of human and robot videos, adapting pre-trained models to the robot domain in a parameter-efficient manner. Experiments on 20 simulated tasks across two different benchmarks and five real-world tasks demonstrate significant improvements. These results span both single-task and language-conditioned multi-task settings, evaluated using two different pre-trained models. Compared to existing pre-trained models, our adaptation method improves the average success rate by over 7% across multiple tasks on both simulated benchmarks and real-world evaluations.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义
- **研究动机**：机器人操作任务通常依赖视觉表征学习，但机器人示教数据规模有限、多样性不足。现有工作尝试利用大规模人类活动视频（如 Ego4D、Kinetics）进行预训练，再将模型迁移到下游机器人任务。然而，人类与机器人在外观、结构、运动学上存在巨大**形态差异**，导致**人-机域差异**（domain discrepancy），使得预训练模型在机器人数据上的泛化性能大打折扣。
- **整体含义**：提出一种**新的适应范式**，不直接冻结或逐个环境微调人类数据预训练模型，而是利用少量**配对的人-机演示视频**作为桥梁，对齐两个域的表征，从而缓解域差异，同时保持模型对多种下游环境的通用性。

### 2. 论文提出的方法论
- **核心思想**：利用语义对齐的配对数据（同一任务的人类视频与机器人遥操作视频），约束「经过适配的机器人视频特征」与「冻结的人类视频特征」在语义空间上保持一致，以此将预训练模型高效地适应到机器人域。
- **关键组件**：
  - **双流设计**：人类视频通过**冻结**的预训练模型 `F` 提取特征 `hf`；机器人视频除冻结分支 `rf` 外，还经过**插入可学习适配器**的模型 `T` 得到 `rt`。
  - **参数高效适配器**：在 `F` 的特定层后插入轻量级 Adapter 模块（下投影 → 激活 → 上投影 + 残差连接），只训练适配器和少量对齐层。
  - **任务感知特征增强**：用任务描述文本经 BERT 编码后作为 Query，通过注意力机制聚合视频特征，得到任务感知的全局表征 `¯hf`, `¯rf`, `¯rt`。
  - **人-机对比对齐损失**：定义如下的对比损失（式6），让同一对的 `¯hf` 与 `¯rt` 靠近，同时推开非配对样本以及未适配的 `¯rf`，从而显式对齐语义：
    \[
    \mathcal{L} = \frac{1}{2M}\sum_{i=1}^M -\log \frac{S(\bar{h}_{f}^i,\bar{r}_{t}^i)}{S(\bar{h}_{f}^i,\bar{r}_{t}^i)+S(\bar{h}_{f}^i,\bar{r}_{f}^i)+\sum_{j\neq i}S(\bar{h}_{f}^i,\bar{r}_{t}^j)} + \text{symmetric term}
    \]
    其中 `S(x,y)=exp(x^T y/τ)`。

### 3. 实验设计
- **预训练模型**：在两个被广泛使用的用人类数据预训练的模型上进行适配：
  - **R3M**（在 Ego4D 上用视觉-语言对比学习预训练）
  - **D4R**（来自 data4robotics，在 Kinetics 上用 MoCo 预训练）
- **配对适应数据**：从 **RH20T** 数据集中抽取约 **5.6 万**对人-机视频用于适配训练。
- **下游任务 Benchmark**：
  - **模拟单任务**：**Adroit** 环境中的 `pen` 与 `relocate` 两个灵巧操作任务。
  - **模拟多任务**：**RLBench** 中的 18 个语言条件任务（如 `put in drawer`, `stack cups` 等），使用单头自注意力结合语言与视觉特征的行为克隆策略，共 1800 条示教。
  - **真实世界任务**：使用 xArm7 机械臂在 5 个任务（如 `put fruit in plate`, `stack cups` 等）上评估，每个任务 40 个示教，测试 20 轮。
- **对比方法**：
  - 未适配的原始预训练模型（`R3M`, `D4R`）。
  - 全参数微调基线：`R3M-PreT`（继续用原始代理任务微调）和 `R3M-ClS`（微调为动作分类），用于验证适配策略的有效性和效率。
  - 消融实验：适配器插入位置（靠前 `E`、中间 `M`、靠后 `L`、全部 `E.M.L`）的影响。

### 4. 资源与算力
- **硬件**：适配过程使用 **4 块 NVIDIA A6000 GPU**。
- **时长**：训练约 **8k 步**，相比原有的大规模人类数据预训练，增加的适配成本很小。

### 5. 实验数量与充分性
- **实验组次**：
  - 2 个模拟基准（共 20 个任务）+ 1 个真实世界基准（5 个任务），覆盖单任务和多任务设定。
  - 2 种预训练模型，每种均有适配前后对比。
  - 消融实验：适配器位置（4 种配置）、对比全参数微调基线（2 种）、t-SNE 特征可视化分析。
- **充分性与公平性**：实验设计较为全面，涵盖了主流的机器人操作平台（Adroit, RLBench, 真实机械臂）。对比对象包含了当时常用的人类数据预训练模型，且对不同适配策略进行了公平对比（保持相同下游策略，只改变视觉骨干）。消融实验也分析了核心部件（适配器位置、任务感知特征、对齐损失）的贡献，但未提供关于适配数据量、任务描述文本质量等的敏感性分析。

### 6. 论文的主要结论与发现
- 论文提出的 **HR-Align 适应范式**能够显著缓解预训练中的人-机域差异，在两个预训练模型、多种任务设置下均带来了 **平均成功率超过 7% 的提升**。
- **参数高效**：仅需调整骨干网络参数的 **6.4%** 左右即可取得超越全参数微调基线的效果，且避免了为每个下游环境单独定制模型，保持了通用性。
- 适配后的表征在特征空间上更加**紧凑、类内聚集**，有利于下游策略学习。

### 7. 优点
- **新范式切实有效**：首次提出利用少量配对数据作为桥梁进行人-机域对齐，既不丢弃人类预训练知识，又能显式适应机器人域，思路清晰。
- **方法简洁通用**：HR-Align 的适配器插入方式和对比损失易于实现，可应用于不同的预训练模型（如 R3M 和 D4R）。
- **验证扎实**：在模拟与真实、单任务与多任务、不同预训练骨干等多种条件下均获得稳定提升，消融实验证明了设计合理性。

### 8. 不足与局限
- **缺少域差异的定量度量**：论文未提供衡量人-机域差异大小的具体指标，无法定量指导适配过程或判断何时适配足够。
- **适配数据依赖性**：方法依赖显式的配对数据（RH20T），虽然此类数据在社区中增多，但对全新场景可能需要额外采集，且文中未讨论配对数据规模、质量或领域偏移对结果的影响。
- **适配与预训练脱节**：将人类数据预训练和适配完全分离，未探索将配对数据融入预训练阶段的可能性，这可能限制最终表征的能力上限。
- **真实世界任务简单且规模小**：仅评估5个相对简短的拾放操作，缺乏长序列、接触丰富或更灵巧的任务，且每个任务仅40个示教，结果的泛化性和鲁棒性有待更大规模验证。
- **下游策略依赖性**：适配效果仍受下游策略学习框架的影响，未对不同策略学习器鲁棒性进行讨论。

（完）
