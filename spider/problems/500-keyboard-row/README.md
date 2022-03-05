# [Keyboard Row][title]

## Description

给你一个字符串数组 `words` ，只返回可以使用在 **美式键盘** 同一行的字母打印出来的单词。键盘如下图所示。

**美式键盘** 中：

  * 第一行由字符 `"qwertyuiop"` 组成。
  * 第二行由字符 `"asdfghjkl"` 组成。
  * 第三行由字符 `"zxcvbnm"` 组成。

![American keyboard](https://assets.leetcode-cn.com/aliyun-lc-
upload/uploads/2018/10/12/keyboard.png)

**示例 1：**
            **输入：** words = ["Hello","Alaska","Dad","Peace"]    **输出：** ["Alaska","Dad"]    

**示例 2：**
            **输入：** words = ["omk"]    **输出：** []    

**示例 3：**
            **输入：** words = ["adsdf","sfd"]    **输出：** ["adsdf","sfd"]    

**提示：**

  * `1 <= words.length <= 20`
  * `1 <= words[i].length <= 100`
  * `words[i]` 由英文字母（小写和大写字母）组成


**Tags:** Array, Hash Table, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return [wd for wd in words  if set(list(wd.lower())).issubset(set(list("qwertyuiop"))) or set(list(wd.lower())).issubset(set(list("asdfghjkl"))) or set(list(wd.lower())).issubset(set(list("zxcvbnm")))]
```

[title]: https://leetcode-cn.com/problems/keyboard-row
