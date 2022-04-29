class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join ([wd[:-1] for wd in sorted(s.split(),key=lambda xx:xx[-1])])