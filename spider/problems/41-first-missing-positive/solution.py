class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nu = sorted(set([0]+[e for e in nums if e>0]))
        for i in range(len(nu)):
            if nu[i]!=i:return i
        return len(nu)
        