# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def pt(nd,nullval):
            if not nd:return nullval
            elif not nd.left and not nd.right: res= [ nd]
            else:res= [nd] + (pt(nd.left,nullval) if nd.left else nullval)+ (pt(nd.right,nullval) if nd.right else nullval)
            return res
        res= pt(root,[])        
        print(res)
        for i in range(len(res)-1):
            res[i].right=res[i+1]
            res[i].left=None