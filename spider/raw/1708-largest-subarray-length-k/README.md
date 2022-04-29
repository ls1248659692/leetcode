# [Largest Subarray Length K][title]

## Description

在数组 `A` 和数组 `B` 中，对于第一个满足 `A[i] != B[i]` 的索引 `i` ，当 `A[i] > B[i]` 时，数组 `A`
大于数组 `B`。

例如，对于索引从 `0` 开始的数组：

  * `[1,3,2,4] > [1,2,2,4]` ，因为在索引 `1` 上， `3 > 2`。
  * `[1,4,4,4] < [2,1,1,1]` ，因为在索引 `0` 上， `1 < 2`。

一个数组的子数组是原数组上的一个连续子序列。

给定一个包含 **不同** 整数的整数类型数组 `nums` ，返回 `nums` 中长度为 `k` 的最大子数组。

**示例 1:**
            **输入:** nums = [1,4,5,2,3], k = 3    **输出:** [5,2,3]    **解释:** 长度为 3 的子数组有： [1,4,5]、 [4,5,2] 和 [5,2,3]。    在这些数组中， [5,2,3] 是最大的。

**Example 2:**
            **输入:** nums = [1,4,5,2,3], k = 4    **输出:** [4,5,2,3]    **解释:** 长度为 4 的子数组有： [1,4,5,2] 和 [4,5,2,3]。    在这些数组中， [4,5,2,3] 是最大的。

**示例 3:**
            **输入:** nums = [1,4,5,2,3], k = 1    **输出:** [5]    

**提示：**

  * `1 <= k <= nums.length <= 105`
  * `1 <= nums[i] <= 109`
  * `nums` 中的所有整数都是 **不同** 的。

**进阶：** 如果允许 `nums` 中存在相同元素，你该如何解决该问题？


**Tags:** Greedy, Array

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        new_nums = nums[:(len(nums)-k+1)]
        max_idx = new_nums.index(max(new_nums))
        return nums[max_idx:max_idx+k]

```

[title]: https://leetcode-cn.com/problems/largest-subarray-length-k
