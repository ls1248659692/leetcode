# [Minimum Cost to Reach Destination in Time][title]

## Description

一个国家有 `n` 个城市，城市编号为 `0` 到 `n - 1` ，题目保证 **所有城市** 都由双向道路 **连接在一起** 。道路由二维整数数组
`edges` 表示，其中 `edges[i] = [xi, yi, timei]` 表示城市 `xi` 和 `yi` 之间有一条双向道路，耗费时间为
`timei` 分钟。两个城市之间可能会有多条耗费时间不同的道路，但是不会有道路两头连接着同一座城市。

每次经过一个城市时，你需要付通行费。通行费用一个长度为 `n` 且下标从 **0** 开始的整数数组 `passingFees` 表示，其中
`passingFees[j]` 是你经过城市 `j` 需要支付的费用。

一开始，你在城市 `0` ，你想要在 `maxTime` **分钟以内** （包含 `maxTime` 分钟）到达城市 `n - 1` 。旅行的
**费用** 为你经过的所有城市 **通行费之和** （ **包括** 起点和终点城市的通行费）。

给你 `maxTime`，`edges` 和 `passingFees` ，请你返回完成旅行的 **最小费用** ，如果无法在 `maxTime`
分钟以内完成旅行，请你返回 `-1` 。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/06/04/leetgraph1-1.png)
            **输入：** maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]    **输出：** 11    **解释：** 最优路径为 0 -> 1 -> 2 -> 5 ，总共需要耗费 30 分钟，需要支付 11 的通行费。    

**示例 2：**

**![](https://assets.leetcode.com/uploads/2021/06/04/copy-of-
leetgraph1-1.png)**
            **输入：** maxTime = 29, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]    **输出：** 48    **解释：** 最优路径为 0 -> 3 -> 4 -> 5 ，总共需要耗费 26 分钟，需要支付 48 的通行费。    你不能选择路径 0 -> 1 -> 2 -> 5 ，因为这条路径耗费的时间太长。    

**示例 3：**
            **输入：** maxTime = 25, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]    **输出：** -1    **解释：** 无法在 25 分钟以内从城市 0 到达城市 5 。    

**提示：**

  * `1 <= maxTime <= 1000`
  * `n == passingFees.length`
  * `2 <= n <= 1000`
  * `n - 1 <= edges.length <= 1000`
  * `0 <= xi, yi <= n - 1`
  * `1 <= timei <= 1000`
  * `1 <= passingFees[j] <= 1000`
  * 图中两个节点之间可能有多条路径。
  * 图中不含有自环。


**Tags:** Graph, Dynamic Programming

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/minimum-cost-to-reach-destination-in-time
