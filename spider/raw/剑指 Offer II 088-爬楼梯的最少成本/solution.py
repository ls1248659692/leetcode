class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache ={}
        def cst(c,m):
            if '%d:%d'%(len(c),m) in cache: return cache['%d:%d'%(len(c),m)]
            if len(c) in[1]: return c[0] if m==1 else 0
            elif len(c) in [2] and m==0:return min(c[0],c[1])
            elif len(c) in [2] and m==1:return c[0]+cst(c[1:],0)
            else:
                if m==1: 
                    res =  c[0]+ cst(c[1:],0)
                else:
                    res =  min(cst(c[1:],1),cst(c[1:],0)+c[0])
                cache['%d:%d'%(len(c),m)] =res
                return res
        return min(cst(cost[1:],1),cst(cost[1:],0)+cost[0] )        