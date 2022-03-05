class Solution:
    def leastMinutes(self, n: int) -> int:
        if n==1:return 1
        return len(bin(n-1))-1