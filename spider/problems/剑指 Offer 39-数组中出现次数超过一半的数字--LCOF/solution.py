class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return [n for n in set(nums) if nums.count(n)>len(nums)/2][0]