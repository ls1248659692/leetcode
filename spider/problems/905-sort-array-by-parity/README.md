# [Sort Array By Parity][title]

## Description

给定一个非负整数数组 `A`，返回一个数组，在该数组中， `A` 的所有偶数元素之后跟着所有奇数元素。

你可以返回满足此条件的任何数组作为答案。



**示例：**
            **输入：** [3,1,2,4]    **输出：** [2,4,3,1]    输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。    



**提示：**

  1. `1 <= A.length <= 5000`
  2. `0 <= A[i] <= 5000`


**Tags:** Array, Two Pointers, Sorting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [e for e in nums if not e%2] +  [e for e in nums if  e%2]
```

[title]: https://leetcode-cn.com/problems/sort-array-by-parity
