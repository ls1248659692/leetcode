# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def mylist(ca):
            sa =[]
            while ca:
                sa.append(ca)
                ca =ca.next
            return sa       
        lst = mylist(head)      
        lst = [e.val for e in lst]
        for i in range(1,len(lst)//2+1):
            if lst[i-1]!=lst[-i]:return False
        return True 