'''
解法二：利用快速排序的分区思想
构建分区函数 partition
将数组 A[left, right+1] 进行分区，随机选择分区位置 pivot_idx，其对应元素值为 pivot_value
函数返回下标位置 new
位于 A[left, new] 中的元素均大于 pivot_value
位于 A[new+1, right+1] 中的元素均小于 pivot_value
初始化 left，right 为数组 A 左右位置边界
调用分区函数，直到返回的下标位置为 k-1，其对应元素即为数组中的第 k 个最大元素
若 new 值大于 k-1，则去数组左边继续找；若小于，则去数组右边找

'''
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        def partition(left, right):
            pivot = nums[left]
            l = left + 1
            r = right
            while l <= r:
                if nums[l] < pivot and nums[r] > pivot:
                    nums[l], nums[r] = nums[r], nums[l]
                if nums[l] >= pivot:
                    l += 1
                if nums[r] <= pivot:
                    r -= 1
            nums[r], nums[left] = nums[left], nums[r]
            return r
        left = 0
        right = len(nums) - 1
        while 1:
            idx = partition(left, right)
            if idx == k - 1:
                return nums[idx]
            if idx < k - 1:
                left = idx + 1
            if idx > k - 1:
                right = idx - 1
