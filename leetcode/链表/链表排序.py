#归并排序
class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        pre, slow, fast = None, head, head
        #归并排序，找到中间部分
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None #分为两部分
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.merge(l1, l2)
    def merge(self, l1, l2):
        dummy = l = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                l.next, l, l1 = l1, l1, l1.next
            else:
                l.next, l, l2 = l2, l2, l2.next
        l.next = l1 if l1 else l2
        return dummy.next

#快排
'''
将第一个链表第一个结点的值作为左轴，然后向右进行遍历，设置一个small指针指向左轴的下一个元素，然后比较如果比左轴小的话，使small指针指向的数据与遍历到的数据进行交换。最后将左轴元素与small指针指向的元素交换即可。之后就是递归。

单链表的实现为：
1.使第一个节点为中心点.
2.创建2个指针(p,q),p指向头结点,q指向p的下一个节点.
3.q开始遍历,如果发现q的值比中心点的值小,则此时p=p->next,并且执行当前p的值和q的值交换,q遍历到链表尾即可.
4.把头结点的值和p的值执行交换.此时p节点为中心点,并且完成1轮快排
5.使用递归的方法即可完成排序
'''
void quicksort(Linklist head, Linklist end): 
    if head == NULL  or  head == end):            #如果头指针为空或者链表为空，直接返回  
        return 
    int t  
    Linklist p = head.next                 #用来遍历的指针  
    Linklist small = head  
    while(p != end):  
        if p.data < head.data):     #对于小于轴的元素放在左边  
            small = small.next  
            t = small.data  
            small.data = p.data  
            p.data = t   
        p = p.next    
    t = head.data                           #遍历完后，对左轴元素与small指向的元素交换  
    head.data = small.data  
    small.data = t  
    quicksort(head, small)                     #对左右进行递归  
    quicksort(small.next, end)  
}  

