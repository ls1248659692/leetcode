# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        tls = []
        left,right=left-1,right-1
        while head:
            tls.append(head)
            head =head.next
        tls[left].next= None
        for i in range(left+1,right+1):
            print('chg',tls[i].val,tls[i-1].val)
            tls[i].next=tls[i-1]
        if right+1 <len(tls):tls[left].next=tls[right+1]
        print(left,right)
        if left-1>=0: tls[left-1].next=tls[right]
        return tls[0] if left-1>=0 else tls[right]