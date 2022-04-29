# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        unit = 1
        def trs(nd,order,nullv,dd):
            if not nd:return [nullv+[order]+[dd]]
            elif not nd.left and not nd.right: res= [[nd.val,order[1:]+str(nd.val)]+[dd*unit]]
            else:
                res= [[nd.val,order+'%d'%nd.val]+[dd]] + trs(nd.left,order+'%d'%nd.val,nullv,dd+1) + trs(nd.right,order+'%d'%nd.val,nullv,dd+1)
            return res        
        tli = trs(root,'r',[None],1) 
        print(tli)        

        def bi2nu(str):
            return sum (2**i*int(str[len(str)-1-i]) for i in range(len(str)))
        lfli = [bi2nu(el[1]) for el in tli if el[1][0]!='r']
        print(lfli)
        return sum(lfli)

        