'''
给定 1->2->3->4, 你应该返回 2->1->4->3.

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/bi-jiao-zhi-jie-gao-xiao-de-zuo-fa-han-tu-jie-by-w/
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = ListNode(-1)
        pre.next = head
        p = pre
        while p.next and p.next.next:
            a,b = p.next,p.next.next
            p.next = b
            temp = b.next
            b.next = a
            a.next = temp
            p = p.next.next
        return pre.next