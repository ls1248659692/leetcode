class Solution:
    def minPartitions(self, n: str) -> int:
        return max([int(ch) for ch in n])