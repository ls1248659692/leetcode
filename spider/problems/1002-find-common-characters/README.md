# [Find Common Characters][title]

## Description

给你一个字符串数组 `words` ，请你找出所有在 `words` 的每个字符串中都出现的共用字符（ **包括重复字符** ），并以数组形式返回。你可以按
**任意顺序** 返回答案。



**示例 1：**
            **输入：** words = ["bella","label","roller"]    **输出：** ["e","l","l"]    

**示例 2：**
            **输入：** words = ["cool","lock","cook"]    **输出：** ["c","o"]    



**提示：**

  * `1 <= words.length <= 100`
  * `1 <= words[i].length <= 100`
  * `words[i]` 由小写英文字母组成


**Tags:** Array, Hash Table, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
         wli = [[wd.count(ch)for ch in  [chr(ord('a')+i) for i in range(26)]]  for wd in words ]
         ali = [[chr(ord('a')+i)]*min([ww[i] for ww in wli] ) for i in range(26)]
         print (ali)
         
         return [el for rr in ali for el in rr]
```

[title]: https://leetcode-cn.com/problems/find-common-characters
