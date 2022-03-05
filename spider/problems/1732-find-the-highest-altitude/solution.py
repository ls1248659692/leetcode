class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        a = [0]*(n+1)
        for i in range(n):
            a[i+1] = a[i]+gain[i]
        return max(a)