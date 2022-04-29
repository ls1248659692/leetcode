# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    import random
    def __init__(self, head: Optional[ListNode]):
        def lkl2ls(lkn):
            tli =[]
            while lkn: 
                tli.append(lkn)
                lkn= lkn.next
            return tli
        self.tls = lkl2ls(head)

    def getRandom(self) -> int:
        r=random.randint(0,len(self.tls)-1)
        return self.tls[r].val



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()