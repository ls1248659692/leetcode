# [Power Set LCCI][title]

## Description

幂集。编写一种方法，返回某集合的所有子集。集合中 **不包含重复的元素** 。

说明：解集不能包含重复的子集。

**示例:**
            **输入** ： nums = [1,2,3]    **输出** ：    [      [3],      [1],      [2],      [1,2,3],      [1,3],      [2,3],      [1,2],      []    ]    


**Tags:** Bit Manipulation, Array, Backtracking

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def sst(n):
            if len(n)==0: return [[]]
            s1  = sst(n[1:])
            s0 = [s+[n[0]] for s in s1]
            return s0+s1
        return sst(nums)        
```

[title]: https://leetcode-cn.com/problems/power-set-lcci
