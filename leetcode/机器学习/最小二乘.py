'''
https://blog.csdn.net/m0_37816922/article/details/97161484
'''
import numpy as np
def leastSquare(x,y):
    sx = sum(x)
    ex = sx/len(x)
    sx2 = sum(x**2)

    sxy = sum(x*y)
    ey = np.mean(y)

    a = (sxy-ey*sx)/(sx2-ex*sx)
    b = (ey*sx2-sxy*ex)/(sx2-ex*sx)
    return a,b


