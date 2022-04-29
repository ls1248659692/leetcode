class Solution:
    def cuttingRope(self, n: int) -> int:
        if n==2:return 1
        if n==3:return 2
        else:
            if n%3==0: return math.prod([3]*(n//3))%1000000007
            elif n%3==1: return math.prod([3]*(n//3-1)+[4])%1000000007
            elif n%3==2: return math.prod([3]*(n//3)+[2])        %1000000007