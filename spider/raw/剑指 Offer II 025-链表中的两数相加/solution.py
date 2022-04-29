# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def lkl(ls):
            lkn = ListNode(ls[0])
            head =lkn
            for n in ls[1:]:
                lkn.next=ListNode(n)
                lkn=lkn.next
            return head

        # def lkl2ls(lkn):
        #     tli =[]
        #     while lkn: 
        #         tli.append(lkn.val)
        #         lkn= lkn.next
        #     return tli

        # def lkl2str(lkn):
        #     tli =[]
        #     while lkn or (tli.append(lkn.val) and lkn ):  lkn= lkn.next
        #     return ''.join([str(e) for e in tli])

        str1,str2 = '','' 
        while l1: l1,str1 = l1.next,str(l1.val) + str1
        while l2: l2,str2 = l2.next,str(l2.val) + str2
            
        result = str(int(str1[::-1]) + int(str2[::-1]))
        return lkl([int(i) for i in result])        