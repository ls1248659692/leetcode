# [Minimum Time Difference][title]

## Description

给定一个 24 小时制（小时:分钟 **"HH:MM"** ）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。



**示例 1：**
            **输入：** timePoints = ["23:59","00:00"]    **输出：** 1    

**示例 2：**
            **输入：** timePoints = ["00:00","23:59","00:00"]    **输出：** 0    



**提示：**

  * `2 <= timePoints.length <= 2 * 104`
  * `timePoints[i]` 格式为 **"HH:MM"**


**Tags:** Array, Math, String, Sorting

**Difficulty:** Medium

## 思路

``` python3
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
```

[title]: https://leetcode-cn.com/problems/minimum-time-difference
