class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(set(timePoints)) > 1440:
            return 0
        li = []
        for i in timePoints:
             s = i.split(':')
             minute = int(s[0])*60 + int(s[1])
             li.append(minute)
        ii = 0
        mi = 1440
        li = sorted(li)
        li.append(li[0])
        print(li)
        while ii < len(li)-1:
            a = min(abs(li[ii]-li[ii+1]),(1440-abs(li[ii]-li[ii+1])))
            if a < mi:
                mi = a
            ii += 1
        return mi