# [Circle and Rectangle Overlapping][title]

## Description

给你一个以 (`radius`, `x_center`, `y_center`) 表示的圆和一个与坐标轴平行的矩形 (`x1`, `y1`, `x2`,
`y2`)，其中 (`x1`, `y1`) 是矩形左下角的坐标，(`x2`, `y2`) 是右上角的坐标。

如果圆和矩形有重叠的部分，请你返回 True ，否则返回 False 。

换句话说，请你检测是否 **存在** 点 (xi, yi) ，它既在圆上也在矩形上（两者都包括点落在边界上的情况）。



**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2020/04/04/sample_4_1728.png)
            **输入：** radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1    **输出：** true    **解释：** 圆和矩形有公共点 (1,0)     

**示例 2：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2020/04/04/sample_2_1728.png)**
            **输入：** radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1    **输出：** true    

**示例 3：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2020/04/04/sample_6_1728.png)**
            **输入：** radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3    **输出：** true    

**示例 4：**
            **输入：** radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1    **输出：** false    



**提示：**

  * `1 <= radius <= 2000`
  * `-10^4 <= x_center, y_center, x1, y1, x2, y2 <= 10^4`
  * `x1 < x2`
  * `y1 < y2`


**Tags:** Geometry, Math

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/circle-and-rectangle-overlapping
