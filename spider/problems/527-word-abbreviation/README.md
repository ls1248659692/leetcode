# [Word Abbreviation][title]

## Description

给你一个字符串数组 `words` ，该数组由 **互不相同** 的若干字符串组成，请你找出并返回每个单词的 **最小缩写** 。

生成缩写的规则如下 **：**

  1. 初始缩写由起始字母+省略字母的数量+结尾字母组成。
  2. 若存在冲突，亦即多于一个单词有同样的缩写，则使用更长的前缀代替首字母，直到从单词到缩写的映射唯一。换而言之，最终的缩写必须只能映射到一个单词。
  3. 若缩写并不比原单词更短，则保留原样。



**示例 1：**
            **输入:** words = ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]    **输出:** ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]    

**示例 2：**
            **输入：** words = ["aa","aaa"]    **输出：** ["aa","aaa"]    



**提示：**

  * `1 <= words.length <= 400`
  * `2 <= words[i].length <= 400`
  * `words[i]` 由小写英文字母组成
  * `words` 中的所有字符串 **互不相同**


**Tags:** Greedy, Trie, Array, String, Sorting

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/word-abbreviation
