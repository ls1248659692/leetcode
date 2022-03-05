# [Bold Words in String][title]

## Description

给定一个关键词集合 `words` 和一个字符串 `s`，将所有 `s` 中出现的关键词 `words[i]` 加粗。所有在标签 `<b>` 和 `<b>`
中的字母都会加粗。

加粗后返回 `s` 。返回的字符串需要使用尽可能少的标签，当然标签应形成有效的组合。



**示例 1:**
            **输入:** words = ["ab","bc"], s = "aabcd"    **输出:** "a<b>abc</b>d"    **解释:** 注意返回 "a<b>a<b>b</b>c</b>d" 会使用更多的标签，因此是错误的。    

**示例 2:**
            **输入:** words = ["ab","cb"], s = "aabcd"    **输出:** "a<b>ab</b>cd"    



**提示:**

  * `1 <= s.length <= 500`
  * `0 <= words.length <= 50`
  * `1 <= words[i].length <= 10`
  * `s` 和 `words[i]` 由小写英文字母组成



**注：** 此题与「616 - 给字符串添加加粗标签」相同 - <https://leetcode-cn.com/problems/add-bold-
tag-in-string/>


**Tags:** Trie, Array, Hash Table, String, String Matching

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/bold-words-in-string
