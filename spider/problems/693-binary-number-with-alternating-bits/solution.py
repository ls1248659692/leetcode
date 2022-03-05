class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bs = str(bin(n))[2:]
        return not [i for i in range(1,len(bs)) if bs[i]==bs[i-1]]