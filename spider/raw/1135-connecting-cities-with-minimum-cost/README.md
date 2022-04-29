# [Connecting Cities With Minimum Cost][title]

## Description

想象一下你是个城市基建规划者，地图上有 `n` 座城市，它们按以 `1` 到 `n` 的次序编号。

给你整数 `n` 和一个数组 `conections`，其中 `connections[i] = [xi, yi, costi]` 表示将城市 `xi`
和城市 `yi` 连接所要的`costi`（ **连接是双向的** ）。

返回连接所有城市的 **最低成本** ，每对城市之间 **至少** 有一条路径。如果无法连接所有 `n` 个城市，返回 `-1`

该 **最小成本** 应该是所用全部连接成本的总和。



**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/07/27/1314_ex2.png)
            **输入：** n = 3, conections = [[1,2,5],[1,3,6],[2,3,1]]    **输出：** 6    **解释：** 选出任意 2 条边都可以连接所有城市，我们从中选取成本最小的 2 条。    

**示例 2：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/07/27/1314_ex1.png)
            **输入：** n = 4, conections = [[1,2,3],[3,4,4]]    **输出：** -1    **解释：** 即使连通所有的边，也无法连接所有城市。    



**提示：**

  * `1 <= n <= 104`
  * `1 <= connections.length <= 104`
  * `connections[i].length == 3`
  * `1 <= xi, yi <= n`
  * `xi != yi`
  * `0 <= costi <= 105`


**Tags:** Union Find, Graph, Minimum Spanning Tree, Heap (Priority Queue)

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/connecting-cities-with-minimum-cost
