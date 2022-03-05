# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def lkl2ls(lkn):
            tli =[]
            while lkn: 
                tli.append(lkn)
                lkn= lkn.next
            return tli
        tls = lkl2ls(head)
        i,j = k-1,len(tls)-k
        if i==j:return tls[0]
        if i>j:  i,j= j,i
        if len(tls)==1 or j>=len(tls):return tls[0]
        print(i,j)
        if i==0:
            if i+1!=j:
                tls[j].next=tls[i+1]
                tls[j-1].next=tls[i]
                tls[i].next=None
            else:
                tls[i].next=None
                tls[j].next=tls[i]
            return tls[j]
        else:
            if i+1!=j:
                tls[i].next,tls[j].next=tls[j+1],tls[i+1]
                tls[i-1].next,tls[j-1].next=tls[j],tls[i]                
            else:
                tls[i].next=tls[j+1]
                tls[j].next=tls[i]
                tls[i-1].next=tls[j]
            return tls[0]

        # if k<len(tls) and tls[-k-1]!=tls[j]:
        #     tls[j].next=None
        #     tls[j-1].next=None
        #     tls[-k].next=None
        #     tls[-k-1].next=None
        #     tls[j-1].next= tls[-k]
        #     tls[-k-1].next=tls[j]
        #     tls[j].next=tls[-k+1]
        #     tls[-k].next=tls[j+1]
        # else:
        #     print('23234')
        #     tls[j].next=None
        #     if j-1>=0:tls[j-1].next=None
        #     if j+1<len(tls):tls[j+1].next=None
        #     if j-1>=0: tls[j-1].next= tls[j+1]     
        #     if j+1<len(tls):tls[j+1].next=tls[j]     
        #     if j+2<len(tls):
        #         tls[j].next= tls[j+2] 
        #     else:
        #         return tls[j+1]
            
        return tls[0]