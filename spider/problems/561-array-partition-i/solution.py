class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sn = sorted(nums)
        return sum([sn[i] for i in range(len(sn)) if i%2==0])