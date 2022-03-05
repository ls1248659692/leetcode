# [Find the Duplicate Number][title]

## Description

给定一个包含 `n + 1` 个整数的数组 `nums` ，其数字都在 `[1, n]` 范围内（包括 `1` 和 `n`），可知至少存在一个重复的整数。

假设 `nums` 只有 **一个重复的整数** ，返回  **这个重复的数** 。

你设计的解决方案必须 **不修改** 数组 `nums` 且只用常量级 `O(1)` 的额外空间。



**示例 1：**
            **输入：** nums = [1,3,4,2,2]    **输出：** 2    

**示例 2：**
            **输入：** nums = [3,1,3,4,2]    **输出：** 3    



**提示：**

  * `1 <= n <= 105`
  * `nums.length == n + 1`
  * `1 <= nums[i] <= n`
  * `nums` 中 **只有一个整数** 出现 **两次或多次** ，其余整数均只出现 **一次**



**进阶：**

  * 如何证明 `nums` 中至少存在一个重复的数字?
  * 你可以设计一个线性级时间复杂度 `O(n)` 的解决方案吗？


**Tags:** Bit Manipulation, Array, Two Pointers, Binary Search

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={n-1:i for i,n in enumerate(nums)}
        print(d)
        return [n for i,n in enumerate(nums) if d[n-1]!=i][0]
```

[title]: https://leetcode-cn.com/problems/find-the-duplicate-number
