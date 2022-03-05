class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        for i in sorted(set(nums),reverse = True):
            if nums.count(i) == 1:
                return i
        return -1