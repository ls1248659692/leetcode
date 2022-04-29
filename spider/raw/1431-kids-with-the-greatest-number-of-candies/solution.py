class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx= max(candies)
        return [e+extraCandies>=mx for e in candies]