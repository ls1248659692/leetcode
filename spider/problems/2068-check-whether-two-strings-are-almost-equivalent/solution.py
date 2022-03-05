class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        return not [lt for lt in [chr(ord('a')+i) for i in range(26)] if abs(word1.count(lt)-word2.count(lt))>3]