class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(nums.count(n)*(nums.count(n)-1)//2 for n in set(nums))