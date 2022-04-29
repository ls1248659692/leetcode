# [Line Reflection][title]

## Description

在一个二维平面空间中，给你 n 个点的坐标。问，是否能找出一条平行于 y ** ** 轴的直线，让这些点关于这条直线成镜像排布？

**注意** ：题目数据中可能有重复的点。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/04/23/356_example_1.PNG)
            **输入：** points = [[1,1],[-1,1]]    **输出：** true    **解释：** 可以找出 x = 0 这条线。    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/04/23/356_example_2.PNG)
            **输入：** points = [[1,1],[-1,-1]]    **输出：** false    **解释：** 无法找出这样一条线。



**提示：**

  * `n == points.length`
  * `1 <= n <= 10^4`
  * `-10^8 <= points[i][j] <= 10^8`



**进阶：** 你能找到比 O( _n_ 2) 更优的解法吗?


**Tags:** Array, Hash Table, Math

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/line-reflection
