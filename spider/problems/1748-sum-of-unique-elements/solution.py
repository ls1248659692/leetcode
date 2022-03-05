class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return  sum([i for i  in nums if nums.count(i) == 1])