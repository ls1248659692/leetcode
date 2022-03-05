# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        def mylist(ca):
            sa =[]
            while ca:
                sa.append(ca)
                ca =ca.next
            return sa       
        lst = mylist(head)
        if not lst:return None 
        d={}
        for e in lst:
            d[e.val]= d.get(e.val,0)+1
        single = [k for k,v in d.items() if v>=2]
        l2 = [e for e in lst if e.val not in single]
        if not l2:return None
        for i in range(len(l2)-1):
            l2[i].next=l2[i+1]
        l2[-1].next=None
        return l2[0]