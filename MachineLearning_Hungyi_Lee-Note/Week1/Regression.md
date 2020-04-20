# Linear Regression

## Regression 的应用: 预测宝可梦的 CP 值

Step1: 建模

Model 指的是一系列的 function.function 的输入是宝可梦的属性(比如草系,初始出生值,种族值),输出是 cp 值.

> Linear Model 的定义: 如果可以把 model 写成: $y=b+\sum w_ix_i$形式,那么这个 Model 就叫做 Linear Model.其中$x$是宝可梦的属性,$w$是 Model 的属性.

Step2: 衡量 Model 好坏的标准

收集很多宝可梦的数据,设计 Loss Function,最一般的线性回归的 Loss Function 是这样的: $L(f)=L(w,b)=\sum^{10}_{n=1}(\hat{y}^n-(b+w*x^n_{cp}))^2$. Loss Function 的目的是通过调整 Model 的属性,让 Model 所代表的曲线能够更好的拟合数据集上的点.

> Loss Function: 其实就是数学上常说的 Distance, 用于描述两个向量之间的距离,如果 Model 属性代表的向量和收集到的数据代表的向量很接近,那么就可以认为这个 Model 产生的属性和原本产生的属性很相似.

Step3: 优化 Model
通过具体的做法是计算 model 和输入点之间的最小 Distance,然后当 Loss Function 位于最小 Distance 值时,Model 的属性即为最佳的属性.
为了使 Loss Function 有如下公式:

$f^*=arg \min_f L(f)$

$w^*,b^*=arg \min_{w,b} L(w,b)$

$w^*,b^*=arg \min_{w,b} \sum_{n=1}^{10}(\hat{y}^n-(b+w*x^n_{cp}))^2$

> Gradient Descent: 用于最小化 Loss Function 的方法,通过求导计算 Loss Function 的梯度(斜率),然后用斜率更新 Model 的属性.通过不断的循环计算更新最终使 Loss Function 达到一个局部最小值(Linear model 的局部最小值就是全局最小值),意味着 Distance 最小,因此 model 可以认为是实际产生数据的 model.

## 例子:

如果 Model 只有一个参数的情况下:

先计算梯度(Gradient)

$\frac{dL}{dw}=|_{w=w^0}$

再更新权值

$w^1\leftarrow w^0 - \mu \frac{dL}{dW}|_{w=w^0}$

再计算梯度(Gradient)

$\frac{dL}{dw}=|_{w=w^1}$

再更新权值

$w^2\leftarrow w^1 - \mu \frac{dL}{dW}|_{w=w^1}$

...

## 如果 Model 是两个参数的情况下:

$w^*,b^*=arg \min_{w,b} L(w,b)$

随机初始化

$w^0,b^0$

计算梯度(Gradient)

$\frac{\partial{L}}{\partial{w}}=|_{w=w^0,b=b^0},\frac{\partial{L}}{\partial{w}}=|_{w=w^0,b=b^0}$

更新权值

$w^1\leftarrow w^0 - \mu \frac{\partial{L}}{\partial{w}}|_{w=w^0,b=b^0}$

$b^1\leftarrow b^0 - \mu \frac{\partial{L}}{\partial{b}}|_{w=w^0,b=b^0}$

...

在线性回归 Linear Regression 中不用单行会取到 极小值 local optimal,因为线性回归中只有一个最小值.

> 计算平均误差的公式: $Average Error on Testing Data = \sum^{10}_{n=1} e^n$

## Model Selection

判断 Model 的是否有足够复杂度,可以计算不同复杂度的 Model 的 Average Error 来判断, Average Error 是纵轴,复杂度(次数)是横轴, Average Error 又分为 Training 的 Average Error 和 Testing 的 Average Error 两类(两张图),过拟合 Overfitting 的表现是这两类的 Average Error 会在一个次数的点之后分开,由于过拟合,Testing 的 Average Error 会突然升高,而 Training 的 Average Error 者会保持在一个很小的浮动范围内.

把 Model 的复杂度比喻成圈圈,如果 Model 越来越复杂则圈圈的范围越来越大,复杂的模型是包含了简单的范围的.

## Regularization

当随着模型越来越复杂,通过在 Loss Function 上加上一个偏置,使 Loss Funtion 越来越平滑

> 因为如果$w$越小, $\triangle{x}$和$w$相乘的值就越小,意味着$x$的改变并不能很大幅度的改变 Loss Function 的值.

$L(f)=L(w,b)=\sum_{n=1}^{10}(\hat{y}^n-(b+w*x^n_{cp}))^2+\lambda\sum(w_i)^2$

$\lambda$的值越大,Loss Function 的值越平滑,Training 的 Average Error 会增大,但是 Testing 的 Average Error 可能会比较小
