# [Maximum Repeating Substring][title]

## Description

给你一个字符串 `sequence` ，如果字符串 `word` 连续重复 `k` 次形成的字符串是 `sequence` 的一个子字符串，那么单词
`word` 的 **重复值为`k`** **** 。单词 `word` 的 **最** **大重复值** 是单词 `word` 在 `sequence`
中最大的重复值。如果 `word` 不是 `sequence` 的子串，那么重复值 `k` 为 `0` 。

给你一个字符串 `sequence` 和 `word` ，请你返回 **最大重复值`k` **。

**示例 1：**
            **输入：** sequence = "ababc", word = "ab"    **输出：** 2    **解释：** "abab" 是 " **abab** c" 的子字符串。    

**示例 2：**
            **输入：** sequence = "ababc", word = "ba"    **输出：** 1    **解释：** "ba" 是 "a **ba** bc" 的子字符串，但 "baba" 不是 "ababc" 的子字符串。    

**示例 3：**
            **输入：** sequence = "ababc", word = "ac"    **输出：** 0    **解释：** "ac" 不是 "ababc" 的子字符串。    

**提示：**

  * `1 <= sequence.length <= 100`
  * `1 <= word.length <= 100`
  * `sequence` 和 `word` 都只包含小写英文字母。


**Tags:** String, String Matching

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        se,wd,k = sequence,word,100//len(word)
        if wd not in se:return 0
        while k>0 and wd*k not in se:
            k-=1
        return k        
```

[title]: https://leetcode-cn.com/problems/maximum-repeating-substring
