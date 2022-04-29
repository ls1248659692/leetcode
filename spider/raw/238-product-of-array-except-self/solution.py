class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p =math.prod([e for e in nums if e])
        return [0]*len(nums) if nums.count(0)>1 else [p if e==0 else 0 for e in nums] if nums.count(0)==1 else [p//e for e in nums]