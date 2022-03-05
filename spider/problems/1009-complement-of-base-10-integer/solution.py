class Solution:
    def bitwiseComplement(self, n: int) -> int:
        hb = ''.join(['0' if c=='1' else '1' for c in bin(n)[2:]])
        return int(hb,base=2)