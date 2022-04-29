class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        new_nums = nums[:(len(nums)-k+1)]
        max_idx = new_nums.index(max(new_nums))
        return nums[max_idx:max_idx+k]
