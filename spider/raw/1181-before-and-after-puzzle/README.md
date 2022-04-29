# [Before and After Puzzle][title]

## Description

给你一个「短语」列表 `phrases`，请你帮忙按规则生成拼接后的「新短语」列表。

「短语」（phrase）是仅由小写英文字母和空格组成的字符串。「短语」的开头和结尾都不会出现空格，「短语」中的空格不会连续出现。

「前后拼接」（Before and After puzzles）是合并两个「短语」形成「新短语」的方法。我们规定拼接时， **第一个短语的最后一个单词**
和 **第二个短语的第一个单词** 必须相同。

返回每两个「短语」 `phrases[i]` 和 `phrases[j]`（`i != j`）进行「前后拼接」得到的「新短语」。

注意，两个「短语」拼接时的顺序也很重要，我们需要同时考虑这两个「短语」。另外，同一个「短语」可以多次参与拼接，但「新短语」不能再参与拼接。

请你按字典序排列并返回「新短语」列表，列表中的字符串应该是 **不重复的** 。



**示例 1：**
            **输入：** phrases = ["writing code","code rocks"]    **输出：** ["writing code rocks"]    

**示例 2：**
            **输入：** phrases = ["mission statement",                    "a quick bite to eat",                    "a chip off the old block",                    "chocolate bar",                    "mission impossible",                    "a man on a mission",                    "block party",                    "eat my words",                    "bar of soap"]    **输出：** ["a chip off the old block party",          "a man on a mission impossible",          "a man on a mission statement",          "a quick bite to eat my words",          "chocolate bar of soap"]    

**示例 3：**
            **输入：** phrases = ["a","b","a"]    **输出：** ["a"]    



**提示：**

  * `1 <= phrases.length <= 100`
  * `1 <= phrases[i].length <= 100`


**Tags:** Array, Hash Table, String, Sorting

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/before-and-after-puzzle
