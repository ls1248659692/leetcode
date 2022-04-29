# [和为s的连续正数序列 LCOF][title]

## Description

输入一个正整数 `target` ，输出所有和为 `target` 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。



**示例 1：**
            **输入：** target = 9    **输出：** [[2,3,4],[4,5]]    

**示例 2：**
            **输入：** target = 15    **输出：** [[1,2,3,4,5],[4,5,6],[7,8]]    



**限制：**

  * `1 <= target <= 10^5`




**Tags:** Math, Two Pointers, Enumeration

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        return [list(range((target*2//qq-qq+1)//2,(target*2//qq-qq+1)//2+qq)) for qq in range(int((target*2)**0.5),1,-1) if target*2%qq==0 and (qq+target*2//qq)%2==1]
```

[title]: https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
