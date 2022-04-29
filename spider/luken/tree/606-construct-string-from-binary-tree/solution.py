# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def t2s(root):
            if not root.left and not root.right: return '(%s)'%root.val
            return '(%s%s%s)'%(root.val , '()'if not root.left else t2s(root.left), '' if not root.right else t2s(root.right))
        return t2s(root)[1:-1]