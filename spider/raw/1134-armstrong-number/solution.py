class Solution:
    def isArmstrong(self, n: int) -> bool:
        s = str(n)
        ans = 0
        k = len(s)
        for i in s:
            ans += int(i)**k
        return n == ans
