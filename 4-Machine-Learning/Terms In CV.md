# Terms In CV

## 1 从分类器开始

### 图像分类

- 分类classify

	- 分类器classifier

- 方差

	- 类内方差 intra-class variance

		- 类内方差是指同一类物体之间的差异，类内方差越大，分类难度越大。例如上面的MNIST数据集中的所有“0”，虽然形态各异，但是差异较小，而上面Cifar-10数据集中的所有“猫”，因为品种、毛色等等方面的区别，就体现出较大的类内差异。显然后者较前者的类内方差更大，完成后者的分类的难度要高于前者。

	- 类间方差 inter-class variance

		- 类间方差指的是不同类物体之间的差异，类间方差越大，分类难度越低。例如，区分“猫”和“房子”要比取分“猫”和“狗”要容易的多。

- 函数 function

	- 分类问题可以理解为让计算机解决类似于由“手写数字8的图片”到“标签8”的映射问题，而我们需要找出的就是完成这一映射的函数。

- 拟合 fit

	- 找到这个“函数”的过程我们通常称为拟合出这个函数。

- 数据驱动 data-driven

	- 让机器从数据中发现规则、规律，拟合出我们想要的函数，从而解决分类问题，而非使用手动的规则。

### 分类器入门

- 特征 feature

  要对图像进行分类，本质上是要通过图像的某些特征对图像进行判别。
  在王二狗的例子中，我们提取了他的三个特征：“高”、“帅”、“富”。

	- 初级特征(low-level feature)

		- 图像上最基础的特征就是初级特征，例如：圆弧、线等等。

	- 高级特征(high-level feature)

		- 高级特征是例如“有眼睛”、“有脸”、“有腿”这样的高层次显著特征

	- 手工设计的特征(hand-crafted feature)
	- 对象特征(Object-level features)

- 特征向量 feature vector

	- 将提取到的多个特征放在一起，就叫做特征向量。

- 特征工程 feature engineering

	- 找到特征的过程一般称为特征工程。

### 

- 可分 separable

	- 例如：我与王二狗是否有钱这一特征，是容易区分的，称之为可分；而让机器看长得一模一样的双胞胎照片，则缺乏能够将二者取分开来的特征，称之为不可分。能否找到足够的特征让机器能够完成分类是十分关键的一点。

- 特征提取 feature extraction

	- 将特征提取出来的过程。深度学习可以自动完成这一过程。

- 特征学习 feature learning

	- 深度学习具备自动完成特征提取，称其为具备特征学习的能力。

- 表示学习 representation learning

	- 用数字/向量/矩阵等方法来表达现实世界中的物体，而且这种表达方式有利于后续的分类或者其他决策问题。

## 2 神经网络基本组成单元

### 神经元 neuron

- 输入 input
- 连接权重 weights
- 输出 output

### 激活函数 activation function

- Sigmoid
- ReLU
- TanH

### 加权和 weighted sum

### 偏置 bias

- 如果将加权和再加上一个常数项b，则这个常数项就称为偏置。

### 层 layer

- 全连接层 fully-connected layer
- 隐含层(hidden layer)
- 输入层(input layer)
- 输出层(output layer)

### 非线性(non-linearity)

### 线性可分(linearly seperable)

## 3 卷积神经网络 CNN

### 卷积(convolution)

- 卷积层 CNN layer 
- 卷积核(kernel)
- 滤波器(filter)
- 特征图(feature map)

### 反卷积

### 池化/采样(pooling)

- 池化层/降采样层 Pooling layer
- 降采样/下采样(down sampling)
- 平均池化(average pooling)
- 最大池化(max pooling)
- 平移不变性(translation invariant)

### 卷积/池化层的参数

- 核尺寸(kernal size)
- 感受野(receptive field)
- 步幅(stride)
- 填充(padding)
- 深度(depth)

	- 实际上是三维的

### softmax

- 独热编码(one hot encoder)
- 概率分布(probability distribution)
- SoftMax

### 批标准化层

- 批标准化(batch normalization)
- 正则化(regularizer)

### 经典网络 VGG

### Batch normalization

### 更多网络 

- 更深的RetNet

	- 残差(residual)
	- 跨层连接(skip connection)

- 更宽的GoogleNet

	- 串接(concatenation)
	- GoogLeNet
	- Inception

### 局部性(locality)

- 从人脑的结构出发，研究证明，人脑中的神经元不会与之前的所有的神经元相连接，例如，初级视皮层上的神经元不会与视网膜上的每一个神经元，而是V1上的每一个神经元只看到视网膜上的一小部分。

## 6 前沿方向

### 目标检测(object detection)

### 语义分割(semantic segmentation)

### 实例分割(instance segmentation)

## 5 神经网络训练

### 训练(train)

### 预测(inference)

### 真值(ground truth)

### 损失函数(lost function)

### 成本函数(cost function)

### 前向传播(forward propagation)

### 反向传播(back propagation)

- 局部极小值(local minimum)
- 全局最小值(global minimun/absolute minimum)
- 随机梯度下降(SGD)
- 冲量(momentum)
- 学习率(learning rate)
- 学习率衰减(learning rate decay)

### 导数(derivative)

- 链式求导法则(chain rule)

### 梯度下降(gradient descent)

- 梯度消失(gradient vanishing)
- 梯度爆炸(gradient exploding)

## 4 让深度学习工作起来

### 模型参数(model parameters)

### 过拟合(overfitting)

- Dropout
- Noise

### 泛化能力(generalization)

### 核弹厂(NVidia)

