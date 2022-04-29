class Solution:
    def divide(self, a: int, b: int) -> int:
        if (a,b)==(-2147483648,-1): return  2147483647
        return int(a/b)