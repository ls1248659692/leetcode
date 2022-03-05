# [Lonely Pixel I][title]

## Description

给你一个大小为 `m x n` 的图像 `picture` ，图像由黑白像素组成，`'B'` 表示黑色像素，`'W'` 表示白色像素，请你统计并返回图像中
**黑色** 孤独像素的数量。

**黑色孤独像素** 的定义为：如果黑色像素 `'B'` 所在的同一行和同一列不存在其他黑色像素，那么这个黑色像素就是黑色孤独像素。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/11/pixel1.jpg)
            **输入：** picture = [["W","W","B"],["W","B","W"],["B","W","W"]]    **输出：** 3    **解释：** 全部三个 'B' 都是黑色的孤独像素    

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/11/11/pixel2.jpg)
            **输入：** picture = [["B","B","B"],["B","B","W"],["B","B","B"]]    **输出：** 0    



**提示：**

  * `m == picture.length`
  * `n == picture[i].length`
  * `1 <= m, n <= 500`
  * `picture[i][j]` 为 `'W'` 或 `'B'`


**Tags:** Array, Hash Table, Matrix

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/lonely-pixel-i
