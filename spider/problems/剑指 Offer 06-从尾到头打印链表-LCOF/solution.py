# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:return []
        t = head
        cli =[]
        while t:
            cli.append(t.val)
            t=t.next
        cli=cli[::-1]      
        print(cli)
        return cli