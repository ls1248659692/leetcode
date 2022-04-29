class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        dp = [nums[0]]+ [0] * (len(nums)-1)
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+ nums[i], nums[i]) if nums[i] > nums[i-1] else nums[i]
        return max(dp)