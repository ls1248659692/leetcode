class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return [ch for ch in set(list(t)) if t.count(ch)-s.count(ch) >0][0]