# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        def v1(node): 
            tli,stk=[],[]
            while node or stk:
                while node and (stk.append(node) or node): node = node.left  
                #print([e.val for e in stk])
                node = stk.pop()
                tli.append(node)
                node = node.right 
            return tli   
        tls = v1(root)    
        for i in range(len(tls)):
            tls[i].right = None if i == len(tls)-1 else tls[i+1]
            tls[i].left = None
        return tls[0] if root else None       