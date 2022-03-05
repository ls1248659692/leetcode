class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        return [min(i) for i in rectangles].count(max([min(i) for i in rectangles]))