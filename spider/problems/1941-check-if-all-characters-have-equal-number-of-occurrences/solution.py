class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set([s.count(ch) for ch in set(list(s))]))==1