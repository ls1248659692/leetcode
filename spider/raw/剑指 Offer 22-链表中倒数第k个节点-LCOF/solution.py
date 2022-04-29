# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        t = head
        cli =[]
        while t.next:
            cli.append(t)
            t=t.next
        cli.append(t)
        return cli[-k] if len(cli)>=k else cli[-k]