# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        def mylist(ca):
            sa =[]
            while ca:
                sa.append(ca)
                ca =ca.next
            return sa       
        lst = mylist(head)
        for i,ln in enumerate(lst):
            if ln.val==val:
                if i>=1:
                    lst[i-1].next=ln.next
                    ln.next=None
                    return lst[0]
                else:
                    return lst[1]