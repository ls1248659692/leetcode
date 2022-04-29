class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n= len(text1),len(text2)
        dp = [[0 ]*(n+1) for _ in range(1+m)]
        for i in range(1,1+m):
            for j in range(1,1+n):
                dp[i][j] = max(dp[i-1][j] ,dp[i][j-1] ,dp[i-1][j-1] +(text1[i-1] == text2[j-1]))
        #return max([e for row in dp for e in row])
        return dp[-1][-1]        