# [Spiral Matrix III][title]

## Description

在 `R` 行 `C` 列的矩阵上，我们从 `(r0, c0)` 面朝东面开始

这里，网格的西北角位于第一行第一列，网格的东南角位于最后一行最后一列。

现在，我们以顺时针按螺旋状行走，访问此网格中的每个位置。

每当我们移动到网格的边界之外时，我们会继续在网格之外行走（但稍后可能会返回到网格边界）。

最终，我们到过网格的所有 `R * C` 个空间。

按照访问顺序返回表示网格位置的坐标列表。



**示例 1：**
            **输入：** R = 1, C = 4, r0 = 0, c0 = 0    **输出：** [[0,0],[0,1],[0,2],[0,3]]        ![](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/08/24/example_1.png)    



**示例 2：**
            **输入：** R = 5, C = 6, r0 = 1, c0 = 4    **输出：** [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]        ![](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/08/24/example_2.png)    



**提示：**

  1. `1 <= R <= 100`
  2. `1 <= C <= 100`
  3. `0 <= r0 < R`
  4. `0 <= c0 < C`


**Tags:** Array, Matrix, Simulation

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/spiral-matrix-iii
