# SVM
## 推导
[推导](https://mp.weixin.qq.com/s/jgPFoI2Z_Fv1H0KU0mYtCg)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200224221732591.png)
对于高维数据、样本量非常大的时候，无法通过简单运算求解，这时候就会通过对偶、核技巧等方法求解
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200224223118486.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM0MjE5OTU5,size_16,color_FFFFFF,t_70)
那么强对偶能解决什么问题呢？强对偶可以根据计算的难度、复杂度在minmax与 maxmin之间转换
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200224225524350.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM0MjE5OTU5,size_16,color_FFFFFF,t_70)
公式推导到这里
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200224225544582.png)
最终最佳超平面的表达式
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200224225733555.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM0MjE5OTU5,size_16,color_FFFFFF,t_70)
可以看到，最佳参数W,b都是关于数据的线性组合，到这里SVM的任务就完成了

(xi ⋅ xj)是内积运算，当有n个样本点时，会构成n*n的矩阵。当x经过非线性变换后为 φ( x)，优化问题转为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200224231729912.png)
核函数是指在低维输入空间中存在一个函数 K(x, x′) ，它恰好等于在高维空间中这个内积，即K( x, x′) =<φ( x) ⋅φ( x′) >，此时将会大大减小计算消耗，这就是为什么很多人将核函数也称为核技巧的原因