# [省份数量][title]

## Description

有 `n` 个城市，其中一些彼此相连，另一些没有相连。如果城市 `a` 与城市 `b` 直接相连，且城市 `b` 与城市 `c` 直接相连，那么城市 `a`
与城市 `c` 间接相连。

**省份** 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 `n x n` 的矩阵 `isConnected` ，其中 `isConnected[i][j] = 1` 表示第 `i` 个城市和第 `j`
个城市直接相连，而 `isConnected[i][j] = 0` 表示二者不直接相连。

返回矩阵中 **省份** 的数量。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg)
            **输入：** isConnected = [[1,1,0],[1,1,0],[0,0,1]]    **输出：** 2    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg)
            **输入：** isConnected = [[1,0,0],[0,1,0],[0,0,1]]    **输出：** 3    



**提示：**

  * `1 <= n <= 200`
  * `n == isConnected.length`
  * `n == isConnected[i].length`
  * `isConnected[i][j]` 为 `1` 或 `0`
  * `isConnected[i][i] == 1`
  * `isConnected[i][j] == isConnected[j][i]`



注意：本题与主站 547 题相同： <https://leetcode-cn.com/problems/number-of-provinces/>


**Tags:** Depth-First Search, Breadth-First Search, Union Find, Graph

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/bLyHh0
