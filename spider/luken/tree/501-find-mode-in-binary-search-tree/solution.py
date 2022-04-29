# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        unit = 1
        def trs(nd,order,nullv,dd):
            if not nd:return [nullv+[order]+[dd]]
            elif not nd.left and not nd.right: res= [[nd.val,order]+[dd*unit]]
            else:
                res= [[nd.val,order]+[dd]] + trs(nd.left,'r%d'%nd.val,nullv,dd+1) + trs(nd.right,'r%d'%nd.val,nullv,dd+1)
            return res        
        tli = trs(root,'r%d'%root.val,[None],1) 
        print(tli)       
        tli = [tt for tt in tli if tt[0] is not None]
        nli = [tt[0] for tt in tli]
        ctli = [(n,nli.count(n)) for n in set(nli)]     
        print(ctli)   
        maxct = max(el[1] for el in ctli)
        return [el[0] for el in ctli if el[1]==maxct]