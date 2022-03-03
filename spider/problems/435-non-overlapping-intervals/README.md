# [Non-overlapping Intervals][title]

## Description

给定一个区间的集合 `intervals` ，其中 `intervals[i] = [starti, endi]` 。返回
_需要移除区间的最小数量，使剩余区间互不重叠  _。



**示例 1:**
            **输入:** intervals = [[1,2],[2,3],[3,4],[1,3]]    **输出:** 1    **解释:** 移除 [1,3] 后，剩下的区间没有重叠。    

**示例 2:**
            **输入:** intervals = [ [1,2], [1,2], [1,2] ]    **输出:** 2    **解释:** 你需要移除两个 [1,2] 来使剩下的区间没有重叠。    

**示例 3:**
            **输入:** intervals = [ [1,2], [2,3] ]    **输出:** 0    **解释:** 你不需要移除任何区间，因为它们已经是无重叠的了。    



**提示:**

  * `1 <= intervals.length <= 105`
  * `intervals[i].length == 2`
  * `-5 * 104 <= starti < endi <= 5 * 104`


**Tags:** Greedy, Array, Dynamic Programming, Sorting

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/non-overlapping-intervals
