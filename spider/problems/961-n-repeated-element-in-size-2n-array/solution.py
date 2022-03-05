class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        for i in nums:
            if nums.count(i) == n:
                return i