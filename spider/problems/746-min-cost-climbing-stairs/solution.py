class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l,r=0,len(cost)
        @lru_cache
        def cst(l,m):
            if r-l in[1]: return cost[l] if m==1 else 0
            else:
                return  min(cst(l+1,1)if m!=1 else float('inf'),cst(l+1,0)+cost[l]) 
        return min(cst(1,1),cst(1,0)+cost[0] )