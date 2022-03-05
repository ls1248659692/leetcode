class Solution:
    def totalMoney(self, n: int) -> int:
        wk = n//7
        wks = sum(7*w+28 for w in range(wk))
        print(list(range(0+wk+1,n-wk*7+wk+1)))
        return wks + sum(list(range(0+wk+1,n-wk*7+wk+1)))