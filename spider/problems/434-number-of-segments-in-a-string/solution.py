class Solution:
    def countSegments(self, s: str) -> int:
        return len([wd for wd in s.split() if wd])