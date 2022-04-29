# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def trs_v2(nd,order,nullv,dd):
            #print(nd)
            if not nd:return [nullv+[dd]]
            elif not nd.left and not nd.right: res= [[nd.val]+[dd+nd.val]]
            else:
                if order=='pre':
                    res= [[nd.val]+[None]] + trs_v2(nd.left,order,nullv,dd+nd.val) + trs_v2(nd.right,order,nullv,dd+nd.val)
            return res        
        tli = trs_v2(root,'pre',[None],0)        
        print(tli)
        return True if root and [el for el in tli if el[0] is not None and el[1]==targetSum]  else False