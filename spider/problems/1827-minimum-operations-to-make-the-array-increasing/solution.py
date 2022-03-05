class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        i, cnt = 0, 0
        while i < len(nums)-1:
            if nums[i] >= nums[i+1]:
                cnt += nums[i] - nums[i+1] +1
                nums[i+1] += nums[i] - nums[i+1] +1
            i += 1
        return cnt