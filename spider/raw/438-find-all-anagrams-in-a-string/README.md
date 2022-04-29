# [Find All Anagrams in a String][title]

## Description

给定两个字符串 `s` 和 `p`，找到 `s` ** ** 中所有 `p` ** ** 的  **异位词
**的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

**异位词** 指由相同字母重排列形成的字符串（包括相同的字符串）。



**示例  1:**
            **输入:** s = "cbaebabacd", p = "abc"    **输出:** [0,6]    **解释:**    起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。    起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。    

**  示例 2:**
            **输入:** s = "abab", p = "ab"    **输出:** [0,1,2]    **解释:**    起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。    起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。    起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。    



**提示:**

  * `1 <= s.length, p.length <= 3 * 104`
  * `s` 和 `p` 仅包含小写字母


**Tags:** Hash Table, String, Sliding Window

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):return []
        sp = ''.join(sorted(list(p)))
        return [i for i in range(len(s)-len(p)+1) if ''.join(sorted(list(s[i:i+len(p)]))) == sp]
```

[title]: https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
