'''
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

'''
class Solution(object):
    def nthUglyNumber(self, index):
        if index <= 1: 
            return index
        res = [1] * index
        i2, i3, i5 = 0, 0, 0
        for i in range(1, index):
            res[i] = min(res[i2]*2, min(res[i3]*3, res[i5]*5))
            if res[i] == res[i2]*2: i2 += 1
            if res[i] == res[i3]*3: i3 += 1
            if res[i] == res[i5]*5: i5 += 1
        return res[-1]