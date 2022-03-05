class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 1
        intervals = sorted(intervals)
        while 0 < i < len(intervals):
            if intervals[i - 1][1] >= intervals[i][0]:
                intervals[i][0] = min(intervals[i-1][0],intervals[i][0])
                intervals[i][1] = max(intervals[i-1][1],intervals[i][1])
                intervals.pop(i-1)
                i = 1
            else:
                i = i + 1
        return(intervals)
