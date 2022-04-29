# [All Paths from Source Lead to Destination][title]

## Description

给定有向图的边 `edges`，以及该图的始点 `source` 和目标终点 `destination`，确定从始点 `source`
出发的所有路径是否最终结束于目标终点 `destination`，即：

  * 从始点 `source` 到目标终点 `destination` 存在至少一条路径
  * 如果存在从始点 `source` 到没有出边的节点的路径，则该节点就是路径终点。
  * 从始点`source`到目标终点 `destination` 可能路径数是有限数字

当从始点 `source` 出发的所有路径都可以到达目标终点 `destination` 时返回 `true`，否则返回 `false`。



**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/03/21/485_example_1.png)
            **输入：** n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2    **输出：** false    **说明：** 节点 1 和节点 2 都可以到达，但也会卡在那里。    

**示例 2：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/03/21/485_example_2.png)
            **输入：** n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3    **输出：** false    **说明：** 有两种可能：在节点 3 处结束，或是在节点 1 和节点 2 之间无限循环。    

**示例 3：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/03/21/485_example_3.png)
            **输入：** n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3    **输出：** true    



**提示：**

  * `1 <= n <= 104`
  * `0 <= edges.length <= 104`
  * `edges.length == 2`
  * `0 <= ai, bi <= n - 1`
  * `0 <= source <= n - 1`
  * `0 <= destination <= n - 1`
  * 给定的图中可能带有自环和平行边。


**Tags:** Depth-First Search, Graph

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/all-paths-from-source-lead-to-destination
