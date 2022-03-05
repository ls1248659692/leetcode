class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sn = sorted(nums) 
        #td = {n:sn.index(n) for n in set(nums)}
        return [{n:sn.index(n) for n in set(nums)}[n] for n in nums]