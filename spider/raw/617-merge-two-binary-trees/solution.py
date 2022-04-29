# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def mg(r1,r2):
            if not r1 and not r2:return None 
            elif r1 and not r2: return r1
            elif not r1 and r2: return r2
            else:
                r1.val +=r2.val
                r1.left=mg(r1.left,r2.left)
                r1.right=mg(r1.right,r2.right)
                return r1
            print(r1,r2)
        res = mg(root1,root2)
        return res
