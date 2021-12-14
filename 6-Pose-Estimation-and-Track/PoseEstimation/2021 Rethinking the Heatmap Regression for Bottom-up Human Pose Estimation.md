本文提出了自适应调整尺度和热力图权重的方法，解决了人体姿态估计（Human Pose Estimation）自底向上（Bottom Up）方法中对于标签生成使用固定的假设$$sigma$$所带来的问题。

---


本文针对
应该有不同的kernel size 的高斯核
新增一个分支预测 scale map s, which are of the shape with ground-truth heatmap.

尺度自适应heatmap回归的名称为**SAHR**（scale-adaptive heatmap regression），权重自适应heatmap回归的名称为**WAHR**（weight-adaptive heatmap regression）

# SAHR


# WAHR
