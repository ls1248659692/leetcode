# [Distinct Numbers in Each Subarray][title]

## Description

给你一个整数数组 `nums`与一个整数 `k`，请你构造一个长度 `n-k+1` 的数组 `ans`，这个数组第`i`个元素 `ans[i]`
是每个长度为k的子数组 `nums[i:i+k-1] = [nums[i], nums[i+1], ..., nums[i+k-1]]`中数字的种类数。

返回这个数组 `ans`。

**示例 1:**
            **输入:** nums = [1,2,3,2,2,1,3], k = 3    **输出:** [3,2,2,2,3]    **解释** ：每个子数组的数字种类计算方法如下：    - nums[0:2] = [1,2,3] 有'1','2','3'三种数字所以      ans[0] = 3    - nums[1:3] = [2,3,2] 有'2','3'两种数字所以          ans[1] = 2    - nums[2:4] = [3,2,2] 有'2','3'两种数字所以          ans[2] = 2    - nums[3:5] = [2,2,1] 有'1','2'两种数字所以          ans[3] = 2    - nums[4:6] = [2,1,3] 有'1','2','3'三种数字所以      ans[4] = 3    

**示例 2:**
            **输入:** nums = [1,1,1,1,2,3,4], k = 4    **输出:** [1,2,3,4]    **解释:** 每个子数组的数字种类计算方法如下：    - nums[0:3] = [1,1,1,1] 只有'1'这一种数字所以         ans[0] = 1    - nums[1:4] = [1,1,1,2] 有'1','2'两种数字所以         ans[1] = 2    - nums[2:5] = [1,1,2,3] 有'1','2','3'三种数字所以     ans[2] = 3    - nums[3:6] = [1,2,3,4] 有'1','2','3','4'四种数字所以 ans[3] = 4    

**提示:**

  * `1 <= k <= nums.length <= 105`
  * `1 <= nums[i] <= 105`


**Tags:** Array, Hash Table, Sliding Window

**Difficulty:** Medium

## 思路

[title]: https://leetcode-cn.com/problems/distinct-numbers-in-each-subarray
