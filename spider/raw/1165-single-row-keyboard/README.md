# [Single-Row Keyboard][title]

## Description

我们定制了一款特殊的键盘，所有的键都 **排列在一行上**  。

给定一个长度为 `26` 的字符串 `keyboard` ，来表示键盘的布局(索引从 `0` 到 `25` )。一开始，你的手指在索引 `0`
处。要输入一个字符，你必须把你的手指移动到所需字符的索引处。手指从索引 `i` 移动到索引 `j` 所需要的时间是 `|i - j|`。

您需要输入一个字符串 `word` 。写一个函数来计算用一个手指输入需要多少时间。



**示例 1：**
            **输入：** keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"    **输出：** 4    **解释：** 从 0 号键移动到 2 号键来输出 'c'，又移动到 1 号键来输出 'b'，接着移动到 0 号键来输出 'a'。    总用时 = 2 + 1 + 1 = 4.     

**示例 2：**
            **输入：** keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"    **输出：** 73    



**提示：**

  * `keyboard.length == 26`
  * `keyboard` 按某种特定顺序排列，并包含每个小写英文字母一次。
  * `1 <= word.length <= 104`
  * `word[i]` 为小写英文字母


**Tags:** Hash Table, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        idx = 0
        cnt = 0
        for i in word:
            idxn =keyboard.index(i)
            cnt += abs(idxn-idx)
            idx = idxn
        return cnt
```

[title]: https://leetcode-cn.com/problems/single-row-keyboard
