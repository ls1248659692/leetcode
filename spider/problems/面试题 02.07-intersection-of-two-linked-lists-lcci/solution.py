# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def mylist(ca):
            sa =[]
            while ca:
                sa.append(ca)
                ca =ca.next
            return sa

        la = mylist(headA)
        lb = mylist(headB)
        sb = set(lb)
        intv =None
        for a in la[::-1]:
            if a not in sb: 
                break
            else:
                intv =a

        return intv       