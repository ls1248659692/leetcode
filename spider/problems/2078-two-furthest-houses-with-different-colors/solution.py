class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_1 = 0
        n = len(colors)
        if colors[0] != colors[-1]:
                return n-1
        for i in range(1,n-1):
            if colors[i] != colors[0] or colors[i] != colors[-1]:
                max_1 = max(i-0 ,n-1-i,max_1)
        return max_1