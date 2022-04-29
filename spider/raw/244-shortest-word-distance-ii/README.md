# [Shortest Word Distance II][title]

## Description

请设计一个类，使该类的构造函数能够接收一个字符串数组。然后再实现一个方法，该方法能够分别接收两个单词 _，_ 并返回列表中这两个单词之间的最短距离。

实现 `WordDistanc` 类:

  * `WordDistance(String[] wordsDict)` 用字符串数组 `wordsDict` 初始化对象。
  * `int shortest(String word1, String word2)` 返回数组 `worddict` 中 `word1` 和 `word2` 之间的最短距离。



**示例 1:**
            **输入:**     ["WordDistance", "shortest", "shortest"]    [[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]    **输出:**    [null, 3, 1]        **解释：**    WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);    wordDistance.shortest("coding", "practice"); // 返回 3    wordDistance.shortest("makes", "coding");    // 返回 1



**注意:**

  * `1 <= wordsDict.length <= 3 * 104`
  * `1 <= wordsDict[i].length <= 10`
  * `wordsDict[i]` 由小写英文字母组成
  * `word1` 和 `word2` 在数组 `wordsDict` 中
  * `word1 != word2`
  *  `shortest` 操作次数不大于 `5000` 


**Tags:** Design, Array, Hash Table, Two Pointers, String

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/shortest-word-distance-ii
