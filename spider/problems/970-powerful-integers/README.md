# [Powerful Integers][title]

## Description

给定三个整数 `x` 、 `y` 和 _ _`bound` _ _ ，返回 _值小于或等于  `bound` 的所有  **强整数**  组成的列表_ 。

如果某一整数可以表示为 `xi + yj` ，其中整数 `i >= 0` 且 `j >= 0`，那么我们认为该整数是一个  **强整数**  。

你可以按 **任何顺序** 返回答案。在你的回答中，每个值 **最多** 出现一次。



**示例 1：**
            **输入：** x = 2, y = 3, bound = 10    **输出：** [2,3,4,5,7,9,10]    **解释：**    2 = 20 + 30    3 = 21 + 30    4 = 20 + 31    5 = 21 + 31    7 = 22 + 31    9 = 23 + 30    10 = 20 + 32

**示例  2：**
            **输入：** x = 3, y = 5, bound = 15    **输出：** [2,4,6,8,10,14]    



**提示：**

  * `1 <= x, y <= 100`
  * `0 <= bound <= 106`


**Tags:** Hash Table, Math

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/powerful-integers
