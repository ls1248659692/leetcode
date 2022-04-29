# [Optimize Water Distribution in a Village][title]

## Description

村里面一共有 `n` 栋房子。我们希望通过建造水井和铺设管道来为所有房子供水。

对于每个房子 `i`，我们有两种可选的供水方案：

  * 一种是直接在房子内建造水井，成本为 `wells[i]`；
  * 另一种是从另一口井铺设管道引水，数组 `pipes` 给出了在房子间铺设管道的成本，其中每个 `pipes[i] = [house1, house2, cost]` 代表用管道将 `house1` 和 `house2` 连接在一起的成本。当然，连接是双向的。

请你帮忙计算为所有房子都供水的最低总成本。



**示例 1：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/08/23/1359_ex1.png)**
            **输入：** n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]    **输出：** 3    **解释：**    上图展示了铺设管道连接房屋的成本。    最好的策略是在第一个房子里建造水井（成本为 1），然后将其他房子铺设管道连起来（成本为 2），所以总成本为 3。    

**示例 2：**
            **输入：** n = 2, wells = [1,1], pipes = [[1,2,1]]    **输出：** 2



**提示：**

  * `1 <= n <= 10000`
  * `wells.length == n`
  * `0 <= wells[i] <= 10^5`
  * `1 <= pipes.length <= 10000`
  * `1 <= pipes[i][0], pipes[i][1] <= n`
  * `0 <= pipes[i][2] <= 10^5`
  * `pipes[i][0] != pipes[i][1]`


**Tags:** Union Find, Graph, Minimum Spanning Tree

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/optimize-water-distribution-in-a-village
