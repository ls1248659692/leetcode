class Solution:
    def check(self, nums: List[int]) -> bool:
        return '-'.join([str(i) for i in sorted(nums)]) in '-'.join([str(i) for i in nums + nums])