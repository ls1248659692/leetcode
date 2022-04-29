class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        st = sorted([[nums[i],i] for i in range(len(nums))])
        return (st[-1][0]-1)*(st[-2][0]-1)