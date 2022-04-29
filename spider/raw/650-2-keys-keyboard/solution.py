class Solution:
    def minSteps(self, n: int) -> int:
        def isprm(n=None):
            r=[]
            for i in range(2,10**3+1):
                isp=True
                for j in range(2,int(i**0.5)+1):
                    if i/j==i//j:
                        if n is not None and n==i:return j
                        isp=False
                        break
                if isp:r.append(i)
            return r if n is None else 1

        def ms(n):
            #print(isprm(None))
            if n==1: return 0
            elif n in isprm(None):return n
            else:
                j= isprm(n)
                print('gyz',j)
                return ms(j) +ms(n//j)
        return ms(n)