# [Number of Connected Components in an Undirected Graph][title]

## Description

你有一个包含 `n` 个节点的图。给定一个整数 `n` 和一个数组 `edges` ，其中 `edges[i] = [ai, bi]` 表示图中 `ai`
和 `bi` 之间有一条边。

返回 _图中已连接分量的数目_  。



**示例 1:**

![](https://assets.leetcode.com/uploads/2021/03/14/conn1-graph.jpg)
            **输入:**n = 5, edges = [[0, 1], [1, 2], [3, 4]]    **输出:** 2    

**示例 2:**

![](https://assets.leetcode.com/uploads/2021/03/14/conn2-graph.jpg)
            **输入:**n = 5, edges = [[0,1], [1,2], [2,3], [3,4]]    **输出:   **1



**提示：**

  * `1 <= n <= 2000`
  * `1 <= edges.length <= 5000`
  * `edges[i].length == 2`
  * `0 <= ai <= bi < n`
  * `ai != bi`
  * `edges` 中不会出现重复的边


**Tags:** Depth-First Search, Breadth-First Search, Union Find, Graph

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dic= {}
        for b,a in edges:
            dic.setdefault(b,[]).append(a)
            dic.setdefault(a,[]).append(b)
        td={}
        for b in dic:
            aset,tset =set(dic[b]),set(dic[b])
            while aset:
                _aset,aset=set(aset),set()
                for bb in _aset:
                    for aa in dic.get(bb,set()):
                        if aa not in tset:
                            aset.add(aa)
                for p in aset:tset.add(p)
            td[b]=tset |set([b])
        for i in range(n):
            td.setdefault(i,set([i]))
        #print(td)
        return len(set([tuple(e) for e in td.values()]))

```

[title]: https://leetcode-cn.com/problems/number-of-connected-components-in-an-undirected-graph
