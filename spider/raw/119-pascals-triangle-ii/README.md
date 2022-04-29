# [Pascal's Triangle II][title]

## Description

给定一个非负索引 `rowIndex`，返回「杨辉三角」的第 `rowIndex` __ 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

![](https://pic.leetcode-cn.com/1626927345-DZmfxB-PascalTriangleAnimated2.gif)

**示例 1:**
            **输入:** rowIndex = 3    **输出:** [1,3,3,1]    

**示例 2:**
            **输入:** rowIndex = 0    **输出:** [1]    

**示例 3:**
            **输入:** rowIndex = 1    **输出:** [1,1]    

**提示:**

  * `0 <= rowIndex <= 33`

**进阶：**

你可以优化你的算法到 `_O_ ( _rowIndex_ )` 空间复杂度吗？


**Tags:** Array, Dynamic Programming

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        start = [1,2,1]
        for j in range(2,rowIndex):
            temp = []
            for i in range(1,len(start)):
                temp = temp + [start[i] + start[i-1]]
            start = [1] + temp + [1]
        return(start)
```

[title]: https://leetcode-cn.com/problems/pascals-triangle-ii
