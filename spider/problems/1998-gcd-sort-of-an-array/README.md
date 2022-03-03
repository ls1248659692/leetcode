# [GCD Sort of an Array][title]

## Description

给你一个整数数组 `nums` ，你可以在 `nums` 上执行下述操作 **任意次** ：

  * 如果 `gcd(nums[i], nums[j]) > 1` ，交换 `nums[i]` 和 `nums[j]` 的位置。其中 `gcd(nums[i], nums[j])` 是 `nums[i]` 和 `nums[j]` 的最大公因数。

如果能使用上述交换方式将 `nums` 按 **非递减顺序** 排列，返回 `true` ；否则，返回 `false` 。



**示例 1：**
            **输入：** nums = [7,21,3]    **输出：** true    **解释：** 可以执行下述操作完成对 [7,21,3] 的排序：    - 交换 7 和 21 因为 gcd(7,21) = 7 。nums = [ _ **21**_ , _ **7**_ ,3]    - 交换 21 和 3 因为 gcd(21,3) = 3 。nums = [ _ **3**_ ,7, _ **21**_ ]    

**示例 2：**
            **输入：** nums = [5,2,6,2]    **输出：** false    **解释：** 无法完成排序，因为 5 不能与其他元素交换。    

**示例 3：**
            **输入：** nums = [10,5,9,3,15]    **输出：** true    **解释：**    可以执行下述操作完成对 [10,5,9,3,15] 的排序：    - 交换 10 和 15 因为 gcd(10,15) = 5 。nums = [ _ **15**_ ,5,9,3, _ **10**_ ]    - 交换 15 和 3 因为 gcd(15,3) = 3 。nums = [ _ **3**_ ,5,9, _ **15**_ ,10]    - 交换 10 和 15 因为 gcd(10,15) = 5 。nums = [3,5,9, _ **10**_ , _ **15**_ ]    



**提示：**

  * `1 <= nums.length <= 3 * 104`
  * `2 <= nums[i] <= 105`


**Tags:** Union Find, Array, Math, Sorting

**Difficulty:** Hard

## 思路

[title]: https://leetcode-cn.com/problems/gcd-sort-of-an-array
