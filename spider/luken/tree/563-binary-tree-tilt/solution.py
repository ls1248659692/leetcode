# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        ut= 1
        def trs_v3(nd,nullv,dd):
            if not nd:return [nullv+[0,0]]
            elif not nd.left and not nd.right: res= [[nd.val]+[nd.val,0]] 
            else:
                left = trs_v3(nd.left,nullv,dd)
                rigt = trs_v3(nd.right,nullv,dd)
                res = left + rigt + [[nd.val]+[nd.val+left[-1][1]+rigt[-1][1],abs(left[-1][1]-rigt[-1][1])]] 
            return res        
        if not root: return 0
        
        tli = trs_v3(root,[None],1)
        print (tli)
        return  sum(el[2] for el in tli) 