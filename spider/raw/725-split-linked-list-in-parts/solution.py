# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        def lkl2ls(lkn):
            tli =[]
            while lkn: 
                tli.append(lkn)
                lkn= lkn.next
            return tli
        tls = lkl2ls(head) 
        base=len(tls)//k 
        lft=len(tls)-base*k     
        print(base,lft)
        nls=[]
        i=0
        while i<len(tls):
            lent = base+1 if len(nls)<lft else base
            print('i=%slent=%s'%(i,lent))
            nls.append(tls[i])
            if i+lent-1<len(tls):tls[i+lent-1].next=None
            i += lent
        while len(nls)<k: nls.append(None)
        return nls