# [扑克牌中的顺子  LCOF][title]

## Description

从 **若干副扑克牌** 中随机抽 `5`
张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A
不能视为 14。



**示例  1:**
            **输入:** [1,2,3,4,5]    **输出:** True



**示例  2:**
            **输入:** [0,0,1,2,5]    **输出:** True



**限制：**

数组长度为 5

数组的数取值为 [0, 13] .


**Tags:** Array, Sorting

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        en =[e for e in nums if e]
        return max(en)-min(en)<=4 and len(en)==len(set(en))
```

[title]: https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof
