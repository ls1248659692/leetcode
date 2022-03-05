class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        s=sorted([(e,i)for i,e in enumerate(nums)])[-k:]
        return [t[0] for t in sorted(s,key=lambda x:x[1])]