# [Sort an Array][title]

## Description

给你一个整数数组 `nums`，请你将该数组升序排列。



**示例 1：**
            **输入：** nums = [5,2,3,1]    **输出：** [1,2,3,5]    

**示例 2：**
            **输入：** nums = [5,1,1,2,0,0]    **输出：** [0,0,1,1,2,5]    



**提示：**

  * `1 <= nums.length <= 5 * 104`
  * `-5 * 104 <= nums[i] <= 5 * 104`


**Tags:** Array, Divide and Conquer, Bucket Sort, Counting Sort, Radix Sort, Sorting, Heap (Priority Queue), Merge Sort

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)
```

[title]: https://leetcode-cn.com/problems/sort-an-array
