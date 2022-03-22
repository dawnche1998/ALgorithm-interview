
>谷歌的Transformer模型最早是用于机器翻译任务，当时达到了SOTA效果。Transformer改进了RNN最被人诟病的训练慢的缺点，利用self-attention机制实现快速并行。并且Transformer可以增加到非常深的深度，充分发掘DNN模型的特性，提升模型准确率
>[图解Transformer CSDN_transformer](https://blog.csdn.net/longxinchen_ml/article/details/86533005)
>[The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)


![](transformer.png)
编码组件部分由一堆编码器（encoder）构成（论文中是将6个编码器叠在一起——数字6没有什么神奇之处，你也可以尝试其他数字）。解码组件部分也是由相同数量（与编码器对应）的解码器（decoder）组成的。

所有的编码器在结构上都是相同的，但是没有共享参数。每个解码器都可以分解成两个子层。
![](transformer2.png)
从编码器输入的句子首先会经过一个自注意力（self-attention）层，这层帮助编码器在对每个单词编码时关注输入句子的其他单词。
自注意力层的输出会传递到前馈（feed-forward）神经网络中。每个位置的单词对应的前馈神经网络都完全一样（译注：另一种解读就是一层窗口为一个单词的一维卷积神经网络）。
解码器中也有编码器的自注意力（self-attention）层和前馈（feed-forward）层。除此之外，这两个层之间还有一个注意力层，用来关注输入句子的相关部分（和seq2seq模型的注意力作用相似）。
