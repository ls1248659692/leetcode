# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(root):
            if not root.left and not root.right: res=[(1,0,root.val)]
            else: 
                dlf = depth(root.left) if root.left else [(0,0,None)]
                drg = depth(root.right)if root.right else [(0,0,None)]
                res = dlf+drg+[(max(dlf[-1][0],drg[-1][0])+1,max(dlf[-1][0],drg[-1][0])-min(dlf[-1][0],drg[-1][0]),root.val)]
            return res
        if not root:return True
        dli = depth(root)
        # print(dli)
        return max(e[1]for e in dli)<=1        