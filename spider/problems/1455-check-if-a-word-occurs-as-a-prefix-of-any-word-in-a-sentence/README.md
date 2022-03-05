# [Check If a Word Occurs As a Prefix of Any Word in a Sentence][title]

## Description

给你一个字符串 `sentence` 作为句子并指定检索词为 `searchWord` ，其中句子由若干用 **单个空格** 分隔的单词组成。请你检查检索词
`searchWord` 是否为句子 `sentence` 中任意单词的前缀。

如果 `searchWord` 是某一个单词的前缀，则返回句子 `sentence` 中该单词所对应的下标（ **下标从 1 开始** ）。如果
`searchWord` 是多个单词的前缀，则返回匹配的第一个单词的下标（ **最小下标** ）。如果 `searchWord` 不是任何单词的前缀，则返回
`-1` **** 。

字符串 `s` 的 **前缀** 是 `s` 的任何前导连续子字符串。



**示例 1：**
            **输入：** sentence = "i love eating burger", searchWord = "burg"    **输出：** 4    **解释：** "burg" 是 "burger" 的前缀，而 "burger" 是句子中第 4 个单词。

**示例 2：**
            **输入：** sentence = "this problem is an easy problem", searchWord = "pro"    **输出：** 2    **解释：** "pro" 是 "problem" 的前缀，而 "problem" 是句子中第 2 个也是第 6 个单词，但是应该返回最小下标 2 。    

**示例 3：**
            **输入：** sentence = "i am tired", searchWord = "you"    **输出：** -1    **解释：** "you" 不是句子中任何单词的前缀。        



**提示：**

  * `1 <= sentence.length <= 100`
  * `1 <= searchWord.length <= 10`
  * `sentence` 由小写英文字母和空格组成。
  * `searchWord` 由小写英文字母组成。


**Tags:** String, String Matching

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        se,sw = sentence.split(),searchWord
        for i in range(len(se)):
            if len(se[i])>=len(sw) and se[i][:len(sw)] ==sw: return i+1
        return -1
```

[title]: https://leetcode-cn.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence
