class Solution:
    def multiply(self, A: int, B: int) -> int:
        def mup(a,b):
            if b<10: return a*b
            b,r,=b//10,b%10
            return mup(a,b)*10 +mup(a,r)
        return mup(A,B)