# [Number of Valid Words in a Sentence][title]

## Description

句子仅由小写字母（`'a'` 到 `'z'`）、数字（`'0'` 到 `'9'`）、连字符（`'-'`）、标点符号（`'!'`、`'.'` 和
`','`）以及空格（`' '`）组成。每个句子可以根据空格分解成 **一个或者多个 token** ，这些 token 之间由一个或者多个空格 `' '`
分隔。

如果一个 token 同时满足下述条件，则认为这个 token 是一个有效单词：

  * 仅由小写字母、连字符和/或标点（不含数字）组成。
  * **至多一个** 连字符 `'-'` 。如果存在，连字符两侧应当都存在小写字母（`"a-b"` 是一个有效单词，但 `"-ab"` 和 `"ab-"` 不是有效单词）。
  * **至多一个** 标点符号。如果存在，标点符号应当位于 token 的 **末尾** 。

这里给出几个有效单词的例子：`"a-b."`、`"afad"`、`"ba-c"`、`"a!"` 和 `"!"` 。

给你一个字符串 `sentence` ，请你找出并返回 __`sentence` 中 **有效单词的数目** 。



**示例 1：**
            **输入：** sentence = " _ **cat**_ _**and**_  _**dog**_ "    **输出：** 3    **解释：** 句子中的有效单词是 "cat"、"and" 和 "dog"    

**示例 2：**
            **输入：** sentence = "!this  1-s b8d!"    **输出：** 0    **解释：** 句子中没有有效单词    "!this" 不是有效单词，因为它以一个标点开头    "1-s" 和 "b8d" 也不是有效单词，因为它们都包含数字    

**示例 3：**
            **输入：** sentence = " _ **alice**_ _**and**_  _**bob**_ _**are**_ _**playing**_ stone-game10"    **输出：** 5    **解释：** 句子中的有效单词是 "alice"、"and"、"bob"、"are" 和 "playing"    "stone-game10" 不是有效单词，因为它含有数字    

**示例 4：**
            **输入：** sentence = " _ **he**_ _**bought**_ 2 _**pencils,**_ 3 _**erasers,**_ _**and**_ 1  _**pencil-sharpener.**_ "    **输出：** 6    **解释：** 句子中的有效单词是 "he"、"bought"、"pencils,"、"erasers,"、"and" 和 "pencil-sharpener."    



**提示：**

  * `1 <= sentence.length <= 1000`
  * `sentence` 由小写英文字母、数字（`0-9`）、以及字符（`' '`、`'-'`、`'!'`、`'.'` 和 `','`）组成
  * 句子中至少有 `1` 个 token


**Tags:** String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def countValidWords(self, sentence: str) -> int:
        st = [el for el in sentence.split() if el ]
        cnt =0
        for wd in st:
            #print(wd)
            if set(list(wd)).issubset( set(list('abcdefghijklmnopqrstuvwxyz-!.,')) ):
                #print('if0',wd)
                if '-' not in wd  or ('-' in wd and wd[0]!='-' and wd[-1]!='-' and wd.count('-')<2  ):
                    if len(wd)>=2 and wd[-1] in '!.,' and wd[-2]=='-':continue
                    #print('if1',wd)
                    if not set(list('!.,')).intersection(list(wd)) or (set(list('!.,')).intersection(list(wd)) and not set(list('!.,')).intersection(list(wd[:-1]))):
                        #print(wd)
                        cnt+=1
        return cnt
```

[title]: https://leetcode-cn.com/problems/number-of-valid-words-in-a-sentence
