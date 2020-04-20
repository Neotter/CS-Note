# Classification

如果使用 Regression 的思路解决 Classification 的问题的话,可能会导致异常点(有些点离散度太大偏离元数据集)把回归的 Model 代表的那条线带偏.

## Ideal Alternatives

一个想法就是讲整个 Regression 的$f(x)$放到一个$g(x)$里面,其中$g(x)$是一个 Sigmod 函数, Loss Function 是这样$L(f)=\sum_n\sigma(f(x^n)\ne\hat{y}^n)$

## Generative Model

Model Generate 一个 x,如果可以计算每一个 x 出现的几率,那么就可以知道 x 的 distribution,然后用这个 distribution 来产生 x.

$P(x)=P(x|C_1)P(C_1)+P(x|C_2)P(C_2)$

> 如何得到$P(x)$:Maximum Likelihood,最终$\mu$等于 dataset 的期望(平均值),$\Sigma$为单个宝可梦的属性之间的协方差

> 为了节省计算时间,可以让不同 Class 相同的$\Sigma$,$\Sigma=\frac{N_1}{N}\Sigma^1+\frac{N_2}{N}\Sigma^2$,共用一个协方差之后两个 class 之间的 boundary 就变成线性的.

> 最终先验概率会变成 Sigmoid Function 和普通的 Regression 的组合.

> Naive Bayes:假设所有的 Feature 他产生的几率都是 independence.
