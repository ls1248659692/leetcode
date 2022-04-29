# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def iseq(node,pv):
            if not node: r= 0
            elif not node.left and not node.right: r= 1 if node.val==pv else 0
            else: 
                lft,rht=iseq(node.left,node.val),iseq(node.right,node.val)
                r= max(lft , rht)+1 if node.val==pv else 0
                if tli[0]<max(lft+rht,r):tli[0]=max(lft+rht,r)
            if tli[0]<r:tli[0]=r
            return r

        tli=[0]
        iseq(root,None)
        #print(tli)
        return max(tli) if tli else 0