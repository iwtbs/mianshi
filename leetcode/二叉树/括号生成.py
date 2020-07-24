'''
n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
'''

'''
每一个括号序列可以用 (a)b 来表示，其中 a 与 b 分别是一个合法的括号序列（可以为空）
那么，要生成所有长度为 2 * n 的括号序列，我们定义一个函数 generate(n) 来返回所有可能的括号序列。那么在函数 generate(n) 的过程中：

我们需要枚举与第一个 ( 对应的 ) 的位置 2 * i + 1；
递归调用 generate(i) 即可计算 a 的所有可能性；
递归调用 generate(n - i - 1) 即可计算 b 的所有可能性；
遍历 a 与 b 的所有可能性并拼接，即可得到所有长度为 2 * n 的括号序列

'''
from typing import List


class Solution:
    def generateParenthesis(self, n: int) :

        res = []
        cur_str = ''

        def dfs(cur_str, left, right, n):
            """
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left: 左括号已经使用的个数
            :param right: 右括号已经使用的个数
            :return:
            """
            if left == n and right == n:
                res.append(cur_str)
                return
            if left < right:
                return

            if left < n:
                dfs(cur_str + '(', left + 1, right, n)

            if right < n:
                dfs(cur_str + ')', left, right + 1, n)

        dfs(cur_str, 0, 0, n)
        return res
