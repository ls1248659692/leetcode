# [Shortest Path with Alternating Colors][title]

## Description

在一个有向图中，节点分别标记为 `0, 1, ..., n-1`。图中每条边为红色或者蓝色，且存在自环或平行边。

`red_edges` 中的每一个 `[i, j]` 对表示从节点 `i` 到节点 `j` 的红色有向边。类似地，`blue_edges` 中的每一个
`[i, j]` 对表示从节点 `i` 到节点 `j` 的蓝色有向边。

返回长度为 `n` 的数组 `answer`，其中 `answer[X]` 是从节点 `0` 到节点 `X`
的红色边和蓝色边交替出现的最短路径的长度。如果不存在这样的路径，那么 `answer[x] = -1`。



**示例 1：**
            **输入：** n = 3, red_edges = [[0,1],[1,2]], blue_edges = []    **输出：** [0,1,-1]    

**示例 2：**
            **输入：** n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]    **输出：** [0,1,-1]    

**示例 3：**
            **输入：** n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]    **输出：** [0,-1,-1]    

**示例 4：**
            **输入：** n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]    **输出：** [0,1,2]    

**示例 5：**
            **输入：** n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]    **输出：** [0,1,1]    



**提示：**

  * `1 <= n <= 100`
  * `red_edges.length <= 400`
  * `blue_edges.length <= 400`
  * `red_edges[i].length == blue_edges[i].length == 2`
  * `0 <= red_edges[i][j], blue_edges[i][j] < n`


**Tags:** Breadth-First Search, Graph

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/shortest-path-with-alternating-colors
