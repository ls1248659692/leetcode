# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:return None
        tls = []
        while head:
            tls.append(head)
            head =head.next       
        
        k=k%len(tls)

        nt=tls[-k:]+tls[:-k]
        for i in range(len(nt)-1):
            nt[i].next=nt[i+1]
        nt[-1].next=None
        return nt[0]