# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n==1 and not head.next:return None
        tli =[]
        while head.next:
            tli.append(head)
            head = head.next
        tli.append(head)
        print(len(tli))
        if n>len(tli):return None
        if n==len(tli):return tli[1]
        tli[-n-1].next = tli[-n+1] if n>1 else None
        return tli[0]