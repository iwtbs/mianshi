'''
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
'''
def rob(self, nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])
    for i in range(2,n):
        dp[i] = max( dp[i-2]+nums[i], dp[i-1] ) 
    return dp[-1]

'''
所有的房屋都围成一圈，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警
'''
def rob1(self, nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])
    for i in range(2,n):
        dp[i] = max( dp[i-2]+nums[i], dp[i-1] ) 
    return dp[-1]

def rob2(self, nums):
    if len(nums) == 1:
        return nums[0]
    a1 = self.rob1(nums[:-1])
    a2 = self.rob1(nums[1:])
    return max(a1,a2)

'''
这个地方的所有房屋的排列类似于一棵二叉树
'''
def rob3(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    def robInternal(root):
        if not root: return [0] * 2
        left, right = robInternal(root.left), robInternal(root.right)
        return [max(left) + max(right), left[0] + right[0] + root.val]

    return max(robInternal(root))