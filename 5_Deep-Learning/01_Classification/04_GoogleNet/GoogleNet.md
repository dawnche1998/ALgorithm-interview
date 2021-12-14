inception块：

用4条有不同超参数的卷积层和池化层的路来抽取不同的信息。

googlenet使用了9个inception块，是第一个达到上百层的网络。

使用不同窗口大小的卷积层
最后有一个Concatenation的连接操作，输出跟输入等同高和宽。
跟单 3x3 或 5x5卷积层对比，inception块用更少的参数个数和计算复杂度。

inception



![](..\..\..\Data\inception.svg)

inception 后续很多优化的版本

1. inception - BN(v2) - 使用 batch normalization

2. inception (v3) - 修改了 inception块

   替换 5×5 为多个 3x3卷积层

   替换5×5 为1×7和7×1卷积层

   替换3×3为1×3和3×1卷积层

   更深

3. inception(v4) - 使用残差连接
