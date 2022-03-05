class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def sst(n):
            if len(n)==0: return [[]]
            s1  = sst(n[1:])
            s0 = [s+[n[0]] for s in s1]
            return s0+s1
        return sst(nums)