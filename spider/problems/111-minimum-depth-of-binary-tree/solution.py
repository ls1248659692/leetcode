# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        unit = 100000
        def trs(nd,order,nullv,dd):
            if not nd:return [nullv+[dd]]
            elif not nd.left and not nd.right: res= [[nd.val]+[dd*unit]]
            else:
                if order=='pre':
                    res= [[nd.val]+[dd]] + trs(nd.left,order,nullv,dd+1) + trs(nd.right,order,nullv,dd+1)
                if order=='pos':
                    res = trs(nd.left,order,nullv,dd+1) + trs(nd.right,order,nullv,dd+1) +[[nd.val]+[dd]]
            return res        
        tli = trs(root,'pre',[None],1)
        #print(tli)
        return min(el[1]//unit for el in tli if el[1]>=unit) if root else 0