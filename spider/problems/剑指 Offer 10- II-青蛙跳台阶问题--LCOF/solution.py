class Solution:
    def numWays(self, n: int) -> int:
        cache={0:1,1:1}
        def cs(n):
            r = 1
            if n in cache: return cache[n]
            if n>1:
                r1 = r*cs(n-1)
                r2 = r*cs(n-2)
                r= r1+r2
            cache[n]=r
            return r %1000000007
        return cs(n)        