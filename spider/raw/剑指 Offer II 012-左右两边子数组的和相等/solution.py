class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        su =sum(nums)
        c=0
        for i in range(len(nums)):
            if c==(su-nums[i])/2:return i
            c+=nums[i]
            
        return -1        