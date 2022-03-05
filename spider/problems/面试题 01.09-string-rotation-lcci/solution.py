class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return s2 in s1+s1 and len(s1)==len(s2)