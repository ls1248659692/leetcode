# [Shifting Letters][title]

## Description

有一个由小写字母组成的字符串 `s`，和一个长度相同的整数数组 `shifts`。

我们将字母表中的下一个字母称为原字母的 _移位_  `shift()` （由于字母表是环绕的， `'z'` 将会变成 `'a'`）。

  * 例如，`shift('a') = 'b', ``shift('t') = 'u'`, 以及 `shift('z') = 'a'`。

对于每个 `shifts[i] = x` ， 我们会将 `s` 中的前 `i + 1` 个字母移位 `x` 次。

返回 _将所有这些移位都应用到`s` 后最终得到的字符串_ 。



**示例 1：**
            **输入：** s = "abc", shifts = [3,5,9]    **输出：** "rpl"    **解释：**    我们以 "abc" 开始。    将 S 中的第 1 个字母移位 3 次后，我们得到 "dbc"。    再将 S 中的前 2 个字母移位 5 次后，我们得到 "igc"。    最后将 S 中的这 3 个字母移位 9 次后，我们得到答案 "rpl"。    

**示例 2:**
            **输入:** s = "aaa", shifts = [1,2,3]    **输出:** "gfd"    



**提示:**

  * `1 <= s.length <= 105`
  * `s` 由小写英文字母组成
  * `shifts.length == s.length`
  * `0 <= shifts[i] <= 109`

​​​​​​


**Tags:** Array, String

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/shifting-letters
