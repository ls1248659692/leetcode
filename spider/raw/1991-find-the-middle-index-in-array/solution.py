class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        c,su= 0,sum(nums)
        for i in range(len(nums)):
            if c ==su-nums[i]-c:
                return i
            c = c+nums[i]
        return -1
