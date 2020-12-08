'''
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
class Solution:
    def subsets(self, nums):
        if not nums:
            return 0
        res = []
        def helper(nums,temp):
            res.append(temp)
            for i in range(len(nums)):
                helper(nums[i+1:],temp+[nums[i]])

        helper(nums,[])
        return res

# https://leetcode-cn.com/problems/subsets/solution/zi-ji-by-leetcode/
def subsets(self, nums) :
    n = len(nums)
    output = [[]]
    
    for num in nums:
        output += [curr + [num] for curr in output]
    
    return output

