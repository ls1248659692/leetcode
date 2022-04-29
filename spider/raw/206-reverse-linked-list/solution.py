# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        h_li=[]
        tmp_h = head
        if not tmp_h: return None
        while tmp_h.next:
            h_li.append(tmp_h.val)
            tmp_h =tmp_h.next
        h_li.append(tmp_h.val)
        h_li.reverse()
        # print(h_li)
        r_ln = ListNode(h_li[-1])
        for ii in range(len(h_li)-2,-1,-1):
            r_ln = ListNode(h_li[ii],r_ln)
        # print(r_ln)
        return r_ln
