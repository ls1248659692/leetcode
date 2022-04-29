# [Perfect Rectangle][title]

## Description

给你一个数组 `rectangles` ，其中 `rectangles[i] = [xi, yi, ai, bi]`
表示一个坐标轴平行的矩形。这个矩形的左下顶点是 `(xi, yi)` ，右上顶点是 `(ai, bi)` 。

如果所有矩形一起精确覆盖了某个矩形区域，则返回 `true` ；否则，返回 `false` 。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/27/perectrec1-plane.jpg)
            **输入：** rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]    **输出：** true    **解释：** 5 个矩形一起可以精确地覆盖一个矩形区域。     

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/03/27/perfectrec2-plane.jpg)
            **输入：** rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]    **输出：** false    **解释：** 两个矩形之间有间隔，无法覆盖成一个矩形。

**示例 3：**

![](https://assets.leetcode.com/uploads/2021/03/27/perfecrrec4-plane.jpg)
            **输入：** rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]    **输出：** false    **解释：** 因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。



**提示：**

  * `1 <= rectangles.length <= 2 * 104`
  * `rectangles[i].length == 4`
  * `-105 <= xi, yi, ai, bi <= 105`


**Tags:** Array, Line Sweep

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/perfect-rectangle
