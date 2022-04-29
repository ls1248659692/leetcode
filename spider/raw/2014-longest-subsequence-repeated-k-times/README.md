# [Longest Subsequence Repeated k Times][title]

## Description

给你一个长度为 `n` 的字符串 `s` ，和一个整数 `k` 。请你找出字符串 `s` 中 **重复** `k` 次的 **最长子序列** 。

**子序列** 是由其他字符串删除某些（或不删除）字符派生而来的一个字符串。

如果 `seq * k` 是 `s` 的一个子序列，其中 `seq * k` 表示一个由 `seq` 串联 `k` 次构造的字符串，那么就称 `seq`
**** 是字符串 `s` 中一个 **重复`k` 次** 的子序列。

  * 举个例子，`"bba"` 是字符串 `"bababcba"` 中的一个重复 `2` 次的子序列，因为字符串 `"bbabba"` 是由 `"bba"` 串联 `2` 次构造的，而 `"bbabba"` 是字符串 `" _ **b**_ a _ **bab**_ c _ **ba**_ "` 的一个子序列。

返回字符串 `s` 中 **重复 k 次的最长子序列**   。如果存在多个满足的子序列，则返回 **字典序最大**
的那个。如果不存在这样的子序列，返回一个 **空** 字符串。



**示例 1：**

![example 1](https://assets.leetcode.com/uploads/2021/08/30/longest-
subsequence-repeat-k-times.png)
            **输入：** s = "letsleetcode", k = 2    **输出：** "let"    **解释：** 存在两个最长子序列重复 2 次：let" 和 "ete" 。    "let" 是其中字典序最大的一个。    

**示例 2：**
            **输入：** s = "bb", k = 2    **输出：** "b"    **解释：** 重复 2 次的最长子序列是 "b" 。    

**示例 3：**
            **输入：** s = "ab", k = 2    **输出：** ""    **解释：** 不存在重复 2 次的最长子序列。返回空字符串。    

**示例 4：**
            **输入：** s = "bbabbabbbbabaababab", k = 3    **输出：** "bbbb"    **解释：** 在 " ** _bb_** a _ **bb**_ a _ **bbbb**_ a _ **b**_ aa _ **b**_ a _ **b**_ a _ **b**_ " 中重复 3 次的最长子序列是 "bbbb" 。    



**提示：**

  * `n == s.length`
  * `2 <= k <= 2000`
  * `2 <= n < k * 8`
  * `s` 由小写英文字母组成


**Tags:** Greedy, String, Backtracking, Counting, Enumeration

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/longest-subsequence-repeated-k-times
