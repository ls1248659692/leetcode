# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def pt(nd):
            if not nd:return 
            if not nd.left and not nd.right: return nd.val
            t=0
            if nd.left: 
                if not pt(nd.left):
                    nd.left=None
                else :
                    t=1
            if nd.right:
                if not pt(nd.right):
                    nd.right=None
                else:
                    t=1
            return max(t,nd.val)
        pt(root)
        if root.val==0 and not root.right and not root.left:return None
        return root