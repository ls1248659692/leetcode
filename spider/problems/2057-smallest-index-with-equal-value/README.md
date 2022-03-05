# [Smallest Index With Equal Value][title]

## Description

给你一个下标从 0 开始的整数数组 `nums` ，返回 `nums` 中满足 __`i mod 10 == nums[i]` __ 的最小下标 `i`
；如果不存在这样的下标，返回 __`-1` __ 。

`x mod y` 表示 `x` 除以 `y` 的 **余数** 。



**示例 1：**
            **输入：** nums = [0,1,2]    **输出：** 0    **解释：**    i=0: 0 mod 10 = 0 == nums[0].    i=1: 1 mod 10 = 1 == nums[1].    i=2: 2 mod 10 = 2 == nums[2].    所有下标都满足 i mod 10 == nums[i] ，所以返回最小下标 0    

**示例 2：**
            **输入：** nums = [4,3,2,1]    **输出：** 2    **解释：**    i=0: 0 mod 10 = 0 != nums[0].    i=1: 1 mod 10 = 1 != nums[1].    i=2: 2 mod 10 = 2 == nums[2].    i=3: 3 mod 10 = 3 != nums[3].    2 唯一一个满足 i mod 10 == nums[i] 的下标    

**示例 3：**
            **输入：** nums = [1,2,3,4,5,6,7,8,9,0]    **输出：** -1    **解释：** 不存在满足 i mod 10 == nums[i] 的下标    

**示例 4：**
            **输入：** nums = [2,1,3,5,2]    **输出：** 1    **解释：** 1 是唯一一个满足 i mod 10 == nums[i] 的下标    



**提示：**

  * `1 <= nums.length <= 100`
  * `0 <= nums[i] <= 9`


**Tags:** Array

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i %10==nums[i]:return i
        return -1
```

[title]: https://leetcode-cn.com/problems/smallest-index-with-equal-value
