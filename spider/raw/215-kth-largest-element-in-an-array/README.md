# [Kth Largest Element in an Array][title]

## Description

给定整数数组 `nums` 和整数 `k`，请返回数组中第 `**k**` 个最大的元素。

请注意，你需要找的是数组排序后的第 `k` 个最大的元素，而不是第 `k` 个不同的元素。

**示例 1:**
            **输入:** [3,2,1,5,6,4] 和 k = 2    **输出:** 5    

**示例 2:**
            **输入:** [3,2,3,1,2,4,5,5,6] 和 k = 4    **输出:** 4

**提示：**

  * `1 <= k <= nums.length <= 104`
  * `-104 <= nums[i] <= 104`


**Tags:** Array, Divide and Conquer, Quickselect, Sorting, Heap (Priority Queue)

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        r =sorted(nums)
        return r[-k]
```

[title]: https://leetcode-cn.com/problems/kth-largest-element-in-an-array
