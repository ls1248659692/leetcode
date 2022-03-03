# [Count The Repetitions][title]

## Description

定义 `str = [s, n]` 表示 `str` 由 `n` 个字符串 `s` 连接构成。

  * 例如，`str == ["abc", 3] =="abcabcabc"` 。

如果可以从 `s2` 中删除某些字符使其变为 `s1`，则称字符串 `s1` 可以从字符串 `s2` 获得。

  * 例如，根据定义，`s1 = "abc"` 可以从 `s2 = "ab _ **dbe**_ c"` 获得，仅需要删除加粗且用斜体标识的字符。

现在给你两个字符串 `s1` 和 `s2` 和两个整数 `n1` 和 `n2` 。由此构造得到两个字符串，其中 `str1 = [s1,
n1]`、`str2 = [s2, n2]` 。

请你找出一个最大整数 `m` ，以满足 `str = [str2, m]` 可以从 `str1` 获得。

**示例 1：**
            **输入：** s1 = "acb", n1 = 4, s2 = "ab", n2 = 2    **输出：** 2    

**示例 2：**
            **输入：** s1 = "acb", n1 = 1, s2 = "acb", n2 = 1    **输出：** 1    

**提示：**

  * `1 <= s1.length, s2.length <= 100`
  * `s1` 和 `s2` 由小写英文字母组成
  * `1 <= n1, n2 <= 106`


**Tags:** String, Dynamic Programming

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/count-the-repetitions
