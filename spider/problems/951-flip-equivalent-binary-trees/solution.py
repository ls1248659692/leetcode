# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def eq( r1,r2):
            if None in (r1,r2): return r1==r2
            if r1.val!=r2.val:return False
            return (eq(r1.left,r2.left) and eq(r1.right,r2.right)) or (eq(r1.left,r2.right) and eq(r1.right,r2.left))

        return eq(root1,root2) 