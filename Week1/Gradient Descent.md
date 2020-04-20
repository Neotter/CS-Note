# Gradient Descent

多维参数的 Gradient 就是各个参数的偏导数, Gradient 是向量,是与函数下降方向相反的向量.

## Learning Rate

Learning Rate 太大会导致梯度爆炸,Learning Rate 太小会导致下降的速度太慢

## Adaptive Learning Rates

动态调整 Learning Rates 有不同的思路:

- 开始训练时给与大的 Learning Rate,当 Loss Function 越接近于极小值,Learning Rates 越来越小.(E.g. $1/t$ Decay: $\eta / \sqrt{t+1}$)
- 不同的参数给与不同的 Learning Rate

## Adagrad(不同的参数给与不同的 Learning Rate)

每一个参数的 Learning Rate 都除与之前的 Learning 的均方根(Root Mean Square)

- Vanilla Gradient Descent: $W^{t+1}\leftarrow W^t - \eta^t g^t$
- Adagrad:$W^{t+1} \leftarrow W^t  - \frac{\eta^t}{\sigma^t}g^t$

> 其中 $\eta^t = \frac{\eta}{\sqrt{t+1}}$, $g^t = \frac{\partial{C(\theta^t)}}{\partial{w}}$, $\sigma^t$是过去的值的 Root Mean Square.

adagrad 的 Intuitive 的理解, $\sigma^t$其实是 Loss Function 的二阶导, 由于存在多个参数,每个参数在 Gradient 方向的平滑程度是不一样的,而二阶导可以体现平滑的程度,二阶导越大,说明在该 Gradient 方向上越陡,反之越平缓.所以通过和二次项相除,越陡峭的地方需要走的距离约越小,因为水平步子走大了容易马上到达最低点.

## Stochastic Gradient Descent

普通的 Gradient Descent 是看完所有的 example 之后才 Update 一次参数,Stochastci Descent 是看一个 example 就 update.

> 普通的 Gradient Descent:
>
> - $L= \sum_n(\hat{y}^n - (b+\sum{w_ix_i^n}))^2$
> - $\theta^i = \theta^i-1 - \eta\triangledown L(\theta^{i-1})$.

> Stochastic Gradient Descent:
> 随机选一个$x^n$
>
> - $L^n = (\hat{y}^n - (b+\sum{w_ix_i^n}))^2$
> - $\theta^i = \theta^{i-1} - \eta\triangledown L^n(\theta^{i-1})$

## Feature Scaling

如果 Model 每个参数的范围大小不一样,把各个参数 plot 在图上会发现它们所占的范围很扁,这样不利于 Gradient Descent,因为这样整体的 Gradient 并不一定是直直朝着圆心走过去的.
