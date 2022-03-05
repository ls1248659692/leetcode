# [Excel Sheet Column Number][title]

## Description

给你一个字符串 `columnTitle` ，表示 Excel 表格中的列名称。返回 _该列名称对应的列序号_  。

例如：
            A -> 1    B -> 2    C -> 3    ...    Z -> 26    AA -> 27    AB -> 28     ...



**示例 1:**
            **输入:** columnTitle = "A"    **输出:** 1    

**示例  2:**
            **输入:** columnTitle = "AB"    **输出:** 28    

**示例  3:**
            **输入:** columnTitle = "ZY"    **输出:** 701



**提示：**

  * `1 <= columnTitle.length <= 7`
  * `columnTitle` 仅由大写英文组成
  * `columnTitle` 在范围 `["A", "FXSHRXW"]` 内


**Tags:** Math, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        # 26**n*a + 26**1*b
        for idx,value in enumerate(reversed(columnTitle)):
            # print(ord(i)-64)
            ans += (ord(value)-64)*26**idx
        return ans
```

[title]: https://leetcode-cn.com/problems/excel-sheet-column-number
