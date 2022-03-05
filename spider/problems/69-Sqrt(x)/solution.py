class Solution:
    def mySqrt(self, x: int) -> int:
        #n = 0
        #while n * n <= x: 
        #    n = n +1
        for n in range(0,x+1):
            if n*n>=x:                
                return  n-1 if n*n>x else n

        
        