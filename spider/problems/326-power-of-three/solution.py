class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        tli=[1]
        while tli[-1]<2**31: tli.append(tli[-1]*3)
        return n in tli