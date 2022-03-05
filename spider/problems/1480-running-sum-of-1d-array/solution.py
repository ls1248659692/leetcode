class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        c=[nums[0]]
        for n in nums[1:]:
            c.append(c[-1]+n)
        return c
            