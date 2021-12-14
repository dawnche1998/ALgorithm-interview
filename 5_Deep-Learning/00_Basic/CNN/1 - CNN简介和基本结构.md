神经网络的结构
=======

神经网络分为输入层、中间层、输出层。如图：  
![](https://img-blog.csdnimg.cn/20191101074534655.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)

卷积神经网络
======

1.  Convolutional Neural Networks CNN：可以有效降低反馈（传统）神经网络的复杂性
2.   CNN 发展的重要方向：层次的增加，从而利用增加的非线性神经元得出目标函数的近似结构，同时得出更好的特征表达。但是也导致了网络整体复杂度增加，使网络更加难优化。很容易产生**模型过拟合 \ 模型退化**情况。
3.  主要层次：
    - 数据输入层（Input Layer）
    - 卷积计算层（CONV Layer）
    - 激励层（Activation Layer）
    - 池化层（Pooling Layer）
    - 全连接层（FC Layer）
    - 批归一化层（Batch Normalization Layer）可能有

数据输入层（Input Layer）
==================

类似神经网络 / 机器学习，输入数据需要进行**预处理**操作，原因：

1.  防止输入数据单位不一样，导致神经网络收敛速度慢、训练时间长。
2.  数据范围大的输入在模式分类中作用偏大，反之偏小。
3.  神经网络中存在的激活函数有值域限制，必须将网络训练的目标数据映射到激活函数值域。
4.  S 形激活函数在（-4,4）区间外很平缓，区分度太低。

### **常见三种数据预处理方式：**  

- 去均值（将输入数据的各个维度中心化到 0）  
- 标准化（将输入数据的各个维度的幅度标准化到同样范围）  
- PCA \ 白化（用 PCA 降维，即去掉特征与特征之间的相关性；在 PCA 基础上对转换后的数据每个特征轴上的幅度标准化为白化）

**去均值 & 标准化**  
![](https://img-blog.csdnimg.cn/20191103080854411.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)  
**PCA & 白化**  
![](https://img-blog.csdnimg.cn/20191103080957421.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)  
**数据特征预处理方法：** 去均值、归一化、标准化、区间缩放法。常用去均值和归一化。  
![](https://img-blog.csdnimg.cn/20191103081314880.png#pic_center)



