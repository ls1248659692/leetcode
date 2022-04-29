# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        def lkl2ls(lkn):
            tli =[]
            while lkn:
                tli.append(lkn)
                lkn= lkn.next
            return tli
        tls = lkl2ls(head)   
        tls = [e for e in tls if e.val < x] +[e for e in tls if e.val >= x]    
        if not tls :return None
        tls[-1].next=None
        for i in range(len(tls)-1):
            tls[i].next=tls[i+1]
        return tls[0]        