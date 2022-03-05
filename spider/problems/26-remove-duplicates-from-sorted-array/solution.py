class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n_nums = []
        for nn in nums:
            if nn not in n_nums: n_nums.append(nn)
        for ii in range(len(n_nums)):
            nums[ii]=n_nums[ii]
        return len(n_nums)