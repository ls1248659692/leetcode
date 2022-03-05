# [Permutation I LCCI][title]

## Description

无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。

**示例1:**
            **输入** ：S = "qwe"    **输出** ：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]    

**示例2:**
            **输入** ：S = "ab"    **输出** ：["ab", "ba"]    

**提示:**

  1. 字符都是英文字母。
  2. 字符串长度在[1, 9]之间。


**Tags:** String, Backtracking

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def permutation(self, S: str) -> List[str]:
        def v1(nums):
            if len(nums)<=1:
                return [nums]
            else:
                res = []
                for ii in range(len(nums)):
                    tli = [ nums[ii] + el for el in v1(nums[:ii]+nums[ii+1:])]
                    res.extend(tli)
                return res
        return v1(S)
```

[title]: https://leetcode-cn.com/problems/permutation-i-lcci
