class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zn=0
        for ii in range(len(nums)-1,-1,-1):
            if nums[ii]==0:
                for jj in range(ii,len(nums)-1-zn):
                    nums[jj]=nums[jj+1]
                zn+=1
                
        for zz in range(len(nums)-zn,len(nums)):
            nums[zz]=0
