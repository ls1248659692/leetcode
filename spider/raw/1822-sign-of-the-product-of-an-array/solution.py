class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for i in nums:
            ans *= i
        if ans > 0:return 1
        elif ans < 0: return -1
        else:return 0