class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def sst(n):
            if len(n)==0: return [[]]
            s1  = sst(n[1:])
            s0 = [[n[0]]+list(s) for s in s1 if not s or n[0]<=s[0]]
            return list(set([tuple(e) for e in s0+s1]))
        r=sst(nums)        
        return [ls for ls in r if len(ls)>1]