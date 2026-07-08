---
title: "Taccel: Scaling Up Vision-based Tactile Robotics via High-performance GPU Simulation"
title_zh: "Taccel: 通过高性能GPU仿真扩展基于视觉的触觉机器人"
authors: "Yuyang Li, Wenxin Du, Chang Yu, Puhao Li, Zihang Zhao, Tengyu Liu, Chenfanfu Jiang, Yixin Zhu, Siyuan Huang"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=PtGMadeONU"
tags: ["query:robot"]
score: 9.0
evidence: 高性能GPU仿真平台用于基于视觉的触觉传感器，支持大规模触觉机器人研究
tldr: Taccel 针对视觉触觉传感器缺乏高效精确仿真工具的问题，集成增量势能接触和仿射体动力学，实现了高达915FPS的高保真仿真平台。该平台大幅降低了触觉机器人研究的仿真门槛，支持大规模触觉操控策略学习。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 视觉触觉传感器物理特性复杂，缺乏高效精确的仿真工具限制了触觉机器人研究的规模。
method: 集成增量势能接触和仿射体动力学，在GPU上实现高保真快速触觉传感器仿真。
result: 仿真速度达到915FPS，且在触觉感知精度上与真实传感器高度一致。
conclusion: Taccel为触觉机器人研究提供了可扩展的高性能仿真基础，有望加速触觉操控的发展。
---

## Abstract
Tactile sensing is crucial for achieving human-level robotic capabilities in manipulation tasks. As a promising solution, Vision-based Tactile Sensors (VBTSs) offer high spatial resolution and cost-effectiveness, but present unique challenges in robotics for their complex physical characteristics and visual signal processing requirements. The lack of efficient and accurate simulation tools for VBTSs has significantly limited the scale and scope of tactile robotics research. We present Taccel, a high-performance simulation platform that integrates Incremental Potential Contact (IPC) and Affine Body Dynamics (ABD) to model robots, tactile sensors, and objects with both accuracy and unprecedented speed, achieving a total of 915 FPS with 4096 parallel environments. Unlike previous simulators that operate at sub-real-time speeds with limited parallelization, Taccel provides precise physics simulation and realistic tactile signals while supporting flexible robot-sensor configurations through user-friendly APIs. Through extensive validation in object recognition, robotic grasping, and articulated object manipulation, we demonstrate precise simulation and successful sim-to-real transfer. These capabilities position Taccel as a powerful tool for scaling up tactile robotics research and development, potentially transforming how robots interact with and understand their physical environment.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
高性能GPU仿真平台用于基于视觉的触觉传感器，支持大规模触觉机器人研究。

### 2. 核心内容
Taccel 针对视觉触觉传感器缺乏高效精确仿真工具的问题，集成增量势能接触和仿射体动力学，实现了高达915FPS的高保真仿真平台。该平台大幅降低了触觉机器人研究的仿真门槛，支持大规模触觉操控策略学习。

### 3. 对应检索需求
tactile sensors and tactile-based manipulation。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=PtGMadeONU](https://openreview.net/forum?id=PtGMadeONU)
