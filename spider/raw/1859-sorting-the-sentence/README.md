# [Sorting the Sentence][title]

## Description

一个 **句子** 指的是一个序列的单词用单个空格连接起来，且开头和结尾没有任何空格。每个单词都只包含小写或大写英文字母。

我们可以给一个句子添加 **从 1 开始的单词位置索引** ，并且将句子中所有单词 **打乱顺序** 。

  * 比方说，句子 `"This is a sentence"` 可以被打乱顺序得到 `"sentence4 a3 is2 This1"` 或者 `"is2 sentence4 This1 a3"` 。

给你一个 **打乱顺序** 的句子 `s` ，它包含的单词不超过 `9` 个，请你重新构造并得到原本顺序的句子。

**示例 1：**
            **输入：** s = "is2 sentence4 This1 a3"    **输出：** "This is a sentence"    **解释：** 将 s 中的单词按照初始位置排序，得到 "This1 is2 a3 sentence4" ，然后删除数字。    

**示例 2：**
            **输入：** s = "Myself2 Me1 I4 and3"    **输出：** "Me Myself and I"    **解释：** 将 s 中的单词按照初始位置排序，得到 "Me1 Myself2 and3 I4" ，然后删除数字。

**提示：**

  * `2 <= s.length <= 200`
  * `s` 只包含小写和大写英文字母、空格以及从 `1` 到 `9` 的数字。
  * `s` 中单词数目为 `1` 到 `9` 个。
  * `s` 中的单词由单个空格分隔。
  * `s` 不包含任何前导或者后缀空格。


**Tags:** String, Sorting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join ([wd[:-1] for wd in sorted(s.split(),key=lambda xx:xx[-1])])
```

[title]: https://leetcode-cn.com/problems/sorting-the-sentence
