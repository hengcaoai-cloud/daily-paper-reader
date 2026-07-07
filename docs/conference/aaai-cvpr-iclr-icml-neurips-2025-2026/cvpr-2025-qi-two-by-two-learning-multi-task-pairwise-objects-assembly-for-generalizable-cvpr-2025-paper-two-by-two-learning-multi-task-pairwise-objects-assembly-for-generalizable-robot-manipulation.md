---
title: "Two by Two: Learning Multi-Task Pairwise Objects Assembly for Generalizable Robot Manipulation"
title_zh: 两两配对：学习多任务成对物体装配以实现可泛化的机器人操作
authors: "Qi, Yu, Ju, Yuanchen, Wei, Tianming, Chu, Chi, Wong, Lawson L.S., Xu, Huazhe"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Qi_Two_by_Two_Learning_Multi-Task_Pairwise_Objects_Assembly_for_Generalizable_CVPR_2025_paper.pdf"
tags: ["query:data"]
score: 8.0
evidence: 提出2BY2数据集，包含18种日常成对物体装配任务，1034个实例。
tldr: 针对现有装配数据集集中于几何碎片或工厂零件而忽略日常交互的问题，本文构建了2BY2——一个大规模成对物体装配数据集，涵盖插插座、插花、放面包等18种现实任务，包含1034实例及位姿和对称性标注。该数据集为通用机器人装配研究提供了关键基准。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-qi-two-by-two-learning-multi-task-pairwise-objects-assembly-for-generalizable-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1805, \"height\": 761, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-qi-two-by-two-learning-multi-task-pairwise-objects-assembly-for-generalizable-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 856, \"height\": 466, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-qi-two-by-two-learning-multi-task-pairwise-objects-assembly-for-generalizable-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 857, \"height\": 556, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-qi-two-by-two-learning-multi-task-pairwise-objects-assembly-for-generalizable-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1782, \"height\": 984, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-qi-two-by-two-learning-multi-task-pairwise-objects-assembly-for-generalizable-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 873, \"height\": 598, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-qi-two-by-two-learning-multi-task-pairwise-objects-assembly-for-generalizable-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1786, \"height\": 1220, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-qi-two-by-two-learning-multi-task-pairwise-objects-assembly-for-generalizable-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1806, \"height\": 345, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-qi-two-by-two-learning-multi-task-pairwise-objects-assembly-for-generalizable-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1799, \"height\": 202, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-qi-two-by-two-learning-multi-task-pairwise-objects-assembly-for-generalizable-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1808, \"height\": 897, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-qi-two-by-two-learning-multi-task-pairwise-objects-assembly-for-generalizable-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 731, \"height\": 161, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-qi-two-by-two-learning-multi-task-pairwise-objects-assembly-for-generalizable-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1810, \"height\": 267, \"label\": \"Table\"}]"
motivation: 日常物体装配任务复杂且现有数据集不足，阻碍通用机器人技能发展。
method: 构建2BY2数据集，收集并标注18类日常成对物体的装配实例。
result: 提供了包含1034个实例和位姿、对称性标注的大规模基准。
conclusion: 2BY2为研究日常场景中可泛化的机器人装配提供了重要数据基础。
---

## Abstract
3D assembly tasks, such as furniture assembly and component fitting, play a crucial role in daily life and represent essential capabilities for future home robots. Existing benchmarks and datasets predominantly focus on assembling geometric fragments or factory parts, which fall short in addressing the complexities of everyday object interactions and assemblies. To bridge this gap, we present 2BY2, a large-scale annotated dataset for daily pairwise objects assembly, covering 18 fine-grained tasks that reflect real-life scenarios, such as plugging into sockets, arranging flowers in vases, and inserting bread into toasters. 2BY2 dataset includes 1,034 instances and 517 pairwise objects with pose and symmetry annotations, requiring approaches that align geometric shapes while accounting for functional and spatial relationships between objects. Leveraging the 2BY2 dataset, we propose a two-step SE(3) pose estimation method with equivariant features for assembly constraints. Compared to previous shape assembly methods, our approach achieves state-of-the-art performance across all 18 tasks in the 2BY2 dataset. Additionally, robot experiments further validate the reliability and generalization ability of our method for complex 3D assembly tasks. More details and demonstrations can be found at https://tea-lab.github.io/TwoByTwo/.

---

## 论文详细总结（自动生成）

## 论文总结

### 1. 核心问题与研究动机
- 现有 3D 装配基准数据集（如 Breaking Bad、Neural Shape Mating 等）大多聚焦于**几何碎片或工厂零件的拼接**，无法充分反映日常生活中的物体配对装配场景（如花瓶插花、面包放入烤面包机、插头插入插座等）。
- 日常装配任务不仅要求几何形状的对齐，还需要考虑**功能性与空间关系**，这对机器人的 6D 姿态估计提出了更高要求。
- 论文的目标是**填补这一空白**，提供一个面向真实日常场景的大规模成对物体装配数据集，并设计一个能够高性能完成多任务装配的通用框架。

### 2. 方法论
- **2BY2 数据集构建**  
  - 从 3D Warehouse、PartNet-Mobility、Objaverse 等来源收集**517 对物体**，共 **1,034 个实例**，覆盖 18 个细粒度装配任务（如 Lid Covering、Inserting、High Precision Placing）。  
  - 所有物体被分为 **Object B（底座/接收件）** 和 **Object A（插入件/配合件）**，模仿人类“先放底座再安装”的顺序。  
  - 统一缩放并标定到 **世界规范坐标系**（物体稳定放置在 XY 平面，最低点对齐 Z=0）。  
  - 点云通过蓝噪采样生成（1024 个点），并对每类物体标注其固有对称性（绕 Z 轴旋转对称或沿 X 轴镜像对称）。

- **两步成对网络架构（Two‑Step Pairwise Network）**  
  - 分为 **Branch B** 和 **Branch A**。  
    - **Branch B** 先预测底座（Object B）的 SE(3) 姿态，将 PB 变换到规范姿态。  
    - **Branch A** 再接收变换后的 PB 和原始 PA，融合两者的几何特征后预测插入件（Object A）的姿态。  
  - 训练时，Branch A 使用 Ground‑Truth 姿态的 PB 进行独立训练；推理时则串联执行，以**避免联合预测带来的误差累积**。

- **特征提取模块**  
  - 使用 **双尺度 VN DGCNN**（Vector Neuron Dynamic Graph CNN）作为编码器，同时提取 **SE(3) 等变特征**和 **SO(3) 不变特征**。  
  - 双 KNN 尺度（不同 K 值）使网络同时捕获局部细节和全局形状信息。  
  - 平移等变性通过将点云减去重心实现（\(f(P+T)=f(P)+T\)）。

- **跨物体特征融合**  
  - Branch A 中将 Object B 的 SO(3) 不变特征 \(I_B\) 与 Object A 的 SE(3) 等变特征 \(E_A\) 逐元素相乘，使 A 的每个点同时感知 B 的几何信息，同时保留 A 的旋转等变性（\(f(R \cdot (I_B * E_A)) = R \cdot f(I_B * E_A)\)）。

- **姿态预测与损失函数**  
  - 两个分支均使用**独立的 MLP 头**分别预测平移向量 \(T \in \mathbb{R}^3\) 和旋转矩阵 \(R \in \mathbb{R}^{3\times3}\)。  
  - 损失函数：平移采用 L1 损失，旋转采用测地距离（Geodesic Distance）。

### 3. 实验设计与对比方法
- **数据集与基准**  
  - 在 2BY2 数据集的 **18 个细粒度任务** 上进行评估，并额外在三个跨类别任务（Lid Covering、Inserting、High Precision Placing）以及全部数据混合（All task）上测试泛化能力。  
  - 评价指标：考虑对称性后的**平移 RMSE** 和**旋转 RMSE**（用欧拉角计算）。

- **对比基线方法**  
  - SE‑3 Assembly（等变直接联合预测）  
  - PuzzleFusion++（扩散模型 + 验证的断裂组装）  
  - Jigsaw（层次几何特征匹配）  
  - Neural Shape Mating（PointNet + Transformer 联合预测）

- **真实机器人实验**  
  - 使用 UR5 机械臂 + Robotiq 2F‑85 夹爪，对 Cup、Flower、Bread、Plug 四个任务进行实验，每组任务 10 次不同初始姿态的装配尝试，对比 SE‑3 Assembly 基线。

### 4. 资源与算力
- 论文**未明确提及**训练所使用的 GPU 型号、数量及具体训练时长。  
- 仅给出了训练超参数：batch size = 4，Adam 优化器初始学习率 \(1\times10^{-4}\)，训练 1000 个 epoch 确保收敛。

### 5. 实验数量与充分性
- 总共设置了 **约 30 组以上的定量实验**：  
  - **18 个细粒度任务** + **3 个跨类别任务** + **1 个 All 任务**，每组均与 4 个基线方法对比。  
  - **消融实验**：针对编码器（双尺度 VN DGCNN vs. VN DGCNN、DGCNN、PointNet）和“两步 vs. 端到端”设计，在 Lid Covering、Inserting、Precision Placing 及 All 任务上进行对比。  
  - **定性结果**：展示了 7 个任务的姿态预测可视化对比。  
  - **真实机器人实验**：4 个任务 × 10 次重复 = 40 次实际操作。  
- 实验覆盖了微观模块验证和宏观泛化能力，对比基线包含基于等变、扩散、图匹配等多种范式，**比较全面、客观且公平**。

### 6. 主要结论与发现
- 2BY2 数据集为**每日成对物体装配**提供了首个大规模、细粒度、带对称性标注的基准，有效弥补了现有几何碎片数据集的不足。  
- 两步成对网络在所有 18 个任务上均达到 **state‑of‑the‑art**，相比最强基线平均降低平移 RMSE 0.046、旋转 RMSE 8.97°，在综合 All 任务上优势更明显（平移降低 0.123，旋转降低 10.90°）。  
- 真实机器人实验中，该方法成功率 **77.5%**（基线 22.5%），展示了强泛化能力。

### 7. 优点与亮点
- **贴近现实的装配场景**：涵盖了厨房、文具、玩具等 18 种日常任务，远超市面其他数据集。  
- **分步装配策略**：模仿人类“先底座后插件”的思路，有效减少姿态预测的相互干扰。  
- **双尺度等变编码**：利用 SE(3) 等变性提升样本效率和泛化性，双尺度 KNN 融合局部与全局几何信息。  
- **跨物体融合模块简单有效**：通过乘法融合，既保护各分支的等变/不变特性，又传递必要的空间关系。  
- **充分的可复现性支撑**：提供项目主页、开源代码（基于论文描述）以及机器人实际验证。

### 8. 不足与局限
- **对称性假设较简化**：仅考虑绕 Z 轴的旋转对称和沿 X 轴的镜像对称，未覆盖更复杂的连续对称或任意轴对称。  
- **真实机器人实验规模有限**：仅测试了 4 个任务，每种 10 次，任务多样性和统计置信度尚待加强。  
- **未涉及感官噪声**：实验输入为理想采样点云，未考虑真实传感器噪声、缺失或遮挡对姿态估计的影响。  
- **闭环装配验证缺失**：仅评估单次姿态估计误差，未衡量机器人执行过程中碰撞修正等闭环调整能力。  
- **训练细节不够透明**：未说明计算资源和训练时间，难以直接复现效率预期。

（完）
