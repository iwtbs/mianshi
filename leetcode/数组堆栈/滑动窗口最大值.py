'''
1、滑动窗口时，每滑动一次，会新加入一个数，同时丢掉一个数。因此需要解决三个数的大小问题，即：当前窗口的最大值、窗口往右滑动时新加入的值和丢掉的值。
2、用一个变量temp记录当前窗口的最大值，先比较新加入的数会不会改变当前窗口的最大值temp,若新加入的数大于temp,更新temp，窗口右滑；新加入的数小于temp，
需要比较丢弃的数与temp的大小，若即将丢弃的数等于temp，意味着这个即将被丢弃的数就是当前窗口的最大值，需要先滑动窗口然后重新找到窗口最大值，
如果即将丢弃的数小于当前窗口最大值，temp不变，窗口右滑即可
3、我这里循环退出时还有最后一个窗口的最大值没有加到ans列表中，故退出循环需要加上temp。
'''

def maxSlidingWindow(self, nums, k: int) :
    n = len(nums)
    if n == 0:
        return []
    ans = []
    temp = max(nums[:k])
    for i in range(n-k):
        ans.append(temp)
        if nums[i+k] > temp:
            temp = nums[i+k]
        else:
            if nums[i] == temp:
                temp = max(nums[i+1:i+1+k])
    ans.append(temp)
    return ans
