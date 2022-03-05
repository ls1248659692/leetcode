# [Sort Array By Parity II][title]

## Description

给定一个非负整数数组 `nums`，  `nums` 中一半整数是 **奇数** ，一半整数是 **偶数** 。

对数组进行排序，以便当 `nums[i]` 为奇数时，`i` 也是 **奇数** ；当 `nums[i]` 为偶数时， `i` 也是 **偶数** 。

你可以返回 _任何满足上述条件的数组作为答案_ 。



**示例 1：**
            **输入：** nums = [4,2,5,7]    **输出：** [4,5,2,7]    **解释：** [4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。    

**示例 2：**
            **输入：** nums = [2,3]    **输出：** [2,3]    



**提示：**

  * `2 <= nums.length <= 2 * 104`
  * `nums.length` 是偶数
  * `nums` 中一半是偶数
  * `0 <= nums[i] <= 1000`



**进阶：** 可以不使用额外空间解决问题吗？


**Tags:** Array, Two Pointers, Sorting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        od,ev = [e for e in nums if e%2],[e for e in nums if not e%2]
        for i in range(len(ev)): nums[i*2:i*2+2]=(ev[i],od[i])
        return nums

```

[title]: https://leetcode-cn.com/problems/sort-array-by-parity-ii
