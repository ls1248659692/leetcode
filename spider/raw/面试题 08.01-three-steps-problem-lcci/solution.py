class Solution:
    def waysToStep(self, n: int) -> int:
        if n < 2:
            return 1
        a = 1
        b = 1
        c = 2
        for _ in range(3,n+1):
            a,b,c = b, c, (a+b+c) %1000000007
        return c