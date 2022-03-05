# [Find if Path Exists in Graph][title]

## Description

有一个具有 `n`个顶点的 **双向** 图，其中每个顶点标记从 `0` 到 `n - 1`（包含 `0` 和 `n - 1`）。图中的边用一个二维整数数组
`edges` 表示，其中 `edges[i] = [ui, vi]` 表示顶点 `ui` 和顶点 `vi` 之间的双向边。 每个顶点对由 **最多一条**
边连接，并且没有顶点存在与自身相连的边。

请你确定是否存在从顶点 `start` 开始，到顶点 `end` 结束的 **有效路径** 。

给你数组 `edges` 和整数 `n`、`start`和`end`，如果从 `start` 到 `end` 存在 **有效路径** ，则返回
`true`，否则返回 `false` 。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/08/14/validpath-ex1.png)
            **输入：** n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2    **输出：** true    **解释：** 存在由顶点 0 到顶点 2 的路径:    - 0 → 1 → 2     - 0 → 2    

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/08/14/validpath-ex2.png)
            **输入：** n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], start = 0, end = 5    **输出：** false    **解释：** 不存在由顶点 0 到顶点 5 的路径.    



**提示:**

  * `1 <= n <= 2 * 105`
  * `0 <= edges.length <= 2 * 105`
  * `edges[i].length == 2`
  * `0 <= ui, vi <= n - 1`
  * `ui != vi`
  * `0 <= start, end <= n - 1`
  * 不存在双向边
  * 不存在指向顶点自身的边


**Tags:** Depth-First Search, Breadth-First Search, Graph

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        seg0 = [[e[1],e[0]] for e in edges]+edges
        dicb,dice={},{}
        for b,e in seg0:
            dicb.setdefault(b,set())
            dicb[b].add(e)
        for b,e in seg0:
            dice.setdefault(e,set())
            dice[e].add(b) 

        rset = set([destination])
        cnt =1
        while cnt<n and source not in rset:
            cnt+=1
            if cnt%100==1: print(cnt,len(rset))
            t0 = list()
            for e in rset:
                t0.append(dice[e])
            rset = set([e for t in t0 for e in t])
        return source in rset

```

[title]: https://leetcode-cn.com/problems/find-if-path-exists-in-graph
