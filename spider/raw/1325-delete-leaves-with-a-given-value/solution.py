# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def rln(node):
            if node:
                rln(node.left)
                rln(node.right)
                for i,c in enumerate( [node.left,node.right]):
                    if c and not c.right and not c.left and c.val==target: 
                        if i==0:node.left=None
                        else:node.right=None

        
        rln(root)
        return root if root.left or root.right or root.val!=target else None