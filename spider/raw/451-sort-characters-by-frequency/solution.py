class Solution:
    def frequencySort(self, s: str) -> str:
        ds = {c:s.count(c) for c in set(list(s))}
        st = sorted(ds.items(),key=lambda xx:xx[1],reverse=True)
        return ''.join([e[0]*e[1] for e in st])