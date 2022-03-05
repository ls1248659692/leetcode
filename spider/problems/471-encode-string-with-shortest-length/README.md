# [Encode String with Shortest Length][title]

## Description

给定一个 **非空** 字符串，将其编码为具有最短长度的字符串。

编码规则是：`k[encoded_string]`，其中在方括号 `encoded_string` __ 中的内容重复 `k` 次。

**注：**

  * _k_ 为正整数
  * 如果编码的过程不能使字符串缩短，则不要对其进行编码。如果有多种编码方式，返回 **任意一种** 即可

**示例 1：**
            **输入：** s = "aaa"    **输出：** "aaa"    **解释：** 无法将其编码为更短的字符串，因此不进行编码。    

**示例 2：**
            **输入：** s = "aaaaa"    **输出：** "5[a]"    **解释：** "5[a]" 比 "aaaaa" 短 1 个字符。    

**示例 3：**
            **输入：** s = "aaaaaaaaaa"    **输出：** "10[a]"    **解释：** "a9[a]" 或 "9[a]a" 都是合法的编码，和 "10[a]" 一样长度都为 5。    

**示例 4：**
            **输入：** s = "aabcaabcd"    **输出：** "2[aabc]d"    **解释：** "aabc" 出现两次，因此一种答案可以是 "2[aabc]d"。    

**示例 5：**
            **输入：** s = "abbbabbbcabbbabbbc"    **输出：** "2[2[abbb]c]"    **解释：** "abbbabbbc" 出现两次，但是 "abbbabbbc" 可以编码为 "2[abbb]c"，因此一种答案可以是 "2[2[abbb]c]"。    

**提示：**

  * `1 <= s.length <= 150`
  * `s` 由小写英文字母组成


**Tags:** String, Dynamic Programming

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/encode-string-with-shortest-length
