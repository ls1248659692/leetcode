# [Number of Ways of Cutting a Pizza][title]

## Description

给你一个 `rows x cols` 大小的矩形披萨和一个整数 `k` ，矩形包含两种字符： `'A'` （表示苹果）和 `'.'`
（表示空白格子）。你需要切披萨 `k-1` 次，得到 `k` 块披萨并送给别人。

切披萨的每一刀，先要选择是向垂直还是水平方向切，再在矩形的边界上选一个切的位置，将披萨一分为二。如果垂直地切披萨，那么需要把左边的部分送给一个人，如果水平地切，那么需要把上面的部分送给一个人。在切完最后一刀后，需要把剩下来的一块送给最后一个人。

请你返回确保每一块披萨包含  **至少**  一个苹果的切披萨方案数。由于答案可能是个很大的数字，请你返回它对 10^9 + 7 取余的结果。



**示例 1：**

**![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2020/05/10/ways_to_cut_apple_1.png)**
            **输入：** pizza = ["A..","AAA","..."], k = 3    **输出：** 3     **解释：** 上图展示了三种切披萨的方案。注意每一块披萨都至少包含一个苹果。    

**示例 2：**
            **输入：** pizza = ["A..","AA.","..."], k = 3    **输出：** 1    

**示例 3：**
            **输入：** pizza = ["A..","A..","..."], k = 1    **输出：** 1    



**提示：**

  * `1 <= rows, cols <= 50`
  * `rows == pizza.length`
  * `cols == pizza[i].length`
  * `1 <= k <= 10`
  * `pizza` 只包含字符 `'A'` 和 `'.'` 。


**Tags:** Memoization, Array, Dynamic Programming, Matrix

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/number-of-ways-of-cutting-a-pizza
