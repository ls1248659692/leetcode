class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ts = ''.join([ str(ord(c)-ord('a')+1) for c in s])
        while k:
            ts = str(sum(int(e) for e in ts))
            k-=1
        return int(ts)