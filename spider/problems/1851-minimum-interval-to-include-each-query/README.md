# [Minimum Interval to Include Each Query][title]

## Description

给你一个二维整数数组 `intervals` ，其中 `intervals[i] = [lefti, righti]` 表示第 `i` 个区间开始于
`lefti` 、结束于 `righti`（包含两侧取值， **闭区间** ）。区间的 **长度** 定义为区间中包含的整数数目，更正式地表达是
`righti - lefti + 1` 。

再给你一个整数数组 `queries` 。第 `j` 个查询的答案是满足 `lefti <= queries[j] <= righti` 的
**长度最小区间`i` 的长度** 。如果不存在这样的区间，那么答案是 `-1` 。

以数组形式返回对应查询的所有答案。

**示例 1：**
            **输入：** intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]    **输出：** [3,3,1,4]    **解释：** 查询处理如下：    - Query = 2 ：区间 [2,4] 是包含 2 的最小区间，答案为 4 - 2 + 1 = 3 。    - Query = 3 ：区间 [2,4] 是包含 3 的最小区间，答案为 4 - 2 + 1 = 3 。    - Query = 4 ：区间 [4,4] 是包含 4 的最小区间，答案为 4 - 4 + 1 = 1 。    - Query = 5 ：区间 [3,6] 是包含 5 的最小区间，答案为 6 - 3 + 1 = 4 。    

**示例 2：**
            **输入：** intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]    **输出：** [2,-1,4,6]    **解释：** 查询处理如下：    - Query = 2 ：区间 [2,3] 是包含 2 的最小区间，答案为 3 - 2 + 1 = 2 。    - Query = 19：不存在包含 19 的区间，答案为 -1 。    - Query = 5 ：区间 [2,5] 是包含 5 的最小区间，答案为 5 - 2 + 1 = 4 。    - Query = 22：区间 [20,25] 是包含 22 的最小区间，答案为 25 - 20 + 1 = 6 。    

**提示：**

  * `1 <= intervals.length <= 105`
  * `1 <= queries.length <= 105`
  * `queries[i].length == 2`
  * `1 <= lefti <= righti <= 107`
  * `1 <= queries[j] <= 107`


**Tags:** Array, Binary Search, Sorting, Line Sweep, Heap (Priority Queue)

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/minimum-interval-to-include-each-query
