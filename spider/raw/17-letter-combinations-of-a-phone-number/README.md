# [Letter Combinations of a Phone Number][title]

## Description

给定一个仅包含数字 `2-9` 的字符串，返回所有它能表示的字母组合。答案可以按 **任意顺序** 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/11/09/200px-
telephone-keypad2svg.png)



**示例 1：**
            **输入：** digits = "23"    **输出：** ["ad","ae","af","bd","be","bf","cd","ce","cf"]    

**示例 2：**
            **输入：** digits = ""    **输出：** []    

**示例 3：**
            **输入：** digits = "2"    **输出：** ["a","b","c"]    



**提示：**

  * `0 <= digits.length <= 4`
  * `digits[i]` 是范围 `['2', '9']` 的一个数字。


**Tags:** Hash Table, String, Backtracking

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:return []
        tdic={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        dic = {kk:list(tdic[kk])for kk in tdic}
        print(dic)
        d_li = [dic[int(dd)]for dd in digits]
        t_li=d_li[0]
        for ii in range(1,len(d_li)):
            tmp_li = []
            for jj in range(len(d_li[ii])):
                tmp_li += [el +d_li[ii][jj] for el in t_li]
            t_li = tmp_li
        return t_li
```

[title]: https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
