# [Reverse String][title]

## Description

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 `s` 的形式给出。

不要给另外的数组分配额外的空间，你必须 **[原地](https://baike.baidu.com/item/原地算法)修改输入数组**、使用 O(1)
的额外空间解决这一问题。



**示例 1：**
            **输入：** s = ["h","e","l","l","o"]    **输出：** ["o","l","l","e","h"]    

**示例 2：**
            **输入：** s = ["H","a","n","n","a","h"]    **输出：** ["h","a","n","n","a","H"]



**提示：**

  * `1 <= s.length <= 105`
  * `s[i]` 都是 [ASCII](https://baike.baidu.com/item/ASCII) 码表中的可打印字符


**Tags:** Recursion, Two Pointers, String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        t =''
        for ii in range(1,len(s)//2+1):
            t=s[ii-1]
            s[ii-1]=s[-ii]
            s[-ii]=t
            
```

[title]: https://leetcode-cn.com/problems/reverse-string
