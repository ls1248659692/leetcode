class Solution:
    import math
    def myPow(self, x: float, n: int) -> float:
        cache={}
        
        def mp2(n):
            if n in cache:return cache[n]
            if n==1: r= x
            else: r= mp2(n//2)*mp2(n//2)
            cache[n]=r
            return r
                
        def mp(n):
            if n==0:return 1
            if n==1:return x
            else:            
                m2= int(math.log2(n))
                n1= n-2**m2
                return mp2(2**m2)*mp(n1)
            
        return mp(abs(n)) if n>=0 else 1/mp(abs(n))