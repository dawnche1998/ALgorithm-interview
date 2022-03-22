**heatmap - based**

Heatmap-based 方法监督模型学习的**高斯概率分布图**，把 GroundTruth 中每个点渲染成一张高斯热图，最后网络输出为K张特征图对应 K 个关键点，然后通过 argmax 或 soft-argmax 来获取最大值点作为估计结果。这种方法由于需要渲染高斯热图，且由于热图中的最值点直接对应了结果，不可避免地需要维持一个相对高分辨率的热图（常见的是64x64，再小的话误差下界过大会造成严重的精度损失），因此也就自然而然导致了很大的计算量和内存开销。

基于关键点回归的几个工作：

- CenterNet [[2020 CenterNet]]
- FCOS 
- Direct Pose - [KPAlign模块](https://blog.csdn.net/qiu931110/article/details/104433832?spm=1001.2101.3001.6650.7&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-7.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-7.pc_relevant_default&utm_relevant_index=10)（关键点对齐） 
- DEKR [[2021 DEKR]]
- MTCNN
- [ Bottom-Up Human Pose Estimation by Ranking Heatmap-Guided Adaptive Keypoint Estimates](https://blog.csdn.net/qq_19784349/article/details/108997395) 



**regression - based**

Regression-based 方法，直接监督模型学习坐标值，计算坐标值的 L1或L2 loss。由于不需要渲染高斯热图，也不需要维持高分辨率，网络输出的特征图可以很小（比如14x14甚至7x7），例如Resnet-50，FLOPs 是 Heatmap-based 方法的两万分之一，这对于计算力较弱的设备（比如手机）是相当友好的，在实际的项目中，也更多地是采用这种方法。

**优点**

- 没有高分辨率热图，计算成本和内存开销比 heatmap 大幅降低。
- 输出为连续的，不用担心量化误差。（Heatmap-based输出的热图最大值点在哪，对应到原图的点也就确定了，输出热图的分辨率越小，这个点放大后对应回去就越不准。Regression-based输出为一个数值，小数点后可以有很多位，精度不受缩放影响）
- 可拓展性高。不论是one-stage还是two-stage，image-based还是video-based，2D还是3D，Regression-based方法都可以一把梭。此前就有用这种方法来将2D和3D数据放在一起联合训练的文章。这是Heatmap-based方法做不到的，因为输出是高度定制化的，2D输出必须渲染2D高斯热图，3D就必须渲染3D的高斯热图，计算量和内存开销也答复增大。

  而Heatmap-based方法通过显式地渲染高斯热图，让模型学习输出的目标分布，也可以看成模型单纯地在学习一种滤波方式，将输入图片滤波成为最终希望得到的高斯热图即可，极大地简化了模型的学习难度，且非常契合卷积网络的特性（卷积本身就可以看成一种滤波），并且这种方式规定了学习的分布，相对于除了结果以外内部一切都是黑盒的Regression-based方法，对于各种情况（遮挡、动态模糊、截断等）要鲁棒得多。基于以上种种优点，Heatmap-based方法在姿态估计领域是处于主导地位的，SOTA方案也都是基于此，这也导致了一种学术研究与算法落地的割裂。


---

## 一、数据增强

1. **正确归一化**
将坐标值归一化到(-0.5, 0.5)之间，公式为（-0.5，0.5）之间：由于目标检测的关系，姿态估计的对象大都会在图像的中央，用这样的归一化能很大的加速模型收敛。

2. **Augmentation by Information Dropping(AID)**
2020 COCO Keypoint Challenge 冠军之路 
地址：https://zhuanlan.zhihu.com/p/210199401
这是COCO2020 冠军团队的论文。作者认为在姿态估计任务中，模型会使用两种信息：外观信息和约束信息。外观信息是定位关键点的基础，而约束信息则在定位困难关键点时具有重要的指导意义。约束信息包括人体关键点之间固有的相互约束关系（如人体关节的活动度），以及人体和环境交互形成的约束关系。直观上看，约束信息相比于外观信息而言，更复杂多样，对于网络而言学习难度更大，这会使得在外观信息充分的情况下，存在约束条件被忽视的可能性（模型会偷懒，不学习/使用约束信息）。基于此假设，作者引入了信息丢失的正则化手段，通过在训练过程中以一定的概率丢失关键点的外观信息，以此避免训练过程拟合外观信息而忽视约束信息。

3. **heatmap**处理 

   - heatmap 平滑处理  DARK Pose [参考]( https://blog.csdn.net/qq_41614538/article/details/108799394) [[2020 DARK Pose]]
   - [UDP pose](https://blog.csdn.net/qq_41614538/article/details/108799394)  [[2020 UDP]]
   - 生成heatmap的方法 :[flow track](https://panjinquan.blog.csdn.net/article/details/108882816?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_antiscanv2&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_antiscanv2&utm_relevant_index=2)  [open pose](https://blog.csdn.net/m0_37477175/article/details/81236115?spm=1001.2101.3001.6650.5&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-5.pc_relevant_antiscanv2&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-5.pc_relevant_antiscanv2&utm_relevant_index=10)
   - 椭圆高斯核 
   - [CetnerNet 和 CornerNet中的Heatmap](https://zhuanlan.zhihu.com/p/388024445)

## 二、 网络结构

1. 更强的激活函数 https://github.com/CoinCheung/pytorch-loss
2. OKDHP和NetAug
OKDHP的全称是Online Knowledge Distillation for Efficient Pose Estimation，总体的思路是为要训练的轻量模型增加几个分支，每个分支都学跟原来模型一样的东西，每个分支可以跟原来的模型一样，也可以不一样，这样相当于同时训练了多个小模型，将结果进行集成。由于集成学习的思想，我们知道小模型集成后的结果往往是好于单个模型的，因此我们可以把集成的结果当成蒸馏中教师网络的输出，让小模型去逼近集成的结果。

3. 自适应卷积层/动态卷积层
	- [[2020  DY-CNN]]
	-  [[2021 FCPose]] 中使用动态卷积层
	- [[2021 DEKR]]
	-  Pixel-Adaptive Convolutional Neural Networks
	- TTFNet

## 三、损失函数

1. **dsnt**
2. **bone Loss**
3. **Automatic Weighted Loss**
4. **L1 Loss**
5. **RLE**
6. 改进 focal loss  https://www.zhihu.com/zvideo/1390808454307667968 一个是2020的G focal loss 另一个是2021 equalified focal loss [[2020 GFocal Loss]]

## 四、后处理

1. **卡尔曼增益：用指数滑动平均滤波来稳定轻量模型的输出**
	 [[Note - 用指数滑动平均滤波来稳定轻量模型的输出]]

---

## Refer

[轻量级姿态估计技巧综述](https://blog.csdn.net/Yong_Qi2015/article/details/121433816)

https://blog.csdn.net/qiu931110/article/details/104318641
