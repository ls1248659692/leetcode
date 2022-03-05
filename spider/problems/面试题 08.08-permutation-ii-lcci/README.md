# [Permutation II LCCI][title]

## Description

有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。

**示例1:**
            **输入** ：S = "qqe"    **输出** ：["eqq","qeq","qqe"]    

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
            vis =set()
            if len(nums)<=1:
                return [nums]
            else:
                res = []
                for i in range(len(nums)):
                    if nums[i] not in vis:
                        tli = [ [nums[i]] + el for el in v1(nums[:i]+nums[i+1:])]
                        vis.add(nums[i])
                        res.extend(tli)
                return res
        r= v1(sorted(list(S)))  
        return [''.join(ls) for ls in r]      
```

[title]: https://leetcode-cn.com/problems/permutation-ii-lcci
