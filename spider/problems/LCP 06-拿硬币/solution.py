class Solution:
    def minCount(self, coins: List[int]) -> int:
        return sum((c+1)//2 for c in coins)