class Solution:
    def secondHighest(self, s: str) -> int:
        nli = [int(el) for el in s if el in '0123456789']
        nset = sorted(list(set(nli)),reverse=True)
        return nset[1] if len(nset)>=2 else -1
