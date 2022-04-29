class Solution:
    def arrangeCoins(self, n: int) -> int:
        for k in range(1,2**31):
            if k*(k+1)//2>n:return k-1

        #(1+k)*k/2<=n <(2+k)*(k+1)/2