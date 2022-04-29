class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([wd[::-1] for wd in s.split()])
        