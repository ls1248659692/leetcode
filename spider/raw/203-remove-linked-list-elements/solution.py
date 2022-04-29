# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        def c2li(head):
            li =[]
            while head.next:
                li.append(head)
                head=head.next
            li.append(head)
            return li
        if not head:return None
        cli = c2li(head)
        for i in range(len(cli)-1,0,-1):
            if cli[i].val == val:
                cli[i-1].next = cli[i].next
        tcli = [l for l in cli if l.val!=val]
        return tcli[0] if tcli else None