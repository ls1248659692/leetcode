# [Word Ladder][title]

## Description

字典 `wordList` 中从单词 `beginWord` _ _ 和 `endWord` 的 **转换序列** 是一个按下述规格形成的序列
`beginWord -> s1 -> s2 -> ... -> sk`：

  * 每一对相邻的单词只差一个字母。
  *  对于 `1 <= i <= k` 时，每个 `si` 都在 `wordList` 中。注意， `beginWord` _ _ 不需要在 `wordList` 中。
  * `sk == endWord`

给你两个单词 __`beginWord` _ _ 和 `endWord` 和一个字典 `wordList` ，返回 _从  `beginWord` 到
`endWord` 的 **最短转换序列** 中的 **单词数目**_ 。如果不存在这样的转换序列，返回 `0` 。



**示例 1：**
            **输入：** beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]    **输出：** 5    **解释：** 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。    

**示例 2：**
            **输入：** beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]    **输出：** 0    **解释：** endWord "cog" 不在字典中，所以无法进行转换。



**提示：**

  * `1 <= beginWord.length <= 10`
  * `endWord.length == beginWord.length`
  * `1 <= wordList.length <= 5000`
  * `wordList[i].length == beginWord.length`
  * `beginWord`、`endWord` 和 `wordList[i]` 由小写英文字母组成
  * `beginWord != endWord`
  * `wordList` 中的所有字符串 **互不相同**


**Tags:** Breadth-First Search, Hash Table, String

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/word-ladder
