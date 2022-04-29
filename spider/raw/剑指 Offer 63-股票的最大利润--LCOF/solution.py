class Solution:
    def maxProfit(self, pr: List[int]) -> int:
        if not pr: return 0
        mipr,mxprof=pr[0],0
        for p in pr[1:]:
            mxprof,mipr = max(p - mipr,mxprof),min(p,mipr)
        return mxprof