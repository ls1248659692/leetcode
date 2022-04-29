# [Merge Intervals][title]

## Description

以数组 `intervals` 表示若干个区间的集合，其中单个区间为 `intervals[i] = [starti, endi]`
。请你合并所有重叠的区间，并返回  _一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间_  。



**示例 1：**
            **输入：** intervals = [[1,3],[2,6],[8,10],[15,18]]    **输出：** [[1,6],[8,10],[15,18]]    **解释：** 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].    

**示例  2：**
            **输入：** intervals = [[1,4],[4,5]]    **输出：** [[1,5]]    **解释：** 区间 [1,4] 和 [4,5] 可被视为重叠区间。



**提示：**

  * `1 <= intervals.length <= 104`
  * `intervals[i].length == 2`
  * `0 <= starti <= endi <= 104`


**Tags:** Array, Sorting

**Difficulty:** Medium

## 思路

``` python3
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

```

[title]: https://leetcode-cn.com/problems/merge-intervals
