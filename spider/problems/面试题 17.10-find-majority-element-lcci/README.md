# [Find Majority Element LCCI][title]

## Description

数组中占比超过一半的元素称之为主要元素。给你一个 **整数** 数组，找出其中的主要元素。若没有，返回 `-1` 。请设计时间复杂度为 `O(N)`
、空间复杂度为 `O(1)` 的解决方案。

**示例 1：**
            **输入：** [1,2,5,9,5,9,5,5,5]    **输出：** 5

**示例 2：**
            **输入：** [3,2]    **输出：** -1

**示例 3：**
            **输入：** [2,2,1,1,1,2,2]    **输出：** 2


**Tags:** Array, Counting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        count = 0
        for num in nums:
            
            if not count: # æ²¡æç¥¨æ°ï¼ææ¶è®¤ä¸ºæ¯å½åçäºº
                ans = num
            
            if num == ans: # æç¸åçäººä¸ç¥¨ï¼ç¥¨æ°å ä¸ï¼å¦åç¥¨æ°åä¸
                count += 1
            else:
                count -= 1

        return ans if count and nums.count(ans) > n // 2 else -1


```

[title]: https://leetcode-cn.com/problems/find-majority-element-lcci
