def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1):   # 外循环控制遍历的次数
        for j in range(n-1-i):  # 内循环控制遍历到哪一位
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1],nums[j]  # 如果后一个数比前一个数大，两个数就交换位置
    return nums  # 在全部遍历完以后，返回排序好的列表

