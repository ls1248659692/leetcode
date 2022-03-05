# [Rearrange String k Distance Apart][title]

## Description

给你一个非空的字符串 `s` 和一个整数 `k` ，你要将这个字符串 `s` 中的字母进行重新排列，使得重排后的字符串中相同字母的位置间隔距离 **至少**
为 `k` 。如果无法做到，请返回一个空字符串 `""`。



**示例 1：**
            **输入:** s = "aabbcc", k = 3    **输出:** "abcabc"     **解释:** 相同的字母在新的字符串中间隔至少 3 个单位距离。    

**示例 2:**
            **输入:** s = "aaabc", k = 3    **输出:** ""     **解释:** 没有办法找到可能的重排结果。    

**示例  3:**
            **输入:** s = "aaadbbcc", k = 2    **输出:** "abacabcd"    **解释:** 相同的字母在新的字符串中间隔至少 2 个单位距离。    



**提示：**

  * `1 <= s.length <= 3 * 105`
  * `s` 仅由小写英文字母组成
  * `0 <= k <= s.length`


**Tags:** Greedy, Hash Table, String, Counting, Sorting, Heap (Priority Queue)

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/rearrange-string-k-distance-apart
