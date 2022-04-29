class Solution:
    def balancedStringSplit(self, s: str) -> int:
       return sum([s[:i].count('L')==s[:i].count('R') for i in range(len(s))])