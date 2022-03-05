# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        t = head
        if not t or not t.next: return True
        cli =[t.val]
        while t.next:
            t=t.next
            cli.append(t.val)   
        #cli.append(t.val)
        print(cli)
        for i in range(len(cli)//2+1):
            if cli[i-1]!=cli[-i]:return False     
        return True