class Solution:
    def maxDepth(self, s: str) -> int:
        return max(s[:i].count('(')-s[:i].count(')') for i in range (len(s)))