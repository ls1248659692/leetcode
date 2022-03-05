# [Longest Word With All Prefixes][title]

## Description

给定一个字符串数组 `words`，找出 `words` 中 **所有的前缀** 都在 `words` 中的 **最长** 字符串。

  * 例如，令 `words = ["a", "app", "ap"]`。字符串 `"app"` 含前缀 `"ap"` 和 `"a"` ，都在 `words` 中。

返回符合上述要求的字符串。如果存在多个（符合条件的）相同长度的字符串，返回字典序中最小的字符串，如果这样的字符串不存在，返回 __`""`。

**示例 1:**
            **输入：** words = ["k","ki","kir","kira", "kiran"]    **输出：** "kiran"    **解释：** "kiran" 含前缀 "kira"、 "kir"、 "ki"、 和 "k"，这些前缀都出现在 words 中。    

**示例 2:**
            **输入：** words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]    **输出：** "apple"    **解释：** "apple" 和 "apply" 都在 words 中含有各自的所有前缀。    然而，"apple" 在字典序中更小，所以我们返回之。    

**示例 3:**
            **输入：** words = ["abc", "bc", "ab", "qwe"]    **输出：** ""    

**提示：**

  * `1 <= words.length <= 105`
  * `1 <= words[i].length <= 105`
  * `1 <= sum(words[i].length) <= 105`


**Tags:** Depth-First Search, Trie

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/longest-word-with-all-prefixes
