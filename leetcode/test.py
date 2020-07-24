def find_k(nums):
    fangcha_min = 0
    re = 0
    # 求总和
    sum_all = sum(nums)
    sum_all_pingfang = 0
    for i in nums:
        sum_all_pingfang += i*i
    # 从左往右算
    sum_left = 0
    sum_left_pingfang = 0
    for i in range(len(nums)):
        sum_left += nums[i]
        sum_left_pingfang += nums[i]*nums[i] 
        sum_right = sum_all - sum_left
        sum_right_pingfang = sum_all_pingfang - sum_left_pingfang
        fangcha_sum = sum_left_pingfang/(i+1) - sum_left*sum_left + sum_right_pingfang/(len(nums)-i-1) -sum_right*sum_right
        if fangcha_sum > fangcha_min:
            fangcha_min = fangcha_sum
            re = i      
    return re

print(find_k([1,2,3,4]))