# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        li_1=[]
        if list1:
            while list1.next:
                li_1.append(list1.val)
                list1=list1.next
            li_1.append(list1.val)
        if list2:
            while list2.next:
                li_1.append(list2.val)
                list2=list2.next
            li_1.append(list2.val)     

        li_1.sort()
        li_1.reverse() 
        if not li_1:return None
        res = ListNode(li_1[0])
        for el in li_1[1:]:
            res=ListNode(el,next=res)
        return res