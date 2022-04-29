# [Minimum Cost to Separate Sentence Into Rows][title]

## Description

给定一个由空格分隔的单词组成的字符串 `sentence` 和一个整数 `k`。你的任务是将 `sentence` 分成 **多行** ，每行中的字符数
**最多** 为 `k`。你可以假设 `sentence` 不以空格开头或结尾，并且 `sentence` 中的单词由单个空格分隔。

你可以通过在 `sentence` 中的单词间插入换行来分隔 `sentence` 。一个单词 **不能**
被分成两行。每个单词只能使用一次，并且单词顺序不能重排。同一行中的相邻单词应该由单个空格分隔，并且每行都不应该以空格开头或结尾。

一行长度为 `n` 的字符串的 **分隔成本** 是 `(k - n)2` ， **总成本** 就是 **除开** 最后一行以外的
**其它所有行的分隔成本** 之和。

  * 以 `sentence = "i love leetcode"` 和`k = 12`为例：     * 将`sentence` 分成 `"i"`, `"love"`, 和`"leetcode"` 的成本为 `(12 - 1)2 + (12 - 4)2 = 185`。    * 将`sentence` 分成 `"i love"`, 和`"leetcode"` 的成本为 `(12 - 6)2 = 36`。    * 将`sentence` 分成 `"i"`, 和`"love leetcode"` 是不可能的，因为 `"love leetcode"` 的长度大于 `k`。

返回 _将_`sentence` _分隔成行的 **最低的** 可能总成本。_



**示例 1:**
            **输入:** sentence = "i love leetcode", k = 12    **输出:** 36    **解释:**    将 sentence 分成"i", "love", 和"leetcode" 的成本为 (12 - 1)2 + (12 - 4)2 = 185.    将 sentence 分成"i love", 和"leetcode" 的成本为 (12 - 6)2 = 36.    将 sentence 分成"i", "love leetcode" 是不可能的，因为 "love leetcode" 的长度为 13.    36是最低的可能总成本，因此返回它    

**示例 2:**
            **输入:** sentence = "apples and bananas taste great", k = 7    **输出:** 21    **解释:**    将 sentence 分成"apples", "and", "bananas", "taste", 和"great" 的成本为 (7 - 6)2 + (7 - 3)2 + (7 - 7)2 + (7 - 5)2 = 21.    21是最低的可能总成本，因此返回它    

**示例 3:**
            **输入:** sentence = "a", k = 5    **输出:** 0    **解释:**    最后一行的成本不包括在总成本中，而sentence只有一行，所以返回0



**提示:**

  * `1 <= sentence.length <= 5000`
  * `1 <= k <= 5000`
  * `sentence` 中每个单词长度最大为 `k`.
  * `sentence` 只包含小写字母和空格.
  * `sentence` 不会以空格开头或结尾.
  * `sentence` 中的单词以单个空格分隔.


**Tags:** Array, Dynamic Programming

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/minimum-cost-to-separate-sentence-into-rows
