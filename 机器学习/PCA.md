# PCA
## 为什么要算协方差矩阵呢？
这时就要想起我们之前的目的：在降维后的每一维度上，方差最大。而方差最大，则容易想到的就是协方差矩阵，去中心化后，协方差矩阵的对角线上的值正好就是各个数据维度的方差
##  PCA算法两种实现方法
1. 基于特征值分解协方差矩阵实现PCA算法
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020021414391256.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM0MjE5OTU5,size_16,color_FFFFFF,t_70)
2. 基于SVD分解协方差矩阵实现PCA算法
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200214144051150.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM0MjE5OTU5,size_16,color_FFFFFF,t_70)
## svd和特征分解的区别
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200214144934758.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200214145019486.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM0MjE5OTU5,size_16,color_FFFFFF,t_70)
