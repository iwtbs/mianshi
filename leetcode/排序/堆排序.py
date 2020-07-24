def heap_sort(ary):
	n = len(ary)
	first = int(n/2-1)    #最后一个非叶子节点
	for start in range(first,-1,-1):    #构建最大堆
		max_heapify(ary,start,n-1)
	for end in range(n-1,0,-1):    #堆排，将最大跟堆转换成有序数组
		ary[end],ary[0] = ary[0], ary[end]    #将根节点元素与最后叶子节点进行互换，取出最大根节点元素，对剩余节点重新构建最大堆
		max_heapify(ary,0,end-1)    #因为end上面取的是n-1，故而这里直接放end-1，相当于忽略了最后最大根节点元素ary[n-1]
	return ary


#最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
#start为当前需要调整最大堆的位置，end为调整边界
def max_heapify(ary,start,end):
	root = start
	while True:
		child = root * 2 + 1    #调整节点的子节点
		if child > end:
			break
		if child + 1 <= end and ary[child] < ary[child+1]:
			child = child + 1   #取较大的子节点
		if ary[root] < ary[child]:    #较大的子节点成为父节点
			ary[root], ary[child] = ary[child], ary[root]    #交换
			root = child
		else:
			break


# 第k大的数
class Solution(object):
    def findKthLargest(self, nums, k):
        # 替换nums[i]后维护最小堆：自顶向下调整新元素位置，直至该值满足(parent value < son value)
        def shift(i,k):
            flag=0
            while (i*2+1)<k and flag==0 :
                t=i
                if nums[i]>nums[2*i+1]:            
                    t=2*i+1
                if (i*2+2)<k and nums[t]>nums[2*i+2]  :            
                    t=2*i+2
                if t==i:
                    flag=1
                else :
                    nums[i],nums[t]=nums[t],nums[i]
                    i=t  
        
        #O(k):建立大小为K的最小堆， k/2-1是最后一个非叶节点，因为shift是向下调整，所以倒序从最下面出发，不然(4 32 1)->(2 34 1)->(2 14 3)->(2 14 3) 结果不对
        for i in range(k/2,-1,-1):
            shift(i,k)

        #O((N-k)logK)，剩余元素依次比较替换
        for i in range(k,len(nums)):
            if nums[0]<nums[i]:
                nums[0]=nums[i]
                shift(0,k)
        return nums[0]
        #sum=O(Nlogk-k(logK-1))