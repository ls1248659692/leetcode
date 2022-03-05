class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins =sorted(coins,reverse=False)
        cache,ln = {},len(coins)

        def chg(amt,lf):
            if (amt,lf) in cache:return cache[(amt,lf)]
            if (amt,) in cache:
                ca=cache[(amt,)]
                if ca[0]==0 and ca[1]<lf:return 0
            #print(amt,coins[lf:])
            if amt==0:return 1
            if amt<0:return 0
            if lf>=ln:return 0
            r=0
            for j in range(amt//coins[lf]+1):
                r+=chg(amt-j*coins[lf],lf+1)
            cache[(amt,lf)]=r
            cache[(amt,)]=(r,lf)
            return r
        return chg(amount,0)