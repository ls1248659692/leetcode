# [Longest Substring Without Repeating Characters][title]

## Description

给定一个字符串 `s` ，请你找出其中不含有重复字符的  **最长子串  **的长度。



**示例  1:**
            **输入:** s = "abcabcbb"    **输出:** 3     **解释:** 因为无重复字符的最长子串是 "abc"，所以其长度为 3。    

**示例 2:**
            **输入:** s = "bbbbb"    **输出:** 1    **解释:** 因为无重复字符的最长子串是 "b"，所以其长度为 1。    

**示例 3:**
            **输入:** s = "pwwkew"    **输出:** 3    **解释:** 因为无重复字符的最长子串是 "wke"，所以其长度为 3。         请注意，你的答案必须是 **子串** 的长度，"pwke" 是一个 _子序列，_ 不是子串。    



**提示：**

  * `0 <= s.length <= 5 * 104`
  * `s` 由英文字母、数字、符号和空格组成


**Tags:** Hash Table, String, Sliding Window

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def v7(s):
            e,wins,mx = 1,s[0],1
            while e<len(s):
                idx =wins.find(s[e])
                wins = (wins[1+idx:] if idx>=0 else wins)+s[e]
                if mx<len(wins): mx=len(wins)
                # if idx<0:
                #     wins = wins+s[e]
                #     if mx<len(wins): mx=len(wins)
                # else:
                #     wins=wins[1+idx:]+s[e]
                e+=1
            return mx
        if not s:return 0
        return v7(s)       
    
```

[title]: https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
