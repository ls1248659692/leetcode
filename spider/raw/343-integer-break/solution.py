class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:return 1
        if n==3:return 2
        else:
            if n%3==0: return math.prod([3]*(n//3))
            elif n%3==1: return math.prod([3]*(n//3-1)+[4])
            elif n%3==2: return math.prod([3]*(n//3)+[2])