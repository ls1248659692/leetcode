# [Vowel Spellchecker][title]

## Description

在给定单词列表 `wordlist` 的情况下，我们希望实现一个拼写检查器，将查询单词转换为正确的单词。

对于给定的查询单词 `query`，拼写检查器将会处理两类拼写错误：

  * 大小写：如果查询匹配单词列表中的某个单词（ **不区分大小写** ），则返回的正确单词与单词列表中的大小写相同。     * 例如：`wordlist = ["yellow"]`, `query = "YellOw"`: `correct = "yellow"`    * 例如：`wordlist = ["Yellow"]`, `query = "yellow"`: `correct = "Yellow"`    * 例如：`wordlist = ["yellow"]`, `query = "yellow"`: `correct = "yellow"`
  * 元音错误：如果在将查询单词中的元音 `('a', 'e', 'i', 'o', 'u')`  分别替换为任何元音后，能与单词列表中的单词匹配（ **不区分大小写** ），则返回的正确单词与单词列表中的匹配项大小写相同。     * 例如：`wordlist = ["YellOw"]`, `query = "yollow"`: `correct = "YellOw"`    * 例如：`wordlist = ["YellOw"]`, `query = "yeellow"`: `correct = ""` （无匹配项）    * 例如：`wordlist = ["YellOw"]`, `query = "yllw"`: `correct = ""` （无匹配项）

此外，拼写检查器还按照以下优先级规则操作：

  * 当查询完全匹配单词列表中的某个单词（ **区分大小写** ）时，应返回相同的单词。
  * 当查询匹配到大小写问题的单词时，您应该返回单词列表中的第一个这样的匹配项。
  * 当查询匹配到元音错误的单词时，您应该返回单词列表中的第一个这样的匹配项。
  * 如果该查询在单词列表中没有匹配项，则应返回空字符串。

给出一些查询 `queries`，返回一个单词列表 `answer`，其中 `answer[i]` 是由查询 `query = queries[i]`
得到的正确单词。



**示例 1：**
            **输入：** wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]    **输出：** ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]

**示例 2:**
            **输入：** wordlist = ["yellow"], queries = ["YellOw"]    **输出：** ["yellow"]    



**提示：**

  * `1 <= wordlist.length, queries.length <= 5000`
  * `1 <= wordlist[i].length, queries[i].length <= 7`
  * `wordlist[i]` 和 `queries[i]` 只包含英文字母


**Tags:** Array, Hash Table, String

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/vowel-spellchecker
