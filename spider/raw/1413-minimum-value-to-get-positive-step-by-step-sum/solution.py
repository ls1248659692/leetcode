class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        lit = [sum(nums[:i+1]) for i in range(len(nums))]
        return -(min(lit)) + 1 if min(lit) < 0 else 1