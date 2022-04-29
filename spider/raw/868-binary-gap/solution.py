class Solution:
    def binaryGap(self, n: int) -> int:
        ls=[i for i,b in enumerate(bin(n)[2:]) if b=='1']
        return max( ls[i]-ls[i-1] if i>0 else 0 for i,n in enumerate(ls))