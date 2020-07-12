'''
输入: [3,30,34,5,9]
输出: "3033459"
'''

class Solution(object):
    def minNumber(self, nums):
        n=len(nums)
        if n==0:
            return ""
        for i in range(n):
            nums[i]=str(nums[i])
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]>nums[j]+nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
        return "".join(nums)