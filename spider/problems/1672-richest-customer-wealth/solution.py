class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(i) for i in accounts])