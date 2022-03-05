class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        c =0
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                for k in range(j+1,len(nums)-1):
                    su=nums[i]+nums[j]+nums[k]
                    if su in nums[k+1:]:
                        c +=nums[k+1:].count(su)
        return c