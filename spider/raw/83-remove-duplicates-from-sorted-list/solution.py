# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        t = head
        if not t or not t.next: return t
        cli =[t]
        while t.next:
            t=t.next
            if cli and t.val ==cli[-1].val:
                cli[-1].next=t.next   
            else:         
                cli.append(t)
            
            
        if cli and t.val ==cli[-1].val: cli[-1].next=t.next
        return cli[0]