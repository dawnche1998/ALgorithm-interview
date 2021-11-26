局部关联：每个神经元看作一个 filter / kernal；

窗口滑动，filter 对局部数据进行计算；

深度 depth、步长 stride、填充值 zero-padding。

# 人的大脑识别图片过程

1. 由不同皮质层处理不同方面数据：颜色、形状、光暗等。
2. 将不同皮质层处理结果进行合并映射操作。
3. 得出最终结果值。   前面实质是局部观察结果，后面是整体合并结果。   ![img](https://img-blog.csdnimg.cn/20191103081548572.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)   ** 局部感知：** 图像的空间联系只是局部的像素联系较紧密，远距离像素相关性弱，所以每个神经元没有必要对全局像素感知。对局部感知，在更高层次对局部信息进行综合操作得出全局信息。   **卷积理解**![img](https://img-blog.csdnimg.cn/20191103131156553.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)

# 全连接特征

![img](https://img-blog.csdnimg.cn/20191103131323345.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)   **卷积计算层演示**   ![img](https://img-blog.csdnimg.cn/20191103131401175.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)   原图像大小：8×8；窗口大小：3×3；步长：1；新图像大小：6×6。   ![img](https://img-blog.csdnimg.cn/20191103131419382.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)   ![img](https://img-blog.csdnimg.cn/20191103131718771.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)   ![img](https://img-blog.csdnimg.cn/2019110313173213.png#pic_center)   ![img](https://img-blog.csdnimg.cn/20191103131744310.png#pic_center)   ![img](https://img-blog.csdnimg.cn/20191103131802681.png#pic_center)   ![img](https://img-blog.csdnimg.cn/20191103131812383.png#pic_center)   ![img](https://img-blog.csdnimg.cn/20191103131826706.png#pic_center)   ![img](https://img-blog.csdnimg.cn/20191103131848233.png#pic_center)   ![img](https://img-blog.csdnimg.cn/20191103131855994.png#pic_center)   ![img](https://img-blog.csdnimg.cn/20191103131904228.png#pic_center)   新图像元素结果 = 两窗口区域对应位置数据乘积和。

# RGB 图片输入卷积计算过程

**输入 RGB 图片时，输入的一个向量，三通道图片。**   ![img](https://img-blog.csdnimg.cn/20191103224516812.png#pic_center)   ![img](https://img-blog.csdnimg.cn/20191103224545312.png#pic_center)   ![img](https://img-blog.csdnimg.cn/20191103224554221.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)   ![img](https://img-blog.csdnimg.cn/20191103224605595.png#pic_center)   ![img](https://img-blog.csdnimg.cn/20191103224638167.png#pic_center)   ![img](https://img-blog.csdnimg.cn/20191103224646107.png#pic_center)   ![img](https://img-blog.csdnimg.cn/20191103224717911.png#pic_center)

1. 局部感知：计算时，将图片划分为一个个区域进行计算。
2. 参数共享机制：每个神经元连接数据窗的权重固定。
3. 滑动窗口重叠：降低窗口之间的边缘不平滑特性。
4. 固定每个神经元的连接权重，将神经元看成一个模板（卷积核），即每个卷积核只关注一个特性。从而大大减少计算权重个数。
5. 卷积：一组固定的权重和窗口内数据做矩阵内积后求和的过程。

## 示例：卷积核

![img](https://img-blog.csdnimg.cn/20191103225641148.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)   ![img](https://img-blog.csdnimg.cn/2019110322590013.png#pic_center)   ![img](https://img-blog.csdnimg.cn/20191103225933968.png#pic_center)   ![img](https://img-blog.csdnimg.cn/20191103230011680.png#pic_center)   ![img](https://img-blog.csdnimg.cn/20191103230030202.png#pic_center)   ![img](https://img-blog.csdnimg.cn/20191103230143293.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)   原始输入一个 channel 的图像，分别做四个不同的卷积操作，输出得到四个 feature map 的结果。这四个 feature map 相当于从四个不同的角度去衡量 / 观测这个原始图像得到的特征信息。

![img](https://img-blog.csdnimg.cn/20191103230355528.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)   ![img](https://img-blog.csdnimg.cn/20191103230434146.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQwNzY2OA==,size_16,color_FFFFFF,t_70#pic_center)