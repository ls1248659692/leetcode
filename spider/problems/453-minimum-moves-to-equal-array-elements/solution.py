class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mi = min(nums)
        return sum(n-mi for n in nums)