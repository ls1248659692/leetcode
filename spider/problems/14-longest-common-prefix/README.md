# [Longest Common Prefix][title]

## Description

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 `""`。



**示例 1：**
            **输入：** strs = ["flower","flow","flight"]    **输出：** "fl"    

**示例 2：**
            **输入：** strs = ["dog","racecar","car"]    **输出：** ""    **解释：** 输入不存在公共前缀。



**提示：**

  * `1 <= strs.length <= 200`
  * `0 <= strs[i].length <= 200`
  * `strs[i]` 仅由小写英文字母组成


**Tags:** String

**Difficulty:** Easy

## 思路

``` python3
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s_n = sorted(strs,key=lambda xx:len(xx))
        #print(s_n)
        for ii in range(len(s_n[0]),-1,-1):
            unmatch =False
            for jj in range(1,len(s_n)):
                if s_n[0][:ii] != s_n[jj][:ii]:
                    unmatch=True
                    break
            if not  unmatch: return s_n[0][:ii]
        return ''
```

[title]: https://leetcode-cn.com/problems/longest-common-prefix
