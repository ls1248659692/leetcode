# [Palindrome Partitioning III][title]

## Description

给你一个由小写字母组成的字符串 `s`，和一个整数 `k`。

请你按下面的要求分割字符串：

  * 首先，你可以将 `s` 中的部分字符修改为其他的小写英文字母。
  * 接着，你需要把 `s` 分割成 `k` 个非空且不相交的子串，并且每个子串都是回文串。

请返回以这种方式分割字符串所需修改的最少字符数。



**示例 1：**
            **输入：** s = "abc", k = 2    **输出：** 1    **解释：** 你可以把字符串分割成 "ab" 和 "c"，并修改 "ab" 中的 1 个字符，将它变成回文串。    

**示例 2：**
            **输入：** s = "aabbc", k = 3    **输出：** 0    **解释：** 你可以把字符串分割成 "aa"、"bb" 和 "c"，它们都是回文串。

**示例 3：**
            **输入：** s = "leetcode", k = 8    **输出：** 0    



**提示：**

  * `1 <= k <= s.length <= 100`
  * `s` 中只含有小写英文字母。


**Tags:** String, Dynamic Programming

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/palindrome-partitioning-iii
