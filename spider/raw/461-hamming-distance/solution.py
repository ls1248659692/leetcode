class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xx =str(bin(x))[2:].zfill(32)
        yy= str(bin(y))[2:].zfill(32)
        print(xx,yy)
        return sum(1 for i in range(len(xx)) if xx[i]!=yy[i])