class Solution:
    def grayCode(self, n: int) -> List[int]:
        def gcd(n):
            if n==1:  return [0,1]
            elif n==2: return [0,1,3,2]
            elif n==3: return [0,1,3,2,6,7,5,4]
            elif n>=4: 
                n1 = gcd(n-1) 
                return n1 + [e+2**(n-1) for e in n1][::-1] #+[2**(n-1)]

        return gcd(n)