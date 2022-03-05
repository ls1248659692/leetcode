# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def midt(node):
            if not node: 
                tli.append(None)
            else:
                if node.left: midt(node.left)       
                tli.append(node.val)      
                if node.right: midt(node.right)  

        tli=[]   
        midt(root)
        return len(tli) if root else 0     