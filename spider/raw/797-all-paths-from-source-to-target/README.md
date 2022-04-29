# [All Paths From Source to Target][title]

## Description

给你一个有 `n` 个节点的 **有向无环图（DAG）** ，请你找出所有从节点 `0` 到节点 `n-1` 的路径并输出（ **不要求按特定顺序** ）

 `graph[i]` 是一个从节点 `i` 可以访问的所有节点的列表（即从节点 `i` 到节点 `graph[i][j]`存在一条有向边）。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/09/28/all_1.jpg)
            **输入：** graph = [[1,2],[3],[3],[]]    **输出：** [[0,1,3],[0,2,3]]    **解释：** 有两条路径 0 -> 1 -> 3 和 0 -> 2 -> 3    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/09/28/all_2.jpg)
            **输入：** graph = [[4,3,1],[3,2,4],[3],[4],[]]    **输出：** [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]    



**提示：**

  * `n == graph.length`
  * `2 <= n <= 15`
  * `0 <= graph[i][j] < n`
  * `graph[i][j] != i`（即不存在自环）
  * `graph[i]` 中的所有元素 **互不相同**
  * 保证输入为 **有向无环图（DAG）**




**Tags:** Depth-First Search, Breadth-First Search, Graph, Backtracking

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        gh,n,paths,tg = graph,len(graph),[[0,e] for e in graph[0]],[]
        while paths:
            _paths,paths =paths[:],[]
            for pa in _paths:
                if pa[-1]==n-1: 
                    tg.append(pa[:])
                else:
                    paths += [pa + [nd] for nd in gh[pa[-1]]]
        return tg
```

[title]: https://leetcode-cn.com/problems/all-paths-from-source-to-target
