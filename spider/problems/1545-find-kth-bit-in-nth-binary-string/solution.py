class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def  v0(n,k):
            if n == 1: return '0'
            s = '0'
            for i in range(1, n):
                s +=  '1' + s.replace('0','F').replace('1','0').replace('F','1')[::-1]
            return s[k-1]

        def v1(n,k):
            if n == 1:return '0'
            mid = 2**(n-1)
            if k == mid:
                return '1'
            if k < mid:
                return v1(n-1,k)
            elif k > mid:
                k = mid*2 - k
                return '0' if v1(n-1,k) == '1' else '1'
        return v0(n,k)