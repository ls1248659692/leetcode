# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        unit = 1
        def trs(nd,order,nullv,dd):
            if not nd:return [nullv+[order]+[dd]]
            elif not nd.left and not nd.right: res= [[nd.val,order]+[dd*unit]]
            else:
                res= [[nd.val,order]+[dd]] + trs(nd.left,'r%d'%nd.val,nullv,dd+1) + trs(nd.right,'r%d'%nd.val,nullv,dd+1)
            return res        
        tli = trs(root,'r%d'%root.val,[None],1) 
        nli = [el[0] for el in tli if el[0] is not None]
        print(tli)        
        return len(set(nli))==1