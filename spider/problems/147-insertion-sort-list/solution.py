# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        def lkl2ls(lkn):
            tli =[]
            while lkn: 
                tli.append(lkn)
                lkn= lkn.next
            return tli
        tls = lkl2ls(head)
        tls = sorted(tls,key=lambda xx:xx.val)
        if not tls :return None
        tls[-1].next=None
        for i in range(len(tls)-1):
            tls[i].next=tls[i+1]
        return tls[0]        