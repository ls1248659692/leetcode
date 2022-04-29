class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sn= sorted(nums)
        for i in range(len(nums)):
            if i!=sn[i]:
                return i
        return len(nums)