# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root.left and not root.right: return ['%d'%root.val]
        else:
            res =[]
            if root.left: 
                res.extend(['%d->'%root.val + path for path in  self.binaryTreePaths(root.left)])
            if root.right: 
                res.extend(['%d->'%root.val + path for path in self.binaryTreePaths(root.right)])
            return res