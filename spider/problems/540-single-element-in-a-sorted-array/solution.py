class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # while len(nums) > 1 and nums[0] == nums[1]:
        #     nums.pop(1)
        #     nums.pop(0)
        # return nums[0]
        if len(nums) == 1:
            return nums[0]
        l = 0
        h = len(nums) -1
        while l<h:
            if nums[l] == nums[l+1]:
                l= l + 2
            else:
                return nums[l]
            if nums[h] == nums[h-1]:
                h= h -2
            else:
                return nums[h]
        return nums[l]