## Convolution Layer

用于提取特征

- 其实就是做相关运算,不过是用矩阵和矩阵做相关运算,找出大的矩阵中和小的矩阵最相似的一块子矩阵.
- 而小的矩阵叫做 Filter,大的矩阵可以是 Image 等需要提取 Feature 的 DataSet.
- 每个卷积层都是由多个 filter 组成
- 多个 Filter 得到多个相关性的矩阵叫做 Feature map,一个卷积层的输出可以是多个 Feature Map 组成.

## Max Polling Layer

用于较少数据量

- 其实就是上采样,可以用每 NxN 个矩阵求平均的方法或者保留最大值.

## Flatten

把矩阵拉直

## CNN in Keras

Tensor 指的是高维的 Vector.

有多个 Filter 创建了多个 Feature map,定义一个叫 Degree of activation 的东西,公式为:$a^k=\sum_{i=1}^{11}\sum_{j=1}^{11}a_{ij}^k$,这个 Degreee 表示了一张图片 x 被一个 filter activate 的程度,越大说明 x 中有更多的 filter 的东西. 还可以使用一个叫做 gradient ascent($x^*=arg\ max_x a^k$)的方法最大化图片 x.

就是说在 CNN 中 Filter 之所以叫做 Filter,是因为 CNN 的目的是为了分类,而分类一样东西需要保存已知的知识才能做到(用已知的知识(Filter)判断未知的数据(x)是属于哪一类.Convolution 和 MaxPooling 的作用是标出未知的数据(x)中,哪个位置存在已知的知识(Filter).然后丢到 NeuronNetwork 中全局的观察,每个 NN 节点的作用是为了统计全局的数据(x)中,某个知识(Filter)存在的程度.若一个未知数据(x)中,存在 n 个 A 知识(A Filter),m 个 B 知识(B Filter), 那么我们认为这个未知知识应该是为 C 类, C 类有一个比较稳定的 patten,而 NN 的目的就是统计 A B 知识并识别出相应的 patten.

因为机器和人看到的东西不同,所以有可能我们人类并不认为是 Object C 的东西也会被机器认为是 Object C.为了让机器和我们人类看到相同的东西,我们可以做一些限制,视频中的限制是:$x^* = arg\ max_x(y^i-\sum_{i,j}|x_{i.j}|)$

每个 NN 的权值其实就是一张图了,所以当输入一张图,这张图的值就是其中一个 NN 的权值,那么肯定这个 NN 最终的 Degress of Activition 是最大的.因此我们直接看这张用 NN 的权值组成的值其实就是看机器所看的东西.
