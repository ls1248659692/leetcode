"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def v1(node): 
            tli,stk=[],[]
            while node or stk:
                while node and (stk.append(node) or node): node = node.left  
                print([e.val for e in stk])
                node = stk.pop()
                tli.append(node)
                node = node.right 
            return tli   
        tls = v1(root)    
        for i in range(len(tls)):
            tls[i].right = tls[0] if i == len(tls)-1 else tls[i+1]
            tls[i].left = tls[-1] if i==0 else tls[i-1]
        return tls[0] if root else None