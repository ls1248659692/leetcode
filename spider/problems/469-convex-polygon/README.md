# [Convex Polygon][title]

## Description

给定 **X-Y** 平面上的一组点 `points` ，其中 `points[i] = [xi, yi]` 。这些点按顺序连成一个多边形。

如果该多边形为  **凸**  多边形[（凸多边形的定义）](https://baike.baidu.com/item/凸多边形/)则返回 `true`
，否则返回 `false` 。

你可以假设由给定点构成的多边形总是一个
简单的多边形[（简单多边形的定义）](https://baike.baidu.com/item/%E7%AE%80%E5%8D%95%E5%A4%9A%E8%BE%B9%E5%BD%A2)。换句话说，我们要保证每个顶点处恰好是两条边的汇合点，并且这些边
**互不相交  **。



**示例 1：**

![](https://assets.leetcode.com/uploads/2021/04/09/covpoly1-plane.jpg)
            **输入:** points = [[0,0],[0,5],[5,5],[5,0]]    **输出:** true

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/04/09/covpoly2-plane.jpg)
            **输入:** points = [[0,0],[0,10],[10,10],[10,0],[5,5]]    **输出:** false



**提示:**

  * `3 <= points.length <= 104`
  * `points[i].length == 2`
  * `-104 <= xi, yi <= 104`
  * 所有点都 **不同**




**Tags:** Geometry, Math

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/convex-polygon
