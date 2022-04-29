# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        unit = 1
        def trs(nd,order,nullv,dd):
            if not nd:return [nullv+[order+'-',dd]]
            elif not nd.left and not nd.right: res= [[nd.val,order+'d']+[dd*unit]]
            else:
                res = trs(nd.left,'l',nullv,dd+1) + trs(nd.right,'r',nullv,dd+1) +[[nd.val,order+'t']+[dd]]
            return res        
        tli = trs(root,'o',[None],1) 
        print(tli)
        vli = []
        mindp = 10000
        last_t = None
        for i in range(len(tli)):

            if tli[i][0] in [p.val,q.val]:
                vli.append(list(tli[i]))
            if len(vli)==2:
                if tli[i][-1]< mindp:
                    last_t = list(tli[i])
                    break
            if vli: 
                if mindp> tli[i][-1]: mindp = tli[i][-1]
        print(vli,last_t)
        val =last_t[0]
        tgli =[]

        def se(nd):
            if tgli:return
            if nd.val== val:tgli.append(nd)
            if nd.left:se(nd.left)
            if nd.right:se(nd.right)
        se(root)        
        return tgli[-1]        