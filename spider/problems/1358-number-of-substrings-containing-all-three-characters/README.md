# [Number of Substrings Containing All Three Characters][title]

## Description

给你一个字符串 `s` ，它只包含三种字符 a, b 和 c 。

请你返回 a，b 和 c 都  **至少  **出现过一次的子字符串数目。



**示例 1：**
            **输入：** s = "abcabc"    **输出：** 10    **解释：** 包含 a，b 和 c 各至少一次的子字符串为 _ "_abc _" , "_abca _" , "_abcab _" , "_abcabc _" , "_bca _" , "_bcab _" , "_bcabc _" , "_cab _" , "_cabc _" _和 _ "_abc _" _( **相同** **字符串算多次** ) _。_    

**示例 2：**
            **输入：** s = "aaacb"    **输出：** 3    **解释：** 包含 a，b 和 c 各至少一次的子字符串为 _ "_aaacb _" , "_aacb _" _和 _ "_acb _" 。_    

**示例 3：**
            **输入：** s = "abc"    **输出：** 1    



**提示：**

  * `3 <= s.length <= 5 x 10^4`
  * `s` 只包含字符 a，b 和 c 。


**Tags:** Hash Table, String, Sliding Window

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/number-of-substrings-containing-all-three-characters
