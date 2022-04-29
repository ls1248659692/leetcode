class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for a in range(len(nums)):
            # if nums[a] != target:
                for b in range(a+1,len(nums)):
                    # if nums[b] + nums [a] != target:
                        for c in range(b+1,len(nums)):
                            # if nums[a]+ nums[b] + nums[c] != target:
                                if target - nums[a] - nums[b] - nums[c] in nums[c+1:len(nums)]:
                                    factor = [nums[a],nums[b],nums[c],target - nums[a] - nums[b] - nums[c]]
                                    if factor not in res:
                                        res.append(factor)
        return res