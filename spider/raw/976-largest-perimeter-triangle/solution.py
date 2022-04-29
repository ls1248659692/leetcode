class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sn = sorted(nums,reverse=True)
        for i in range(len(sn)-2):
            if sn[i]<sn[i+1]+sn[i+2]: 
                return sn[i]+sn[i+1]+sn[i+2]
        return 0