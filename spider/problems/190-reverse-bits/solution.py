class Solution:
    def reverseBits(self, n: int) -> int:
        c=0
        rn= str(bin(int(n)))[2:]
        rn = rn.zfill(32)
        print(len(rn),rn)
        for i in range(len(rn)):
            print(i)
            c+=int(rn[i])*(2**i)
        n=c
        return c