# [数组中出现次数超过一半的数字  LCOF][title]

## Description

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。



你可以假设数组是非空的，并且给定的数组总是存在多数元素。



**示例  1:**
            **输入:** [1, 2, 3, 2, 2, 2, 5, 4, 2]    **输出:** 2



**限制：**

`1 <= 数组长度 <= 50000`



注意：本题与主站 169 题相同：<https://leetcode-cn.com/problems/majority-element/>




**Tags:** Array, Hash Table, Divide and Conquer, Counting, Sorting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return [n for n in set(nums) if nums.count(n)>len(nums)/2][0]
```

[title]: https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
