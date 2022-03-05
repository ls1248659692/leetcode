class Solution:
    def findComplement(self, num: int) -> int:
        hb = ''.join(['0' if c=='1' else '1' for c in bin(num)[2:]])
        return int(hb,base=2)