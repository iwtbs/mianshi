class Solution:
    def maxArea(self, height):
        re = 0
        n = len(height)
        left,right = 0,n-1
        while left < right:
            cur = min(height[left],height[right]) * (right-left)
            re = max(re,cur)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return re

# 接雨水
def trap(self, height):
    re,left_max,right_max = 0,0,0
    left_l,right_l = [],[]

    for i in height:
        if i>left_max:
            left_max = i
        left_l.append(left_max)
    for i in height[::-1]:
        if i > right_max:
            right_max = i
        right_l.append(right_max)
    right_l = right_l[::-1]

    for i in range(len(height)):
        h = min(left_l[i],right_l[i])
        if h>height[i]:
            re += h-height[i]
    return re

# 柱状图中最大的矩形
'''
当我们找 i 左边第一个小于 heights[i] 如果 heights[i-1] >= heights[i] 其实就是和 heights[i-1] 左边第一个小于 heights[i-1] 一样。
依次类推，右边同理。
'''
def largestRectangleArea(self, heights) -> int:
    if not heights:
        return 0
    n = len(heights)
    left_i = [0] * n
    right_i = [0] * n
    left_i[0] = -1
    right_i[-1] = n
    for i in range(1, n):
        tmp = i - 1
        while tmp >= 0 and heights[tmp] >= heights[i]:
            tmp = left_i[tmp]
        left_i[i] = tmp
    for i in range(n - 2, -1, -1):
        tmp = i + 1
        while tmp < n and heights[tmp] >= heights[i]:
            tmp = right_i[tmp]
        right_i[i] = tmp
    # print(left_i)
    # print(right_i)
    res = 0
    for i in range(n):
        res = max(res, (right_i[i] - left_i[i] - 1) * heights[i])
    return res
