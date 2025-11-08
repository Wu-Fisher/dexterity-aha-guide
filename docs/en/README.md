<div align="center">

# 🤖 Dexterous Hand General Manipulation Guide

### Dexterity-Aha-Guide

**Code to Hand, Zero to Hero**

[![Stars](https://img.shields.io/github/stars/Wu-Fisher/dexterity-aha-guide?style=social)](https://github.com/Wu-Fisher/dexterity-aha-guide)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![中文文档](https://img.shields.io/badge/文档-中文-red.svg)](README.md)
[![English](https://img.shields.io/badge/docs-English-blue.svg)](./docs/en/README.md)

**English Documentation** | [Chinese Documentation](./README.md)

---

</div>

## 💡 What is this?

If you are curious about **Embodied Intelligence**, **Robot Dexterous Manipulation Algorithms**, or want to build a custom high-degree-of-freedom end effector and design your own unique embodied perception dexterous hand cerebellum model, then this guide is for you.

> **Why focus on dexterous hands?**
> Dexterous hands are the "crown jewel" of embodied intelligence—they require not only exquisite mechanical design but also powerful algorithmic support. From hardware to software, from theory to practice, this is a challenging but extremely fascinating field.

**This guide covers:**
- 🔧 **Hardware Design** - Detailed explanations of various dexterous hand solutions, from tendon-driven to direct-drive
- 🧠 **Algorithm Advancement** - Latest research in reinforcement learning, imitation learning
- 📊 **Dataset Resources** - Guide to obtaining high-quality training data
- 🎮 **Operation Collection** - Practical solutions like VR teleoperation, data gloves
- 🌐 **Simulation Platforms** - Recommended tools like Isaac, MuJoCo, Genesis

---


## 🔥 Dexterous Hand Hardware Starter Recommendation: Assemble Your Dexterous Hand Like Lego!


**GaiaHand** is an open-source dexterous hand based on miniature joint modules, assemble your robot hand like building Lego! The miniature joint modules integrate drive and control, and we plan to provide open-source mechanical structure solutions for dexterous hands with **15, 16 active degrees of freedom**!

<div align="center">
  <img src="./assets/gifs/GaiaBall.gif" alt="GaiaHand15 Ball Demo" width="400">
</div>

<div align="center">
  <img src="./assets/gifs/Gaia16Gesture.gif" alt="GaiaHand16 Gesture Demo" width="400">
</div>


### 📚 Resource Links

- **[Bilibili Assembly Tutorial](https://www.bilibili.com/video/BV1Ysjzz4E6D)** - Step-by-step assembly guide

  <div align="center">
    <img src="./assets/gifs/gaiahand-a.gif" alt="Assembly Process" width="400">
  </div>

- **[Open Source Structure Files](https://cad.onshape.com/documents/913853e62f859c54c2954e0c/w/21739ff31a266b40d3f94263/e/46f10b356fc4737c5aaaa4b3)** - CAD ONSHAPE Online Viewing

> 💬 **Need help? or Customized solutions** Email contact: timmoraty@hotmail.com

---


📝 **Want to see specific content?** Welcome to leave a message in [Issues](https://github.com/Wu-Fisher/dexterity-aha-guide/issues)!

---

## 📖 How to Use This Guide

### 🚀 Beginner's Path

1. **Start with Hardware** - First understand the mechanical structure and working principles of dexterous hands
2. **Understand Physical Interaction** - Master the interaction logic between hardware and the real world
3. **Enter the Algorithm World** - Learn methods like reinforcement learning, imitation learning
4. **Hands-on Practice** - Build your own dexterous hand, collect data, train models

> 💡 **Core Concept**: Only by deeply understanding the hardware can you design truly effective algorithms!

### 🎓 Advanced Researchers

- Jump directly to chapters of interest
- Consult the latest papers and open-source projects
- Reference Benchmarks and datasets

---

## 📑 Table of Contents Navigation

<details>
<summary><b>Click to expand full table of contents</b></summary>

- [💡 What is this?](#-what-is-this)
- [🔥 Dexterous Hand Hardware Starter Recommendation: Assemble Your Dexterous Hand Like Lego!](#-dexterous-hand-hardware-starter-recommendation-assemble-your-dexterous-hand-like-lego)
- [📖 How to Use This Guide](#-how-to-use-this-guide)
- [📑 Table of Contents Navigation](#-table-of-contents-navigation)

- [1️⃣ Dexterous Hand Hardware Design](#1️⃣-dexterous-hand-hardware-design)
  - [Commercial Products Overview](#commercial-products-overview)
  - [🪢 Tendon-Driven Dexterous Hand](#🪢-tendon-driven-dexterous-hand)
  - [🔗 Linkage Transmission Dexterous Hand](#-linkage-transmission-dexterous-hand)
  - [⚡ Direct-Drive Motor Dexterous Hand](#-direct-drive-motor-dexterous-hand)
  - [🧪 New Material Driven Dexterous Hand](#-new-material-driven-dexterous-hand)
  - [🖐️ Tactile Sensors](#-tactile-sensors)

- [2️⃣ Dexterous Manipulation Algorithms](#2️⃣-dexterous-manipulation-algorithms)
  - [🎯 Reinforcement Learning](#-reinforcement-learning)
  - [🎯 Imitation Learning](#-imitation-learning)
    - [📹 Simulation Generated Trajectory Data](#📹-simulation-generated-trajectory-data)
    - [📹 Video-Based Data](#📹-video-based-data)
    - [🎮 Teleoperation-Based Data](#🎮-teleoperation-based-data)
    - [🎮 Combining Reinforcement Learning to Fine-tune Imitation Learning](#🎮-combining-reinforcement-learning-to-fine-tune-imitation-learning)
    - [🤖 General-Purpose Manipulation Large Models](#🤖-general-purpose-manipulation-large-models)
  - [🔄 Redirection Algorithms](#-redirection-algorithms)

- [3️⃣ Datasets and Benchmark](#3️⃣-datasets-and-benchmark)

- [4️⃣ Data Collection Solutions](#4️⃣-data-collection-solutions)

- [5️⃣ Simulation Platforms](#5️⃣-simulation-platforms)

- [6️⃣ General Knowledge](#6️⃣-general-knowledge)
  - [Grasping Classification Methods](#grasping-classification-methods)

- [🔗 Friendly Links](#-friendly-links)
- [👥 About Us](#-about-us)


</details>

---

## 1️⃣ Dexterous Hand Hardware Design

> **Why start with hardware?**
> The mechanical design of a dexterous hand directly determines what it can do and how well it can do it. Understanding the pros and cons of different drive methods allows you to choose the solution best suited for your application scenario.

Dexterous hands can be categorized by drive method:

- **Tendon-Driven** - Controlled by pulling tendons like a puppet, fingers are lightweight and flexible
- **Linkage Transmission** - Power transmission through gears and linkages, compact structure
- **Direct-Drive Motor** - Each joint has a small motor, fast response
- **New Material Driven** - Uses "black tech" like shape memory alloys, liquid crystal elastomers

### Commercial Products Overview

<details>
<summary><b>Expand to view mainstream domestic commercial dexterous hands</b></summary>

| Company | Product | Core Features | Application Scenarios |
|------|------|----------|----------|
| **Lingqiao Intelligence** | DexHand021 | 19 DOF, force control accuracy 0.01N | Medical surgery, industrial assembly |
| **Inspire Robots** | RH56 Series | Underactuated design, power-off self-locking | Industrial inspection, education/research |
| **Qiangnao Technology** | Revo 2 | Brain-computer interface, 30+ material recognition | Disability assistance, remote operation |
| **Unitree** | Unitree Dex5 | Backdrivable technology, power consumption only 10W | Logistics sorting, entertainment interaction |
| **Zhiyuan Robot** | OmniHand | Vision-tactile dual-modal perception | Automotive manufacturing, precision tool use |

> More details please refer to the full comparison table ↓

</details>

### 🪢 Tendon-Driven Dexterous Hand

**Working Principle**: Motors are installed in the palm or forearm, controlling finger flexion and extension by tightening/loosening tendons.

**Advantages**: Fingers are lightweight, suitable for high-DOF complex actions
**Disadvantages**: Tendons are prone to wear, require regular maintenance

> 💡 **Analogy**: Like controlling a puppet, pull the string and the action comes!

#### Recommended Solutions

1. **[Shadow Hand](https://www.shadowrobot.com)** - UK Shadow Robot Company, benchmark product in the research community, representative work of tendon-driven dexterous hands

2. **[Tesla Optimus Gen3](https://www.tesla.com)** - Tesla Optimus Gen3's tendon-driven dexterous hand
   - 📺 [YouTube Demo Video](https://www.youtube.com/shorts/jm47b6O3eYQ)

3. **[Korean Bionic Tendon-Driven Hand FLLEX HAND](https://zhuanlan.zhihu.com/p/561350692)** - Korean research bionic tendon-driven hand, human-like impact absorption design
   - 📺 [Bilibili Production Tutorial](https://www.bilibili.com/video/BV1B54y1o7vS)
   - 📄 [Paper](https://doi.org/10.1109/LRA.2019.2929988)

4. **[DexHand Open Source Solution](https://www.dexhand.org)** - YouTube master's work, most popular open-source replication project
   - 📺 [Assembly Tutorial](https://willcogley.notion.site/Dexhand)

5. **[ORCA Hand](https://www.orcahand.com)** - ETH Zurich Soft Robotics Lab, soon to be fully open-source
   - 📄 [Paper](https://arxiv.org/abs/2504.04259)

6. **[Open Parametric Hand](https://github.com/kg398/100_fingers)** - Featured on the cover of Science Robotics!
   - 56 adjustable parameters, customizable hand shapes from human to primate
   - 📄 [Paper](https://www.science.org/doi/10.1126/scirobotics.ads6437)

7. **[Apex Hand](https://www.bilibili.com/video/BV1MCh1zzE2g/?spm_id_from=333.337.search-card.all.click&vd_source=b9a952aeb6ad36adfd92f02ff3b34f58)** Yuansheng Intelligence commercial dexterous hand, industry's first dexterous hand capable of operating a mobile phone with one hand
   - 📺 [Bilibili Demo Video](https://www.bilibili.com/video/BV1MCh1zzE2g/?spm_id_from=333.337.search-card.all.click&vd_source=b9a952aeb6ad36adfd92f02ff3b34f58)

8. **[D22 PRO](https://botyard.ai/?page_id=72)** Boya Intelligence commercial dexterous hand, 22 active DOF, forearm integrated solution
   - 📺 [Bilibili Demo Video](https://www.bilibili.com/video/BV1vRKxzAEHF/?spm_id_from=333.337.search-card.all.click&vd_source=b9a952aeb6ad36adfd92f02ff3b34f58)

---

### ⚙️ Linkage Transmission Dexterous Hand

Divided into **serial linkage** and **parallel linkage** types, with different force transmission paths and control strategies.

**Advantages**: Compact structure, good rigidity
**Disadvantages**: Complex design, higher cost

#### Recommended Solutions

1. **[ILDA Hand](https://www.nature.com/articles/s41467-021-27261-0)** - Classic representative of parallel linkage
   - 📖 [Chinese Detailed Explanation](https://zhuanlan.zhihu.com/p/563973849)

2. **[Inspire Robots Dexterous Hand RH56](https://www.inspire-robots.com)** - Domestic commercial serial linkage solution

3. **[Linker Hand](https://www.linkerbot.cn)** - Dual structure with linkage + tendon, price only 1/20 of Shadow Hand

4. **[Unitree Dex5](https://www.unitree.com)** - Backdrivable technology, 20 DOF

---

### ⚡ Direct-Drive Motor Dexterous Hand

**Working Principle**: Each joint is directly driven by a miniature motor, no intermediate transmission mechanism.

**Advantages**: Fast response, high control precision
**Disadvantages**: Fingers are heavier, complex structure

> 💡 **Analogy**: Each joint has a small motor attached, moves when you want!

#### Recommended Solutions

1. **[LEAP Hand](https://v1.leaphand.com)** - Open-source direct-drive motor, available on Taobao

2. **[HIT-DLR Hand](https://www.dlr.de/en/rm/research/robotic-systems/hands/dlr-hit-hand)** - Harbin Institute of Technology × German Aerospace Center

3. **[Zhaowei Dexterous Hand](https://www.zwgear.com)** - Self-developed miniature coreless motor, 17-20 DOF

4. **[DexterousHand GX11](https://github.com/Democratizing-Dexterous/DexterousHandGX11)** - Open-source by Donglin Zhongsheng expert
   - Three-finger 11 DOF, also comes with [12 DOF exoskeleton](https://github.com/Democratizing-Dexterous/ExoskeletonGloveEX12)

---

### 🧪 New Material Driven Dexterous Hand

Uses new materials like **Shape Memory Alloy (SMA)**, **Liquid Crystal Elastomer (LCE)**, **Flexible Pneumatic Chambers** as actuators.

**Advantages**: Lightweight, high biomimetic degree
**Disadvantages**: Complex control, durability needs verification

#### Recommended Solutions

1. **[SMA Driven Dexterous Hand](https://www.mdpi.com/2076-0825/10/1/6)** - Driven by shape memory alloy coils

2. **[LCE Soft Finger](https://www.researchgate.net/publication/336447702)** - Tsinghua University Zhongqiang Yang's team, power density close to human muscle
   - 📄 Reference: [Matter 2025](https://doi.org/10.1016/j.matt.2024.11.003)

3. **[Harvard Flexible Pneumatic Hand](https://www.science.org/doi/10.1126/scirobotics.abn4155)** - Robert Wood's team
   - 3D printed inflatable structure, achieves biomimetic grasping
   - Related work: [Stochastic Topology Grasping](https://www.pnas.org/doi/10.1073/pnas.2209819119) | [Dexterous Flexible Hand](https://ieeexplore.ieee.org/document/9134855)

---

### 🖐️ Tactile Sensors

The "skin" of the dexterous hand—without tactile feedback, even the most flexible hand is "grasping blindly".

| Type | Principle | Advantages | Disadvantages |
|------|------|------|------|
| **Vision-Tactile** | Camera captures contact deformation | High resolution, multimodal information | High computational complexity |
| **Resistive** | Resistance changes under pressure | Simple structure, low cost | Prone to fatigue, nonlinear |
| **Capacitive** | Changes in plate spacing | High sensitivity, low power consumption | Susceptible to electromagnetic interference |
| **Magnetic** | Magnetic material displacement | Strong anti-interference, wear-resistant | Complex calibration |

#### 🔍 Vision-Tactile Sensors

Capture contact deformation through high-resolution images to obtain multidimensional information like texture, force distribution.

**Reference Solutions:**

1. **[9DTact](https://linchangyi1.github.io/9DTact/)** - Tsinghua open-source solution
   - 📺 [Bilibili Production Tutorial](https://www.bilibili.com/video/BV1nu411w7t4/)

2. **[GelSight](https://www.gelsight.com)** - Pioneer of vision-tactile sensing
   - 📖 [Development History Review](https://zhuanlan.zhihu.com/p/691621404)

3. **[PP-TAC](https://peilin-666.github.io/projects/PP-Tac)** - RSS 2025, first vision-tactile hand capable of grasping thin paper-like objects
   - 📄 [Paper](https://arxiv.org/pdf/2504.16649)

4. **[MinSight](https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/aisy.202300042)** - Human fingertip size, 60Hz output of 3D force distribution

#### 🧲 Magnetic (Hall Effect) Tactile Sensors

Use Hall effect sensors to measure magnetic field changes, calculate force, deformation and other physical quantities through magnetic field changes. High detection sensitivity, can perceive high-frequency changes, but susceptible to electromagnetic interference.

**Reference Solutions:**

1. **Soft Magnetic Flexible Skin Solution**
   - 📄 [ieeexplore](https://ieeexplore.ieee.org/abstract/document/9050905)

2. **Self-Decoupled 3D Force Sensor**
   - 📄 [HKUST Yajing Shen's Team](https://www.science.org/doi/abs/10.1126/scirobotics.abc8801)
   - 📄 [HKU Jia Pan's Team](https://www.nature.com/articles/s42256-024-00904-9)

3. **AnySkin** - Open-source Hall effect tactile sensor from New York University
   - 📄 [arXiv 2024](https://arxiv.org/abs/2409.08276)
   - 🌐 [Project Link](https://any-skin.github.io/)

4. **PX-6AX GEN3** - Paxini Technology commercial tactile sensor
   - 🌐 [Official Website](https://paxini.com/)

#### 📊 Resistive Tactile Sensors

The most traditional solution, low cost, fast response.

**Reference Solutions:**

1. **[RP-C7.6-ST](https://www.dfrrobot.com/product-1841.html)** - DFRobot film pressure sensor

---

## 2️⃣ Dexterous Manipulation Algorithms

Hardware is the body, algorithms are the soul.

Based on training methods, we have the following classifications:

- **Reinforcement Learning (RL)** - Models the value function, allowing the robot to learn through trial and error, master the optimal policy in a simulation environment, and then transfer it to the real world; the latest progress can achieve reinforcement learning directly in the real world [SERL](https://www.bilibili.com/video/BV1Bh1hBaEb3/?spm_id_from=333.337.search-card.all.click&vd_source=b9a952aeb6ad36adfd92f02ff3b34f58)
- **Imitation Learning (IL)** - Learns from a large amount of simulation/real-world expert operation data. Evolving from past Single-Task imitation learning to the [Scaling Law](https://generalistai.com/blog/nov-04-2025-GEN-0) of data. Through multi-stage training including Pre-training, Post-training, and RL, it achieves Multi-Task or even generalization capabilities for tasks in general domains.

> 📚 **Recommended AWESOME Link**: [Awesome Embodied Robotics and Agent](https://github.com/zchoi/Awesome-Embodied-Robotics-and-Agent)

---

### 🎮 Reinforcement Learning

**Core Idea**: Through "trial and error + reward," the robot autonomously explores the optimal manipulation policy.

**Advantages**: Strong adaptive ability, capable of handling complex environments and uncertainties.
**Disadvantages**: Long training time, requires extensive simulation or real-world trial and error.

#### Selected Papers

<details>
<summary><b>Click to expand the Reinforcement Learning paper list</b></summary>

1. **PPO** - Proximal Policy Optimization, the foundation of RL basics.
   - 📄 [arXiv 2017](https://arxiv.org/abs/1707.06347)

2. **SERL** - Real-world Reinforcement Learning
   - 📄 [ICRA 2024](https://arxiv.org/abs/2401.16013)
   - 🌐 [Project Link](https://srl-ethz.github.io/serl/)
   - 📄 [Science Robotics 2025](https://hil-serl.github.io/static/hil-serl-paper.pdf) HIL-SERL (Human-in-the-loop SERL)

2. **DexPoint** - General point cloud reinforcement learning for sim2real.
   - 📄 [CORL 2023](https://proceedings.mlr.press/v205/qin23a.html)
   - 🌐 [Project Link](https://yzqin.github.io/dexpoint/)

3. **RoboPianist** - Reinforcement learning for dexterous piano playing.
   - 🌐 [Project Link](https://kzakka.com/robopianist/)
   - 📄 [ICLR 2024](https://openreview.net/forum?id=HDYMjiukjn)

4. **Getting the Ball Rolling** - ETH, learning rolling contact policies for tendon-driven hands.
   - 🌐 [Project Link](https://srl-ethz.github.io/get-ball-rolling/)
   - 📄 [arXiv 2023](https://arxiv.org/abs/2308.02453)

5. **ArrayBot** - Distributed tactile manipulation generalization, turning a table into a robot.
   - 🌐 [Project Link](https://steven-xzr.github.io/ArrayBot/)
   - 📄 [arXiv 2023](https://arxiv.org/abs/2306.16857)
   - 📺 [Video Demo](https://www.xiaohongshu.com/discovery/item/690f2d5400000000070370e8?source=webshare&xhsshare=pc_web&xsec_token=ABstpKTBiYRIdy-GfLGNl-QP9Jh1vicrqAofLbsoWq5d8=&xsec_source=pc_share)

6. **HuDOR** - Generating reward signals through hand-object trajectory differences.
   - 🌐 [Project Link](https://object-rewards.github.io/)
   - 📄 [arXiv 2024](https://arxiv.org/abs/2410.23289)

7. **DexSinGrasp** - Unified policy for object separation and grasping.
   - 📄 [arXiv 2025](https://arxiv.org/abs/2504.04516)

8. **RobustDexGrasp** - Zero-shot dynamic grasping, based on hand-centered dynamic distance vectors.
   - 📄 [arXiv 2025](https://arxiv.org/pdf/2504.05287)

9. **DexMachina** - Curriculum-based reinforcement learning based on task and functional retargeting.
   - 🌐 [Project Link](https://project-dexmachina.github.io/)
   - 📄 [arXiv 2025](https://arxiv.org/abs/2505.24853)

</details>

---

### 🎯 Imitation Learning

**Core Idea**: Learns directly from human or expert demonstrations, bypassing the lengthy trial-and-error process.

**Advantages**: Fast convergence, low training cost, high data quality.
**Disadvantages**: Relies on data distribution, relatively weaker generalization ability.

> 📖 **Survey Paper**: [A Survey of Dexterous Manipulation Methods Based on Imitation Learning](https://arxiv.org/pdf/2504.03515)

We classify based on data sources:
 - **Simulation-generated Trajectories** - Generate expert data in virtual environments.
 - **Video Data** - Understand tasks from human operation videos.
 - **Teleoperation Data** - Collect real operation data via VR/gloves.

Based on more advanced training schemes, we supplement the classification with the following introductions:
- **Combining Reinforcement Learning to Fine-tune Imitation Learning** - Enhances the generalization ability of imitation learning through reinforcement learning.
- **General-Purpose Generalization Manipulation Large Models** - General-purpose generalization manipulation large models trained on massive data, usable as base models for imitation learning in various tasks, possessing preliminary general capabilities.

#### 📹 Simulation-Generated Trajectory Data

<details>
<summary><b>Expand to view paper list</b></summary>

1. **D(R,O) Grasp** - A general grasping imitation learning framework independent of the dexterous hand's embodiment.
   - 📄 [ICRA 2025](https://arxiv.org/abs/2410.01702)
   - 🌐 [Project Link](https://nus-lins-lab.github.io/drograspweb/)

2. **DexGarmentLab** - Imitation learning framework for garment-related operations, generated based on IsaacSim.
   - 📄 [NeurIPS 2025](https://arxiv.org/pdf/2505.11032)
   - 🌐 [Project Link](https://wayrise.github.io/DexGarmentLab/)

</details>

#### 📹 Based on Video Data

<details>
<summary><b>Expand to view paper list</b></summary>

1. **Robotic Telekinesis** - Learning robotic hand manipulation from web videos.
   - 🌐 [Project Link](https://robotic-telekinesis.github.io/)
   - 📄 [arXiv 2022](https://arxiv.org/abs/2202.10448)

2. **DexVIP** - Learning grasping from videos using hand pose priors.
   - 🌐 [Project Link](https://vision.cs.utexas.edu/projects/dexvip-dexterous-grasp-pose-prior)
   - 📄 [arXiv 2022](https://arxiv.org/abs/2202.00164)

</details>

#### 🎮 Based on Teleoperation Data

<details>
<summary><b>Expand to view paper list</b></summary>

1. **Tilde** - Efficient demonstration collection + Diffusion Policy.
   - 🌐 [Project Link](https://sites.google.com/view/tilde-)
   - 📄 [arXiv 2024](https://arxiv.org/pdf/2405.18804)

2. **GLOSH** - Allegro Hand teleoperation + visuomotor diffusion policy.
   - 🌐 [Project Link](https://dex-manip.github.io/)
   - 📄 [arXiv 2025](https://arxiv.org/pdf/2503.02587)

3. **CordViP** - 6D pose estimation + hand-object interaction-aware point cloud.
   - 🌐 [Project Link](https://aureleopku.github.io/CordViP/)
   - 📄 [arXiv 2025](https://www.arxiv.org/abs/2502.08449)

4. **ViTacFormer** - Based on exoskeleton teleoperation for humanoid dexterous hand robots, with tactile data collection for training.
   - 🌐 [Project Link](https://github.com/RoboVerseOrg/ViTacFormer)
   - 📄 [arXiv 2025](https://arxiv.org/abs/2506.15953)

</details>

#### 🎮 Combining RL to Fine-tune Imitation Learning

<details>
<summary><b>Expand to view paper list</b></summary>

1. **DIME** - Single RGB camera teleoperation imitation learning, efficient demonstration data collection.
   - 🌐 [Project Link](https://nyu-robot-learning.github.io/dime/)
   - 📄 [arXiv 2022](https://arxiv.org/abs/2203.13251)

2. **DexNDM** - Using only distributionally biased real data to accurately bridge the Sim2Real gap for dexterous hand rotation operations.
   - 🌐 [Project Link](https://meowuu7.github.io/DexNDM/)
   - 📄 [arXiv 2025](https://meowuu7.github.io/DexNDM/static/pdfs/DexNDM.pdf)

3. 

</details>

#### 🤖 General-Purpose Generalization Manipulation Large Models

<details>
<summary><b>Expand to view paper list</b></summary>

1. **NVIDIA GR00T N1** - Open foundation model integrating fast and slow models.
   - 📄 [arXiv 2025](https://arxiv.org/abs/2503.14734)
   - 📖 [Zhihu Detailed Explanation](https://zhuanlan.zhihu.com/p/32622954748)

2. **DexGraspVLA** - Lingchu Intelligence, domain-invariant representation.
   - 🌐 [Project Link](https://dexgraspvla.github.io/)
   - 📄 [arXiv 2025](https://arxiv.org/abs/2502.20900)

3. **Video Prediction Policy** - Xingdong Jiyuan, predictive visual representation.
   - 🌐 [Project Link](https://video-prediction-policy.github.io)
   - 📄 [arXiv 2024](https://arxiv.org/pdf/2412.14803)

4. **π0.5** - Physical Intelligence, two-stage reasoning-enhanced generalization, subtask decomposition and reasoning.
   - 🌐 [Project Link](https://www.physicalintelligence.company/blog/pi05)
   - 📄 [Technical Report](https://www.physicalintelligence.company/download/pi05.pdf)

5. **wall-x** - Independent Variable X-Square-Robot general open-source manipulation large model.
   - 🌐 [Project Link](https://github.com/X-Square-Robot/wall-x)
   - 📄 [Technical Report](https://arxiv.org/pdf/2509.11766)

6. **Gen0** - Generalist AI general manipulation large model, the first embodied large model Scaling Law in real industrial/application scenarios (the author currently considers this the most impressive DEMO on the market 👍👍👍, although it hasn't used dexterous hands yet).
   - 🌐 [Project Link](https://generalistai.com/blog/nov-04-2025-GEN-0#science-of-pretraining)
   - 📺 [YouTube Demo](https://youtu.be/mhfleCK_IAI)

</details>

#### 
---

### 🔄 Retargeting Algorithms

**Core Idea**: Mapping human hand operations to dexterous hands with different structures.

#### Recommended Solutions

1. **[Dex-Retargeting](https://github.com/dexsuite/dex-retargeting)** - Open-sourced by AnyTeleop, supports multiple dexterous hands.

2. **[GeoRT](https://github.com/facebookresearch/GeoRT)** - Meta, unsupervised retargeting based on five geometric principles, can achieve 1kHz real-time speed, supports multiple human data collection and fast fine-tuning adaptation schemes.

3. **[Retargeting](https://mingrui-yu.github.io/retargeting/)** - Tsinghua Intelligent Robotic Manipulation Lab, dexterous hand retargeting based on geometric constraints.

---



## 3️⃣ Datasets and Benchmarks

**Why are datasets important?**

Dexterous hand manipulation tasks are highly complex and require high-quality, diverse training data. However, compared to grippers, the barrier to collecting dexterous hand data is higher:

- ❌ Requires recording multi-degree-of-freedom temporal actions
- ❌ Requires complete force contact distribution information
- ❌ Expensive collection systems, occlusion is difficult to eliminate

### Recommended Datasets

<details>
<summary><b>Expand to view dataset list</b></summary>

1.  **[DexMimicGen](https://dexmimicgen.github.io/)** - 60 real data points → 20k+ simulation data points

2.  **[DexManipNet](https://maniptrans.github.io/)** - Transfers various Human-Object interactions to dexterous hands

3.  **[DexCap](https://dex-cap.github.io/)** - Portable human hand manipulation motion capture data

4.  **[ARCTIC](https://arctic.is.tue.mpg.de/)** - 2.1 million frames of bimanual articulated object manipulation, includes 3D hand meshes

5.  **[DexArt](https://www.chenbao.tech/dexart/)** - Dexterous hand articulated object manipulation Benchmark

6.  **[RealDex](https://4dvlab.github.io/RealDex_page/)** - Multimodal teleoperation grasping dataset

7.  **[GraspM3](https://github.com/lihaoming45/GraspM3)** - Isaac Gym generated + LLM semantic annotation

8.  **[EgoDex](https://arxiv.org/abs/2505.11709)** - Egocentric data collected using Apple Vision Pro
    - 📄 [arXiv 2025](https://arxiv.org/abs/2505.11709)

9.  **[DexGarmentLab](https://wayrise.github.io/DexGarmentLab/)** - Bimanual garment manipulation simulation environment

10. **[OphNet-3D](https://www.arxiv.org/abs/2505.17677)** - Medical domain ophthalmic surgery RGB-D dataset

11. **[Dexonomy](https://pku-epic.github.io/Dexonomy/)** - 9.5M data points, 31 grasp types

12. **[Dex1B](https://jianglongye.com/dex1b/)** - Billion-scale conditional generation dataset

</details>

---

## 4️⃣ Data Collection Solutions

Three mainstream methods for obtaining high-quality dexterous manipulation data:

-   **Data Gloves** - Directly record the angle and pose of each finger
-   **VR Teleoperation** - Remote control via virtual reality devices
-   **Exoskeleton Systems** - Arm + hand tracking with force feedback

> 📖 **Detailed Classification**: [Detailed Explanation of Embodied AI Data Collection Systems](https://zhuanlan.zhihu.com/p/5777752031)

### 🧤 Data Gloves

<details>
<summary><b>Expand to view solution list</b></summary>

1.  **[DO-Glove](https://do-glove.github.io/)** - Stanford Dr. Han Zhang's exoskeleton glove

2.  **[Manus MetaGloves Pro](https://www.manus-meta.com/products/metagloves-pro)** - Commercial-grade high-fidelity fingertip tracking

3.  **[DexWild](https://dexwild.github.io/)** - Low-cost portable system for large-scale human data collection

</details>

### 🥽 VR Teleoperation Systems

<details>
<summary><b>Expand to view solution list</b></summary>

1.  **[Bunny-VisionPro](https://dingry.github.io/projects/bunny_visionpro)** - Haptic feedback enhanced perception
    - 📄 [arXiv 2024](https://arxiv.org/abs/2407.03162)

2.  **[DEXCAP](https://dex-cap.github.io/)** - SLAM + electromagnetic field precise tracking
    - 📄 [arXiv 2024](https://arxiv.org/abs/2403.07788)

3.  **[OPEN TEACH](https://open-teach.github.io/)** - Meta Quest 3, real-time control of various robots
    - 📄 [arXiv 2024](https://arxiv.org/abs/2403.07870)

4.  **[OpenVR](https://github.com/Abraham190137/TeleoperationUnity)** - Oculus remote control for Franka Panda
    - 📄 [arXiv 2023](https://arxiv.org/pdf/2305.09765)

5.  **[Holo-Dex](https://holo-dex.github.io/)** - Immersive mixed reality teleoperation
    - 📄 [arXiv 2022](https://arxiv.org/pdf/2210.06463)

</details>

### 🦾 Exoskeleton Systems

<details>
<summary><b>Expand to view solution list</b></summary>

1.  **[ACE](https://ace-teleop.github.io/)** - Cross-platform visual exoskeleton
    - 📄 [arXiv 2024](https://arxiv.org/pdf/2408.11805)

2.  **[AirExo](https://airexo.github.io/)** - Low-cost dual-arm exoskeleton
    - 📄 [arXiv 2023](https://arxiv.org/abs/2309.14975)

3.  **[Inspire Robots Force-Control Glove](https://www.inspire-robots.com/tuijian/lqspeijian/2025-04-17/253.html)** - 5 linear servo actuators, with force feedback

4.  **[Damon Wearable System](https://www.dmrobot.com/products/p3/dm-exton.html)** - Commercial teleoperation solution

</details>

---

## 5️⃣ Simulation Platforms

Simulation is the "training ground" for dexterous hand research – rapid iteration in the virtual world, then transfer to the real environment.

> 🌐 **Recommended Community**: [Simulately Wiki](https://simulately.wiki/) - Focuses on robot physics simulation

### Simulation Model Resources

1.  **[MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie)** - Google DeepMind high-quality MJCF models

2.  **[Dex-URDF](https://github.com/dexsuite/dex-urdf)** - URDF dexterous hand models provided by DexSuite

---

### 🟢 Isaac Family

**Features**: NVIDIA product, high-fidelity physics simulation + powerful rendering

<details>
<summary><b>Expand to view tool list</b></summary>

1.  **[Isaac Sim](https://developer.nvidia.com/isaac/sim)** - Based on Omniverse, extensive simulation assets

2.  **[Isaac Lab](https://developer.nvidia.com/isaac/lab)** - High-fidelity simulation, bridging the perception and training gap

3.  **[NVIDIA Warp](https://nvidia.github.io/warp/)** - Differentiable simulation, supports PyTorch/JAX

</details>

---

### 🔵 MuJoCo Family

**Features**: Lightweight and efficient, precise physics engine

<details>
<summary><b>Expand to view tool list</b></summary>

1.  **[Robosuite](https://github.com/ARISE-Initiative/robosuite)** - Modular simulation framework, latest version v5.0

2.  **[MuJoCo Playground](https://playground.mujoco.org/)** - Based on MJX, simplifies sim-to-real

3.  **[MuJoCo Warp](https://github.com/google-deepmind/mujoco_warp)** - Combines MuJoCo + NVIDIA Warp

</details>

---

### 🟣 Genesis Family

**Features**: Lightweight + high-fidelity, leading in soft body and tactile simulation

<details>
<summary><b>Expand to view tool list</b></summary>

1.  **[Genesis](https://github.com/Genesis-Embodied-AI/Genesis)** - General-purpose robot simulation platform, supports synthetic data generation

</details>

---

## 6️⃣ General Knowledge

### Human Grasp Posture Systems

**Why study human grasping?**

Humans, through millions of years of evolution, have developed grasp postures that embody the natural wisdom of stability, flexibility, and tactile feedback, providing an "inherently reasonable" reference for dexterous hand design.

#### Quick Reference Table of Typical Classification Systems

| Classification System          | Main Characteristics                                  | Applicable Scenarios         | Representative Reference                                                              |
| ------------------------------ | ----------------------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------- |
| **Napier Dichotomy**           | Earliest "Power vs. Precision" functional perspective | Quick task type discrimination | [Paper](https://scispace.com/pdf/the-prehensile-movements-of-the-human-hand-3cwm2534xp.pdf) |
| **Cutkosky 16 Classes**        | Combines manufacturing scenarios, tree-like hierarchy | Industrial assembly, fixture design | [Paper](https://www.researchgate.net/publication/3298011)                             |
| **Science Robotics 28 Classes** | Covers daily interaction and social handing           | Service robots, human-robot collaboration | [Paper](https://www.science.org/doi/10.1126/scirobotics.aau9757)                      |
| **GRASP 33 Classes**           | Unifies multiple standards, four-dimensional coding   | Academic research, general algorithms | [Paper](https://www.eng.yale.edu/grablab/pubs/Feix_THMS2016.pdf)                      |
| **Quantitative Comprehensive Classification** | Statistical + mechanical metric quantification        | Data-driven evaluation       | [Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC6377750/)                            |

> 💡 **Usage Suggestions**:
> - Industrial scenarios → Cutkosky system
> - Daily operations → Science Robotics or GRASP
> - Multi-level evaluation: Use Power/Precision for coarse level, use 28/33 classes for fine level

---

## 🔗 Related Links

-   **[Lumina Embodied AI Community](https://github.com/TianxingChen/Embodied-AI-Guide)** - Embodied AI Learning Guide

---

## 👥 About Us

### Contributors

**Core Members**: [Dehao Wei](https://scholar.google.com/citations?user=ZT8JOZEAAAAJ&hl=en), Tong Wu, [Chuanjun Guo](https://github.com/sen-code-lost), [Wensheng Wang](https://github.com/woltium), Qingquan Lin, Donglin Zhongsheng

<a href="https://github.com/Wu-Fisher/dexterity-aha-guide/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Wu-Fisher/dexterity-aha-guide" />
</a>

### Join Us

Welcome to promote, contribute, exchange, and collaborate!

- 📧 **Email**: wutfisher@outlook.com
- ⭐ **GitHub**: Give us a Star to let more people see it!
- 💬 **Issue**: Have suggestions or questions? Directly submit an [Issue](https://github.com/Wu-Fisher/dexterity-aha-guide/issues)

---

<div align="center">

**🌟 Star History 🌟**

[![Star History Chart](https://api.star-history.com/svg?repos=Wu-Fisher/dexterity-aha-guide&type=Date)](https://star-history.com/#Wu-Fisher/dexterity-aha-guide&Date)

---

*Code to Hand, Zero to Hero*

**Made with ❤️ by the Dexterity Manipulation Community**

</div>