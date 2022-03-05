# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        unit = 1
        sm = []

        def trs(nd,order,nullv,dd):
            if not nd:return [nullv+[dd]]
            elif not nd.left and not nd.right: 
                res= [[nd.val]+[dd*unit]]
                if order=='left': sm.append(nd.val)
            else:
                res= [[nd.val]+[dd]] + trs(nd.left,'left',nullv,dd+1) + trs(nd.right,'right',nullv,dd+1)
            return res        
        tli = trs(root,'root',[None],1)  
        print(sum(sm))
        return sum(sm)      