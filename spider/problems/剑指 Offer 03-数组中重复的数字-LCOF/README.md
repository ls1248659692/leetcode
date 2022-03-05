# [数组中重复的数字 LCOF][title]

## Description

找出数组中重复的数字。

  
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1
的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

**示例 1：**
            **输入：**    [2, 3, 1, 0, 2, 5, 3]    **输出：** 2 或 3     



**限制：**

`2 <= n <= 100000`


**Tags:** Array, Hash Table, Sorting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dic ={}
        for n in nums:
            dic.setdefault(n,0)
            dic[n] +=1
            if dic[n]>1:return n
        #for n in set(nums):
        #    if nums.count(n)>1:return n
        #return [n for n in set(nums) if nums.count(n)>1][0]
```

[title]: https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
