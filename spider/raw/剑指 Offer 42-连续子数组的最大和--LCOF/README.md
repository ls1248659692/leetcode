# [连续子数组的最大和  LCOF][title]

## Description

输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。



**示例1:**
            **输入:** nums = [-2,1,-3,4,-1,2,1,-5,4]    **输出:** 6    **解释:**  连续子数组 [4,-1,2,1] 的和最大，为 6。



**提示：**

  * `1 <= arr.length <= 10^5`
  * `-100 <= arr[i] <= 100`

注意：本题与主站 53 题相同：<https://leetcode-cn.com/problems/maximum-subarray/>




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

[title]: https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof
