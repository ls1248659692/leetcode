class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dif = [nums[i]-nums[i-1] for i in range(1,len(nums))]
        dp,qf=[1]+[0]*(len(dif)-1),0
        #print(dif,dp)
        for i in range(1,len(dif)):
            #print(dp[:i],dif[:i+1])
            if dif[i]==dif[i-1]: 
                dp[i]=dp[i-1]+1
                if dp[i]>=2:qf+=(dp[i]-1)
            else:
                dp[i]=1
        #print(dp,dif)
        return qf if len(dif)>=2 else 0