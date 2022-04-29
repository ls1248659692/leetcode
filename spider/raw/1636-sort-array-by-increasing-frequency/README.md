# [Sort Array by Increasing Frequency][title]

## Description

给你一个整数数组 `nums` ，请你将数组按照每个值的频率 **升序** 排序。如果有多个值的频率相同，请你按照数值本身将它们 **降序** 排序。

请你返回排序后的数组。

**示例 1：**
            **输入：** nums = [1,1,2,2,2,3]    **输出：** [3,1,1,2,2,2]    **解释：** '3' 频率为 1，'1' 频率为 2，'2' 频率为 3 。    

**示例 2：**
            **输入：** nums = [2,3,1,3,2]    **输出：** [1,3,3,2,2]    **解释：** '2' 和 '3' 频率都为 2 ，所以它们之间按照数值本身降序排序。    

**示例 3：**
            **输入：** nums = [-1,1,-6,4,5,-6,1,4,1]    **输出：** [5,-1,4,4,-6,-6,1,1,1]

**提示：**

  * `1 <= nums.length <= 100`
  * `-100 <= nums[i] <= 100`


**Tags:** Array, Hash Table, Sorting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: (nums.count(x), -x))

```

[title]: https://leetcode-cn.com/problems/sort-array-by-increasing-frequency
