# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def lkl(ls):
            lkn = ListNode(ls[0])
            head =lkn
            for n in ls[1:]:
                lkn.next=ListNode(n)
                lkn=lkn.next
            return head
            
        str1,str2 = '','' 
        while l1: l1,str1 = l1.next,str(l1.val) + str1
        while l2: l2,str2 = l2.next,str(l2.val) + str2
        print(str1,str2)
        result = str(int(str1) + int(str2)) #
        print(result)
        return lkl([int(i) for i in result[::-1]])          