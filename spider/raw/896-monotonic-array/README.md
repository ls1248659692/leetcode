# [Monotonic Array][title]

## Description

如果数组是单调递增或单调递减的，那么它是  **单调** _的_ 。

如果对于所有 `i <= j`，`nums[i] <= nums[j]`，那么数组 `nums` 是单调递增的。 如果对于所有 `i <=
j`，`nums[i]> = nums[j]`，那么数组 `nums` 是单调递减的。

当给定的数组 `nums` 是单调数组时返回 `true`，否则返回 `false`。



**示例 1：**
            **输入：** nums = [1,2,2,3]    **输出：** true    

**示例 2：**
            **输入：** nums = [6,5,4,4]    **输出：** true    

**示例 3：**
            **输入：** nums = [1,3,2]    **输出：** false    



**提示：**

  * `1 <= nums.length <= 105`
  * `-105 <= nums[i] <= 105`


**Tags:** Array

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return nums==sorted(nums) or nums ==sorted(nums,reverse=True)
```

[title]: https://leetcode-cn.com/problems/monotonic-array
