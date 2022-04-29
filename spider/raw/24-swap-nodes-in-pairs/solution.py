# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def lkl2ls(lkn):
    tli = []
    while lkn:
        tli.append(lkn)
        lkn = lkn.next
    return tli

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        tli = lkl2ls(head)
        # if len(tli)<=1:return head
        mod = len(tli)%2
        for i in range(0,len(tli)-mod,2):
            tli[i+1].next, tli[i].next =tli[i], tli[i+3-(mod if mod and i+3-mod==len(tli)-1 else 0)] if i+3-mod < len(tli) else None
        return tli[1] if len(tli)>1 else head  