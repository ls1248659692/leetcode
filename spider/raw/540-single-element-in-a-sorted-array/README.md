# [Single Element in a Sorted Array][title]

## Description

给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。

请你找出并返回只出现一次的那个数。

你设计的解决方案必须满足 `O(log n)` 时间复杂度和 `O(1)` 空间复杂度。



**示例 1:**
            **输入:** nums = [1,1,2,3,3,4,4,8,8]    **输出:** 2    

**示例 2:**
            **输入:** nums =  [3,3,7,7,10,11,11]    **输出:** 10    



**提示:**

  * `1 <= nums.length <= 105`
  * `0 <= nums[i] <= 105`


**Tags:** Array, Binary Search

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # while len(nums) > 1 and nums[0] == nums[1]:
        #     nums.pop(1)
        #     nums.pop(0)
        # return nums[0]
        if len(nums) == 1:
            return nums[0]
        l = 0
        h = len(nums) -1
        while l<h:
            if nums[l] == nums[l+1]:
                l= l + 2
            else:
                return nums[l]
            if nums[h] == nums[h-1]:
                h= h -2
            else:
                return nums[h]
        return nums[l]
```

[title]: https://leetcode-cn.com/problems/single-element-in-a-sorted-array
