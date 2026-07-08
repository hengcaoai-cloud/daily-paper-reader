---
title: "EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video"
title_zh: EgoDex：从大规模自我中心视频中学习灵巧操作
authors: "Ryan Hoque, Peide Huang, David J. Yoon, Mouli sivapurapu, Jian Zhang"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=FFxkFMU89E"
tags: ["query:robot"]
score: 10.0
evidence: 最大规模的带有3D手部/手指跟踪的自我中心人类数据集，用于灵巧操作学习
tldr: EgoDex针对灵巧操作模仿学习的数据稀缺问题，利用Apple Vision Pro采集了829小时带有3D手部姿态标注的自我中心视频，构建了最大规模的人类灵巧操作数据集。该数据集提供了精确的手指跟踪和场景重建，为从人类视频中学习灵巧操作提供了高质量的数据基础，并展示了其在机器人策略学习中的潜力。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 灵巧操作缺乏互联网规模的数据，现有自我中心数据集缺少手部姿态标注且不专注于物体操作。
method: 使用Apple Vision Pro采集大规模带有3D手部跟踪数据的自我中心视频，构建EgoDex数据集。
result: 数据集包含829小时视频，具有精确的3D手部和手指跟踪以及场景重建信息。
conclusion: 该数据集为灵巧操作模仿学习提供了关键的数据资源，有望推动从人类视频到机器人技能的转移。
---

## Abstract
Imitation learning for manipulation has a well-known data scarcity problem. Unlike natural language and 2D computer vision, there is no Internet-scale corpus of data for dexterous manipulation. One appealing option is egocentric human video, a passively scalable data source. However, existing large-scale datasets such as Ego4D do not have native hand pose annotations and do not focus on object manipulation. To this end, we use Apple Vision Pro to collect EgoDex: the largest and most diverse dataset of dexterous human manipulation to date. EgoDex has 829 hours of egocentric video with paired 3D hand and finger tracking data collected at the time of recording, where multiple calibrated cameras and on-device SLAM can be used to precisely track the pose of every joint of each hand. The dataset covers a wide range of diverse manipulation behaviors with everyday household objects in 194 different tabletop tasks ranging from tying shoelaces to folding laundry. Furthermore, we train and systematically evaluate imitation learning policies for hand trajectory prediction on the dataset, introducing metrics and benchmarks for measuring progress in this increasingly important area. By releasing this large-scale dataset, we hope to push the frontier of robotics, computer vision, and foundation models. EgoDex is publicly available for download at https://github.com/apple/ml-egodex.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
最大规模的带有3D手部/手指跟踪的自我中心人类数据集，用于灵巧操作学习。

### 2. 核心内容
EgoDex针对灵巧操作模仿学习的数据稀缺问题，利用Apple Vision Pro采集了829小时带有3D手部姿态标注的自我中心视频，构建了最大规模的人类灵巧操作数据集。该数据集提供了精确的手指跟踪和场景重建，为从人类视频中学习灵巧操作提供了高质量的数据基础，并展示了其在机器人策略学习中的潜力。

### 3. 对应检索需求
how to use large scale first person human videos for robot dexterous manipulation。

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=FFxkFMU89E](https://openreview.net/forum?id=FFxkFMU89E)
