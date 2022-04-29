# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        td = TreeNode(val)
        def trav(node,par):
            nonlocal root,td
            if td.left:return
            if not node: 
                par.right=td
                td.left=1
                return
            if node.val<val:
                td.left=node
                if not par: root= td
                if  par and par.left == node:par.left =td
                if  par and par.right == node:par.right =td
            else:
                trav(node.right,node)
                #trav(node.left,node)

        trav(root,None)
        if td.left==1: td.left=None
        return root
                
