# [Two Sum Less Than K][title]

## Description

给你一个整数数组 `nums` 和整数 `k` ，返回最大和 `sum` ，满足存在 `i < j` 使得 `nums[i] + nums[j] =
sum` 且 `sum < k` 。如果没有满足此等式的 `i,j` 存在，则返回 `-1` 。

**示例 1：**
            **输入：** nums = [34,23,1,24,75,33,54,8], k = 60    **输出：** 58    **解释：**    34 和 24 相加得到 58，58 小于 60，满足题意。    

**示例 2：**
            **输入：** nums = [10,20,30], k = 15    **输出：** -1    **解释：**    我们无法找到和小于 15 的两个元素。

**提示：**

  * `1 <= nums.length <= 100`
  * `1 <= nums[i] <= 1000`
  * `1 <= k <= 2000`


**Tags:** Array, Two Pointers, Binary Search, Sorting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = -1
        l,r = 0,len(nums)-1
        while l < r:
            if nums[l] + nums[r] < k:
                ans = max(ans, nums[l] + nums[r])
                l += 1
            if nums[l] + nums[r] >= k:
                r -= 1
        return ans

```

[title]: https://leetcode-cn.com/problems/two-sum-less-than-k
