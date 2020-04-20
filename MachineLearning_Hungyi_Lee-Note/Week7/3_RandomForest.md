# Random Forest

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_12.png>)

Random Forest 的方法就是多棵 Decision tree 做 Bagging，但是传统的 Bagging 是同一个数据集随机重采样后把所有的 Features Training 多个 Model 再做 Bagging，对于 Decision tree 来说得到的每棵 Tree 实际上都没有太大差别（因为 这样得到的 Tree 的 Model 都是一样的，没有简单和复杂之分）。

所以实际上 Random Forest 还会随机选取 Features/Questions 做 Split，比如有 x1，x2，x3，x4 这 4 个 features，Tree1 我只用 x1，x2 Train，Tree2 我只用 x3，x4 Train...这样每棵 Decision Tree 都是不一样的（不同的复杂度）。最后把所有 Decision Tree 的结果集合起来就可以得到 Random Forest。

Out-of-bag validation 是一种 Bagging 的 Validation 的方法。一般的 Train 是把 Training Set 切成 Training Set 和 Validation Set 两块来做 Training 和 Validation，如果是用 Bagging 的方法的话可以不用切，一样有 Validation 的效果。具体步骤是使用分开的多个数据集 Train 多个 Model， 每个 model 存在着有些 testing data 并没有看过， 在通过把没有过看过的 testing data 和 model 组合去 Testing，比如有四笔 data $x^1$ 到 $x^4$ ， 第一个 model $f_1$ 用 data $x^1$ 和 $x^2$ train ,第一个 model $f_2$ 用 data $x^3$ 和 $x^4$ train etc. 最后得到四个 model。

为什么可以这样做，因为训练出来的 model $f_1$到$f_4$每个没有用到全部的数据集，比如有的$f_1$是用$x^1$ 和 $x^2$ train 的，没有看过$x^3$ 和 $x^4$，所以可以用$x^3$ 和 $x^4$ testing。

做 Bagging 并不能使你的 model 更能够 fit dat，但是他和重采样的 Random Forest 比起来更加的平滑，

## Experiment：Function of Miku

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_13.png>)

Random Forest 用在初音分类问题上的结果，可以对比 DecisionTree 中的结果看看。
