# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        tli=[]
        def se(nd,cnd,q):
             if not nd:return
             if tli:return
             if nd==q:tli.append( cnd)
             se(nd.left,cnd.left,q)
             se(nd.right,cnd.right,q)
        se(original,cloned,target)
        return tli[0]