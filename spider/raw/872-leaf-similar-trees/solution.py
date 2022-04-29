# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tli =[]
        def tr(nd):
            if not nd:return 
            if not nd.left and not nd.right: tli.append(nd.val)
            tr(nd.left)
            tr(nd.right)
        tr(root1)
        t1 = list(tli)
        tli=[]
        tr(root2)
        t2 = list(tli)
        print('t1=%s,t2=%s'%(t1,t2))
        return  t1==t2