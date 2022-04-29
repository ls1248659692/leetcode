# [Minimum Distance to the Target Element][title]

## Description

给你一个整数数组 `nums` （下标 **从 0 开始** 计数）以及两个整数 `target` 和 `start` ，请你找出一个下标 `i` ，满足
`nums[i] == target` 且 `abs(i - start)` **最小化** 。注意：`abs(x)` 表示 `x` 的绝对值。

返回 `abs(i - start)` 。

题目数据保证 `target` 存在于 `nums` 中。

**示例 1：**
            **输入：** nums = [1,2,3,4,5], target = 5, start = 3    **输出：** 1    **解释：** nums[4] = 5 是唯一一个等于 target 的值，所以答案是 abs(4 - 3) = 1 。    

**示例 2：**
            **输入：** nums = [1], target = 1, start = 0    **输出：** 0    **解释：** nums[0] = 1 是唯一一个等于 target 的值，所以答案是 abs(0 - 0) = 0 。    

**示例 3：**
            **输入：** nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0    **输出：** 0    **解释：** nums 中的每个值都是 1 ，但 nums[0] 使 abs(i - start) 的结果得以最小化，所以答案是 abs(0 - 0) = 0 。    

**提示：**

  * `1 <= nums.length <= 1000`
  * `1 <= nums[i] <= 104`
  * `0 <= start < nums.length`
  * `target` 存在于 `nums` 中


**Tags:** Array

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = len(nums)
        for i, num in enumerate(nums):
            if num == target:
                res = min(res, abs(i - start))
        return res
```

[title]: https://leetcode-cn.com/problems/minimum-distance-to-the-target-element
