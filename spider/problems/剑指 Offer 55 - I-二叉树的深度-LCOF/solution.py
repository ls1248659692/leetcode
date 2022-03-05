# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def trs(nd,order,nullv,dd):
            if not nd:return [nullv+[dd]]
            elif not nd.left and not nd.right: res= [[nd.val]+[dd*100000]]
            else:
                if order=='pre':
                    res= [[nd.val]+[dd]] + trs(nd.left,order,nullv,dd+1) + trs(nd.right,order,nullv,dd+1)
                if order=='pos':
                    res = trs(nd.left,order,nullv,dd+1) + trs(nd.right,order,nullv,dd+1) +[[nd.val]+[dd]]
            return res        
        tli = trs(root,'pre',[None],1)
        #print(tli)
        return max(el[1]//100000 for el in tli if el[1]>=100000) if root else 0        