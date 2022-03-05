# Definition for a binary tree nd.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def f(nd):
            if nd in cache: return cache[nd]
            if nd is None :return 0
            f1= f(nd.left)+f(nd.right)
            f2= (f(nd.left.left)+f(nd.left.right) if nd.left else 0) +(f(nd.right.left)+f(nd.right.right) if nd.right else 0)+nd.val
            res= max(f1,f2)
            cache[nd]=res
            return res
        cache={}
        return f(root)