class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return [len(el) for el in s.split() if el][-1]