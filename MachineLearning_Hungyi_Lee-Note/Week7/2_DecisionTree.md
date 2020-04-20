<!--
 * @Author: your name
 * @Date: 2020-01-06 14:14:07
 * @LastEditTime: 2020-04-20 13:35:06
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /CS-Note/MachineLearning_Hungyi_Lee-Note/Week7/2_DecisionTree.md
 -->

# Decision Tree

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_09.png>)

根据问题（阈值）分类。

比如 x1<0.5，x2<0.3 就小于属于 Class1，x1>0.5,x2>0.3 就属于 Class2。每一次提问我们称为 Split，每个 Class 我们称为 Leaf

## Experiment：Funtion of Miku

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_10.png>)

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_11.png>)

Decision Tree 的 Depth 分别为 5，10，15，20 时，能够区别分区域。可以看见树的 Depth 越大，可以识别的约精确。

只要你想就可以把任何 Decision Tree 的 Accuracy 变成 100%，只要增加 Depth 就可以了，可是会造成的问题是 Decision Tree 的 Depth 越大，那么模型就越复杂。

一个解决方案就是做 Bagging，也就是做 Random Forest.
