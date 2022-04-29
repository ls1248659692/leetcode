"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def lkl2ls(lkn):
            tli =[]
            while lkn: 
                tli.append(lkn)
                lkn= lkn.next
            return tli
        tls = lkl2ls(head)
        if not tls:return None
        randidx = [ tls.index(e.random) if e.random is not None else None for e in tls]
        nls =[Node(nd.val) for nd in tls] 
        for i in range(len(nls)-1):
            nls[i].next= nls[i+1]
            if randidx[i] is not None: nls[i].random=nls[randidx[i]] 
        if randidx[-1] is not None: nls[-1].random=nls[randidx[-1]]     
        return nls[0]
           
                