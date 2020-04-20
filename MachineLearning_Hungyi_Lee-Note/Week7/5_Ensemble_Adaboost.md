# Adaboost

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_17.png>)

Adaboost 的思想是找一组新的 Training data(re-weight)，而这组 training data 在$f_1(x)$中得到的 performance 很烂，然后用这组 training data 再 training 一个 model $f_2(x)$。这样最终结果是我们得到了一个$f_1(x)$和一个$f_2(x)$这两个 Model 在面对 re-weight 的 training data 时会互补。

那么怎么找到那个可以让$f_1(x)$坏掉的 training data 呢,看 PPT，先定义$f_1(x)$的 Error rate，找到一个小于 0.5 的 Error rate（可以通过改变 weight 的值达到目的，比如一开始算出来的 Error rate 是 0.8，那我就乘个 一组 weight 让他们加起来之后小于 0.5），假设原来的 training data weight 是 u1，新的 training data weight 是 u2，我们的目标是把 u1 换成 u2，让 $f_1(x)$ 的 Error rate 等于 0.5。这相当于说 re-weight 了，re-weight 之后还要除以$Z_2$用于 normalize weight。

然后把$u_1^n$换成$u_2^n$，这个$u_2^n$可以让整个 Error Rate 等于 0.5。再用$u_2^n$的 data 进行 training

可以这么理解 Error Rate 的 weight：每个预测出来的 Result 和 GroundTurth 之间都有一个 Distance，如果 Distance 大，表明预测的 Result 和 GroundTurth 并不相同，预测错了，如果 Distance 小，表明预测的 Result 和 GroundTurth 相同或者很接近，预测对了。而 Error Rate 就是所有 Distance 的和，对于大的 Distance，对整个 Error Rate 的贡献大，对于小的 Distance，对于整个 Error Rate 的贡献小,因此 Re-weight 的作用相当于改变了 Distance 对于 Error Rate 的贡献，让预测错的 Distance 更大，进而使 Error Rate 更加大（知道 Error Rate 等于 0.5）。Re-weight 之后的 Training data 在前一个 Model 之中结果是很不好的（Error Rate = 0.5），于是用 Re-weight 之后的 Training data 再 Train 一个 Model，那么由于 Re-weight 的操作增加了 Distance 大的 Sample 的贡献，结果这个 Model 对于错误的样本更加重视。。

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_18.png>)

这一页是例子，这里有 4 个 data，一开始每个 data 都分配相同的 weight，然后让$f_1(x)$去分类，当遇到分类错误的 data，比如第二个 data 答错了，就给他大一点的 weight，其他 weight 给小的 weight。这样做的目的相当于考试答题，一开始你以为每道题做对了都给相同的分数，想不到最后改考卷的缺德老师故意把你打错的题目的分值给高让你扣多点，又把你答对的题目分值给低让你得分的少点。这样$f_1(x)$的 error rate 就会等于 0.5，这时新的 training 在$f_1(x)$上结果很烂，但是经过$f_2(x)$的训练，这个 re-weight 的 data set 在$f_2(x)$上会比$f_1(x)$好。

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_19.png>)

如果 xn 被 f1 分类错误，那我们就把 xn 乘上一个权重 d1 其中 d1 > 1
如果 xn 被 f1 分类正确，那我们就把 xn 除上一个权重 d1 , d1 > 1
那么
d1 的值要设多少呢？才能使得 f1 的 error rate = 0.5

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_20.png>)

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_21.png>)

一些数学上的公式求得结论 $d1 = \sqrt{(1-\epsilon1)/\epsilon1}$

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_22.png>)

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_23.png>)

AdaBoost 的算法伪代码。

training data 一开始初始的 weight 都是 1
接着跑 T 次 iteration
每一笔 data 都有一个 weight 值 u
每一次的 iteration 会计算出一个 epsilon_t 然后根据 epsilon_t 的值来更新 weight
因为 dt = sqrt( (1 - epsilon_t ) / epsilon_t )
另一种表示法，定义 alpha_t = ln( dt ) = ln( sqrt( (1 - epsilon_t ) / epsilon_t ) )
有了 alpha_t 就可以把式子变得更简便一点.

Uniform weight:
把 T 个 Classifier 值通通加起来再取正负号，整合起来看结果
Non-uniform weight:
但是 T 个 Classifiers 当中的表现有好有坏，所以在每一个 classifier 的结果前面
再乘以一个权重 alpha_t 这样下去整合结果会更好.

如果某个 classifier 错误率 epsilon_t = 0.1 可以计算出 alpha_t = 1.10
如果另一个 classifier 错误率 epsilon_t = 0.4 计算出来的 alpha_t = 0.20
所以 classifier 的错误率越小，分辨的比较准的时候 alpha_t 就会比较大！

## Toy Example

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_24.png>)

以 10 个数据的二元分类作为例子

f1 分类器切下去，发现有 3 笔分类错误，所以错误率 epsilon_1 = 0.3
并可以由 epsilon 的值计算出 d1 = 1.53, alpha_1 = 0.42
接着，我们把分类错的资料 weight 变大乘以 1.53 (d1)，分类对的 weight 变小 除以 1.53 (d1)

然后我们使用新的 classifier f2 切一刀，左边是 positive 右边是 negative，
针对我们上一步骤调整后的 data 来做分类

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_25.png>)

f2 总共分类错三笔 data，经过计算，可以得到 f2 的 error rate: epsilon*2 =
(0.65 * 3) / (1.53 \_ 3 + 0.65 \* 7) = 0.21
再根据 epsilon_2 可以计算出 d2 = 1.94, alpha_2 = 0.66
然后我们把分类错的资料 weight 变大乘以 1.94 (d2)，分类对的 weight 变小除以 1.94 (d2)
更新 data weight

第三个 classifier 切一刀，上面是 positive 下面是 negative，总共分错三笔资料

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_26.png>)

根据前面的方法，再次操作一遍，得到 epsilon_3 = 0.13, d3 = 2.59, alpha_3 = 0.95
假设我们只跑三个 iteration 就结束了，所以 weight 就打住不更新了

整合起来，得到最后的 Classifier H(x)
目前三个 classifier 把空间切成六块

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_27.png>)

左上角：大家都觉得是蓝色的，没有争议就是蓝的
右上角：f1 跟 f2 觉得是红的 总共占 0.42 + 0.66 = 1.08 ， f3 觉得是蓝的但只有 0.95 输了，
所以结论，右上角是红的
左下角：f1, f2 都觉得是蓝的，总共 weight 1.08 > f3 觉得是红的且 weight 0.95 也输了！
所以结论，左下角是蓝的

f1, f2, f3 这三个 classifier 分别都会犯错，
但是我们透过 AdaBoost algorithm 把它们组合起来后，得到好的结果！

## 证明 AdaBoost 跑的越多，performance 越好

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_28.png>)

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_29.png>)

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_31.png>)

## AdaBoost 的神秘现象

横轴 iteration 纵轴 error rate
我们发现 training data 的 error rate 在五个 weak classifier 合力下就会变 0 了
加了更多的 weak classifier 后，training data error 已经不会再下降，但是 testing error 居然还能持续下降

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_33.png>)

如果我们 train weak classifier 的演算法可以让 error rate 变零的话，使用 Adaboost 是会有问题的！
Adaboost 的使用时机是，使用在一大堆 weak classifier 上，所以一定要是 weak 不能太强！

g(x) : 代表 weak classifiers 整合后的 output 我们希望 g(x) 是个非常大的值
定义：g(x)\*y-hat 为 Margin 也就是使用整合后的分类器，分类正确的情形

Adaboost 的 (upper bound) Margin 变化图，可以发现，
只有 5 个 weak classifier 时，margin 是虚线，但是增加 weak classifier 的数量时，
增加到 1000 个 classifiers 时我们发现 Margin 会增加，如图中的黑色实线
虽然在 training set 的 error rate 已经是 0 不会再下降，
也就是 y-hat 已经跟所有的 g(x) 同号了，但是增加 classifier 数量时，
仍然可以让 margin 增加，使得在 testing 的 error rate 下降。

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_35.png>)

使用深度为 5 的 decision tree，之前的实验中，深度 5 的 tree 几乎都是不能用的
但是用 Adaboost 可以发挥群众的力量
找 10 棵 tree 结果就有轮廓出来了
20 棵 tree 时结果更好了
找 100 棵 tree 时，几乎可以把完整的初音描绘出来了！

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_36.png>)
