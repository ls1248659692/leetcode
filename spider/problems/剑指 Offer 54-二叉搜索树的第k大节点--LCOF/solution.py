# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        unit = 1
        def trs(nd,order,nullv,dd):
            if not nd:return [nullv+[dd]]
            elif not nd.left and not nd.right: res= [[nd.val]+[dd*unit]]
            else:
                if order=='pre':
                    res= [[nd.val]+[dd]] + trs(nd.left,order,nullv,dd+1) + trs(nd.right,order,nullv,dd+1)
            return res        
        tli = trs(root,'pre',[None],1)     
        print(tli)
        return sorted([el[0] for el in tli if el[0] is not None])[-k]   