# Motivation
在传统方法中，编码时我们将heatmap作为一种高斯概率分布，解码时却只利用了最大值信息。DARK-Pose认为模型预测出的heatmap应与ground truth有一致性，即假设预测出的heatmap也是一个高斯分布，我们应该利用整个分布的信息来进行keypoint的精确位置预测。具体地，通过泰勒二阶展开，我们可以预测从最大值点到真实keypoint的偏移。具体推导见论文。
![](../Data/darkpose2.png)

# Contribution

进一步探讨了现有方法中广泛使用的标准坐标译码方法的设计局限性，
（1）提出了一种更有原则的分布式感知译码方法，基于泰勒展开的高效坐标解码，
（2）我们通过为无偏模型训练生成精确的热图分布来改进标准坐标编码过程

把这两个创新点结合起来，formulate了一种新的基于分布感知的关键点坐标表示方法（Distribution-Aware Coordinate Representation for Human Pose Estimation）(DARK) 。


---




## 编码
## 解码

![](../Data/darkpose1.png)
整个解码过程如上图所示，其中第一步就是将预测出的heatmap进行平滑(使用与编码时相同的高斯核)，消除真值附近的多个峰值；第二步是根据分布信息预测偏移；第三步是恢复到原图尺度。


---
https://blog.csdn.net/weixin_43916755/article/details/105731954