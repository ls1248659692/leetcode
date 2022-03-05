# [Sum of Square Numbers][title]

## Description

给定一个非负整数 `c` ，你要判断是否存在两个整数 `a` 和 `b`，使得 `a2 + b2 = c` 。



**示例 1：**
            **输入：** c = 5    **输出：** true    **解释：** 1 * 1 + 2 * 2 = 5    

**示例 2：**
            **输入：** c = 3    **输出：** false    



**提示：**

  * `0 <= c <= 231 - 1`


**Tags:** Math, Two Pointers, Binary Search

**Difficulty:** Medium

## 思路

``` python3
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nu=[i*i for i in range(math.ceil(math.sqrt(c+1)))]
        snu = set(nu)
        for n in nu:
            if c-n in snu: return True
        return False
```

[title]: https://leetcode-cn.com/problems/sum-of-square-numbers
