### 重新考察 CNN

<img src="D:\OneDrive\04_AlgorithmNotes\Data\decoder.png" style="zoom: 33%;" />

编码器：将输入编程为中间表达形式（特征）

解码器：将中间表示解码成输出

### 重新考察 RNN

<img src="D:\OneDrive\04_AlgorithmNotes\Data\decoder_rnn.png" style="zoom:33%;" />

编码器：将文本表示成向量

解码器：向量表示成输出



### 编码器解码器架构

一个模型被分为两块：

编码器处理输出

解码器生成输出

![](D:\OneDrive\04_AlgorithmNotes\Data\decoder2.png)



### CODE

#### 编码器

在编码器接口中，我们只指定长度可变的序列作为编码器的输入`X`。 任何继承这个`Encoder` 基类的模型将完成代码实现。

```python
from torch import nn

#@save
class Encoder(nn.Module):
    """编码器-解码器架构的基本编码器接口"""
    def __init__(self, **kwargs):
        super(Encoder, self).__init__(**kwargs)

    def forward(self, X, *args):
        raise NotImplementedError
```

#### 解码器

在下面的解码器接口中，我们新增一个`init_state`函数， 用于将编码器的输出（`enc_outputs`）转换为编码后的状态。 注意，此步骤可能需要额外的输入，例如：输入序列的有效长度。 为了逐个地生成长度可变的词元序列， 解码器在每个时间步都会将输入 （例如：在前一时间步生成的词元）和编码后的状态 映射成当前时间步的输出词元。

```python
#@save
class Decoder(nn.Module):
    """编码器-解码器架构的基本解码器接口"""
    def __init__(self, **kwargs):
        super(Decoder, self).__init__(**kwargs)

    def init_state(self, enc_outputs, *args): # 将encode输出转换为一个state
        raise NotImplementedError

    def forward(self, X, state): # 这里有一个输入X和输入state 转换为输出
        raise NotImplementedError
```

#### 合并编码器和解码器

总而言之，“编码器-解码器”架构包含了一个编码器和一个解码器， 并且还拥有可选的额外的参数。 在前向传播中，编码器的输出用于生成编码状态， 这个状态又被解码器作为其输入的一部分。

```python
#@save
class EncoderDecoder(nn.Module):
    """编码器-解码器架构的基类"""
    def __init__(self, encoder, decoder, **kwargs):
        super(EncoderDecoder, self).__init__(**kwargs)
        self.encoder = encoder
        self.decoder = decoder

    def forward(self, enc_X, dec_X, *args):
        enc_outputs = self.encoder(enc_X, *args)
        dec_state = self.decoder.init_state(enc_outputs, *args)
        return self.decoder(dec_X, dec_state)
```

“编码器－解码器”体系架构中的术语“状态” 可能会启发你使用具有状态的神经网络来实现该架构。 在下一节中，我们将学习如何应用循环神经网络， 来设计基于“编码器－解码器”架构的序列转换模型。

#### 小结

- “编码器－解码器”架构可以将长度可变的序列作为输入和输出，因此适用于机器翻译等序列转换问题。
- 编码器将长度可变的序列作为输入，并将其转换为具有固定形状的编码状态。
- 解码器将具有固定形状的编码状态映射为长度可变的序列。