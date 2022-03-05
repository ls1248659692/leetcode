class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high-high%2-low-low%2)//2  + high%2  + low%2 