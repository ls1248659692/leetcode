# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def it(nd,v):
            nonlocal par,direct
            while nd:
                if v<nd.val: par,direct,nd =nd,'L',nd.left
                else: par,direct,nd= nd,'R',nd.right
            print(nd,par.val)
            if par:
                if direct=='L': 
                    par.left=TreeNode(v)
                if direct=='R': 
                    par.right=TreeNode(v)   
                                 
        par,direct=None,''
        if not root:return TreeNode(val)
        it(root,val)     
        return root
