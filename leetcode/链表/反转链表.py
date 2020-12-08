class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

#迭代
def reverseList(self, head):
    pre = None
    cur = head
    while cur:
        temp = cur.next   # 先把原来cur.next位置存起来
        cur.next = pre
        pre = cur
        cur = temp
    return pre
