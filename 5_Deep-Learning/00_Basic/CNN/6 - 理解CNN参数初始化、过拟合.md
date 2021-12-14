可视化理解 CNN
=========

1.  保存层级的网络结构。
2.  不同层级有不同形式运算和功能。  
    ![](https://img-blog.csdnimg.cn/20191106211725326.png#pic_center)  
    ![](https://img-blog.csdnimg.cn/20191106211734277.png#pic_center)  
    ![](https://img-blog.csdnimg.cn/20191106211745983.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)  
    ![](https://img-blog.csdnimg.cn/20191106211805695.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)  
    ![](https://img-blog.csdnimg.cn/20191106211815175.png#pic_center)

CNN 优缺点
=======

**优点**

1.  局部感知的共享卷积核，轻松处理高维参数。
2.  特征属性不敏感，特征值通过训练权重得到。
3.  通过深层次的网络，可以抽取更丰富的图像信息，具有更好的表达效果。

**缺点**

1.  需要调参和大量样本，训练迭代次数较多，使用 GPU 训练最佳。
2.  物理含义不明确，很难从每层输出看出含义。

参数初始化
=====

**CNN 中，神经元之间的连接通过权重ω和偏置 b 实现，且ω、b 的取值直接影响模型训练速度和训练精度。**

权重的初始化
------

**建议方式：** 随机数很小。多层深度神经网络中，值太小导致回传梯度很小。

1.  服从均值为 0，方差较小的高斯分布随机数列。2/n，n 为权重数量。
2.  Xavier 服从均匀分布的随机数列。

**错误方式：**

全部初始化为 0，即全部设置为 0，在反向传播时梯度值一样，导致网络权重无法差异化，就无法学习到东西。

**注意：**

1.  Weight Standarization 即权重ω标准化，类似批归一化，是对权重系数做标准化操作，让模型效果更好。
2.  卷积和 FC 操作前，对ω做标准化操作。卷积操作中以每个卷积核为单位计算均值 μ 和标准差 σ 。
3.  FC 操作时，以当前层次的所有权重为单位计算均值 μ 和标准差 σ 。

偏置项的初始化
-------

一般直接设为 0，网络中存在 RLU 激活函数时，可以设为一个很小的正数。

Xavier
------

![](https://img-blog.csdnimg.cn/2019110621380283.png#pic_center)  
nj：输入维度数目。 nj+1：输出维度数目。

过拟合
===

![](https://img-blog.csdnimg.cn/20191106213912251.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)

---

# Pytorch 网络参数初始化

## 初始化时间

### 1. 使用 `self.modules` ，声明网络时初始化并加载权重

pytorch 模型应是 nn.Module 的子类
self.modules: nn.Module类中的一个方法, 返回该网络中的所有 modules

可以利用self.modules 来对网络进行初始化。

```python
class Network(nn.Module):
	def __init__(self):
		supe().__init__()
		self.Conv2d = nn.Conv2d(3, 10)
		sefl.bn = nn.BatchNorm2d(10)
		self.relu = nn.ReLU()
		self._init_weight()  #在初始化网络时, 会执行该函数,然后初始化网络中的每个module
		
	def forward(self, x):
		x = self.Conv2d(x)
		x = self.bn(x)
		return self.relu(x)
		
	def _init_weight(self):
		for m in self.modules()   #继承nn.Module的方法
			if isinstance(m, nn.Conv2d):
				torch.nn.init.kaiming_normal_(m.weight)
			elif isinstance(m, nn.BatchNorm2d):
				m.weight.data.fill_(1)
				m.bias.data.zero_()

```

### 2. 先定义网络，后加载权重, 使用`net.apply()`

```python
import torch.nn as nn

class NET(nn.Module):  # 声明网络
'''
 定义网络层
'''
net = NET()  # 定义网络

def weight_init(m):  #初始化权重
    if isinstance(m, nn.Conv3d):
        n = m.kernel_size[0] * m.kernel_size[1] * m.kernel_size[2] * m.out_channels
        m.weight.data.normal_(0, math.sqrt(2.0 / n))
        m.bias.data.zero_()
    elif isinstance(m, nn.BatchNorm3d):
        m.weight.data.fill_(1)
        m.bias.data.zero_()
    elif isinstance(m, nn.Linear):
        m.weight.data.normal_(0, 0.02)
        m.bias.data.zero_()
        
net.apply(weight_init)  # 加载权重

```

---

## 初始化方法

### kaiming 正态分布

`torch.nn.init.kaiming_normal_(tensor, a=0, mode=‘fan_in’, nonlinearity=‘leaky_relu’)` 

### kaiming 均匀分布

`torch.nn.init.kaiming_uniform_(tensor, a=0, mode=‘fan_in’, nonlinearity=‘leaky_relu’)`

---

详细参数参考官方文档：[TORCH.NN.INIT](https://blog.csdn.net/shanglianlm/article/details/85165523)

[pytorch中的参数初始化方法总结](https://blog.csdn.net/ys1305/article/details/94332007?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link)

https://blog.csdn.net/goes_on/article/details/109097234

[PyTorch学习之十一种权重初始化方法](https://blog.csdn.net/shanglianlm/article/details/85165523)