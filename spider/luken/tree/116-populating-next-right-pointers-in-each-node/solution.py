"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        unt =1
        def trs_he(nd,order,nullv,dd):
            if not nd:return [[dd,nullv[0]]]
            elif not nd.left and not nd.right: res= [[dd*unt,nd]]
            else:
                res= [[dd,nd]] + trs_he(nd.left,order,nullv,dd+1) + trs_he(nd.right,order,nullv,dd+1)
            #print(nd,res)
            return res        

        tli = trs_he(root,'pre',[None],1)
        print('...tli=%s'%tli)
        dic = {}
        for tt in tli:
            dic.setdefault(tt[0],[])
            if tt[1] is not None: dic[tt[0]].append(tt[1])
        #print(dic)
        for he,nodes in dic.items():
            for i in range(len(nodes)):
                #print(i,len(nodes))
                nodes[i].next= nodes[i+1] if i<len(nodes)-1 else None

        # if not root:return []
        return root