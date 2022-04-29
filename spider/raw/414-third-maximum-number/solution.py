class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        return sorted(list(set(nums)))[-3:][0] if len(set(nums))>=3 else sorted(nums)[-1]