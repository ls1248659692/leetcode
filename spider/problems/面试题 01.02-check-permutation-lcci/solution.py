class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return sorted(list(s1))==sorted(list(s2))