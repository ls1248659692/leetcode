# [Valid Word Abbreviation][title]

## Description

字符串可以用 **缩写** 进行表示， **缩写** 的方法是将任意数量的 **不相邻** 的子字符串替换为相应子串的长度。例如，字符串
`"substitution"` 可以缩写为（不止这几种方法）：

  * `"s10n"` (`"s _**ubstitutio**_ n"`)
  * `"sub4u4"` (`"sub _**stit**_ u _**tion**_ "`)
  * `"12"` (`" _ **substitution**_ "`)
  * `"su3i1u2on"` (`"su _**bst**_ i _**t**_ u _**ti**_ on"`)
  * `"substitution"` (没有替换子字符串)

下列是不合法的缩写：

  * `"s55n"` (`"s  _ubsti_   _tutio_  n"`，两处缩写相邻)
  * `"s010n"` (缩写存在前导零)
  * `"s0ubstitution"` (缩写是一个空字符串)

给你一个字符串单词 `word` 和一个缩写 `abbr` ，判断这个缩写是否可以是给定单词的缩写。

**子字符串** 是字符串中连续的 **非空** 字符序列。



**示例 1：**
            **输入：** word = "internationalization", abbr = "i12iz4n"    **输出：** true    **解释：** 单词 "internationalization" 可以缩写为 "i12iz4n" ("i _**nternational**_ iz _**atio**_ n") 。    

**示例 2：**
            **输入：** word = "apple", abbr = "a2e"    **输出：** false    **解释：** 单词 "apple" 无法缩写为 "a2e" 。    



**提示：**

  * `1 <= word.length <= 20`
  * `word` 仅由小写英文字母组成
  * `1 <= abbr.length <= 10`
  * `abbr` 由小写英文字母和数字组成
  * `abbr` 中的所有数字均符合 32-bit 整数范围


**Tags:** Two Pointers, String

**Difficulty:** Easy

## 思路

[title]: https://leetcode-cn.com/problems/valid-word-abbreviation
