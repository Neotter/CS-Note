# Where does the error come from?

Error 可能来自采样到的 dataset 中的误差,采样到的 dataset 会有 Low/High Bias, Low/High Variance 四种情况. Bias 的高低意味着 dataset 离$\hat f$的远近,一般 Low Bias&Variance 最好,Low Bias 意味着 dataset 里目标的$\hat f$很近,采样的结果很可信.Low Variance 意味着 dataset 的离散程度不大,数据很集中于$f^*$.

> $\hat f$ 是目标函数 $f^*$是估计函数.

简单的 Model 有 Large Bias 和 Small Variance,复杂的 Model 有 Small Bias 和 Large Variance.

所以随着 Model 从简单到复杂,Bias 的曲线是不断向下的,而 Variance 是先平稳在变大,如果同时考虑 Bias 和 Variance,那么整体就是向上的.
如果 Bias 在总的 Error 中占据了主导,那么就是 Underfitting,如果 Variance 占据的主导那么就是 Overfitting.
要记住每一个 Model 都是一堆 Function 的集合(Function Set), 如果是一个简单的 Model,那么这个 Model 包含的 Target Funtion 比较少甚至完全不包含,所以 Bias 有可能比较大,Variance 比较小.而复杂的 Model 包含的 Function Set 比较大,那么 Variance 比较大,能包括的 Function 比较多.

用 Model 去 Fit 一个 Function 就像是打靶,简单的 Model 的准星小(Low Variance),离靶心距离远(Large Bias),打不中靶心,复杂的 Model 的准星大(Large Variance),覆盖的范围大,总的准星的质心离靶心近,但是因为覆盖的范围大,所以也瞄不准.

Underfitting: Model 不能 fit training examples, 有 Large Bias, 增加复杂度,修改模型.

Overfitting: Model 能够 fit traing examples, 但是不能 fit testing data,那么是 Large variance,减少复杂度,增加 data.做 Regularization.

## Cross Validation

把 Dataset 分成三份,一份是 Training Set, 一份是 Validation Set, 一份是 Testing Set.
先用 Training 好之后先用 Validation Set 去试,如果数据集的 Error 很小之后再用 Testing 去试.

## N-fold Cross Validation

把 Dataset 的 Training Set 分成是 3 份,其中三份轮流交换标签: TrainingSet1,TrainingSet2,ValidationSet,得到三个 Models,计算每个 Model 在不同标签下的 Error,最后得到三个 Model 在不同标签下的平均 Error,最后选出结果最好的 Model. 接着用最好的 Model 训练所有 Training Set,再 Test.
