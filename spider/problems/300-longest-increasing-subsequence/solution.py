class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1,dp[i])
        return max(dp)