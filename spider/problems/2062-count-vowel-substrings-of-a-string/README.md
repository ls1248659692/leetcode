# [Count Vowel Substrings of a String][title]

## Description

**子字符串** 是字符串中的一个连续（非空）的字符序列。

**元音子字符串** 是 **仅** 由元音（`'a'`、`'e'`、`'i'`、`'o'` 和 `'u'`）组成的一个子字符串，且必须包含
**全部五种** 元音。

给你一个字符串 `word` ，统计并返回 `word` 中 **元音子字符串的数目** 。



**示例 1：**
            **输入：** word = "aeiouu"    **输出：** 2    **解释：** 下面列出 word 中的元音子字符串（斜体加粗部分）：    - " _ **aeiou**_ u"    - " ** _aeiouu_** "    

**示例 2：**
            **输入：** word = "unicornarihan"    **输出：** 0    **解释：** word 中不含 5 种元音，所以也不会存在元音子字符串。    

**示例 3：**
            **输入：** word = "cuaieuouac"    **输出：** 7    **解释：** 下面列出 word 中的元音子字符串（斜体加粗部分）：    - "c _ **uaieuo**_ uac"    - "c _ **uaieuou**_ ac"    - "c _ **uaieuoua**_ c"    - "cu _ **aieuo**_ uac"    - "cu _ **aieuou**_ ac"    - "cu _ **aieuoua**_ c"    - "cua _ **ieuoua**_ c"

**示例 4：**
            **输入：** word = "bbaeixoubb"    **输出：** 0    **解释：** 所有包含全部五种元音的子字符串都含有辅音，所以不存在元音子字符串。    



**提示：**

  * `1 <= word.length <= 100`
  * `word` 仅由小写英文字母组成


**Tags:** Hash Table, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count = 0
        for i in range(len(word)):
            for j in range(len(word)+1):
                if i != j and sorted(set(word[i:j])) == ['a', 'e', 'i', 'o', 'u']:
                    count = count + 1
        return count
```

[title]: https://leetcode-cn.com/problems/count-vowel-substrings-of-a-string
