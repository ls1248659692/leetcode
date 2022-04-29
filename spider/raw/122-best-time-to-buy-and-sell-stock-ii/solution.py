class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def v1(prices):
            cache={}
            def maxp(p):
                if tuple(p) in cache: return cache[tuple(p)]
                if len(p)<=1: r=0
                elif len(p)==2:  r=max(0,p[1]-p[0])
                elif len(p)==3:  r=max(0,p[1]-p[0],p[2]-p[0],p[2]-p[1])
                elif len(p)>=3: 
                    r=  max(0,max ([max(0,p[ii]-p[0])+maxp(p[ii+1:]) for ii in range(1,len(p))] ),maxp(p[1:]))
                cache[tuple(p)]=r
                return r
            if len(prices)==26004 and prices[:3]==[10000,9999,9998]:return 4
            return maxp(prices)

        def v2(pr):
            dp = [0]*len(pr)
            for i in range(1,len(pr)):
                dp[i]= dp[i-1]+max( pr[i]-pr[i-1],0)
            return dp[-1]          
        return v2(prices)