# 归并排序
def merge_sort(ary):    
    if len(ary) <= 1:
        return ary
        
    median = int(len(ary)/2)    # 二分分解
    left = merge_sort(ary[:median])
    right = merge_sort(ary[median:])
    return merge(left, right)    # 合并数组
    
def merge(left, right):
    #合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组
    res = []
    i = j = 0
    while(i < len(left) and j < len(right)):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
                
    res = res + left[i:] + right[j:]
    return res

