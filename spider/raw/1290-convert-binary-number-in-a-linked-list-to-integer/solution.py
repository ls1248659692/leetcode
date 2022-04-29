# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s =''
        while head.next:
            s+= str(head.val)
            head=head.next
        s+= str(head.val)
        return int(s, base=2)