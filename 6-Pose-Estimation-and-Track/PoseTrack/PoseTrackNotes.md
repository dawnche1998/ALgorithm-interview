# Pose Track 

## 1. Datasets

- PoseTrack [Paper](http://openaccess.thecvf.com/content_cvpr_2018/papers/Andriluka_PoseTrack_A_Benchmark_CVPR_2018_paper.pdf) [Address](https://posetrack.net/) 

---

## 2.  PoseTrack Papers

### 2.1 ReID method

1. **FastPose: Towards Real-time Pose Estimation and Tracking via Scale-normalized Multi-task Networks [Paper](https://arxiv.org/pdf/1908.05593.pdf)**

2. **2019 CVPR - LightTrack: A Generic Framework for Online Top-Down Human Pose Tracking  [Paper](https://arxiv.org/pdf/1905.02822.pdf) [Code](https://github.com/Guanghan/lighttrack)** 

   提出了SGCN作为一个ReID模块进行姿势跟踪。

   - SGCN提取的特征具有人体姿势的相关性，并且具备可解释性。并且在边界框有很强的关系，对边界框有直接的强制约束。
   - 通过使用人体关键点可以更好的进行跟踪，得到ROI区域。
   - 保证了候选区域之间的区分度，可以使用姿势特征做基于骨架的姿势匹配。
   
3. **15 Keypoints Is All You Need (2019) [Paper](https://arxiv.org/abs/1912.02323)**

### 2.2 时空关系

1. **2017 ICCV - Global Pose Refinement using Bidirectional Long-Short Term Memory [Paper](https://posetrack.net/workshops/iccv2017/pdfs/MPR.pdf)**
2. **JointFlow: Temporal Flow Fields for Multi Person Pose Tracking [Paper](https://arxiv.org/abs/1805.04596)**
3. **2018 ECCV - Learning to Detect and Track Visible and Occluded Body Joints in a Virtual World  [Paper](http://openaccess.thecvf.com/content_ECCV_2018/papers/Matteo_Fabbri_Learning_to_Detect_ECCV_2018_paper.pdf)**
4. **2019 CVPR - Multi-person Articulated Tracking with Spatial and Temporal Embeddings [Paper](https://arxiv.org/pdf/1903.09214.pdf)**
5. **2019 CVPR - Efficient online multi-person 2d pose tracking with recurrent spatio-temporal affinity fields [Paper](https://arxiv.org/pdf/1811.11975.pdf) [Code](https://github.com/soulslicer/openpose)**
6. **Pose estimator and tracker using temporal flow maps for limbs [Paper](https://arxiv.org/pdf/1905.09500.pdf)**

### 2.3 GNN图卷积

**2021.06_Learning Dynamics via Graph Neural Networks for Human Pose Estimation and Tracking**

### 2.4 结合光流

1. **2014.09_MoDeep-A Deep Learning Framework Using Motion Features for Human Pose Estimation**
2. **2015.11_Flowing ConvNets for Human Pose Estimation in Videos**
3. **Simple Baselines for Human Pose Estimation and Tracking(2018 ECCV): Optical Flow [Code](https://github.com/microsoft/human-pose-estimation.pytorch)**
4. **2020.10_A Simple Baseline for Pose Tracking in Videos of Crowded Scenes**
5. **2020.10_Towards Accurate Human Pose Estimation in Videos of Crowded**

### 2.5 结合 LSTM

**2018.03_LSTM Pose Machines**

### 2.6 自监督

**2021.03_Self-supervised Keypoint Correspondences for Multi-Person Pose Estimation and Tracking in Videos**

### 2.7 Transformer

**2020.03_(KeyTrack) 15 Keypoints Is All You Need**



### Others

1. **Movement science needs different pose tracking algorithms [Paper]**
   **2016.04_A Framework for Human Pose Estimation in Videos**
   
2. **Towards Multi-Person Pose Tracking: Bottom-up and Top-down Methods(2017 ICCV) [Paper](https://posetrack.net/workshops/iccv2017/pdfs/BUTD.pdf)**

3. **PoseTrack: Joint Multi-Person Pose Estimation and Tracking(2017 CVPR) [Paper](https://arxiv.org/pdf/1611.07727.pdf)** 

4. **Arttrack: Articulated multi-person tracking in the wild(2017 Arxiv)[Paper](https://arxiv.org/abs/1612.01465.pdf)**

5. **2018.04_Learning to Refine Human Pose Estimation**

6. **Detect-and-Track: Efficient Pose Estimation in Videos(2018 CVPR): [Paper](http://openaccess.thecvf.com/content_cvpr_2018/papers/Girdhar_Detect-and-Track_Efficient_Pose_CVPR_2018_paper.pdf) [Code](https://github.com/facebookresearch/DetectAndTrack/)**

7. **2018.06_(JointFlow) Temporal Flow Fields for Multi Person Pose Tracking**

8. **Pose Flow: Efficient Online Pose Tracking(2018 BMVC) [Paper](https://arxiv.org/pdf/1802.00977.pdf) [Code](https://arxiv.org/abs/1802.00977)**

9. **2018.10_Multi-Domain Pose Network for Multi-Person Pose Estimation and Tracking**

10. **2019.01_A Top-down Approach to Articulated Human Pose Estimation and Tracking**

11. **2019.02_(HRNet) Deep High-Resolution Representation Learning for Human Pose Estimation**

12. **2019.05_Pose estimator and tracker using temporal flow maps for limbs**

13. **2019.06(STAF) Efficient Online Multi-Person 2D Pose Tracking with Recurrent Spatio-Temporal Affinity Fields**

14. **2019.08(FastPose) Towards Real-time Pose Estimation and Tracking via Scale-normalized Multi-task Networks**

15. **2019.10(POINet) Pose-Guided Ovonic Insight Network for Multi-Person Pose Tracking**

16. **2019.11(mm-Pose) Real-Time Human Skeletal Posture Estimation using mmWave Radars and CNNs**

17. **2020.01(UniPose) Unified Human Pose Estimation in Single Images and Videos**

18. **2020 CVPR - Combining detection and tracking for human pose estimation in videos  [Paper](https://arxiv.org/pdf/2003.13743.pdf)**

    Top-down 方法

    ![](D:\CheXiaoTong\lihang-code-master\Algorithm-Interview\Data\Combining1.png)

19. **2020.07_Key Frame Proposal Network for Efficient Pose Estimation in Videos**

20. **2021.03(OpenPifPaf) Composite Fields for Semantic Keypoint Detection and Spatio-Temporal Association**

21. **2021.01_Iterative Greedy Matching For 3D Human Pose Tracking From Multiple Views**

22. **2021.07_Do Different Tracking Require Different Appearance Models**

23. **2021.07_Relation-Based Associative Joint Location for Human Pose Estimation in Videos**

---

## 3. 评价指标

- **MOTA**
- **mAP**

---

**Refer**

> [A 2019 guide to Human Pose Estimation with Deep Learning](https://nanonets.com/blog/human-pose-estimation-2d-guide/?utm_source=reddit&utm_medium=social&utm_campaign=pose&utm_content=GROUP_NAME)
>
> https://blog.csdn.net/qq_42974561/article/details/108091561