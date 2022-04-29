# [Product of Array Except Self][title]

## Description

给你一个整数数组 `nums`，返回 _数组  `answer` ，其中 `answer[i]` 等于 `nums` 中除 `nums[i]`
之外其余各元素的乘积_ 。

题目数据 **保证** 数组 `nums`之中任意元素的全部前缀元素和后缀的乘积都在  **32 位** 整数范围内。

请 **不要使用除法，** 且在 `O( _n_ )` 时间复杂度内完成此题。



**示例 1:**
            **输入:** nums = [1,2,3,4]    **输出:** [24,12,8,6]    

**示例 2:**
            **输入:** nums = [-1,1,0,-3,3]    **输出:** [0,0,9,0,0]    



**提示：**

  * `2 <= nums.length <= 105`
  * `-30 <= nums[i] <= 30`
  * **保证** 数组 `nums`之中任意元素的全部前缀元素和后缀的乘积都在  **32 位** 整数范围内



**进阶：** 你可以在 `O(1)` 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 **不被视为** 额外空间。）


**Tags:** Array, Prefix Sum

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p =math.prod([e for e in nums if e])
        return [0]*len(nums) if nums.count(0)>1 else [p if e==0 else 0 for e in nums] if nums.count(0)==1 else [p//e for e in nums]
```

[title]: https://leetcode-cn.com/problems/product-of-array-except-self
