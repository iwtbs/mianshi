from numpy import *
def sigmoid(inX):  #sigmoid函数
    return 1.0/(1+exp(-inX))

def gradAscent(dataMat, labelMat): #梯度上升求最优参数
    dataMatrix=mat(dataMat) #将读取的数据转换为矩阵
    classLabels=mat(labelMat).transpose() #将读取的数据转换为矩阵
    _,n = shape(dataMatrix)
    alpha = 0.001  #设置梯度的阀值，该值越大梯度上升幅度越大
    maxCycles = 500 #设置迭代的次数，一般看实际数据进行设定，有些可能200次就够了
    weights = ones((n,1)) #设置初始的参数，并都赋默认值为1。注意这里权重以矩阵形式表示三个参数。
    for _ in range(maxCycles):
        h = sigmoid(dataMatrix*weights)
        error = (classLabels - h)     #求导后差值
        weights = weights + alpha * dataMatrix.transpose()* error #迭代更新权重
    return weights