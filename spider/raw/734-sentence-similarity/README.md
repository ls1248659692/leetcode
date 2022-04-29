# [Sentence Similarity][title]

## Description

我们可以将一个句子表示为一个单词数组，例如，句子 `"I am happy with leetcode"` 可以表示为 `arr =
["I","am",happy","with","leetcode"]`

给定两个句子 `sentence1` 和 `sentence2` 分别表示为一个字符串数组，并给定一个字符串对 `similarPairs` ，其中
`similarPairs[i] = [xi, yi]` 表示两个单词 `xi` and `yi` 是相似的。

如果 `sentence1` 和 `sentence2` 相似则返回 `true` ，如果不相似则返回 `false` 。

两个句子是相似的，如果:

  * 它们具有 **相同的长度** (即相同的字数)
  * `sentence1[i]` 和 `sentence2[i]` 是相似的

请注意，一个词总是与它自己相似，也请注意，相似关系是不可传递的。例如，如果单词 `a` 和 `b` 是相似的，单词 `b` 和 `c` 也是相似的，那么
`a` 和 `c`  **不一定相似** 。



**示例 1:**
            **输入:** sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]    **输出:** true    **解释:** 这两个句子长度相同，每个单词都相似。    

**示例 2:**
            **输入:** sentence1 = ["great"], sentence2 = ["great"], similarPairs = []    **输出:** true    **解释:** 一个单词和它本身相似。

**示例 3:**
            **输入:** sentence1 = ["great"], sentence2 = ["doubleplus","good"], similarPairs = [["great","doubleplus"]]    **输出:** false    **解释:** 因为它们长度不同，所以返回false。    



**提示:**

  * `1 <= sentence1.length, sentence2.length <= 1000`
  * `1 <= sentence1[i].length, sentence2[i].length <= 20`
  * `sentence1[i]` 和 `sentence2[i]` 只包含大小写英文字母
  * `0 <= similarPairs.length <= 2000`
  * `similarPairs[i].length == 2`
  * `1 <= xi.length, yi.length <= 20`
  * 所有对 `(xi, yi)` 都是 **不同** 的


**Tags:** Array, Hash Table, String

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/sentence-similarity
