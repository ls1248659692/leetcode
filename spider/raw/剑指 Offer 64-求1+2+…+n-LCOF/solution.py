class Solution:
    def sumNums(self, n: int) -> int:
        return n and self.sumNums(n-1) + n