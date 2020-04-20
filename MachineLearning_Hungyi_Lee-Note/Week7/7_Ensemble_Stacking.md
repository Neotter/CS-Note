# Stacking

## Stacking

把 data x 放到多个训练好的 Model，得出结果，之后使用多数投票表决这个 x 是属于哪个类。

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_43.png>)

但是并不是每个系统都是好的，就是说多数投票表决并不是每一个系统的权重都是一样的。

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_44.png>)

这时可以再在结果后面接一个 Final Classifier，让它自己决定前面的 Model 哪个可以信。

使用 Stacking 方法
把 training data 切成两部分
一部分拿来 Learn 前面的 classifier
另一部分拿来 train 后面的 Final Classifier

Final Classifier 可以不用太复杂，倘若前面的都太复杂了，
那最后的 Final Classifier 可以是单纯的 Logistic regression 就可以了
