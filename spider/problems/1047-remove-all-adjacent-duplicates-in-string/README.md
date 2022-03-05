# [Remove All Adjacent Duplicates In String][title]

## Description

给出由小写字母组成的字符串 `S`， **重复项删除操作** 会选择两个相邻且相同的字母，并删除它们。

在 S 上反复执行重复项删除操作，直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。



**示例：**
            **输入：** "abbaca"    **输出：** "ca"    **解释：**    例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。    



**提示：**

  1. `1 <= S.length <= 20000`
  2. `S` 仅由小写英文字母组成。


**Tags:** Stack, String

**Difficulty:** Easy

## 思路

``` python3
def dupa(s,b):
    for i in range(b+1,len(s)):
        b,e,m = i-1,i,False
        while b>=0 and e<len(s) and s[b]==s[e]:
            b-=1
            e+=1
            m=True
        if m: return b+1,e-1
    return -1,-1  

class Solution:
    def removeDuplicates(self, s: str) -> str:
        b,e =   dupa(s,0)    
        while b>=0: 
            s= s[:b]+s[e+1:]
            b,e =   dupa(s,b)
        return s
```

[title]: https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string
