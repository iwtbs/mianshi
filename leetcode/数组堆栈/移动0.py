'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
'''
def moveZeroes(self, nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # 循环遍历数组，当遇到非零元素则开始交换慢指针所指的0元素
    # i 为慢指针 指向最新一个0元素的位置
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums
