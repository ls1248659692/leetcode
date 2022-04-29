# [Contiguous Sequence LCCI][title]

## Description

给定一个整数数组，找出总和最大的连续数列，并返回总和。

**示例：**
            **输入：** [-2,1,-3,4,-1,2,1,-5,4]    **输出：** 6    **解释：** 连续子数组 [4,-1,2,1] 的和最大，为 6。    

**进阶：**

如果你已经实现复杂度为 O( _n_ ) 的解法，尝试使用更为精妙的分治法求解。


**Tags:** Array, Divide and Conquer, Dynamic Programming

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c, cdiffmax,cleftmin=nums[0],nums[0],nums[0] if nums[0]<0 else 0
        for n in nums[1:]:
            c,cdiffmax,cleftmin, = c+n,max(cdiffmax,c+n-cleftmin),min(c+n,cleftmin)
        return cdiffmax        
```

[title]: https://leetcode-cn.com/problems/contiguous-sequence-lcci
