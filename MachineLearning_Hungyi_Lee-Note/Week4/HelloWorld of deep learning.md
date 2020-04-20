# Keras 使用

## Step 1 define a set of function

```python
model = Sequential()
model.add(Dense(input_dim = 28*28,output_dim=500))//新版的output_dim改成了units
model.add(Activation('sigmoid'))//softplus,softsign,relu,tanh,hard_sigmoid,linear
model.add(Dense(output_dim=500))
model.add(Activation('sigmoid'))
model.add(Dense(output_dim=10))
model.add(Activation('softmax'))
```

新版 Kares:

```python
model = Sequential()
model.add(Dense(input_dim = 28*28,unit=500))//新版的output_dim改成了units
model.add(Activation('sigmoid'))//softplus,softsign,relu,tanh,hard_sigmoid,linear
model.add(Dense(unit=500,activation='relu'))
model.add(Dense(unit=10,activation='softmax'))
```

## Step 2 goodness of function

```python
model.compile(loss='categorical_crossentropy',optimizer='adam',metrice=['accuracy'])
```

## Step 3 pick the best function

Step 3.1: Configuration

```python
optimizer='adam'//SGD,RMSprop,Adagrad,Adadelta,Adam,Adamax,Nadam
```

Step 3.2: Find the optimal network parameters

```python
model.fit(x_train, y_train, batch_size=100, nb_epoch=20)
```

## Mini-Batch

实际做 NN 的时候并不会真的去 minimize total loss,并且 每次只随机拿一部分的数据训练一个 NN,这个步骤叫做 mini-Batch.

Randomly initialize network parameters,

Pick the 1st batch: 总的 loss 为:$L'=L^1+L^{31}+...$,Update parameters once

Pick the 2nd batch: 总的 loss 为:$L'=L^2+L^{16}+...$,Update parameters once

...

Until all mini-batches have been picked.

把以上运行一次叫做一个 epoch

batch_size=100, nb_epoch=20 的意思是每个 batch 有随机选的 100 个 examples(直到所有的 examples 被分完,比如我有 99 个 examples,那么就只有一个 batch,我有 900 个 examples,那么就有 9 个 batches), 所有 batch 被看过 20 次.

这个操作就相当于是 Stochastic gradient descent.区别是如果是 Stochastic gradient descent 等同于 mini batch size 是 1,那么一个 epoch 会 updates 50000 次参数,如果 batch szie 设为 10,那么一个 epoch 会 updates 5000 次参数,与普通方法的区别是 Loss 的计算方式和 updates 的方式,Mini-batch 是把一个 batch 所有的 Loss 合成一个来 updates 参数.

batch 的方法优点是运算速度快,GPU 可以并行运算.

## Save and load models

How to use the neural network(testing):

case 1:

```python
score = model.evaluate(x_test,y_test)
print('Total loss on Testing Set:',score[0])
print('Accuracy of Testing Set:',score[1])
```

case 2:

```python
result = model.predict(x_test)
```

## Dropout

通过屏蔽某些 activation node 防止过拟合
