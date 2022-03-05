class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([ el for el in  s.strip().split()[::-1] if el])