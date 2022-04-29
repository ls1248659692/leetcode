# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def lkl2ls(lkn):
            tli =[]
            while lkn: 
                tli.append(lkn)
                lkn= lkn.next
            return tli
        tls = lkl2ls(head)
        if not tls :return None
        for i in range(len(tls)): tls[i].next=None

        nt = []
        n= len(tls)-1
            
        for i in range((len(tls)+1)//2):
            nt.append(tls[i])
            if n-i!=i: nt.append(tls[n-i])

        tls = nt
        
        tls[-1].next=None
        for i in range(len(tls)-1):
            tls[i].next=tls[i+1]
        head= tls[0]
        return head        