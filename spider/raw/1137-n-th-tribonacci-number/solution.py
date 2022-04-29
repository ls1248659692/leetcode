class Solution:
    def tribonacci(self, n: int) -> int:
        def v1(n):
            t1,t2,t3=1,1,0
            while n>=3: t1,t2,t3,n =t1+t2+t3,t1,t2, n-1
            return t1 if n>=1 else 0

        def v0(n):
            cache={}
            def tb(n):
                if n in cache:return cache[n]
                if n==0:return 0
                elif n==1:return 1
                elif n==2:return 1
                else:
                    res = tb(n-3)+tb(n-2)+tb(n-1)
                    cache[n]=res
                return res
            return tb(n)
        return v1(n)