# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1,list2=l1,l2
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
