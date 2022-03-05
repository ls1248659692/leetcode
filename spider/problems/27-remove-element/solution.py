class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        t_nums = [nn for nn in nums if nn!=val]
        print(t_nums)
        # nums = list(t_nums)
        for ii in range(len(t_nums)):
            nums[ii]=t_nums[ii]
        return len(t_nums)
            