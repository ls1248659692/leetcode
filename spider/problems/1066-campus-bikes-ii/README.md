# [Campus Bikes II][title]

## Description

在由 2D 网格表示的校园里有 `n` 位工人（`worker`）和 `m` 辆自行车（`bike`），`n <= m`。所有工人和自行车的位置都用网格上的
2D 坐标表示。

我们为每一位工人分配一辆专属自行车，使每个工人与其分配到的自行车之间的 **曼哈顿距离** 最小化。

返回 `每个工人与分配到的自行车之间的曼哈顿距离的最小可能总和` 。

`p1` 和 `p2` 之间的 **曼哈顿距离** 为 `Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y -
p2.y|`。



**示例 1：**

![](https://assets.leetcode.com/uploads/2019/03/06/1261_example_1_v2.png)
            **输入：** workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]    **输出：** 6    **解释：**    自行车 0 分配给工人 0，自行车 1 分配给工人 1 。分配得到的曼哈顿距离都是 3, 所以输出为 6 。    

**示例 2：**

![](https://assets.leetcode.com/uploads/2019/03/06/1261_example_2_v2.png)
            **输入：** workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]    **输出：** 4    **解释：**    先将自行车 0 分配给工人 0，再将自行车 1 分配给工人 1（或工人 2），自行车 2 给工人 2（或工人 1）。如此分配使得曼哈顿距离的总和为 4。    

**示例 3:**
            **输入：** workers = [[0,0],[1,0],[2,0],[3,0],[4,0]], bikes = [[0,999],[1,999],[2,999],[3,999],[4,999]]    **输出：** 4995    



**提示：**

  * `n == workers.length`
  * `m == bikes.length`
  * `1 <= n <= m <= 10`
  * `workers[i].length == 2`
  * `bikes[i].length == 2`
  * `0 <= workers[i][0], workers[i][1], bikes[i][0], bikes[i][1] < 1000`
  * 所有的工人和自行车的位置都是 **不同**  的。


**Tags:** Bit Manipulation, Array, Dynamic Programming, Backtracking, Bitmask

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/campus-bikes-ii
