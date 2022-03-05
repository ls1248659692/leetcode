class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        def v2(pr):
            dp = [[0,pr[0],None] for _ in range(len(pr))] #prof min sellpr(Noneè¡¨ç¤ºæ°çäº¤æå¨æ)   
            for i in range(1,len(pr)):
                #print(dp[:i])
                lastDp= dp[i-1][:]
                if lastDp[2] is not None:
                    if lastDp[2]<pr[i]:
                        lastDp[0],lastDp[2]=lastDp[0]+pr[i]-lastDp[2],pr[i]
                    elif lastDp[2]-fee<pr[i]:
                        lastDp[1]=pr[i]
                    else:
                        lastDp[1], lastDp[2]=pr[i],None
                else:
                    if lastDp[1]<pr[i]-fee:
                        lastDp[0],lastDp[2]=lastDp[0]+pr[i]-lastDp[1]-fee,pr[i]
                    elif lastDp[1]>pr[i]:
                        lastDp[1]=pr[i]
                dp[i][0],dp[i][1],dp[i][2]=lastDp
            return dp[-1]          
        return v2(prices)[0]       