# ResNet

![](..\..\..\Data\ResNet2.png)


---
ResNet 改善梯度消失的问题：
$$
\frac{\partial f(g(x))}{\partial x} = \frac{\partial f(g(x))}{\partial g(x)} \frac{\partial g(x)}{\partial x}
$$
$$
\frac{\partial (f(g(x)) + g(x))}{\partial x} = \frac{\partial f(g(x))}
{\partial g(x)} \frac{\partial g(x)}{\partial x} + \frac{\partial g(x)}{\partial x}
$$
