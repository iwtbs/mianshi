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