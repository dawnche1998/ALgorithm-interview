
> 受光照、模型参数量、输入尺寸、模型泛化能力、数据增强等因素影响，轻量的关键点定位模型（姿态估计、检测、关键点识别等）在实际应用部署中，输出的结果常常会出现抖动，不利于我们进行一些比较精细的判定。除了优化模型以外，在工程上我们其实还可以通过后处理的方式，简单快捷地提升小模型的稳定性，这篇文章介绍一种简单的方式——指数滑动平均，能够快速应用到实际的项目工程中。

1. 原理
---------

所谓的” 指数滑动平均 “，说白了其实就是**多次测量取平均值**，我们的问题在于，对于相同的输入，模型的输出是不会变的，而画面轻微的改变（有时候甚至是摄像头噪点）却导致了输出结果的明显抖动。

一个比较朴素的想法是设置一个滑动窗口，比如将相邻的几帧图片一起送入模型，对结果取平均值，这样的确也符合多次测量取平均的思想，但问题在于我们将不得不保存很多帧的结果，这在实现上是不高效的。

解决的方法也很简单，通过数学公式的推导，我们可以将上面的实现简化为递归算法的形式，每次只需要保留上一帧的计算结果：

![](https://pic4.zhimg.com/v2-356d6dcf090960037b9f56c869b3ee3b_r.jpg)

经过变换，我们每一帧的预测结果变为了只需要在上一帧的基础上作出一点变动，而这里的 1/k 可以看成我们滑动窗口的大小导致的延迟系数，当然它还有一个更牛逼的名字，叫卡尔曼增益，当有多个结果希望进行数据融合得到一个更可信的预测时，卡尔曼滤波是非常好用的手段，但对于我们的姿态模型来说，目前只有单个轻量模型的输出，因此并不需要用到完整的卡尔曼滤波，只需要实现一个简易的滑动滤波即可。

如果有同学对卡尔曼滤波有兴趣，可以参考这个视频，以上图片也是来自于此：

2.  代码实现
-----------

这里给出我自己用 python 实现的指数滑动均值滤波：

```python
class ExponentialMovingAverage:
    def __init__(self, alpha):
        self.alpha = alpha
        self.cur = None

    def add(self, v):
        if self.cur is None:
            self.cur = v
        else:
            self.cur = self.cur * (1-self.alpha) + v * self.alpha
        return self.cur
    def get(self):
        return self.cur

class Point:
    def __init__(self, alpha):
        self.x = ExponentialMovingAverage(alpha)
        self.y = ExponentialMovingAverage(alpha)
        self.z = ExponentialMovingAverage(alpha)

    def add(self, pt):
        return (int(self.x.add(pt[0])), int(self.y.add(pt[1])), int(self.z.add(pt[2])))

class KFJointCoord:
    def __init__(self, alpha):
        self.jc = [Point(alpha) for i in range(21)]

    def update(self, jc):
        for i, pt in enumerate(jc):
            self.jc[i].add(pt)
    def tolist(self):
        jc_list = []
        for pt in self.jc:
            jc_list.append([pt.x.get(), pt.y.get(), pt.z.get()])
        return jc_list
```

实际应用中可以每一帧用模型的输出来更新这个类的成员变量：

```python
joint_coord = KFJointCoord(0.85)
preds = model(inputs)
joint_coord.update(preds)
print(joint_coord.tolist())
```
---
## refer 
https://zhuanlan.zhihu.com/p/433571477

https://blog.csdn.net/Yong_Qi2015/article/details/121433816 轻量级技巧