# [最长不含重复字符的子字符串 LCOF][title]

## Description

请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。



**示例  1:**
            **输入:** "abcabcbb"    **输出:** 3     **解释:** 因为无重复字符的最长子串是 "abc"，所以其长度为 3。    

**示例 2:**
            **输入:** "bbbbb"    **输出:** 1    **解释:** 因为无重复字符的最长子串是 "b"，所以其长度为 1。    

**示例 3:**
            **输入:** "pwwkew"    **输出:** 3    **解释:** 因为无重复字符的最长子串是 "wke"，所以其长度为 3。         请注意，你的答案必须是 **子串** 的长度，"pwke" 是一个 _子序列，_ 不是子串。    



提示：

  * `s.length <= 40000`

注意：本题与主站 3 题相同：<https://leetcode-cn.com/problems/longest-substring-without-
repeating-characters/>


**Tags:** Hash Table, String, Sliding Window

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        rli = [(i,i+1) for i in range(len(s))]
        while rli:
            rla= rli
            rli = [(i-1,j) for i,j in rli if i>=1 and s[i-1]not in s[i:j]]
        return rla[0][1]-rla[0][0]
```

[title]: https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof
