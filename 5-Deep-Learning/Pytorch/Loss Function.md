# Loss Function

> 很多 loss 函数都有 `size_avarage` 和 `reduce` 两个布尔类型的参数，因为一般损失函数都是直接计算 batch 的数据，因此返回的 loss 结果都是维度为 (batch_size, ) 的向量。
>
> - 如果 reduce = 'sum'，那么 size_average 参数失效，直接返回向量形式的 loss；
> - 如果 reduce = 'mean'，那么 loss 返回的是标量
>   - 如果 size_average = True，返回 loss.mean();
>   - 如果 size_average = False，返回 loss.sum();

### nn.L1Loss

$$
loss (x_i, y_i) = \frac{1}{n}|x_i - y_i|
$$

```python
import torch
import torch.nn as nn
loss = nn.L1Loss()
input = torch.randn(3,5, requires_grad = True)
target = torch.randn(3,5)
output = loss(input, target)
output.backward()
print(f'{input}\n{output}\n{target}')
```

### nn.MSELoss 均方损失函数

$$
loss (x_i, y_i) = \frac{1}{n}\sum{(x_i-y_i)}^2
$$

``` python
loss = nn.MSELoss()
input = torch.randn(3, 5, requires_grad=True)
target = torch.randn(3, 5)
output = loss(input, target)
output.backward()
```

### nn.BCELoss

二分类用的交叉熵，用的时候需要在该层前面加上 `Sigmoid` 函数。交叉熵的定义参考  [Cross Entropy](https://en.wikipedia.org/wiki/Cross_entropy#Cross-entropy_error_function_and_logistic_regression)

### nn.BCEWithLogitsLoss

上面的 nn.BCELoss 需要手动加上一个 Sigmoid 层，这里是结合了两者，这样做能够利用 log_sum_exp trick，使得数值结果更加稳定（numerical stability）。建议使用这个损失函数。

值得注意的是，文档里的参数只有 weight, size_average 两个，但是实际测试 reduce 参数也是可以用的。此外两个损失函数的 target 要求是 FloatTensor，而且不一样是只能取 0, 1 两种值，任意值应该都是可以的。

### nn.CrossEntropyLoss

多分类用的交叉熵损失函数，用这个loss前面不需要加 Softmax 层

交叉熵定义参考这里 [Cross entropy](https://en.wikipedia.org/wiki/Cross_entropy#Cross-entropy_error_function_and_logistic_regression)

---



### nn.NLLLoss

### nn.NLLLoss2d

### nn.KLDivLoss

### nn.MarginRankingLoss

### nn.MultiMarginLoss

### nn.MultiLabelMarginLoss

### nn.SoftMarginLoss

### nn.MultiLabelSoftMarginLoss

### nn.CosineEmbeddingLoss

### nn.HingeEmbeddingLoss

### nn.TripleMarginLoss