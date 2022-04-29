# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        tli =[]
        def sh(nd):
            #print(nd.val,tli)
            if low<=nd.val<=high:tli.append(nd.val)
            if nd.left: sh(nd.left)
            if nd.right: sh(nd.right)
        sh(root)
        return sum(tli) if tli else 0       