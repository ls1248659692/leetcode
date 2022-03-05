# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        def mylist(ca):
            sa =[]
            while ca:
                sa.append(ca)
                ca =ca.next
            return sa       
        lst = mylist(head)
        if not lst:return None 
        d,l2={},[]
        for e in lst:
            if e.val not in d:
                l2.append(e)
            d[e.val]= d.get(e.val,0)+1
        if not l2:return None
        for i in range(len(l2)-1):
            l2[i].next=l2[i+1]
        l2[-1].next=None
        return l2[0]        