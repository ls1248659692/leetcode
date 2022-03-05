# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def toli(head):
            tli =[]
            while head.next:
                tli.append(head)
                head = head.next
            tli.append(head)
            return tli

        if not head:return None
        tli = toli(head)      
        if len(tli)==1:return head
        if k==1: return head

        md = len(tli)% k
        for i in range(0,len(tli)-md,k):
            if md!=0 and i+k>= len(tli)-md-1:
                 tli[i].next =tli[i+k]
            else:
                tli[i].next =tli[i+2*k-1] if i+2*k-1 < len(tli) else None
            for t in range(1,k):
               tli[i+t].next = tli[i+t-1]

        return  tli[k-1]        