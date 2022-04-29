# [Generalized Abbreviation][title]

## Description

单词的 **广义缩写词** 可以通过下述步骤构造：先取任意数量的 **不重叠、不相邻** 的子字符串，再用它们各自的长度进行替换。

  * 例如，`"abcde"` 可以缩写为：     * `"a3e"`（`"bcd"` 变为 `"3"` ）    * `"1bcd1"`（`"a"` 和 `"e"` 都变为 `"1"`）    * `"5"` (`"abcde"` 变为 `"5"`)    * `"abcde"` (没有子字符串被代替)
  * 然而，这些缩写是 **无效的** ：     * `"23"`（`"ab"` 变为 `"2"` ，`"cde"` 变为 `"3"` ）是无效的，因为被选择的字符串是相邻的    * `"22de"` (`"ab"` 变为 `"2"` ， `"bc"` 变为 `"2"`)  是无效的，因为被选择的字符串是重叠的

给你一个字符串 `word` ，返回  _一个由_  `word` 的 _所有可能 **广义缩写词** 组成的列表_ 。按 **任意顺序** 返回答案。



**示例 1：**
            **输入：** word = "word"    **输出：** ["4","3d","2r1","2rd","1o2","1o1d","1or1","1ord","w3","w2d","w1r1","w1rd","wo2","wo1d","wor1","word"]    

**示例 2：**
            **输入：** word = "a"    **输出：** ["1","a"]    



**提示：**

  * `1 <= word.length <= 15`
  * `word` 仅由小写英文字母组成


**Tags:** Bit Manipulation, String, Backtracking

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/generalized-abbreviation
