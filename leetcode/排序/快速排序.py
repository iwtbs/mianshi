def ks(nums):
    if len(nums) < 2:
        return nums
    mid = nums[0]
    left,right = [],[]
    for i in range(1,len(nums)):
        if nums[i] > mid:
            right.append(nums[i])
        else:
            left.append(nums[i])
    return ks(left) + [mid] + ks(right)

        