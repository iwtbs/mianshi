'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次
'''
class Solution:
    def deleteDuplicates(self, head):
        p = head
        if not head or not head.next:
            return head

        while p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head

'''
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现的数字
'''
class Solution1:
    def deleteDuplicates(self, head):
        thead = ListNode('a')
        thead.next = head
        pre,cur = None,thead
        while cur:
            pre=cur
            cur=cur.next
            while cur and cur.next and cur.next.val == cur.val:
                t=cur.val
                while cur and cur.val==t:
                    cur=cur.next
            pre.next=cur
        return thead.next
