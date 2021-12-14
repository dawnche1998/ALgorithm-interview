激活层
===



## **梯度消失和梯度爆炸**
> https://blog.csdn.net/qq_27825451/article/details/80172070

梯度消失：参数更新过小，在每次更新时几乎不会移动，导致无法学习。

梯度爆炸：参数更新过大，破坏了模型的稳定收敛。

梯度消失和梯度爆炸问题都是因为网络太深，网络权值更新不稳定造成的，本质上是**因为梯度反向传播中的连乘效应**。对于更普遍的梯度消失问题，可以考虑一下三种方案解决：

1. 用 ReLU、Leaky-ReLU、P-ReLU、R-ReLU、Maxout 等非饱和得激活函数替代 sigmoid 函数。
2. 批量规范化 Batch Normalization。
2. 梯度截断 Gradient Clippiing
3. LSTM 的结构设计也可以改善 RNN 中的梯度消失问题。

---



激活层 Activation Function Layer：将卷积层的输出结果做一次非线性映射，即激活。  
![](..\..\Data\activationLayer.jpg)

> 常用非线性映射函数：Sigmoid(S 形函数)、Tanh(双曲正切，双 S 形函数)、ReLU、Leaky ReLU、ELU、Maxout。

Sigmoid 激活函数
------------

优点：取值范围（0，1）、简单、易理解； 
缺点：容易饱和和终止梯度传递，即死神经元；函数输出没有 0 中心化。![](https://img-blog.csdnimg.cn/20191104072729374.png#pic_center)  
![](https://img-blog.csdnimg.cn/20191104072750512.png#pic_center)

Tanh 激活函数
---------

优点：取值范围（-1,1）、易理解、0 中心化；  
缺点：容易饱和和终止梯度传递，即死神经元。

![](https://img-blog.csdnimg.cn/20191104072955190.png#pic_center)  
![](https://img-blog.csdnimg.cn/20191104073003153.png#pic_center)

ReLU 修正线性单元 函数
------------------------------------------

The Rectified Linear Unit

对于输出的 x 以 0 为分界线，左侧均为 0，右侧为 y=x。  
缺点：没有边界，可以使用变种 ReLU:min(max(0,x),6)；比较脆弱，容易陷入死神经元，可以通过较小学习率解决。 

> 解释：训练神经网络的时候，一旦学习率没有设置好，第一次更新权重的时候，输入是负值，那么这个含有ReLU的神经节点就会死亡，再也不会被激活。因为：ReLU的导数在x>0的时候是1，在x<=0的时候是0。如果x<=0，那么ReLU的输出是0，那么反向传播中梯度也是0，权重就不会被更新，导致神经元不再学习。
>
> 也就是说，这个ReLU激活函数在训练中将不可逆转的死亡，导致了训练数据多样化的丢失。在实际训练中，如果学习率设置的太高，可能会发现网络中40%的神经元都会死掉，且在整个训练集中这些神经元都不会被激活。所以，设置一个合适的较小的学习率，会降低这种情况的发生。为了解决神经元节点死亡的情况，有人提出了Leaky ReLU、P-ReLu、R-ReLU、ELU等激活函数

优点：比上述两个提升收敛速度；梯度求解公式简单，不会产生梯度消失和梯度爆炸。![](https://img-blog.csdnimg.cn/20191104073332987.png#pic_center)  
![](https://img-blog.csdnimg.cn/20191104073345197.png#pic_center)  
**ReLU 函数从生物学角度，模拟出脑神经元接受信号更加准确的激活模型。**  
![](https://img-blog.csdnimg.cn/2019110407351999.png#pic_center)  
**ReLU 函数对比 Sigmoid 函数的优点：**  

- 单侧抑制,输出不是 “零为中心”(Notzero-centered output)；  
- 相对宽阔的兴奋边界；  
- 稀疏激活性；  
- 更快的收敛速度。

Leaky ReLU 激活函数
---------------

为了解决 ReLU 激活函数中的死神经元问题，对 x ≤ 0 部分修正，但实际效果有限。Leaky ReLU 函数中的α，需要通过先验知识人工赋值。![](https://img-blog.csdnimg.cn/2019110407400352.png#pic_center)

ELU 激活函数
--------

指数线性激活函数：对 ReLU 激活函数 x ≤ 0 部分的转换进行指数修正，放弃线性修正。  缺点：计算的时候是需要计算指数的，计算效率低的问题。
![](https://img-blog.csdnimg.cn/20191104074240964.png#pic_center)

> 还有RReLU（Leaky ReLU的random版本）在训练过程中，α是从一个高斯分布中随机出来的，然后再测试过程中进行修正。
>
> 以及PReLU等

Maxout 激活函数
-----------

简介：类似在深度学习网络加入了一层激活函数层，包含参数 k，拟合能力很强。  
特殊点：增加 k 个神经元进行激活，再输出激活值的最大值。  
优点：计算简单，避免神经元饱和；很少出现死神经元。  
缺点：参数 double，计算量变复杂。  
![](https://img-blog.csdnimg.cn/20191104074538313.png#pic_center)  
![](https://img-blog.csdnimg.cn/20191104074756754.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)

激励层使用建议
-------

——CNN 尽量避免使用 sigmoid 激活函数，必须使用时最好只在全连接层使用。  
——首先使用 ReLU 激活函数，因为迭代速度快，虽然效果可能不佳。  
——如果 ReLU 激活函数失效，再使用 Leaky ReLU 或者 Maxout 激活函数，可以解决大部分场景。  
——Tanh 激活函数在部分情况下效果较好，但应用场景较少。