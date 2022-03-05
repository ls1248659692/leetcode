class Solution:
    def firstUniqChar(self, s: str) -> str:
        #tli = [ch for ch in s if s.count(ch)==1]
        for ch in s:
            if s.count(ch)==1:return ch
        return ' ' 