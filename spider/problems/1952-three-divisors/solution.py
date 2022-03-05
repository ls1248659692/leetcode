class Solution:
    def isThree(self, n: int) -> bool:
        return math.sqrt(n) % 1 == 0 and [n % (1 + ii) for ii in range(int(math.sqrt(n)))].count(0) == 2        