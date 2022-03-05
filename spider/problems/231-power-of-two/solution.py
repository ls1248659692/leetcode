class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n in [2**i for i in range(32)]