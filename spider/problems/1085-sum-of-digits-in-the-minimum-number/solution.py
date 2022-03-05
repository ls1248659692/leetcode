class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        s = min(nums)
        ans = 0
        for i in str(s):
            ans += int(i)
        return 1 if ans%2 == 0 else 0