# [Perform String Shifts][title]

## Description

给定一个包含小写英文字母的字符串 `s` 以及一个矩阵 `shift`，其中 `shift[i] = [direction, amount]`：

  * `direction` 可以为 `0` （表示左移）或 `1` （表示右移）。
  * `amount` 表示 `s` 左右移的位数。
  * 左移 1 位表示移除 `s` 的第一个字符，并将该字符插入到 `s` 的结尾。
  * 类似地，右移 1 位表示移除 `s` 的最后一个字符，并将该字符插入到 `s` 的开头。

对这个字符串进行所有操作后，返回最终结果。



**示例 1：**
            **输入：** s = "abc", shift = [[0,1],[1,2]]    **输出：** "cab"    **解释：**    [0,1] 表示左移 1 位。 "abc" -> "bca"    [1,2] 表示右移 2 位。 "bca" -> "cab"

**示例 2：**
            **输入：** s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]    **输出：** "efgabcd"    **解释：**     [1,1] 表示右移 1 位。 "abcdefg" -> "gabcdef"    [1,1] 表示右移 1 位。 "gabcdef" -> "fgabcde"    [0,2] 表示左移 2 位。 "fgabcde" -> "abcdefg"    [1,3] 表示右移 3 位。 "abcdefg" -> "efgabcd"



**提示：**

  * `1 <= s.length <= 100`
  * `s` 只包含小写英文字母
  * `1 <= shift.length <= 100`
  * `shift[i].length == 2`
  * `0 <= shift[i][0] <= 1`
  * `0 <= shift[i][1] <= 100`


**Tags:** Array, Math, String

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/perform-string-shifts
