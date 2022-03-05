# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        tli =[]
        while head.next:
            tli.append(head)
            head=head.next
        tli.append(head)
        return tli[len(tli)//2 + (0 if len(tli)%2 else 0)]