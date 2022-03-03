# [Rectangle Area II][title]

## Description

我们给出了一个（轴对齐的）二维矩形列表 `rectangles` 。 对于 `rectangle[i] = [x1, y1, x2,
y2]`，其中（x1，y1）是矩形 `i` 左下角的坐标， `(xi1, yi1)` 是该矩形 **左下角** 的坐标， `(xi2, yi2)` 是该矩形
**右上角** 的坐标。

计算平面中所有 `rectangles` 所覆盖的 **总面积** 。任何被两个或多个矩形覆盖的区域应只计算 **一次** 。

返回 _**总面积** _。因为答案可能太大，返回 `109 + 7` 的  **模**  。



**示例 1：**

![](https://s3-lc-
upload.s3.amazonaws.com/uploads/2018/06/06/rectangle_area_ii_pic.png)
            **输入：** rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]    **输出：** 6    **解释：** 如图所示，三个矩形覆盖了总面积为6的区域。    从(1,1)到(2,2)，绿色矩形和红色矩形重叠。    从(1,0)到(2,3)，三个矩形都重叠。    

**示例 2：**
            **输入：** rectangles = [[0,0,1000000000,1000000000]]    **输出：** 49    **解释：** 答案是 1018 对 (109 + 7) 取模的结果， 即 49 。    



**提示：**

  * `1 <= rectangles.length <= 200`
  * `rectanges[i].length = 4`
  * `0 <= xi1, yi1, xi2, yi2 <= 109`
  * 矩形叠加覆盖后的总面积不会超越 `2^63 - 1` ，这意味着可以用一个 64 位有符号整数来保存面积结果。


**Tags:** Segment Tree, Array, Ordered Set, Line Sweep

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/rectangle-area-ii
