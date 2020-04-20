# Bagging

## Review: Bias v.s. Variance

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_05.png>)

前面的课程讲过在做 Machine Learning 的时候会有 Bias 和 Variance 的 tradeoff，如果有一个很简单的 Model，会有 Large Bias 和 Small Variance，而一个复杂的 Model 相反，会有 Small Bias 和 Large Variance。在 Bias 和 Variance 的组合下，随着 Model 复杂度的增加，我们会看到 Model 的 Error Rate 会随着复杂度的增加逐渐下降再增加。

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_06.png>)

假设我们要训练预测宝可梦的 Model，训练多个不同 Model 就像是在不同的平行世界训练预测宝可梦的 Model，所有世界本身都有一个相同的固有 Model 用于产生宝可梦，可是我们并不知道这个固有的 Model，所以我们要用补抓到的宝可梦数据训练一可以个预测宝可梦的 Model。

而根据我们选择的预测 Model 的不同，相应的 Bias 和 Varience 也不同，在有的世界我们认为是 Easy 难度，于是就建立了简单的模型，有的世界我们认为是 Hard 难度，于是就建立了复杂的模型。

简单的模型 Bias 很大 Varience 很小，复杂的模型 Bias 很小 Varience 很大。

当我们把不同的模型，统统集合起来，比如把不同的模型输出做一个模型平均起来，那么得到的新的模型就会更跟正确的模型十分接近。

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_07.png>)

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_08.png>)

为了模拟多个平行世界，假设我们有 N 个 Training examples,那么我们从这个 N 个 examples 中再采样 N'个 examples（就是有放回的抽签），得到几个 Set（每个 Set 的 example 有可能重合）。

用得到的每个 Set 各自 Training 一个 Model，然后用 Testing data 验证每个 Model 的结果，有了每个 Model 的结果那么可以把这些结果做 Average（Regression） 或者 voting （Classification）得到最终 Performance，通常最终 Performance 会比只有靠一个 Model 来得更加好。这种方法叫做 Bagging

什么时候做 Bagging？只有你的 Model 很复杂，你担心会 Overfitting 的时候才做 Gagging，做 Gagging 的目的是为了减低 Variance。比如 Decision Tree 就很容易 Overfitting。
