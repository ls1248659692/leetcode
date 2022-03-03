# [Valid Permutations for DI Sequence][title]

## Description

给定一个长度为 `n` 的字符串 `s` ，其中 `s[i]` 是:

  * `“D”` 意味着减少，或者
  * `“I”` 意味着增加

**有效排列**  是对有 `n + 1` 个在 `[0, n]`  范围内的整数的一个排列 `perm` ，使得对所有的 `i`：

  * 如果 `s[i] == 'D'`，那么 `perm[i] > perm[i+1]`，以及；
  * 如果 `s[i] == 'I'`，那么 `perm[i] < perm[i+1]`。

返回 _**有效排列**  _`perm` _的数量_ 。因为答案可能很大，所以请 **返回你的答案对**  `109 + 7` **  取余**。



**示例 1：**
            **输入：** s = "DID"    **输出：** 5    **解释：**    (0, 1, 2, 3) 的五个有效排列是：    (1, 0, 3, 2)    (2, 0, 3, 1)    (2, 1, 3, 0)    (3, 0, 2, 1)    (3, 1, 2, 0)    

**示例 2:**
            **输入:** s = "D"    **输出:** 1    



**提示:**

  * `n == s.length`
  * `1 <= n <= 200`
  * `s[i]` 不是 `'I'` 就是 `'D'`


**Tags:** Dynamic Programming

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/valid-permutations-for-di-sequence
