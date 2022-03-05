# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        def lkl2ls(lkn):
            tli =[]
            while lkn: 
                tli.append(lkn)
                lkn= lkn.next
            return tli
        tls = lkl2ls(head)
        nums = [e.val for e in tls]
        nls,stk = [0]*len(nums),[]
        ln= len(tls)

    


        for i in range(ln):
            #print(nums[i],stk)
            while stk and nums[i]>stk[-1][0]:
                nls[stk[-1][1]]=nums[i]
                stk.pop()
            stk.append((nums[i],i))
  
        return nls