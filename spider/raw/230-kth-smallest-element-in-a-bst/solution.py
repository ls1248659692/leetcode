# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def midt(node):
            if not node: 
                pass
                #tli.append(None)
            else:
                if node.left: midt(node.left)       
                tli.append(node.val)      
                if node.right: midt(node.right)  

        tli=[]   
        midt(root)
        print(tli)
        return tli[k-1] if root else []       