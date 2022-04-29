# [Find Words That Can Be Formed by Characters][title]

## Description

给你一份『词汇表』（字符串数组） `words` 和一张『字母表』（字符串） `chars`。

假如你可以用 `chars` 中的『字母』（字符）拼写出 `words` 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。

注意：每次拼写（指拼写词汇表中的一个单词）时，`chars` 中的每个字母都只能用一次。

返回词汇表 `words` 中你掌握的所有单词的 **长度之和** 。



**示例 1：**
            **输入：** words = ["cat","bt","hat","tree"], chars = "atach"    **输出：** 6    **解释：**    可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。    

**示例 2：**
            **输入：** words = ["hello","world","leetcode"], chars = "welldonehoneyr"    **输出：** 10    **解释：**    可以形成字符串 "hello" 和 "world"，所以答案是 5 + 5 = 10。    



**提示：**

  1. `1 <= words.length <= 1000`
  2. `1 <= words[i].length, chars.length <= 100`
  3. 所有字符串中都仅包含小写英文字母


**Tags:** Array, Hash Table, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cd = {ch:chars.count(ch) for ch in set(list(chars))}
        res = [wd for wd in words if sum(1 for ch in set(list(wd)) if cd.get(ch,0)-wd.count(ch)<0)<=0]
        print(res)
        return sum(len(el) for el in res)
```

[title]: https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters
