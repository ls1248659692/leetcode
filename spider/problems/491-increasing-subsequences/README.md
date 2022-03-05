# [Increasing Subsequences][title]

## Description

给你一个整数数组 `nums` ，找出并返回所有该数组中不同的递增子序列，递增子序列中 **至少有两个元素** 。你可以按 **任意顺序** 返回答案。

数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。



**示例 1：**
            **输入：** nums = [4,6,7,7]    **输出：** [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]    

**示例 2：**
            **输入：** nums = [4,4,3,2,1]    **输出：** [[4,4]]    



**提示：**

  * `1 <= nums.length <= 15`
  * `-100 <= nums[i] <= 100`


**Tags:** Bit Manipulation, Array, Hash Table, Backtracking

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def sst(n):
            if len(n)==0: return [[]]
            s1  = sst(n[1:])
            s0 = [[n[0]]+list(s) for s in s1 if not s or n[0]<=s[0]]
            return list(set([tuple(e) for e in s0+s1]))
        r=sst(nums)        
        return [ls for ls in r if len(ls)>1]
```

[title]: https://leetcode-cn.com/problems/increasing-subsequences
