# [Sort Colors][title]

## Description

给定一个包含红色、白色和蓝色、共 `n` __ 个元素的数组 `nums` ，
**[原地](https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95)**
对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 `0`、 `1` 和 `2` 分别表示红色、白色和蓝色。

必须在不使用库的sort函数的情况下解决这个问题。



**示例 1：**
            **输入：** nums = [2,0,2,1,1,0]    **输出：** [0,0,1,1,2,2]    

**示例 2：**
            **输入：** nums = [2,0,1]    **输出：** [0,1,2]    



**提示：**

  * `n == nums.length`
  * `1 <= n <= 300`
  * `nums[i]` 为 `0`、`1` 或 `2`



**进阶：**

  * 你可以不使用代码库中的排序函数来解决这道题吗？
  * 你能想出一个仅使用常数空间的一趟扫描算法吗？


**Tags:** Array, Two Pointers, Sorting

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 1
        while 0 < i < len(nums):
            if nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                i = 1
            else:
                i = i + 1
```

[title]: https://leetcode-cn.com/problems/sort-colors
