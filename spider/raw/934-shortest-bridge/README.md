# [Shortest Bridge][title]

## Description

在给定的二维二进制数组 `A` 中，存在两座岛。（岛是由四面相连的 `1` 形成的一个最大组。）

现在，我们可以将 `0` 变为 `1`，以使两座岛连接起来，变成一座岛。

返回必须翻转的 `0` 的最小数目。（可以保证答案至少是 `1` 。）

**示例 1：**
            **输入：** A = [[0,1],[1,0]]    **输出：** 1    

**示例 2：**
            **输入：** A = [[0,1,0],[0,0,0],[0,0,1]]    **输出：** 2    

**示例 3：**
            **输入：** A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]    **输出：** 1

**提示：**

  * `2 <= A.length == A[0].length <= 100`
  * `A[i][j] == 0` 或 `A[i][j] == 1`


**Tags:** Depth-First Search, Breadth-First Search, Array, Matrix

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/shortest-bridge
