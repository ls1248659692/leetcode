class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ts =timeSeries
        c = 0
        for i in range(1,len(ts)):
            c+= ts[i]-ts[i-1] if ts[i]<ts[i-1]+duration else duration
        return c+duration