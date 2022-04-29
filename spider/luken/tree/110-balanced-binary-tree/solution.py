# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        ut= 1
        def trs_v3(nd,nullv,dd):
            if not nd:return [nullv+[0,0]]
            elif not nd.left and not nd.right: res= [[nd.val]+[1,1]] 
            else:
                left = trs_v3(nd.left,nullv,dd)
                rigt = trs_v3(nd.right,nullv,dd)
                res = left + rigt + [[nd.val]+[max(left[-1][1:])+1,max(rigt[-1][1:])+1]] 
            return res        
        if not root: return True
        
        tli = trs_v3(root,[None],1)
        print (tli)
        return True if sum(abs(el[1]-el[2])>1 for el in tli)==0 else False   