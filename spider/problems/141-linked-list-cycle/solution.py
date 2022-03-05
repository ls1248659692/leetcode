# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:return False
        n_li =[]
        while head.next and len(n_li)<10**4+1:
            n_li.append(head.val)
            head = head.next
        print(len(n_li))
        return len(n_li)==10**4+1