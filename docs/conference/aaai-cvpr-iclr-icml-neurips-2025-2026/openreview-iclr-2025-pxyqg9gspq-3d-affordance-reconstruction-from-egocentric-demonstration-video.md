---
title: 3D Affordance Reconstruction from Egocentric Demonstration Video
title_zh: 从自我中心演示视频的3D可供性重建
authors: "Egil Diau, Yueh-Feng Ku, Chi Ming Chung, Ting-Jun Wang, Min Sun, Winston H. Hsu"
date: 2024-09-26
pdf: "https://openreview.net/pdf?id=pxYqG9GSpQ"
tags: ["query:data"]
score: 8.0
evidence: 从第一人称演示视频重建3D可供性
tldr: 提出一种免训练方法，从第一人称演示视频中重建3D可供性，利用DUST3R基础模型克服2D可供性缺乏空间信息的局限。该方法无需COLMAP，直接分析视频帧，生成含深度与几何的3D可供性，为机器人操作学习提供手物交互的空间表征。实验展示其在机器人操作任务中引导抓取与交互的有效性，推动人类视频向机器人可操作知识的转化。
source: ICLR-2025-Public
selection_source: conference_retrieval
motivation: 现有2D可供性方法忽视空间信息，难以用于精确的机器人操作。
method: 免训练的框架，使用DUST3R从稀疏帧进行3D重建，并分析视频生成3D可供性。
result: 在多个操作场景中，3D可供性有效指导了抓取和交互规划。
conclusion: 3D可供性重建为机器人从人类视频中学习操作技能提供了关键的空间表征。
---

## Abstract
Developing robots capable of generalized skills remains an exceedingly challenging task. Drawing from psychology, the concept of affordance has emerged as a promising intermediate representation to guide robot manipulation. However, prior work has primarily focused on 2D affordances from video, neglecting critical spatial information such as camera positioning, absolute position, depth and geometry. In this paper, we present a novel training-free method that constructs 3D affordances from egocentric demonstration videos. To address the challenge of insufficient static, high-quality frames for 3D reconstruction in egocentric videos, we employ the 3D foundational model DUST3R, which reconstructs scenes from sparse images without requiring COLMAP. We analyze videos using hand detection to identify contact times and 2D contact points, reconstruct these interactions using DUST3R, and project the 2D contact points into 3D space using gaussian heatmaps. Finally, we derive hand trajectories through 3D hand pose estimation and process them using linear regression to integrate the spatiotemporal dynamics of human-object interactions. We demonstrate the effectiveness of our method on the ego4d-exo dataset for seven real-world hand-object manipulation tasks in cooking scenes.

---

## 论文详细总结（自动生成）

# 论文总结：从自我中心演示视频的3D可供性重建

## 1. 论文的核心问题与整体含义
- **研究动机**：现有可供性（affordance）研究多停留在2D图像层面，缺少相机位姿、绝对位置、深度及几何形状等关键空间信息，难以直接用于精准的机器人操作。
- **核心问题**：如何从第一人称（自我中心）演示视频中，在不依赖额外训练的情况下，重建出**包含空间深度和几何信息的3D可供性**，从而为机器人学习可迁移的操作技能提供一种中间表征。
- **整体含义**：通过将人类视频转化为富含空间关系的3D可供性，桥接了人类演示与机器人可执行知识之间的鸿沟，为机器人操作学习提供了更完整的空间感知基础。

## 2. 论文提出的方法论
- **核心思想**：一种**免训练**的框架，直接利用现有3D基础模型从稀疏视频帧中重建场景，并分析视频得到接触点与手部轨迹，投影到3D空间构成可供性。
- **关键技术细节**：
  - **稀疏帧3D重建**：为了解决自我中心视频中难以获取足够静态、高质量帧用于传统三维重建（如COLMAP）的问题，采用**DUST3R基础模型**，仅凭少量稀疏图像即可重建场景结构与相机位姿，无需COLMAP流程。
  - **2D接触点提取**：对视频进行**手部检测**，确定手与物体发生接触的时刻，并定位2D接触点。
  - **3D接触点投影**：利用高斯热图，将2D接触点投影到经由DUST3R重建出的3D空间，得到对应的3D接触点。
  - **手部轨迹整合**：通过**3D手部姿态估计**得到手部轨迹，再使用**线性回归**处理轨迹数据，整合出人-物交互的时空动力学信息，形成完整的3D可供性表征（包含接触位置、交互姿态、运动轨迹等）。
- **算法流程**（文字说明）：
  1. 输入自我中心演示视频。
  2. 手部检测模块逐帧识别手的位置，提取手与场景接触的时间片段及2D接触点坐标。
  3. 从视频中选取若干稀疏但关键帧，输入DUST3R获得场景3D重建及相机参数。
  4. 结合相机参数，将2D接触点通过高斯热图投影至3D空间，确定交互的3D位置。
  5. 利用3D手部姿态估计器得到手部运动轨迹，对轨迹进行线性回归，得到平滑、可供机器人参考的交互路径。
  6. 输出3D可供性，包括作用点、方向和手部运动方式。

## 3. 实验设计
- **数据集/场景**：使用 **ego4d-exo** 数据集，从中选取 **7 个现实世界厨房操作任务**的手-物交互场景（具体任务未在摘要中详列，推测涉及抓取、放置、搅拌等常见动作）。
- **评估基准/对比方法**：
  - 摘要中未明确提及定量对比的baseline方法，文章主要是展示所提方法的**有效性**，可能侧重于定性展示或机器人抓取/交互规划任务上的成功应用，而非在某个固定benchmark上对比其他可供性方法。
  - 由于3D可供性从视频重建是一个较新的设定，较难找到直接对应的对比基线。
- **验证方式**：实验展示该方法能够在机器人操作场景中**引导抓取和交互规划**，证明3D可供性作为中间表征确实提升了操作的可执行性。

## 4. 资源与算力
- **文献提及情况**：在提供的摘要及元数据中，**未明确说明**使用的GPU型号、数量、训练时长等算力信息。
- **可能推断**：由于方法免训练，主要计算开销在于DUST3R的前向推理、手部检测、姿态估计等，这些通常可以在单块消费级GPU上完成，但具体数值需参见论文全文。

## 5. 实验数量与充分性
- **实验组数概况**：
  - 从已有信息看，仅在 **ego4d-exo 数据集**的 **7个操作任务** 上进行实验，实验场景限于厨房。
  - 缺少消融实验（如无DUST3R而用其他重建方法的对比、有/无线性回归的对比等）的提及。
- **充分性评价**：
  - **任务覆盖面有限**：仅7个厨房任务，场景种类较单一，可能不足以全面验证方法的泛化性。
  - **对比不足**：未给出与其他方法的定量比较（如2D可供性方法在抓取成功率上的提升），难以客观判断3D带给下游操作任务的确切益处。
  - **实验设计的客观性与公平性**：由于是免训练方法且可能没有直接竞争者，实验设计更多是概念验证性质，公平性尚可，但客观比较较为缺失。

## 6. 论文的主要结论与发现
- 从自我中心视频中重建3D可供性是**可行且有效的**，能够为机器人操作任务提供包含空间位置、深度和运动动态的关键信息。
- 借助DUST3R这种免COLMAP的3D基础模型，可以**克服自我中心视频静态帧不足的问题**，实现稀疏帧下的可靠3D重建。
- 最终的3D可供性表征成功指导了多种厨房场景下的抓取与交互规划，说明该方法能够将人类演示转化为机器人可操作的空间感知知识。

## 7. 优点
- **免训练**：直接利用现有基础模型，无需额外标注数据或重新训练，部署成本低。
- **突破2D局限**：解决传统2D可供性忽视空间信息的问题，使可供性更贴近机器人操作需求。
- **利用先进基础模型**：引入DUST3R，避免依赖COLMAP等传统流程，提高了在动态自我中心视频上的适用性和鲁棒性。
- **时空整合**：不仅提取空间接触点，还通过3D手部轨迹和线性回归捕捉交互的时空动态，提供给机器人更丰富的运动先验。
- **应用导向明确**：直接面向机器人操作任务进行设计，结果能用于实际抓取和运动规划。

## 8. 不足与局限
- **实验覆盖有限**：仅在单一数据集（ego4d-exo）的7个厨房任务上验证，缺乏在不同场景、不同物体、不同操作类型下的泛化评估。
- **对比实验缺乏**：未与2D可供性方法、其他3D可供性重建尝试、或者直接用视频运动规划的方法进行量化对比，难以量化3D可供性带来的实际性能提升幅度。
- **算力信息缺失**：未报告计算资源需求，无法评估方法的实时性（如是否可用于在线学习）和落地成本。
- **可能的偏差风险**：依赖手部检测与姿态估计的精度，若这些模块在特定条件下（遮挡、模糊）失败，会影响最终可供性质量；选取稀疏帧的策略也未明确，可能引入选择偏差。
- **应用限制**：方法是为“从演示视频学习”设计，要求有第一人称手物交互视频，对于非演示视频或无手可见的场景可能不适用；输出是手部位姿和接触点，未考虑机器人末端执行器的差异（如手爪vs灵巧手），迁移时可能需要额外映射。

（完）
