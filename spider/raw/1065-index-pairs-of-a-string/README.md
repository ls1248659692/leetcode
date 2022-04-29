# [Index Pairs of a String][title]

## Description

给出  **字符串**`text` 和  **字符串列表** `words`, 返回所有的索引对 `[i, j]` 使得在索引对范围内的子字符串
`text[i]...text[j]`（包括 `i` 和 `j`）属于字符串列表 `words`。



**示例 1:**
            **输入:** text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]    **输出:** [[3,7],[9,13],[10,17]]    

**示例 2:**
            **输入:** text = "ababa", words = ["aba","ab"]    **输出:** [[0,1],[0,2],[2,3],[2,4]]    **解释:** 注意，返回的配对可以有交叉，比如，"aba" 既在 [0,2] 中也在 [2,4] 中    



**提示:**

  1. 所有字符串都只包含小写字母。
  2. 保证 `words` 中的字符串无重复。
  3. `1 <= text.length <= 100`
  4. `1 <= words.length <= 20`
  5. `1 <= words[i].length <= 50`
  6. 按序返回索引对 `[i,j]`（即，按照索引对的第一个索引进行排序，当第一个索引对相同时按照第二个索引对排序）。


**Tags:** Trie, Array, String, Sorting

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/index-pairs-of-a-string
