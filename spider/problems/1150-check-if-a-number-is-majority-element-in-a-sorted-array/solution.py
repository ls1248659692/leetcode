class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        return nums.count(target) >= len(nums)//2 +1