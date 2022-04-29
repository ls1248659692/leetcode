# [Missing Number LCCI][title]

## Description

数组`nums`包含从`0`到`n`的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。你有办法在O(n)时间内完成吗？

**注意：** 本题相对书上原题稍作改动

**示例 1：**
            **输入：** [3,0,1]    **输出：** 2



**示例 2：**
            **输入：** [9,6,4,2,3,5,7,0,1]    **输出：** 8    


**Tags:** Bit Manipulation, Array, Hash Table, Math, Sorting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        r = [0]*(len(nums)+1)
        for n in nums:
            r[n]=1
        for j in range(len(r)):
            if not r[j]:return j
```

[title]: https://leetcode-cn.com/problems/missing-number-lcci
