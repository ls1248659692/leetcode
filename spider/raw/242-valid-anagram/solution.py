class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s))==sorted(list(t))