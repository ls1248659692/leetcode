# [Sentence Screen Fitting][title]

## Description

给你一个 `rows x cols` 的屏幕和一个用 **非空** 的单词列表组成的句子，请你计算出给定句子可以在屏幕上完整显示的次数。

**注意：**

  1. 一个单词不能拆分成两行。
  2. 单词在句子中的顺序必须保持不变。
  3. **在一行中** 的两个连续单词必须用一个空格符分隔。
  4. 句子中的单词总量不会超过 100。
  5. 每个单词的长度大于 0 且不会超过 10。
  6. 1 ≤ `rows`, `cols` ≤ 20,000.



**示例 1：**
            **输入：**    rows = 2, cols = 8, 句子 sentence = ["hello", "world"]        **输出：**    1        **解释：**    hello---    world---        **字符 '-' 表示屏幕上的一个空白位置。**    



**示例 2：**
            **输入：**    rows = 3, cols = 6, 句子 sentence = ["a", "bcd", "e"]        **输出：**    2        **解释：**    a-bcd-     e-a---    bcd-e-        **字符 '-' 表示屏幕上的一个空白位置。**    



**示例 3：**
            **输入：**    rows = 4, cols = 5, 句子 sentence = ["I", "had", "apple", "pie"]        **输出：**    1        **解释：**    I-had    apple    pie-I    had--        **字符 '-' 表示屏幕上的一个空白位置。**    




**Tags:** String, Dynamic Programming, Simulation

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/sentence-screen-fitting
