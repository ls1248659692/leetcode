# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        def lkl2ls(lkn):
            tli =[]
            while lkn and lkn not in tli: 
                tli.append(lkn)
                lkn= lkn.next
            return tli
        tls = lkl2ls(head)
        print([e.val for e in tls])
        if not tls or tls[-1].next is None:return None
        for i in range(len(tls)):
            if tls[i]==tls[-1].next:
                return tls[i]
        # print()
        # return tls[1]