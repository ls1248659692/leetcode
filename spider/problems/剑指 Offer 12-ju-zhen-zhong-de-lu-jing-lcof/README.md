# [矩阵中的路径  LCOF][title]

## Description

给定一个 `m x n` 二维字符网格 `board` 和一个字符串单词 `word` 。如果 `word` 存在于网格中，返回 `true` ；否则，返回
`false` 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。

![](https://assets.leetcode.com/uploads/2020/11/04/word2.jpg)

**示例 1：**
            **输入：** board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"    **输出：** true    

**示例 2：**
            **输入：** board = [["a","b"],["c","d"]], word = "abcd"    **输出：** false    

**提示：**

  * `1 <= board.length <= 200`
  * `1 <= board[i].length <= 200`
  * `board` 和 `word` 仅由大小写英文字母组成

**注意：** 本题与主站 79 题相同：<https://leetcode-cn.com/problems/word-search/>


**Tags:** Array, Backtracking, Matrix

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
