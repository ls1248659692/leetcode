class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        p = [abs(px-x)+abs(py-y)if px==x or py==y else 999999 for px,py in points ]
        md = min(p)
        return [i for i in range(len(p)) if p[i]==md][0] if md!=999999 else -1