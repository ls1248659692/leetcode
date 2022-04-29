# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def binsrt(ls,k):
            if not ls or ls[-1][1].val<=k[1].val: 
                ls.append(k)
            else:
                for i in range(len(ls)):
                    if ls[i][1].val>=k[1].val: 
                        ls.insert(i,k)
                        break
            #print('len_ls=%s'%len(ls))

        ls =[e for e in lists if e is not None]        
        if not ls:return None
        if len(ls)==1:return ls[0]
        pls,nls,vls = [(i,ls[i]) for i in range(len(ls))],[],[]
        pls = sorted(pls,key=lambda x:x[1].val)
        #print(pls)
        cnt=1000000
        while cnt and pls:
            cnt-=1
            lsi,nd = pls.pop(0)
            #print('cnt=%s p1=%s lsi=%s'%(cnt,len(pls),lsi))
            if nls:nls[-1].next=nd
            nls.append(nd)
            vls.append(nd.val)
            #print(vls)
            if ls[lsi].next:
                ls[lsi] = ls[lsi].next 
                binsrt(pls,(lsi,ls[lsi]))
            else:
                print('end_nd%s'%lsi)
        return nls[0] 