# [Check if the Sentence Is Pangram][title]

## Description

**全字母句** 指包含英语字母表中每个字母至少一次的句子。

给你一个仅由小写英文字母组成的字符串 `sentence` ，请你判断 `sentence` 是否为 **全字母句** 。

如果是，返回 __`true` ；否则，返回 __`false` 。

**示例 1：**
            **输入：** sentence = "thequickbrownfoxjumpsoverthelazydog"    **输出：** true    **解释：**sentence 包含英语字母表中每个字母至少一次。    

**示例 2：**
            **输入：** sentence = "leetcode"    **输出：** false    

**提示：**

  * `1 <= sentence.length <= 1000`
  * `sentence` 由小写英语字母组成


**Tags:** Hash Table, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return set(sentence)==set(list('abcdefghijklmnopqrstuvwxyz'))
```

[title]: https://leetcode-cn.com/problems/check-if-the-sentence-is-pangram
