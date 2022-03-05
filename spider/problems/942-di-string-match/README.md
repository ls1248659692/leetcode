# [DI String Match][title]

## Description

由范围 `[0,n]` 内所有整数组成的 `n + 1` 个整数的排列序列可以表示为长度为 `n` 的字符串 `s` ，其中:

  * 如果 `perm[i] < perm[i + 1]` ，那么 `s[i] == 'I'` 
  * 如果 `perm[i] > perm[i + 1]` ，那么 `s[i] == 'D'` 

给定一个字符串 `s` ，重构排列 `perm` 并返回它。如果有多个有效排列perm，则返回其中 **任何一个** 。



**示例 1：**
            **输入：** s = "IDID"    **输出：** [0,4,1,3,2]    

**示例 2：**
            **输入：** s = "III"    **输出：** [0,1,2,3]    

**示例 3：**
            **输入：** s = "DDI"    **输出：** [3,2,0,1]



**提示：**

  * `1 <= s.length <= 105`
  * `s` 只包含字符 `"I"` 或 `"D"`


**Tags:** Greedy, Array, Math, Two Pointers, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res=[0]
        for c in s:
            if c=='I': res.append(max(res)+1)
            else: res.append(min(res)-1)
        r =[el-min(res) for el in res]
        print(r)
        return r
        
```

[title]: https://leetcode-cn.com/problems/di-string-match
