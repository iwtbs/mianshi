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


