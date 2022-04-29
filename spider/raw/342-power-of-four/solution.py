class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        cli=[1]
        while cli[-1]<=2**31-1:cli.append(cli[-1]*4)
        return n in cli