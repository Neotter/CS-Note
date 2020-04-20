# Boosting

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_15.png>)

当 Model 比较复杂（强）时，可以使用 Bagging 的方法做 Ensemble，而当 Model 比较简单时可以使用 Boosting 的方法提高它的 Performance。

只要你有一些 Error rate 小于 50%的模型，Boosting 可以保证这些模型组合起来之后 Error rate 减少到 0%。

Boosting 的原理是互补，先找第一个 Classifier $f_1(x)$，再找个其他的 Classifier $f_2(x)$,而$f_2(x)$可以和$f_1(x)$进行互补。直到找到所有的 Classifier 能够得到一个很低的 Error Rate。

Boosting 找 Classifiers 是有顺序的，而 Bagging 没有。

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_16.png>)

关于如何找到不同的 Classifiers，一种方法是制造不同的 training data set 的方式，比如：

- Re-sampling，从已经收集到的数据中随机抽选数据从而组成一个新的 Set。
- Re-weighting，给每一组 Data 一个 Weight，借由改变 Weight 制造不同的 data set。而在 Training 的时候 loss function 在计算每一笔 error 的时候在 training example 的 input 和 target 都会乘以该笔 data 的 weight，使得它在 training 的时候被多考虑一点，或者是被多忽略一点。
- 其实 Re-sampling 本质上都是改了 weight，如果一个 data 被 sampling 了两次，那么它的 weight 就是 2，可是 re-sampling 只能改变 weight 为整数，而 re-weighting 可以改变 weight 为任意数。

这里可以看图，在 x 和 y 都与一个 weight u 相乘之后，Loss Function 其实就只是与不同上标的 x 和 y 对应的 u 相乘，注意 PPT 中的那个并不是指数而是上边。
