# [Unique Length-3 Palindromic Subsequences][title]

## Description

给你一个字符串 `s` ，返回 `s` 中 **长度为 3** 的 **不同回文子序列** 的个数。

即便存在多种方法来构建相同的子序列，但相同的子序列只计数一次。

**回文** 是正着读和反着读一样的字符串。

**子序列** 是由原字符串删除其中部分字符（也可以不删除）且不改变剩余字符之间相对顺序形成的一个新字符串。

  * 例如，`"ace"` 是 `" ** _a_** b ** _c_** d ** _e_** "` 的一个子序列。

**示例 1：**
            **输入：** s = "aabca"    **输出：** 3    **解释：** 长度为 3 的 3 个回文子序列分别是：    - "aba" (" ** _a_** a ** _b_** c ** _a_** " 的子序列)    - "aaa" (" ** _aa_** bc ** _a_** " 的子序列)    - "aca" (" ** _a_** ab ** _ca_** " 的子序列)    

**示例 2：**
            **输入：** s = "adc"    **输出：** 0    **解释：** "adc" 不存在长度为 3 的回文子序列。    

**示例 3：**
            **输入：** s = "bbcbaba"    **输出：** 4    **解释：** 长度为 3 的 4 个回文子序列分别是：    - "bbb" (" ** _bb_** c ** _b_** aba" 的子序列)    - "bcb" (" ** _b_** b ** _cb_** aba" 的子序列)    - "bab" (" ** _b_** bcb ** _ab_** a" 的子序列)    - "aba" ("bbcb ** _aba_** " 的子序列)    

**提示：**

  * `3 <= s.length <= 105`
  * `s` 仅由小写英文字母组成


**Tags:** Hash Table, String, Prefix Sum

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/unique-length-3-palindromic-subsequences
