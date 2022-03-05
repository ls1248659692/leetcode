# [Move Zeroes][title]

## Description

给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。

**请注意**  ，必须在不复制数组的情况下原地对数组进行操作。



**示例 1:**
            **输入:** nums = [0,1,0,3,12]    **输出:** [1,3,12,0,0]    

**示例 2:**
            **输入:** nums = [0]    **输出:** [0]



**提示** :

  * `1 <= nums.length <= 104`
  * `-231 <= nums[i] <= 231 - 1`



**进阶：** 你能尽量减少完成的操作次数吗？


**Tags:** Array, Two Pointers

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zn=0
        for ii in range(len(nums)-1,-1,-1):
            if nums[ii]==0:
                for jj in range(ii,len(nums)-1-zn):
                    nums[jj]=nums[jj+1]
                zn+=1
                
        for zz in range(len(nums)-zn,len(nums)):
            nums[zz]=0

```

[title]: https://leetcode-cn.com/problems/move-zeroes
