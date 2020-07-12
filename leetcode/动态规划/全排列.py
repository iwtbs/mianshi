'''
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
'''
# 数组
class Solution:
    def permuteUnique(self, nums) :
        res=[]
        nums.sort()
        def helper(nums,temp):
            if not nums:
                res.append(temp)
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                helper(nums[:i]+nums[i+1:],temp+[nums[i]])
        helper(nums,[])
        return res

# 字符串
class Solution1:
    def permutation(self, s: str):
        if not s: return 
        s=list(sorted(s))
        res=[]
        def helper(s,tmp):
            if not s: res.append(''.join(tmp))
            for i,char in enumerate(s):
                if i>0 and s[i]==s[i-1]:
                    continue
                helper(s[:i]+s[i+1:],tmp+[char])
        helper(s,[])
        return res
