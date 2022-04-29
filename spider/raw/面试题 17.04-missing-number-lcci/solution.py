class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        r = [0]*(len(nums)+1)
        for n in nums:
            r[n]=1
        for j in range(len(r)):
            if not r[j]:return j