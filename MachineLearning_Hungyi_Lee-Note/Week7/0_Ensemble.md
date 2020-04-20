# Ensemble

![](<https://raw.githubusercontent.com/Neotter/NTU_DeepLearning_Note/master/Week7/images/14-Ensemble%20(v6)_%E9%A1%B5%E9%9D%A2_03.png>)

其实就是团队合作，用好几个训练好的模型一起上。Ensemble 就像是组队打副本，当你训练了一打的 Classifiers，单个 Classifier 每个都是已经满级了，但是凭借单个角色依然很难单挑副本中的 Boss，不过当他们组队一起上的时候就能爆发出超越他们极限的力量。

当然打副本需要各种职业的配合，比如 LOL 有 ADC 有奶有坦有辅助，而 Ensemble 训练好的每个 Classifier 当然也要有自己擅长的工作，专业点就是说 Classifier should be diverse。

然后 Ensemble 要做的就是把不同的 Classifiers 集合在一起，分配各自的权重，这相当于说在打 Boss 中每个人都应该有自己的站位和资源分配，负责输出的 Classifier 等级要高点，给他的资源就多点，负责辅助的 Classifier 等级可以低点，那么给她的资源就少点。

Ensemble 是最后的大招，如果你训练好的模型的结果已经提升不上去了，可以考虑 Ensemble 的方法，通俗来说就是漫画中的主角发现自己一个人单挑不过 Boss 就找人组队来群殴 Boss。
