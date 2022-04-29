# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def isinc(p,q):
            if None in [p,q]:
                return  p==q  
            else:
                return p.val==q.val and (isinc(p.left,q.left) if q.left else True) and (isinc(p.right,q.right) if q.right else True) 

        def search(node,q):
            stk=[]
            while node or stk:
                while node and (stk.append(node) or node): node = node.left  
                #print([e.val for e in stk])
                node = stk.pop()
                if node.val ==q.val:
                    if isinc(node,q): return True
                node = node.right 
            return False
            
        return search(A,B) if B else False              