# [Minimum Moves to Reach Target with Rotations][title]

## Description

你还记得那条风靡全球的贪吃蛇吗？

我们在一个 `n*n` 的网格上构建了新的迷宫地图，蛇的长度为 2，也就是说它会占去两个单元格。蛇会从左上角（`(0, 0)` 和 `(0,
1)`）开始移动。我们用 `0` 表示空单元格，用 1 表示障碍物。蛇需要移动到迷宫的右下角（`(n-1, n-2)` 和 `(n-1, n-1)`）。

每次移动，蛇可以这样走：

  * 如果没有障碍，则向右移动一个单元格。并仍然保持身体的水平／竖直状态。
  * 如果没有障碍，则向下移动一个单元格。并仍然保持身体的水平／竖直状态。
  * 如果它处于水平状态并且其下面的两个单元都是空的，就顺时针旋转 90 度。蛇从（`(r, c)`、`(r, c+1)`）移动到 （`(r, c)`、`(r+1, c)`）。  
![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/09/28/image-2.png)

  * 如果它处于竖直状态并且其右面的两个单元都是空的，就逆时针旋转 90 度。蛇从（`(r, c)`、`(r+1, c)`）移动到（`(r, c)`、`(r, c+1)`）。  
![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/09/28/image-1.png)

返回蛇抵达目的地所需的最少移动次数。

如果无法到达目的地，请返回 `-1`。



**示例 1：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2019/09/28/image.png)**
            **输入：** grid = [[0,0,0,0,0,1],                   [1,1,0,0,1,0],                   [0,0,0,0,1,1],                   [0,0,1,0,1,0],                   [0,1,1,0,0,0],                   [0,1,1,0,0,0]]    **输出：** 11    **解释：** 一种可能的解决方案是 [右, 右, 顺时针旋转, 右, 下, 下, 下, 下, 逆时针旋转, 右, 下]。    

**示例 2：**
            **输入：** grid = [[0,0,1,1,1,1],                   [0,0,0,0,1,1],                   [1,1,0,0,0,1],                   [1,1,1,0,0,1],                   [1,1,1,0,0,1],                   [1,1,1,0,0,0]]    **输出：** 9    



**提示：**

  * `2 <= n <= 100`
  * `0 <= grid[i][j] <= 1`
  * 蛇保证从空单元格开始出发。


**Tags:** Breadth-First Search, Array, Matrix

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/minimum-moves-to-reach-target-with-rotations
