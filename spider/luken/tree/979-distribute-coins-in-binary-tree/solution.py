# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dbc(nd):
            if not nd: c_act,c_up= (0,0)
            elif not nd.left and not nd.right: c_act,c_up= (abs(nd.val-1),nd.val-1)
            else:
                lft_act,lft_up = dbc(nd.left) 
                rgt_act,rgt_up =  dbc(nd.right) 
                c_up =lft_up+rgt_up +nd.val-1
                c_act= lft_act+rgt_act +abs(c_up)
            return c_act,c_up

        c_act,c_up= dbc(root)
        return c_act