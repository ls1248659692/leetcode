# [Tree Diameter][title]

## Description

给你这棵「无向树」，请你测算并返回它的「直径」：这棵树上最长简单路径的 **边数** 。

我们用一个由所有「边」组成的数组 `edges` 来表示一棵无向树，其中 `edges[i] = [u, v]` 表示节点 `u` 和 `v`
之间的双向边。

树上的节点都已经用 `{0, 1, ..., edges.length}` 中的数做了标记，每个节点上的标记都是独一无二的。



**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/10/31/1397_example_1.png)
            **输入：** edges = [[0,1],[0,2]]    **输出：** 2    **解释：**    这棵树上最长的路径是 1 - 0 - 2，边数为 2。    

**示例 2：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/10/31/1397_example_2.png)
            **输入：** edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]    **输出：** 4    **解释：**    这棵树上最长的路径是 3 - 2 - 1 - 4 - 5，边数为 4。    



**提示：**

  * `0 <= edges.length < 10^4`
  * `edges[i][0] != edges[i][1]`
  * `0 <= edges[i][j] <= edges.length`
  * `edges` 会形成一棵无向树


**Tags:** Tree, Depth-First Search, Breadth-First Search

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/tree-diameter
