# 池化层（存在于连续的卷积层中间）

1. 主要功能：通过逐步减小表征的空间尺寸来减小参数量和网络中的计算，提取重要特征，删除冗余的噪音特征信息。
2. 池化层在每个特征图上独立操作。
3. 作用：压缩数据和参数量，减小过拟合。

## 压缩减少特征数量的两种策略

Max Pooling：最大池化，较普遍。   Average Pooling：平均池化。![img](https://img-blog.csdnimg.cn/20191104223346223.png#pic_center)

# FC 全连接层 

1. FC 层中的神经元连接之前层次的所有激活输出。
2. 两层之间所有神经元都有权重连接。
3. CNN 中，FC 层只出现在尾部。
4. CNN 结构：   ——INPUT   ——[[CONV -> RELU] * N - > POOL? ] * M   ——[FC -> RELU] * K   ——FC（Full Connection Layer）

# BN 层

1. 训练神经网络时，一般将输入样本的特征进行标准化处理，将数据变为均值为 0、标准差为 1 的高斯分布，或者范围在 0 附近的分布。
2. 若数据不进行预处理，样本特征分布过于分散，导致学习速度慢或者不能学习。
3. **较好的数据分布利于加快神经网络训练速度，得到更好效果。**   ![img](https://img-blog.csdnimg.cn/20191104224421103.png#pic_center)
4. 由于训练模型时模型参数更新，除了输入层外的每一层输入都在不断变化。所以在训练中间层时，称数据分布的改变为 Internal Covariate Shift。为解决训练过程中间层数据改变的状况，提出 BN 层。![img](https://img-blog.csdnimg.cn/20191104224859845.png#pic_center)
5. BN 层期望输出结果服从高斯分布，所以修正了神经元的输出。文章中建议放在卷积层 / FC 层后、激励层 / 池化层前，实际应用一般放激励层后。   ![img](https://img-blog.csdnimg.cn/20191104225343909.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)

## BN 训练步骤

1. 求解每个训练批次数据的均值。
2. 求解每个训练批次数据的方差。
3. 使用求得均值和方差对该批次数据做标准化处理，获得 0-1 分布。
4. 尺度变换和偏移：使用标准化之后的 x 乘γ（尺度因子）调整数值，再加β（平移因子）增加偏移从而得到输出值 y。   引入尺度因子和平移因子解决标准化后 x 基本被限制在正态分布下，导致网络表达能力下降问题。![img](https://img-blog.csdnimg.cn/20191105221747698.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)
5. 训练时采用一个批次中的样本的均值和标准差进行 BN 操作。但使用训练阶段所有批次记录的均值和方差的期望值作为预测阶段的 BN 均值和方差。
6. 实际应用中，采用类似 momentum 动量法中使用的滑动平均进行计算测试时的均值和方差。   ![img](https://img-blog.csdnimg.cn/20191105222724758.png#pic_center)   ![img](https://img-blog.csdnimg.cn/20191105222742401.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)

## BN 层优缺点

优点：

1. 梯度传递计算更顺畅，较少出现神经元饱和。
2. 设置较大的学习率加快训练速度。
3. 对模型参数的初始化方式和取值不敏感，稳固网络学习，提高模型训练精度。
4. 具有一定正则效果。

缺点：

1. 在网络层次深的模型中会减缓训练速度。
2. 训练批次建议 16 以上。

## 实例化

![img](https://img-blog.csdnimg.cn/20191105223159771.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)   第一个神经元 均值 1.65 ，方差 0.44 ，ε 1e-8。   ![img](https://img-blog.csdnimg.cn/20191105223801232.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)   第一层的输入 每个特征的分布 均值 0、标准差 1.

# 总结

1. CNN 特征对应到一个 feature map 特征图上。所以，CNN 中做 BN 不是以神经元为单位，以 feature map 特征图为单位。
2. 针对一个批次中的一个 channel 的所有 feature map 计算一对参数γ、β，从而减小模型的参数数目。
3. 已知：batch_size=8，feature map 大小 = 32×32，feature map 数量 = 10，得到：传统 BN 参数量 20480，CNN 中 BN 参数量 20.

