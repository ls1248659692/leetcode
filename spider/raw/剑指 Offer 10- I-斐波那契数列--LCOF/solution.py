class Solution:
    def fib(self, n: int) -> int:
        def v1(n):
            f1,f2=0, 1
            for i in range(n):f1,f2 = f2,f1+f2
            return f1 % 1000000007
                
        def v0(n):
            cache={0:0,1:1}
            def myfib(n):
                if n in cache:return cache[n]
                if n==0: return 0
                elif n==1:return 1
                else: 
                    r= (myfib(n-1)+myfib(n-2))%(1000000007)
                    cache[n]=r
                    return r
            return myfib(n)
        return v1(n)