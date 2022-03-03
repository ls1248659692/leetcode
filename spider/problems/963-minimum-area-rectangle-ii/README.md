# [Minimum Area Rectangle II][title]

## Description

给定在 xy 平面上的一组点，确定由这些点组成的任何矩形的最小面积，其中矩形的边 **不一定平行于** x 轴和 y 轴。

如果没有任何矩形，就返回 0。



**示例 1：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2018/12/22/1a.png)**
            **输入：** [[1,2],[2,1],[1,0],[0,1]]    **输出：** 2.00000    **解释：** 最小面积的矩形出现在 [1,2],[2,1],[1,0],[0,1] 处，面积为 2。

**示例 2：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/23/2.png)
            **输入：** [[0,1],[2,1],[1,1],[1,0],[2,0]]    **输出：** 1.00000    **解释：** 最小面积的矩形出现在 [1,0],[1,1],[2,1],[2,0] 处，面积为 1。    

**示例 3：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/23/3.png)
            **输入：** [[0,3],[1,2],[3,1],[1,3],[2,1]]    **输出：** 0    **解释：** 没法从这些点中组成任何矩形。    

**示例 4：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2018/12/21/4c.png)**
            **输入：** [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]    **输出：** 2.00000    **解释：** 最小面积的矩形出现在 [2,1],[2,3],[3,3],[3,1] 处，面积为 2。    



**提示：**

  1. `1 <= points.length <= 50`
  2. `0 <= points[i][0] <= 40000`
  3. `0 <= points[i][1] <= 40000`
  4. 所有的点都是不同的。
  5. 与真实值误差不超过 `10^-5` 的答案将视为正确结果。


**Tags:** Geometry, Array, Math

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/minimum-area-rectangle-ii
