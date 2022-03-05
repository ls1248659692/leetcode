# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        tli =[]
        def sh(nd,val):
            #print(nd.val,tli)
            if tli:return
            if nd.val == val:tli.append(nd)
            if nd.left: sh(nd.left,val)
            if nd.right: sh(nd.right,val)
        sh(root,val)
        return tli[-1] if tli else None