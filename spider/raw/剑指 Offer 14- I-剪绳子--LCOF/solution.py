class Solution:
    def cuttingRope(self, n: int) -> int:
        def accum(ar):
            c=1
            for n in ar:c*=n
            return c
        if n==2:return 1
        if n==3:return 2
        if n==4:return 2*2
        else:
            if n%3==0: return accum([3]*(n//3))
            elif n%3==1: return accum([3]*(n//3-1)+[4])
            elif n%3==2: return accum([3]*(n//3)+[2])        