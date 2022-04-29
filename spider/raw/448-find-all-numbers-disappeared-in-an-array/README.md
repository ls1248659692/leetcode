# [Find All Numbers Disappeared in an Array][title]

## Description

给你一个含 `n` 个整数的数组 `nums` ，其中 `nums[i]` 在区间 `[1, n]` 内。请你找出所有在 `[1, n]`
范围内但没有出现在 `nums` 中的数字，并以数组的形式返回结果。

**示例 1：**
            **输入：** nums = [4,3,2,7,8,2,3,1]    **输出：** [5,6]    

**示例 2：**
            **输入：** nums = [1,1]    **输出：** [2]    

**提示：**

  * `n == nums.length`
  * `1 <= n <= 105`
  * `1 <= nums[i] <= n`

**进阶：** 你能在不使用额外空间且时间复杂度为 __`O(n)` __ 的情况下解决这个问题吗? 你可以假定返回的数组不算在额外空间内。


**Tags:** Array, Hash Table

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nset = set(nums)
        return [i+1 for i in range(len(nums))if i+1 not in nset ]
            
        #a =  [ii+1 for ii in range(len(nums)) if ii+1 not in nums]
        #return a
        
```

[title]: https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array
