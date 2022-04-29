class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = -1
        l,r = 0,len(nums)-1
        while l < r:
            if nums[l] + nums[r] < k:
                ans = max(ans, nums[l] + nums[r])
                l += 1
            if nums[l] + nums[r] >= k:
                r -= 1
        return ans
