# [Network Delay Time][title]

## Description

有 `n` 个网络节点，标记为 `1` 到 `n`。

给你一个列表 `times`，表示信号经过 **有向** 边的传递时间。 `times[i] = (ui, vi, wi)`，其中 `ui`
是源节点，`vi` 是目标节点， `wi` 是一个信号从源节点传递到目标节点的时间。

现在，从某个节点 `K` 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 `-1` 。



**示例 1：**

![](https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png)
            **输入：** times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2    **输出：** 2    

**示例 2：**
            **输入：** times = [[1,2,1]], n = 2, k = 1    **输出：** 1    

**示例 3：**
            **输入：** times = [[1,2,1]], n = 2, k = 2    **输出：** -1    



**提示：**

  * `1 <= k <= n <= 100`
  * `1 <= times.length <= 6000`
  * `times[i].length == 3`
  * `1 <= ui, vi <= n`
  * `ui != vi`
  * `0 <= wi <= 100`
  * 所有 `(ui, vi)` 对都 **互不相同** （即，不含重复边）


**Tags:** Depth-First Search, Breadth-First Search, Graph, Shortest Path, Heap (Priority Queue)

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, kk: int) -> int:
        MA,MI=float('inf'),float('-inf')
        e=[[MA for j in range(n)] for i in range(n)]
        for i,j,w in times:
            e[i-1][j-1]=w
        #for _r in e:print(_r)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    e[i][j]=min(e[i][k]+e[k][j],e[i][j])
        #print('
')
        for _r in e:print(_r)
        kk=kk-1
        r=[e[kk][i] for i in range(n) if i!=kk]
        print(r)
        return -1 if max(r)==MA else max(r)      
```

[title]: https://leetcode-cn.com/problems/network-delay-time
