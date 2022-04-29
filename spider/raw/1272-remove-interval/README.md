# [Remove Interval][title]

## Description

实数集合可以表示为若干不相交区间的并集，其中每个区间的形式为 `[a, b)`（左闭右开），表示满足 `a <= x < b` 的所有实数  `x`
的集合。如果某个区间 `[a, b)` 中包含实数 `x` ，则称实数 `x` 在集合中。

给你一个 **有序的** 不相交区间列表 `intervals` 。`intervals` 表示一个实数集合，其中每一项 `intervals[i] =
[ai, bi]` 都表示一个区间 `[ai, bi)` 。再给你一个要删除的区间 `toBeRemoved` 。

返回 _一组实数，该实数表示`intervals` 中  **删除**  了 `toBeRemoved` 的部分_ 。
_换句话说，返回实数集合，并满足集合中的每个实数`x` 都在 `intervals` 中，但不在 `toBeRemoved`
中。你的答案应该是一个如上所述的 **有序的** 不相连的间隔列表 。_





**示例 1：**

![](https://assets.leetcode.com/uploads/2020/12/24/removeintervalex1.png)
            **输入：** intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]    **输出：** [[0,1],[6,7]]    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/12/24/removeintervalex2.png)
            **输入：** intervals = [[0,5]], toBeRemoved = [2,3]    **输出：** [[0,2],[3,5]]    

**示例 3：**
            **输入：** intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]    **输出：** [[-5,-4],[-3,-2],[4,5],[8,9]]    



**提示：**

  * `1 <= intervals.length <= 104`
  * `-109 <= ai < bi <= 109`


**Tags:** Array

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/remove-interval
