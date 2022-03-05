# [Pascal's Triangle][title]

## Description

给定一个非负整数 _`numRows`，_生成「杨辉三角」的前 _`numRows` _行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

![](https://pic.leetcode-cn.com/1626927345-DZmfxB-PascalTriangleAnimated2.gif)

**示例 1:**
            **输入:** numRows = 5    **输出:** [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]    

**示例 2:**
            **输入:** numRows = 1    **输出:** [[1]]    

**提示:**

  * `1 <= numRows <= 30`


**Tags:** Array, Dynamic Programming

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:return [[1]]
        elif numRows==2:return [[1],[1,1]]
        else:
            res = self.generate(numRows-1)
            res.append([1]+ [res[-1][i]+res[-1][i+1] for i in range(numRows-2)]+[1])
            return res
```

[title]: https://leetcode-cn.com/problems/pascals-triangle
