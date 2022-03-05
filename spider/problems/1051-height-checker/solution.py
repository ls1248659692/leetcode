class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s = sorted(heights)
        cnt = 0
        for i in range(len(s)):
            if s[i] != heights[i]:
                cnt += 1
        return cnt