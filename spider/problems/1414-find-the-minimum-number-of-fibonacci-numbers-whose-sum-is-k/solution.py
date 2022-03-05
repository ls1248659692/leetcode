class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        def maxfib(k):
            f1,f2=1, 1
            while f1<=k:
                f1,f2 = f1+f2,f1
            return f2
        cnt =0    
        while k>0:
            cnt,k = cnt+1,k-maxfib(k)     
        return cnt

        def fib(k):
            f0 ,f1 = 1,1
            while f1 <= k:
                f0 ,f1 = f1 ,f0+f1
            return f0
        cnt = 0
        while k > 0:
            k -= fib(k)
            cnt += 1
        return cnt

        return fib(k)