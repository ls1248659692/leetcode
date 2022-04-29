# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        def iseq(p,q):
            return  p==q if None in [p,q] else p.val==q.val and iseq(p.left,q.left) and iseq(p.right,q.right)
        def search(node,q):
            stk=[]
            while node or stk:
                while node and (stk.append(node) or node): node = node.left  
                node = stk.pop()
                if node.val ==q.val:
                    if iseq(node,q): return True
                node = node.right 
            return False
            
        return search(t1,t2) if t2 else False                    