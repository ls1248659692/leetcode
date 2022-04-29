
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        num = 2**p - 1
        mod = 10**9+7
        pairs =pow( (num-1),(2**(p-1)-1),(mod))
        return num* pairs % (mod)
