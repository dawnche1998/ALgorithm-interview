# Pose Estimation

## 1. Dataset
- **COCO keypoints**
- **MPII**
- **PoseTrack**
## 2. Evaluation Metrics
- **mAP** (最常用) 参考 [这里](http://blog.sina.com.cn/s/blog_9db078090102whzw.html)  和 [average precision](https://sanchom.wordpress.com/tag/average-precision/)
- **PCKh** ：以头部长度(头部gt bbox的对角线长度的60%)的某个比例为参考。PCKh@0.5是目前常用的评价指标。
- **OKS** (Commonly used in the COCO keypoints ) 通过OKS取不同阈值，可计算AP和mAP
- **PDJ  (Percentage of Detected Joints)** A detected joint is considered correct if the distance between the predicted and the true joint is within a certain fraction of the torso diameter. PDJ@0.2 = distance between predicted and true joint < 0.2 * torso diameter.
- **PCP (Percentage of Correct Parts)** 逐渐被弃用

## 3. 组成
- 3.1 backbones

## 4. Multi-person Pose Estimation (2D) Papers
### 4.1 top - down

>缺点：1）detection阶段遗漏的目标人无法恢复 2）运行时间与人数正相关 3）对位置相近的人表现较差

1. Mask RCNN, ICCV2017
2. **Cascaded Pyramid Network for Multi-Person Pose Estimation, CVPR2018**
3. **A coarse-fine network for keypoint localization, ICCV2017**
4. **RMPE: Regional Multi-Person Pose Estimation, ICCV2017**
5. **Rethinking on Multi-Stage Networks for Human Pose Estimation, Arxiv2019**
6. **Simple Baselines for Human Pose Estimation and Tracking, ECCV2018**
7. **Spatial Shortcut Network for Human Pose Estimation, Arxiv2019**

### 4.2 bottom - up

> Bottom-Up的思路就是，先检测出图像中所有的关节点，然后对这些关节点分组，以此构成每个人体的完整姿态结果。Bottom-Up的方法相比较于Top-Down的方法，不容易受到图片中人数的影响，性能上，虽然还比不过Top-Down的方法，但差距已经没有之前那么大了。

1. **2017 CVPR - OpenPose: Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields**
2. **2017 NIPS - Associative embedding End-to-end learning for joint detection and grouping**
3. **2018 ECCV - MultiPoseNet: Fast Multi-Person Pose Estimation using Pose Residual Network**
4. **2018 ECCV - PersonLab: Person Pose Estimation and Instance Segmentation with a Bottom-Up Part-Based Geometric Embedding Model**
5. **2016 DeepCut / DeeperCut**
6. **PPN**
7. **PiPafNet**
5. **2019 Arxiv - Object as Points** [[2020 CenterNet]]
6. **2020 CVPR - Higher HRNet**
7. Mid-range Offset
8. 


### 4.3 one-stage net

1. 2017 heatmap and  associative embedding maps
2. **2019.08 Single-Stage Multi-Person Pose Machines**
3.  **2019.11(DirectPose) Direct End-to-End Multi-Person Pose Estimation**
4.  **2021.05(FCPose) Fully Convolutional Multi-Person Pose Estimation with Dynamic Instance-Aware Convolutions** [[2021 FCPose]]
5. **2021.07(InsPose) Instance-Aware Networks for Single-Stage Multi-Person Pose Estimation**
6. **2021.07(PoseDet) Fast Multi-Person Pose Estimation Using Pose Embedding**

### 4.4 多任务学习 

1. **2018.01_Mask R-CNN **
2. **2018.03_(PersonLab) Person Pose Estimation and Instance Segmentation with a Bottom-Up, Part-Based, Geometric Embedding Model **
3. **2019.05_Multi-task human analysis in still images-2D_3D pose, depth map, and multi-part segmentation **
4. **2021.08_MultiTask-CenterNet (MCN)-Efficient and Diverse Multitask Learning using an Anchor Free Approach**

### 4.5 无监督

### 4.6 GAN 

1. **2017.05_Adversarial PoseNet-A Structure-aware Convolutional Network for Human Pose Estimation**
2. **2017.08_Self Adversarial Training for Human Pose Estimation**
3. **2021.05_When Human Pose Estimation Meets Robustness-Adversarial Algorithms and Benchmarks**

### 4.7 图网络 

1. **2019.01_Human Pose Estimation with Spatial Contextual Information**
2. **2020.03_Peeking into occluded joints A novel framework for crowd pose estimation**
3. **2020.07_Graph-PCNN-Two Stage Human Pose Estimation with Graph Pose Refinement**

### 4.8 Backbone 

1. 2019 (HRNet) Deep High-Resolution Representation Learning for Human Pose Estimation一种高分辨率的backbone，更好提取热图
2. 2020 (RSN) Learning Delicate Local Representations for Multi-Person Pose Estimation 更好的利用各个尺度的信息。

### 4.9 使用Transformer 

1. **2020.12_(TransPose) Towards Explainable Human Pose Estimation by Transformer**
2. **2021.03_(TFPose) Direct Human Pose Estimation with Transformers**
3. **2021.04_Pose Recognition with Cascade Transformers**

### 4.10 Super Resolution

### 4.11 Refinement 

1. **2019.03_PoseFix-Model-agnostic General Human Pose Refinement Network 提出了一种精细网络用于精细姿态结果，是一个插件，后处理方式。**
2. **2019.10_(DARK) Distribution-Aware Coordinate Representation for Human Pose Estimation**
3. **2021.07_Polarized Self-Attention-Towards High-quality Pixel-wise Regression**
4. **2021.07_Adaptive Dilated Convolution For Human Pose Estimation**

### 4.12 轻量化 

1. **2019.04_Fast Human Pose Estimation**
2. **2020.01_Simple and Lightweight Human Pose Estimation**
3. **2021.07_(FasterPose) A Faster Simple Baseline for Human Pose Estimation**

### 4.13 其他 

1. **2018.05_Jointly Optimize Data Augmentation and Network Training: Adversarial Data Augmentation in Human Pose Estimation 使用优化的训练技巧提升精度。** #DL/trick 
2. **2019.04_Spatial Shortcut Network for Human Pose Estimation**
3. **2019.05_Multi-Person Pose Estimation with Enhanced Channel-wise and Spatial Information**
4. **2019.10_TRB: A Novel Triplet Representation for Understanding 2D Human Body**
5. **2020.01_(UniPose) Unified Human Pose Estimation in Single Images and Videos**
6. **2020.02_Towards High Performance Human Keypoint Detection**
7. **2020.02_Toward fast and accurate human pose estimation via soft-gated skip connections**
8. **2020.12_The Devil is in the Details-Delving into Unbiased Data Processing for Human Pose Estimation**
9. **2020.12_Efficient Human Pose Estimation by Learning Deeply Aggregated Representations**
10. **2020.12_(EfficientPose) Scalable single-person pose estimation 相比openpose，提出准确又快速的模型（但是实际效果很差）**
11. 2021.07_Is 2D Heatmap Representation Even Necessary for Human Pose Estimation
12. Rethinking the Heatmap Regression for Bottom-up Human Pose Estimation [[2021 Rethinking the Heatmap Regression for Bottom-up Human Pose Estimation]]