class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join([wd for wd in s.split()][:k])