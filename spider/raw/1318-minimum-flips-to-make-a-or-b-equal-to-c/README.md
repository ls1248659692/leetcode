# [Minimum Flips to Make a OR b Equal to c][title]

## Description

给你三个正整数 `a`、`b` 和 `c`。

你可以对 `a` 和 `b` 的二进制表示进行位翻转操作，返回能够使按位或运算   `a` OR `b` == `c`  成立的最小翻转次数。

「位翻转操作」是指将一个数的二进制表示任何单个位上的 1 变成 0 或者 0 变成 1 。



**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2020/01/11/sample_3_1676.png)
            **输入：** a = 2, b = 6, c = 5    **输出：** 3    **解释：** 翻转后 a = 1 , b = 4 , c = 5 使得 a OR b == c

**示例 2：**
            **输入：** a = 4, b = 2, c = 7    **输出：** 1    

**示例 3：**
            **输入：** a = 1, b = 2, c = 3    **输出：** 0    



**提示：**

  * `1 <= a <= 10^9`
  * `1 <= b <= 10^9`
  * `1 <= c <= 10^9`


**Tags:** Bit Manipulation

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/minimum-flips-to-make-a-or-b-equal-to-c
