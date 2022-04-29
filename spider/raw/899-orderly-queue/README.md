# [Orderly Queue][title]

## Description

给定一个字符串 `s` 和一个整数 `k` 。你可以从 `s` 的前 `k` 个字母中选择一个，并把它加到字符串的末尾。

返回 _在应用上述步骤的任意数量的移动后，字典上最小的字符串  _。



**示例 1：**
            **输入：** s = "cba", k = 1    **输出：** "acb"    **解释：**    在第一步中，我们将第一个字符（“c”）移动到最后，获得字符串 “bac”。    在第二步中，我们将第一个字符（“b”）移动到最后，获得最终结果 “acb”。    

**示例 2：**
            **输入：** s = "baaca", k = 3    **输出：** "aaabc"    **解释：** 在第一步中，我们将第一个字符（“b”）移动到最后，获得字符串 “aacab”。    在第二步中，我们将第三个字符（“c”）移动到最后，获得最终结果 “aaabc”。    



**提示：**

  * `1 <= k <= S.length <= 1000`
  * `s` 只由小写字母组成。


**Tags:** Math, String, Sorting

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/orderly-queue
