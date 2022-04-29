class Solution:
    def numTrees(self, n: int) -> int:
            # if n==1:return 1
            # if n==2: return 2
            # elif n=3: return ct(2)+ct(1)*ct(1)+ct(2)
            # elif n==4: return ct(3)+ct(2)*ct(1) +ct(1)*ct(2) ct(3)
        c=[1,1,2,5]
        for nn in range(4,n+1):
            c.append(sum(c[j]*c[nn-1-j] for j in range(0,nn)))
        return c[n]
