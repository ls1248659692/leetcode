class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def v1(prices):
            prs = prices
            nli = [[0,prs[0],0,prs[0]]] # ii,pr,mxprof, max,min
            for ii in range(1,len(prs)):
                if prs[ii]>nli[-1][-1]:
                    mxp = prs[ii]-nli[-1][-1]
                    mxp = mxp if mxp>nli[-1][-2] else nli[-1][-2]
                else:
                    mxp = nli[-1][-2]
                tmin = prs[ii] if prs[ii]<nli[-1][-1] else nli[-1][-1]
                nli.append([ii,prs[0],mxp,tmin])
            return max([el[2] for el in nli])
            
        def v2(pr):
            if not pr: return 0
            mipr,mxprof=pr[0],0
            for p in pr[1:]:
                mxprof,mipr = max(p - mipr,mxprof),min(p,mipr)
            return mxprof
          

        def v3(pr):
            dp = [pr[0]]*len(pr)
            for i in range(len(pr)):
                dp[i]= min(pr[i],dp[i-1])
            return max([pr[i]-dp[i] for i in range(len(pr))])

        return v3(prices)              
                