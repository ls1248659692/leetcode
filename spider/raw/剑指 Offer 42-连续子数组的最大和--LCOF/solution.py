class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c, cdiffmax,cleftmin=nums[0],nums[0],nums[0] if nums[0]<0 else 0
        for n in nums[1:]:
            c,cdiffmax,cleftmin, = c+n,max(cdiffmax,c+n-cleftmin),min(c+n,cleftmin)
        return cdiffmax