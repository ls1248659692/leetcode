# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        def dn(node,up):
            if not node:return
            print(node.val)
            if node.val in to_delete :
                if up and up.left == node: up.left=None
                if up and up.right == node: up.right=None
                if node.left and node.left.val not in to_delete:
                    tli.append(node.left)
                if node.right and node.right.val not in to_delete:
                    tli.append(node.right)
               
            dn(node.left,node)    
            dn(node.right,node)
        tli=[root] if root.val not in to_delete else []
        dn(root,None)
        return tli
