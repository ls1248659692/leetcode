# [Largest Unique Number][title]

## Description

给你一个整数数组 `A`，请找出并返回在该数组中仅出现一次的最大整数。

如果不存在这个只出现一次的整数，则返回 -1。



**示例 1：**
            **输入：** [5,7,3,9,4,9,8,3,1]    **输出：** 8    **解释：**    数组中最大的整数是 9，但它在数组中重复出现了。而第二大的整数是 8，它只出现了一次，所以答案是 8。    

**示例 2：**
            **输入：** [9,9,8,8]    **输出：** -1    **解释：**    数组中不存在仅出现一次的整数。    



**提示：**

  1. `1 <= A.length <= 2000`
  2. `0 <= A[i] <= 1000`


**Tags:** Array, Hash Table, Sorting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        for i in sorted(set(nums),reverse = True):
            if nums.count(i) == 1:
                return i
        return -1
```

[title]: https://leetcode-cn.com/problems/largest-unique-number
