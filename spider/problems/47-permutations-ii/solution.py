class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def v1(nums):
            vis =set()
            if len(nums)<=1:
                return [nums]
            else:
                res = []
                for i in range(len(nums)):
                    if nums[i] not in vis:
                        tli = [ [nums[i]] + el for el in v1(nums[:i]+nums[i+1:])]
                        vis.add(nums[i])
                        res.extend(tli)
                return res
        return v1(sorted(nums))