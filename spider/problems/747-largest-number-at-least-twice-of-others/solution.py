class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        ts = sorted(list(set(nums)),reverse=True)
        if len(ts)==1:return 0
        if  ts[0]<ts[1]*2:return -1
        return nums.index(ts[0])